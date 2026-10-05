"""Minimal MCP server exposing the day's market movers as a tool (spec T-1).

Runnable standalone over stdio: `python -m src.app.mcp_server`. The FastAPI app
uses the same `MoversProvider`; this module is the MCP tool surface.
"""
from .models import MoversResponse
from .movers import default_provider

try:
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("stock-guru-movers")

    @mcp.tool()
    def get_market_movers(limit: int = 25) -> dict:
        """Return the day's candidate market movers (top gainers/losers)."""
        return get_movers(limit).model_dump()

    def _run() -> None:
        mcp.run()

except ImportError:  # pragma: no cover - mcp optional at runtime
    mcp = None

    def _run() -> None:
        raise SystemExit("mcp package not installed")


def get_movers(limit: int = 25) -> MoversResponse:
    """Plain callable used by the API and tests (tool implementation)."""
    return default_provider().get(limit)


if __name__ == "__main__":  # pragma: no cover
    _run()
