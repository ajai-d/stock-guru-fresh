from typing import Literal

from pydantic import BaseModel, Field

Risk = Literal["low", "medium", "high"]


class Mover(BaseModel):
    ticker: str
    name: str
    sector: str
    change_pct: float
    price: float


class MoversResponse(BaseModel):
    as_of: str
    movers: list[Mover]


class RiskProfile(BaseModel):
    risk: Risk
    sectors: list[str] = Field(default_factory=list)


class Recommendation(BaseModel):
    ticker: str
    rationale: str
    confidence: float = Field(ge=0.0, le=1.0)


class Watchlist(BaseModel):
    watchlist: list[Recommendation]
    disclaimer: str


class UsageRecord(BaseModel):
    request_id: str
    tokens_in: int
    tokens_out: int
    est_cost_usd: float
    scope: str
    outcome: str
