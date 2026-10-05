# Discovery Transcript — Daily Stock Advisor (baseline buildout)

Delegated discovery (the AI Agent decides and discloses). Specialization:
`sdlc-for-agentic-apps`. Recorded as the `spec/1a` discovery record.

## Upfront mode questions (front-loaded precondition, asked before any elicitation)

| Question | Answer |
|----------|--------|
| Discovery mode | **Delegated** |
| UX mode | **Delegated** |
| API mode | **Delegated** |

These three were put to the Human User as the first action of `spec/1a`, before
reading beyond the project seed and before drafting any spec content.

## Config interview (bindings) — `meta/config`

Resolved against the `sdlc-for-agentic-apps` default-config chain:

- **Inherited unchanged:** `harness` (GitHub Copilot), `devtools` (GitHub),
  `cloud` (azure), `agentic-stack` (Microsoft Agent Framework on Azure AI
  Foundry — model repinned to `gpt-4.1-mini`, the current deployable small
  model), `risk-calibration` ladder (default), `policies`, `best-practices`,
  `tokenomics.build`, `reusable-assets.skills` (the methodology skills
  directory; the applicable **Impeccable** UX skill is applied at EXECUTE).
- **Override:** `tokenomics.product = bounded` (per-request cost bounded + logged;
  ceilings in spec §11).
- **Runtime:** `risk-level = level-2` (SEED).

Recorded in `twtty/twtty-runtime-config/runtimeconfig.md` (overrides + runtime).

## Key Delegated decisions disclosed (with rationale)

| Area | Decision | Rationale |
|------|----------|-----------|
| Scope | Single domain, 3 use cases (grounded watchlist, inspect reasoning, health probe) | Minimal coherent product; matches the seed's "done looks like" |
| Grounding | Hard 100% grounding (recommended ⊆ movers), enforced at the response boundary | Core safety property; prevents fabricated tickers |
| Eval | Hybrid: programmatic DIM-1/2/3 (deterministic) + LLM-judge DIM-4 (stochastic, N=20, K=16) | §10 requires stochastic dimensions use a multi-run pass rule at gate time |
| Model | Azure OpenAI `gpt-4.1-mini` via managed identity (no keys) | Current deployable small model (gpt-4o-mini:2024-07-18 is blocked for new deployments); keyless per cloud/azure.md |
| UX | §13.6 Testing added: axe-core in CI + rendered-UI test + Nielsen checklist | The prior run asserted UI quality instead of verifying it; make it mechanical |
| API | REST/JSON, 3 endpoints, disclaimer as a response field, OpenAPI contract in CI | Minimal surface consumed by its own UI; contract verified, not assumed |
| Infra | Reuse existing `rg-stock-guru` (no re-provisioning) | Avoids a second bill; exercises the reuse-first identity path |
