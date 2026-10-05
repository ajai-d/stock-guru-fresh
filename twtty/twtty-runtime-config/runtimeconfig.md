# runtimeconfig — stock-guru-fresh

This file records **only the settings this project set explicitly**. Anything not listed here uses the
TWTTY methodology default. The full resolved configuration (defaults + the entries below) is
recorded in the iteration's `meta/config` replay-log entry.

It has two parts:
- **Overrides** — settings we changed from a methodology default, grouped by the
  specialization `default-config.md` they override.
- **Runtime** — settings chosen during a run that have no fixed default (e.g. the risk
  level, set at SEED).

```yaml
specialization: sdlc-for-agentic-apps
```

## Overrides

### sdlc-for-agentic-apps — overrides `sdlc-for-agentic-apps/config/default-config.md`

```yaml
tokenomics:
  product: bounded     # per-request cost bounded + logged; the ceilings and degradation
                       # policy are defined in spec §11 (the gate).
                       # Default: product-profile1.md — all caps none.
```

## Runtime

Selected during the run; no fixed default.

```yaml
risk-level: level-2    # assessed/selected at SEED (meta/risk-level); floor L1.
                       # The risk-calibration ladder file itself is inherited.
```
