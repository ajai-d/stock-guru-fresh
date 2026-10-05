import json
import os
from datetime import date
from pathlib import Path

from .models import Mover, MoversResponse

_SEED_PATH = Path(__file__).resolve().parents[2] / "data" / "movers_seed.json"


class MoversProvider:
    """Interface for the day's market movers (spec T-1)."""

    def get(self, limit: int = 25) -> MoversResponse:  # pragma: no cover - interface
        raise NotImplementedError


class SeededMoversProvider(MoversProvider):
    """Deterministic movers from a bundled fixture — used in dev/CI/eval and as the
    default provider when no live market-data source is configured (spec §4)."""

    def __init__(self, path: Path | None = None) -> None:
        self._path = path or _SEED_PATH
        with open(self._path, encoding="utf-8") as fh:
            self._data = json.load(fh)

    def get(self, limit: int = 25) -> MoversResponse:
        if limit < 1 or limit > 50:
            raise ValueError("invalid_limit")
        movers = [Mover(**m) for m in self._data["movers"]][:limit]
        as_of = self._data.get("as_of") or date.today().isoformat()
        return MoversResponse(as_of=as_of, movers=movers)


def default_provider() -> MoversProvider:
    # A live provider could be selected here via env; the seeded provider is the
    # offline/CI default.
    return SeededMoversProvider()
