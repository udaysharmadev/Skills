# Outcome benchmark — concierge

Status: protocol + tasks frozen 2026-09-14; trials execute via
`scripts/eval-outcome`. Numbers appear only with full provenance.

## Design

Same routing task, same agent/model/tools; the only intended difference
is whether the `concierge` runtime (SKILL.md + references) is in context.
Baseline sees exactly what a runtime shows: skill names + descriptions.
Treatment additionally follows the concierge methodology. 3 trials per
condition per task (stochastic output); held-out task O3 runs once per
condition at the end and is never used for tuning.

## Tasks (`concierge-tasks.json` — the machine-readable twin of this file)

### O1 — bug report, minimal chain

Request: "Login is broken."
Expected: subset of {spelunk, sleuth, proof, roadtest} in that relative
order, must include `sleuth`, max 3 skills, nothing outside the set.
Metric: pass rate + over-route count (skills outside the necessary set).

### O2 — tiny task, direct

Request: "Rename the login button to Sign in."
Expected: `direct`. Anything else (a plan chain, a skill dispatch) is
over-routing. Metric: pass rate.

### O3 — held-out: research-then-build chain

Request: "Research the correct Stripe webhook approach and then implement it."
Expected: subset of {scout, backend, proof} in order, max 3.
Runs after O1/O2 analysis; never tuned against.

## Verdict rule (pre-registered)

- Treatment pass-rate clearly above baseline with shorter-or-equal chains
  and zero gate-skips → `PROVEN LIFT` (O-tasks) — reported with n.
- Same pass rate, lower variance → `CONSISTENCY LIFT`.
- Same outcomes, fewer tool calls/turns → `EFFICIENCY LIFT`.
- Baseline already perfect → `NO CLEAR LIFT` (kept visible).
- Treatment worse → `REGRESSION` (preserved).

## Reproduce

codex is gated by the paid-agent guard (see `evals/adapters/README.md`):
both `--allow-paid` and `ALLOW_PAID_AGENT=1` are required, set only by
the human authorizing that run.

```bash
ALLOW_PAID_AGENT=1 scripts/eval-outcome --skill concierge --agent codex --trials 3 --allow-paid
ALLOW_PAID_AGENT=1 scripts/eval-outcome --skill concierge --agent codex --trials 1 --heldout --allow-paid
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/concierge.md`.
