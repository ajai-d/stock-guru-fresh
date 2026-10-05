import os

# Safety: the non-advice disclaimer is attached to every recommendation response
# (spec SP-1 / DIM-3). Centralized so it is impossible to drift.
DISCLAIMER = "This is not financial advice."

# Azure OpenAI (spec §4). Auth is via managed identity — no API keys.
AOAI_ENDPOINT = os.getenv("AOAI_ENDPOINT", "")
AOAI_DEPLOYMENT = os.getenv("AOAI_DEPLOYMENT", "gpt-4o-mini")
AOAI_API_VERSION = os.getenv("AOAI_API_VERSION", "2024-10-21")

# Cost controls (spec §11). Per-request caps; the agent fails closed on breach.
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "1500"))
PER_REQUEST_COST_CAP_USD = float(os.getenv("PER_REQUEST_COST_CAP_USD", "0.01"))

# gpt-4o-mini approximate pricing (USD per 1K tokens) — used only to estimate/meter cost.
PRICE_IN_PER_1K = float(os.getenv("PRICE_IN_PER_1K", "0.00015"))
PRICE_OUT_PER_1K = float(os.getenv("PRICE_OUT_PER_1K", "0.0006"))

USAGE_LOG_PATH = os.getenv("USAGE_LOG_PATH", "reports/usage/usage.jsonl")

# When AOAI is not configured (local/CI/offline), the agent uses a deterministic
# stub so the app and tests run without a live model (spec §4 constraint).
USE_STUB_MODEL = os.getenv("USE_STUB_MODEL", "" ) == "1" or not AOAI_ENDPOINT
