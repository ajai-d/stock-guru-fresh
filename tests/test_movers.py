from src.app.movers import SeededMoversProvider

import pytest


def test_movers_schema_and_limit():
    """AC-1: get_market_movers returns a valid movers payload from the seeded feed."""
    resp = SeededMoversProvider().get(10)
    assert resp.as_of
    assert len(resp.movers) == 10
    m = resp.movers[0]
    assert m.ticker and m.sector and isinstance(m.change_pct, float)


def test_movers_invalid_limit():
    with pytest.raises(ValueError):
        SeededMoversProvider().get(0)
    with pytest.raises(ValueError):
        SeededMoversProvider().get(99)
