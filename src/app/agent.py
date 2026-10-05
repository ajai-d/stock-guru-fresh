import asyncio
import json
import uuid
from pathlib import Path

from . import config
from .models import Mover, Recommendation, RiskProfile, Watchlist

# Agent instructions (spec §12 safety + §4 grounding). The agent is built on
# Microsoft Agent Framework (bound `agentic-stack`); the model is an Azure AI
# Foundry / Azure OpenAI deployment reached via managed identity (no keys).
_INSTRUCTIONS = (
    "You are a cautious stock-watchlist assistant. You are given the day's market "
    "movers and a user's risk profile. Choose 3 to 5 tickers STRICTLY from the "
    "provided movers (never invent a ticker). For each, give a one-line rationale "
    "that references the ticker's sector or its price move, and a confidence between "
    "0 and 1. Do NOT give personalized financial advice or buy/sell directives. "
    'Return ONLY JSON: {"watchlist":[{"ticker","rationale","confidence"}]}'
)


def _estimate_cost(tokens_in: int, tokens_out: int) -> float:
    return round(
        tokens_in / 1000 * config.PRICE_IN_PER_1K
        + tokens_out / 1000 * config.PRICE_OUT_PER_1K,
        6,
    )


def _log_usage(record: dict) -> None:
    path = Path(config.USAGE_LOG_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")


class CostCapExceeded(Exception):
    code = "cost_cap_exceeded"


class InsufficientCandidates(Exception):
    code = "insufficient_candidates"


def _rank(movers: list[Mover], profile: RiskProfile) -> list[Mover]:
    """Deterministic candidate ordering used by the stub and as a grounded fallback:
    prefer the user's sectors, then larger absolute moves."""
    sectors = {s.lower() for s in profile.sectors}

    def key(m: Mover) -> tuple:
        in_sector = 1 if m.sector.lower() in sectors else 0
        return (in_sector, abs(m.change_pct))

    return sorted(movers, key=key, reverse=True)


def _rationale(m: Mover) -> str:
    direction = "gained" if m.change_pct >= 0 else "fell"
    return f"{m.sector} name that {direction} {abs(m.change_pct):.1f}% today."


def _stub_watchlist(movers: list[Mover], profile: RiskProfile) -> Watchlist:
    ranked = _rank(movers, profile)[:5]
    if len(ranked) < 3:
        raise InsufficientCandidates()
    recs = [
        Recommendation(
            ticker=m.ticker,
            rationale=_rationale(m),
            confidence=round(min(0.95, 0.4 + abs(m.change_pct) / 20), 2),
        )
        for m in ranked
    ]
    _log_usage(
        {
            "request_id": str(uuid.uuid4()),
            "tokens_in": 0,
            "tokens_out": 0,
            "est_cost_usd": 0.0,
            "scope": "per_request",
            "outcome": "ok_stub",
        }
    )
    return Watchlist(watchlist=recs, disclaimer=config.DISCLAIMER)


def _enforce(raw: list[dict], movers: list[Mover]) -> list[Recommendation]:
    """Grounding + schema enforcement: keep only tickers present in movers,
    clamp confidence to [0,1], require a non-empty rationale, cap at 5."""
    valid_tickers = {m.ticker for m in movers}
    out: list[Recommendation] = []
    for item in raw:
        ticker = str(item.get("ticker", "")).upper().strip()
        if ticker not in valid_tickers:
            continue  # drop ungrounded / invented tickers
        rationale = str(item.get("rationale", "")).strip()
        if not rationale:
            continue
        try:
            conf = float(item.get("confidence", 0.5))
        except (TypeError, ValueError):
            conf = 0.5
        conf = max(0.0, min(1.0, conf))
        out.append(Recommendation(ticker=ticker, rationale=rationale, confidence=conf))
        if len(out) == 5:
            break
    return out


def _top_up(recs: list[Recommendation], movers: list[Mover], profile: RiskProfile):
    """Ensure at least 3 grounded recommendations by filling from the ranking."""
    existing = {r.ticker for r in recs}
    for m in _rank(movers, profile):
        if len(recs) >= 3:
            break
        if m.ticker in existing:
            continue
        recs.append(
            Recommendation(
                ticker=m.ticker,
                rationale=_rationale(m),
                confidence=round(min(0.9, 0.4 + abs(m.change_pct) / 20), 2),
            )
        )
    return recs


async def _run_agent(user_prompt: str) -> tuple[str, int, int]:
    """Run the Microsoft Agent Framework agent against the Azure AI Foundry /
    Azure OpenAI deployment using managed identity (no keys). Returns
    (text, tokens_in, tokens_out).

    Uses `agent_framework.openai.OpenAIChatCompletionClient` wrapping a
    managed-identity `AsyncAzureOpenAI` client — the current Agent Framework
    surface for Azure OpenAI (the former `agent_framework.azure.AzureOpenAIChatClient`
    was removed). Chat Completions is used (compatible with the configured
    `AOAI_API_VERSION`)."""
    from openai import AsyncAzureOpenAI
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    from agent_framework import Agent
    from agent_framework.openai import OpenAIChatCompletionClient

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
    )
    azure_openai = AsyncAzureOpenAI(
        azure_endpoint=config.AOAI_ENDPOINT,
        azure_ad_token_provider=token_provider,
        api_version=config.AOAI_API_VERSION,
    )
    client = OpenAIChatCompletionClient(
        model=config.AOAI_DEPLOYMENT, async_client=azure_openai
    )
    agent = Agent(client=client, name="stock-guru", instructions=_INSTRUCTIONS)
    response = await agent.run(user_prompt)
    text = getattr(response, "text", None) or str(response)
    usage = getattr(response, "usage_details", None) or getattr(response, "usage", None)
    tokens_in = int(
        getattr(usage, "input_token_count", 0) or getattr(usage, "prompt_tokens", 0) or 0
    )
    tokens_out = int(
        getattr(usage, "output_token_count", 0)
        or getattr(usage, "completion_tokens", 0)
        or 0
    )
    return text, tokens_in, tokens_out


def recommend(profile: RiskProfile, movers: list[Mover]) -> Watchlist:
    """T-2: produce a grounded 3-5 item watchlist. Uses the deterministic stub
    when the model is not configured (offline/CI); otherwise runs the Microsoft
    Agent Framework agent and enforces grounding/schema/cost/safety on its output."""
    if config.USE_STUB_MODEL:
        return _stub_watchlist(movers, profile)

    movers_json = json.dumps([m.model_dump() for m in movers], ensure_ascii=False)
    user_prompt = (
        f"Risk profile: {profile.model_dump()}\n"
        f"Today's movers: {movers_json}\n"
        "Pick 3-5 grounded tickers."
    )
    request_id = str(uuid.uuid4())
    text, tokens_in, tokens_out = asyncio.run(_run_agent(user_prompt))

    est_cost = _estimate_cost(tokens_in, tokens_out)
    outcome = "cost_cap_exceeded" if est_cost > config.PER_REQUEST_COST_CAP_USD else "ok"
    _log_usage(
        {
            "request_id": request_id,
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "est_cost_usd": est_cost,
            "scope": "per_request",
            "outcome": outcome,
        }
    )
    if outcome == "cost_cap_exceeded":
        raise CostCapExceeded()

    try:
        # The model may wrap JSON in prose; extract the JSON object.
        start = text.find("{")
        end = text.rfind("}")
        parsed = json.loads(text[start : end + 1]) if start >= 0 else {}
        raw = parsed.get("watchlist", [])
    except (json.JSONDecodeError, ValueError):
        raw = []
    recs = _enforce(raw, movers)
    if len(recs) < 3:
        recs = _top_up(recs, movers, profile)
    return Watchlist(watchlist=recs[:5], disclaimer=config.DISCLAIMER)
