# UX design — Daily Stock Advisor

## Platform

web

## Stack

Python 3.12 + FastAPI backend serving a static single-page frontend (established by
the spec constraints; backend is Azure-deployed via Container Apps). Frontend is a
single accessible HTML/CSS/JS page served at `/`.

## Users

Primary user: a **retail investor** checking in **once a day**, usually mornings
before or near market open, on desktop or phone. They are not professionals and do
not have a Bloomberg terminal; they want a fast, explainable *starting point* for
what to pay attention to today — not a trade to execute. State of mind: curious,
time-pressed, slightly wary of hype.

## Product Purpose

Turn the day's market movers into a small, **explained** watchlist. The user sets a
risk tolerance and sectors of interest and receives **3–5 tickers**, each drawn
strictly from today's movers, with a one-line rationale and a calibrated confidence
score. Success = the user leaves with a short, trustworthy list of things to look
into, understanding *why* each is there, and clearly aware this is **not financial
advice**.

## Positioning

The mechanism a neighboring product cannot truthfully copy: **every recommendation
is grounded in the day's actual movers — the system never invents a ticker — and
every pick shows its work** (the source mover and a plain-language reason) with an
honest confidence score. It is an *explainable, grounded daily shortlist*, not a
black-box signal, a hot-stock newsletter, or a brokerage's buy/sell call.

## Operating Context

A daily ritual: open once, set/confirm a profile, read a handful of cards, maybe
expand one or two for the reasoning, close. No portfolio, no account, no execution.
The cultural world around it is the **daily financial press and the almanac/tip-sheet
tradition** — morning market columns, the broadsheet markets page, the curated daily
list — not a trading terminal (the user does not operate one).

## Capabilities and Constraints

- Movers tool returns the day's candidate gainers/losers (live source or seeded feed
  offline); recommend tool returns 3–5 grounded tickers with rationale + confidence.
- Hard grounding: recommended tickers are a strict subset of the movers (no
  fabrication), enforced at the response boundary.
- Public, non-sensitive data only. **No PII, no accounts, no persistence**; the
  in-session profile (risk + sectors) is not stored.
- Per-recommendation model cost is bounded and logged; the model is reached via
  managed identity (no keys).
- Terminology: *movers*, *watchlist*, *rationale*, *confidence*, *source mover*.

## Brand Commitments

- Name: **Daily Stock Advisor**.
- Voice: plain, calm, non-hype, honest about uncertainty. Never prescriptive
  ("buy/sell"); always framed as a starting point.
- A persistent, unmissable **"Not financial advice"** statement is mandatory and
  must always be visible.

## Evidence on Hand

Real content the design must carry: a ticker symbol, company name, sector, a signed
percent change, a price, a one-line rationale, and a confidence value in [0,1], per
card, for 3–5 cards; plus an "as of" date. No testimonials, customers, prices, or
benchmarks exist — future work must not fabricate any.

## Product Principles

1. **Grounded or nothing** — never show a ticker that isn't in today's movers; show
   the source mover behind every pick.
2. **Show the reasoning** — a pick without a plain-language "why" is not shippable.
3. **Honest confidence** — confidence is a first-class, legible value, never implied
   by color alone.
4. **Calm, not hype** — the tone and visuals must read as a trustworthy daily brief,
   not a trading-floor adrenaline screen.
5. **Safety travels with the data** — the "not financial advice" frame is always
   present, in the UI and in the API response.

## Accessibility & Inclusion

WCAG 2.2 AA minimum: contrast ≥ 4.5:1 (text) / 3:1 (UI + large text), full keyboard
operability, accessible names/roles, confidence exposed to assistive tech (not
color-only), responsive from 360px. Automated axe-core checks run in CI.
