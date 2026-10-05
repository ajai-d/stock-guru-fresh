from src.app.agent import recommend
from src.app.config import DISCLAIMER
from src.app.models import RiskProfile
from src.app.movers import SeededMoversProvider


def _movers():
    return SeededMoversProvider().get(25).movers


def test_recommend_grounded_and_sized():
    """AC-2: 3-5 recommendations, all tickers present in movers (grounding / DIM-1)."""
    movers = _movers()
    valid = {m.ticker for m in movers}
    wl = recommend(RiskProfile(risk="medium", sectors=["Technology"]), movers)
    assert 3 <= len(wl.watchlist) <= 5
    for rec in wl.watchlist:
        assert rec.ticker in valid  # grounding


def test_recommend_schema_and_disclaimer():
    """AC-3 / AC-4: confidence in [0,1], non-empty rationale, disclaimer present."""
    movers = _movers()
    wl = recommend(RiskProfile(risk="high", sectors=["Energy"]), movers)
    assert wl.disclaimer == DISCLAIMER
    for rec in wl.watchlist:
        assert 0.0 <= rec.confidence <= 1.0
        assert rec.rationale.strip()
