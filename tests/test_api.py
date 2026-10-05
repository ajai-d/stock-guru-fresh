from fastapi.testclient import TestClient

from src.app.config import DISCLAIMER
from src.app.main import app

client = TestClient(app)


def test_healthz():
    """AC-6: GET /healthz -> 200."""
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_movers_endpoint():
    """AC-6: GET /api/movers -> 200 with as_of + movers."""
    r = client.get("/api/movers", params={"limit": 5})
    assert r.status_code == 200
    body = r.json()
    assert body["as_of"] and len(body["movers"]) == 5


def test_movers_invalid_limit():
    r = client.get("/api/movers", params={"limit": 999})
    assert r.status_code == 422


def test_recommend_endpoint():
    """AC-5 / AC-4: POST /api/recommend -> 200 with watchlist + disclaimer."""
    r = client.post("/api/recommend", json={"risk": "medium", "sectors": ["Technology"]})
    assert r.status_code == 200
    body = r.json()
    assert 3 <= len(body["watchlist"]) <= 5
    assert body["disclaimer"] == DISCLAIMER


def test_recommend_invalid_body():
    r = client.post("/api/recommend", json={"risk": "banana"})
    assert r.status_code == 422
