# Nielsen 10 Usability Heuristics — Daily Stock Advisor (baseline)

Acceptance checklist reviewed against the **live** dashboard
(`https://stock-guru-fresh.thankfulgrass-c495f526.eastus2.azurecontainerapps.io/`)
and the shipped `frontend/index.html`, before `EXECUTE-EXIT` (spec §13.4, AC-11).
Reviewer: AI Agent (Delegated UX mode). Date: 2026-10-05.

| # | Heuristic | Verdict | Evidence / notes |
|---|-----------|:------:|------------------|
| 1 | **Visibility of system status** | Pass | Submit immediately disables the button and shows skeleton cards; results show an "As of … · N ideas" status line; the mode toggle reflects state via `aria-pressed` and a changing label. One warm replica keeps first-response latency ~2s (cold-start hang fixed). |
| 2 | **Match between system and the real world** | Pass | Language mirrors the financial-press domain — "watchlist", "movers", "confidence", "Not financial advice". Confidence is shown as a familiar pip meter **plus** the numeric value. No developer jargon in the UI. |
| 3 | **User control and freedom** | Pass | No irreversible actions. Reasoning expands/collapses on demand; **Escape** collapses an expanded card. The user can re-submit with a changed profile at any time; light/dark is user-switchable. |
| 4 | **Consistency and standards** | Pass | Standard web controls (radiogroup, checkboxes, submit button) with native semantics; one consistent broadsheet design system via CSS tokens; identical component treatment across light and dark themes. |
| 5 | **Error prevention** | Pass | The profile ships valid defaults (Medium risk, Technology selected) so an empty/invalid submit is not possible from the UI; risk is a constrained radiogroup; the API rejects malformed bodies with 422 (AC-6). |
| 6 | **Recognition rather than recall** | Pass | Everything needed is on one screen — risk options, sector list, and the always-visible "Not financial advice" notice. Each recommendation carries its own rationale and source framing, so the user need not remember prior context. |
| 7 | **Flexibility and efficiency of use** | Pass | Single-page, one primary task; full keyboard operability (tab order, visible focus, Enter submits, Escape collapses). Expandable reasoning is progressive disclosure — fast path for scanners, detail on demand. |
| 8 | **Aesthetic and minimalist design** | Pass | Distinctive but restrained editorial layout; no decorative clutter; the design-quality/anti-pattern scan reports **0 findings** on both themes (AC-11). Every element serves the task. |
| 9 | **Help users recognize, diagnose, and recover from errors** | Pass | On API failure the results area shows a plain, non-alarming message ("Could not produce a grounded watchlist. Please try again."); the submit button re-enables so the user can retry. Verified by the `error state` UI test. |
| 10 | **Help and documentation** | Pass (proportional) | The standfirst explains what the product does and its limits; the rail note states "No account. No data stored."; the persistent disclaimer sets expectations. For a single-task tool no separate help system is warranted. |

**Result:** 10 / 10 heuristics reviewed — no blocking usability issues. The one
issue found during review (cold-start latency reading as a hang) was fixed by
keeping one replica warm; re-reviewed under heuristic #1 as Pass.
