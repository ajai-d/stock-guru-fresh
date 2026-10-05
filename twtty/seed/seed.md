## What I Want To Build

An AI "Daily Stock Advisor." An MCP server exposes the day's market movers
(top gainers/losers) as a tool; an LLM agent reads a user's risk profile and
sectors of interest and produces a concise, reasoned watchlist — 3–5 tickers,
each with a one-line rationale and a confidence score, grounded strictly in the
movers data. A clean web dashboard lets the user set their profile and view the
latest recommendations, with the agent's reasoning available on demand. For
retail investors who want a fast, explainable daily starting point. (Explicitly
not financial advice.)

## Done Looks Like

- MCP server returns the day's candidate movers (a live market-data source, or a
  seeded/stubbed feed for offline runs).
- The agent outputs 3–5 tickers with a one-line rationale + confidence, every
  ticker present in the input movers (no invented symbols).
- Web UI: a profile form (risk tolerance + sectors) and a dashboard of
  recommendation cards with expandable reasoning and a persistent
  "not financial advice" disclaimer.
- Evaluations cover grounding (recommended ⊆ movers), output-schema validity,
  and the safety disclaimer always present.
- Per-recommendation token/cost is bounded and logged.
- Clone-and-run locally; unit tests + evals pass.
