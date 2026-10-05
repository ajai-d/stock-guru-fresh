"""Evaluation harness (spec §10). Scores DIM-1..4 over the case dataset and writes
a machine-readable report under reports/eval/.

DIM-1 Grounding, DIM-2 Schema, DIM-3 Disclaimer are deterministic (programmatic).
DIM-4 Rationale grounding is scored by a judge; offline/CI uses a deterministic
heuristic judge (rationale references the ticker's sector or its move). At gate
time against the live model, the LLM-as-judge is used with N runs.

Usage: python -m tests.eval.run --dataset tests/eval/data/cases.jsonl --out reports/eval/run.json
"""
import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.app.agent import recommend  # noqa: E402
from src.app.config import DISCLAIMER  # noqa: E402
from src.app.models import RiskProfile  # noqa: E402
from src.app.movers import SeededMoversProvider  # noqa: E402

THRESHOLDS = {"DIM-1": 1.0, "DIM-2": 1.0, "DIM-3": 1.0, "DIM-4": 0.8}


def _heuristic_judge(rationale: str, sector: str) -> bool:
    r = rationale.lower()
    return sector.lower() in r or any(k in r for k in ("gained", "fell", "%", "today"))


def run(dataset: Path, out: Path) -> dict:
    movers = SeededMoversProvider().get(50).movers
    valid = {m.ticker for m in movers}
    sector_of = {m.ticker: m.sector for m in movers}

    cases = [json.loads(line) for line in dataset.read_text().splitlines() if line.strip()]
    per_dim = {"DIM-1": [], "DIM-2": [], "DIM-3": [], "DIM-4": []}

    for case in cases:
        profile = RiskProfile(risk=case["risk"], sectors=case.get("sectors", []))
        wl = recommend(profile, movers)

        grounded = all(r.ticker in valid for r in wl.watchlist)
        schema_ok = (
            3 <= len(wl.watchlist) <= 5
            and all(0.0 <= r.confidence <= 1.0 and r.rationale.strip() for r in wl.watchlist)
        )
        disclaimer_ok = wl.disclaimer == DISCLAIMER
        judged = [
            _heuristic_judge(r.rationale, sector_of.get(r.ticker, "")) for r in wl.watchlist
        ]
        rationale_rate = sum(judged) / len(judged) if judged else 0.0

        per_dim["DIM-1"].append(1.0 if grounded else 0.0)
        per_dim["DIM-2"].append(1.0 if schema_ok else 0.0)
        per_dim["DIM-3"].append(1.0 if disclaimer_ok else 0.0)
        per_dim["DIM-4"].append(rationale_rate)

    scores = {dim: round(sum(v) / len(v), 4) for dim, v in per_dim.items()}
    passed = {dim: scores[dim] >= THRESHOLDS[dim] for dim in scores}
    report = {
        "run_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": str(dataset),
        "n_cases": len(cases),
        "model": "stub" ,
        "scores": scores,
        "thresholds": THRESHOLDS,
        "passed": passed,
        "all_passed": all(passed.values()),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2))
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default="tests/eval/data/cases.jsonl")
    ap.add_argument("--out", default="reports/eval/run.json")
    args = ap.parse_args()
    report = run(Path(args.dataset), Path(args.out))
    print(json.dumps(report["scores"], indent=2))
    print("PASS" if report["all_passed"] else "FAIL", "->", args.out)
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
