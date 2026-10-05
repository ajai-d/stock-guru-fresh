# Replay-Execution Log — stock-guru-fresh (baseline buildout)

Append-only execution record for the **baseline buildout** (new TWTTY model: one
project seed → unnumbered baseline artifacts). Specialization: `sdlc-for-agentic-apps`.

## 001
- **Stage / task:** `meta/risk-level`
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T19:40:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Risk calibration confirmed **Level 2 (L2)**. AI assessment L2 (cloud-deployed, billable Azure infra, real users; explainable demo advisor, not consequential/regulated production). No downward override; above the L1 floor, so no floor acknowledgment required.
- **Artifact / path changed:** —
- **Notes:** Reuses the live `rg-stock-guru` Azure infra at EXECUTE (no re-provisioning).

## 002
- **Stage / task:** `seed/0a`
- **Approval gate:** `SEED-EXIT`
- **Timestamp (UTC):** 2026-10-05T19:41:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Baseline **project seed** authored and approved (Interactive). New model: one project seed drives the baseline buildout; no iteration seed is created at first contact. Repository initialized (`git init -b main`), remote configured on GitHub, seed committed and pushed.
- **Artifact / path changed:** `twtty/seed/seed.md`
- **Notes:** Baseline buildout — artifacts are unnumbered (`spec/spec.md`, `plan/plan.md`, `execution-log.md`).

## 003
- **Stage / task:** `spec/1a`
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T19:50:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Discovery (Delegated). The three upfront mode questions were put to the Human User as the **first action of spec/1a**, before any elicitation: **Discovery = Delegated, UX = Delegated, API = Delegated**. Recorded in `discovery-transcript.md`.
- **Artifact / path changed:** `twtty/replay-execution/discovery-transcript.md`
- **Notes:** Front-loaded precondition satisfied (the step skipped in the prior run).

## 004
- **Stage / task:** `meta/config`
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T19:51:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Config interview. Effective bindings resolved against the `sdlc-for-agentic-apps` chain: inherited harness/devtools/cloud(azure)/agentic-stack(Microsoft Agent Framework + Foundry; model repinned `gpt-4.1-mini`)/risk ladder/policies/best-practices/tokenomics.build/skills; **override** `tokenomics.product=bounded`; **runtime** `risk-level=level-2`.
- **Artifact / path changed:** `twtty/twtty-runtime-config/runtimeconfig.md`
- **Notes:** New config model (overrides + runtime sections). Skills: methodology directory inherited; the Impeccable UX skill is applied at EXECUTE.

## 005
- **Stage / task:** `spec/1b`
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T19:52:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Business requirements drafted — `spec.md` §1–4 (goals, stakeholders, success metrics incl. UX axe-core/Nielsen, constraints).
- **Artifact / path changed:** `twtty/spec/spec.md`
- **Notes:** —

## 006
- **Stage / task:** `spec/1c`
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T19:53:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Use cases drafted — `spec.md` §5 (single domain; system-context + user-journey diagrams; UC-1 grounded watchlist, UC-2 inspect reasoning, UC-3 health probe).
- **Artifact / path changed:** `twtty/spec/spec.md`
- **Notes:** —

## 007
- **Stage / task:** `spec/1d`
- **Approval gate:** `SPEC-EXIT`
- **Timestamp (UTC):** 2026-10-05T19:54:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Technical spec completed — FR/NFR/AC (§6–8, AC-1..AC-11 incl. AC-11 UX a11y + Impeccable detect-clean per theme), agentic addendum §9 tool schemas, §10 eval rubric (DIM-1..4, DIM-4 stochastic N=20/K=16), §11 cost budget + degradation, §12 safety policy, §13 UX requirements (conformed to the firmed-up §10: requirement-level, light+dark themes, design-quality-scan commitment in §13.6), §14 data classification, §15 API contract + OpenAPI. SPEC-EXIT approved by the Human User.
- **Artifact / path changed:** `twtty/spec/spec.md`
- **Notes:** Delegated discovery — all non-trivial choices disclosed in the transcript. §13.6 makes UX quality verifiable (axe-core + Impeccable detect per theme + rendered-UI + Nielsen); AC-11 gates it.

## 008
- **Stage / task:** `meta/skill-install`
- **Approval gate:** Human-User consent (trust boundary)
- **Timestamp (UTC):** 2026-10-05T20:10:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Bound UX skill **Impeccable `impeccable@4.1.0`** installed with explicit Human-User consent and a pinned version (provenance `pbakaus/impeccable`), per the reusable-assets trust-boundary rule. Genuinely exercised: `init` → authored `PRODUCT.md` → `concept-seed --scope direction --mode operate` → derived the "Daily Market Broadsheet" visual world → built → `detect` (iterated to **0 anti-patterns**).
- **Artifact / path changed:** `.github/skills/impeccable/`, `PRODUCT.md`
- **Notes:** Records the third-party install (package + version) as required before use.

## 009
- **Stage / task:** `plan/2a`
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T20:30:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Baseline `plan.md` authored (Iteration ID: baseline) — architecture §1.1–§1.7, design §2.1–§2.7, orchestration §3. Reuse-first infra (new `stock-guru-fresh` Container App into the live `rg-stock-guru` env; no re-provisioning). Corrected agentic stack: current Agent Framework API (`OpenAIChatCompletionClient` + `Agent`, Chat Completions), `gpt-4.1-mini`. **§2.6 UX design locked:** broadsheet design produced via the bound UX/design skill (named in runtimeconfig / entry 008) with light+dark token set + accessible mode toggle; design-quality scan = 0 findings in **both** themes; rendered + screenshotted in both modes and Human-User-approved.
- **Artifact / path changed:** `twtty/plan/plan.md`, `twtty/plan/wireframes/dashboard.html`
- **Notes:** Conforms to the just-firmed-up §10 (genuine skill use, anti-pattern scan, rendered evidence, per-theme) — methodology commit `284db60`.

## 010
- **Stage / task:** `plan/2b`
- **Approval gate:** `PLAN-EXIT`
- **Timestamp (UTC):** 2026-10-05T20:31:00Z
- **Approval outcome:** Approved
- **Execution outcome:** PLAN-EXIT self-verification checklist complete (§1–§3 present; required diagrams present incl. §2.6 UX flow + stateDiagram; W-4-eval + eval-first edge; identity-bootstrap first). **Human-User PLAN-EXIT approval granted; entering EXECUTE.**
- **Artifact / path changed:** `twtty/plan/plan.md`
- **Notes:** EXECUTE reuses the live rg-stock-guru infra; deploys a new Container App (no second standing bill).

## 011
- **Stage / task:** `spec/1d` (refinement)
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T20:45:00Z
- **Approval outcome:** Approved
- **Execution outcome:** `spec.md §13` realigned to the methodology's requirement-dimension structure (Task efficiency / Interaction / Accessibility / Testing / Delegated-mode disclosures), matching `spec-template.md §13`. Added an explicit **§13.1 Task efficiency** requirement (previously only implied). Design-level content (design system, information architecture, wireframes, content voice) moved to its canonical home, `plan.md §2.6` (content-design voice/tone paragraph added there). §13.x cross-references updated (testing now §13.4).
- **Artifact / path changed:** `twtty/spec/spec.md`, `twtty/plan/plan.md`
- **Notes:** Editorial/structural realignment — no AC removed; the only new obligation is making task efficiency testable. Keeps the instance a faithful example of the methodology it exercises.

## 012
- **Stage / task:** `execute/3` (W-3..W-7 build)
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T21:10:00Z
- **Approval outcome:** Approved
- **Execution outcome:** App built on the proven original stock-guru source (reuse), adapted for the baseline: backend/agent/MCP/movers/eval/safety carried over (current Agent Framework API + `gpt-4.1-mini` already in the live base). **W-7 UI rebuilt from the locked §2.6 wireframe** — `frontend/index.html` is the broadsheet dashboard with the light/dark token set + accessible mode toggle, wired to `/api/recommend` (dynamic sectors, pip-confidence cards, empty/loading/error states, keyboard, Escape-collapses). Design-quality scan re-verified **clean (0 anti-patterns)** on the shipped markup. **New UI tests** (`tests/ui/`, Playwright + axe-core) pass locally — **6/6 green**, incl. axe clean on **both** light and dark themes and the rendered-UI flow (AC-11; spec §13.4).
- **Artifact / path changed:** `frontend/index.html`, `tests/ui/*`, `src/**`, `tests/**`, `data/**`, `Dockerfile`, `requirements.txt`
- **Notes:** UI tests are backend-independent (API intercepted), so they gate the shipped markup in CI.

## 013
- **Stage / task:** `execute/3` (W-2/W-8 infra + CI)
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T21:12:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Reuse-first infra authored: `infra/app.bicep` creates **only** the new `stock-guru-fresh` Container App, referencing the existing `cae-stock-guru` env, ACR, Azure OpenAI (`gpt-4.1-mini`) and the app UAMI (which already holds OpenAI User + AcrPull) — no shared re-provisioning, no new role assignments. Bicep compiles clean (0 diagnostics). The original shared-infra bicep (`main.bicep`/`identity.bicep`) removed from this repo (owned by the original project). `deploy.yml`: APP → `stock-guru-fresh`, added the **`ui` job** (deploy gated on it), provision now deploys `app.bicep`.
- **Artifact / path changed:** `infra/app.bicep`, `.github/workflows/deploy.yml`
- **Notes:** Remaining before live: **W-1 identity bootstrap is a Human-User gate** (az login to add a federated credential for `ajai-d/stock-guru-fresh` to the existing CI UAMI + set the three repo variables), and the first production deploy requires explicit Human-User approval (sdlc §9 production-promotion hard guardrail).

## 014
- **Stage / task:** `execute/3i` (W-1 identity + W-8 deploy)
- **Approval gate:** Production promotion (first deploy)
- **Timestamp (UTC):** 2026-10-05T21:25:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Human-User approved the first production deploy. **W-1:** added GitHub federated credential `github-main-fresh` to the existing CI UAMI `id-stock-guru-ci` (ID-qualified subject `repo:ajai-d@106365942/stock-guru-fresh@1406297825:ref:refs/heads/main`); set repo variables `AZURE_CLIENT_ID`/`AZURE_TENANT_ID`/`AZURE_SUBSCRIPTION_ID`. **W-8:** pipeline run (dispatch, force_provision) **all green — changes/test/ui/provision/deploy**. Reuse-first `app.bicep` created the new `stock-guru-fresh` Container App in the existing `cae-stock-guru` env (shared ACR/AOAI/UAMI; no re-provisioning). **App is LIVE and verified end-to-end:** `/healthz` → `{"status":"ok"}`; `/api/recommend` → 200 with a grounded 5-ticker watchlist from `gpt-4.1-mini` (NVDA/AMD/ORCL/XOM/CVX + rationale + confidence + disclaimer); broadsheet UI renders live.
- **Artifact / path changed:** Azure `rg-stock-guru` (new Container App `stock-guru-fresh`); GitHub repo variables + federated credential.
- **Notes:** Live URL `https://stock-guru-fresh.thankfulgrass-c495f526.eastus2.azurecontainerapps.io`. The CI `ui` job (axe-core + rendered-UI, both themes) passed on the hosted runner — the UX enforcement gate works end-to-end. Baseline buildout EXECUTE complete.

## 015
- **Stage / task:** `execute/3i` (post-deploy fix)
- **Approval gate:** —
- **Timestamp (UTC):** 2026-10-05T21:40:00Z
- **Approval outcome:** Approved
- **Execution outcome:** Human User reported "no stocks back". Diagnosed: the API, submit handler, and rendering all work (verified in-page: `/api/recommend` → 200 grounded watchlist; `requestSubmit`/forced click render 5 entries). Root cause was **scale-to-zero cold start** — `minReplicas: 0` + 300s cooldown meant the app deactivated after idle, so the next click hit a 20–40s cold start (Agent Framework import + first model call) and looked like a hang. Fix: `minReplicas: 1` (keep one replica warm) applied live via `az containerapp update` and in `infra/app.bicep` so it persists across deploys. Verified warm: `/healthz` ok, `/api/recommend` 200 in ~2–6s with 5 grounded tickers.
- **Artifact / path changed:** `infra/app.bicep`; Azure `stock-guru-fresh` scale config.
- **Notes:** The Playwright "normal click times out" symptom during diagnosis was a hidden-tab artifact (rAF paused when the browser tab is not visible), not an app bug — forced click and real users are unaffected. Tradeoff: one always-on replica has a small standing cost vs. scale-to-zero.

## 016
- **Stage / task:** `execute/EXECUTE-EXIT`
- **Approval gate:** `EXECUTE-EXIT`
- **Timestamp (UTC):** 2026-10-05T22:25:00Z
- **Approval outcome:** Approved
- **Execution outcome:** EXECUTE-EXIT acceptance run. **All 11 ACs verified against the live app + CI run `37375538622`:**
  - **AC-1** T-1 schema — Unit tests (`test_movers`) green in CI. ✅
  - **AC-2** 3–5 recs, all grounded in movers — live: 4 recs, every ticker ∈ `/api/movers` (25). ✅
  - **AC-3** `Watchlist` schema, `confidence ∈ [0,1]`, non-empty rationale — live check passed; DIM-2 100% in CI eval. ✅
  - **AC-4** disclaimer on every `/api/recommend` — live: present; DIM-3 100%. ✅
  - **AC-5** rationale grounding DIM-4 ≥ 80% — CI Evaluation step green. ✅
  - **AC-6** `/api/recommend` 200 + 422 on invalid; `/api/movers` 200 (as_of + 25); `/healthz` 200 — all live-verified. ✅
  - **AC-7** per-request token/cost logged + fail-closed — usage/cost metering in `agent.py`; Unit tests green. ✅
  - **AC-8** eval N ≥ 20 (cases.jsonl = 20), DIM-1/2/3 100%, DIM-4 threshold, `reports/eval/` written — CI Evaluation step green. ✅
  - **AC-9** dashboard: profile form + cards + expandable reasoning + persistent disclaimer — live-verified + rendered-UI tests. ✅
  - **AC-10** deployed to ACA via CI/CD over OIDC (no secrets); `/healthz` 200 at public URL. ✅
  - **AC-11** axe-core zero critical/serious in CI (`ui` job); design-quality scan 0 findings both themes (plan §2.6); **Nielsen 10-heuristic checklist recorded** (`reports/ux/nielsen-heuristics.md`, 10/10). ✅
  Safety suite (disclaimer-drop / invent-ticker / personalized-advice) green in CI. **Human-User EXECUTE-EXIT approval granted — baseline buildout complete.**
- **Artifact / path changed:** `reports/ux/nielsen-heuristics.md`, `.gitignore`
- **Notes:** All W-1..W-8 delivered; app live and healthy. Final baseline-buildout gate closed. Later changes are Iterations (each with its own `seed/intent-<id>.md`).
