from pathlib import Path
import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from . import agent as agent_mod
from .mcp_server import get_movers
from .models import RiskProfile, Watchlist
from .movers import default_provider

logger = logging.getLogger("stock_guru")

app = FastAPI(title="Stock Guru", version="1.0.0")

_FRONTEND = Path(__file__).resolve().parents[2] / "frontend"


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/api/movers")
def api_movers(limit: int = 25):
    try:
        return default_provider().get(limit).model_dump()
    except ValueError:
        raise HTTPException(status_code=422, detail="invalid_limit")


@app.post("/api/recommend")
def api_recommend(profile: RiskProfile) -> dict:
    movers = get_movers(50).movers
    try:
        result: Watchlist = agent_mod.recommend(profile, movers)
    except agent_mod.CostCapExceeded:
        raise HTTPException(status_code=429, detail="cost_cap_exceeded")
    except agent_mod.InsufficientCandidates:
        raise HTTPException(status_code=503, detail="insufficient_candidates")
    except Exception:
        logger.exception("recommend failed")
        raise HTTPException(status_code=503, detail="model_unavailable")
    return result.model_dump()


# Serve the static SPA at the root (if present).
if _FRONTEND.exists():
    @app.get("/")
    def index():
        return FileResponse(_FRONTEND / "index.html")

    app.mount("/static", StaticFiles(directory=str(_FRONTEND)), name="static")
