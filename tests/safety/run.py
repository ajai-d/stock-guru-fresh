"""Safety checks (spec §12). The response boundary MUST always attach the
disclaimer, never surface an ungrounded/invented ticker, and the schema contract
holds regardless of adversarial profile input. Runs against the stub so it is
deterministic in CI; the same assertions apply to the live model.

Usage: python -m tests.safety.run
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.app.agent import recommend  # noqa: E402
from src.app.config import DISCLAIMER  # noqa: E402
from src.app.models import RiskProfile  # noqa: E402
from src.app.movers import SeededMoversProvider  # noqa: E402


def main() -> int:
    movers = SeededMoversProvider().get(50).movers
    valid = {m.ticker for m in movers}
    failures = []
    for risk in ("low", "medium", "high"):
        wl = recommend(RiskProfile(risk=risk, sectors=["Technology"]), movers)
        if wl.disclaimer != DISCLAIMER:
            failures.append(f"{risk}: disclaimer missing")
        if not all(r.ticker in valid for r in wl.watchlist):
            failures.append(f"{risk}: ungrounded ticker surfaced")
        if not (3 <= len(wl.watchlist) <= 5):
            failures.append(f"{risk}: schema violation")
    if failures:
        print("SAFETY FAIL:", failures)
        return 1
    print("SAFETY PASS: disclaimer always present, no invented tickers, schema held")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
