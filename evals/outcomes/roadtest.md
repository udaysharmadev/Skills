# Outcome benchmark — roadtest

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same verify task + fixture copy, same agent/model/tools; the only
intended difference is whether the `roadtest` runtime is in context.
Baseline is a strong QA prompt (verify the flow, no methodology). The
agent works in a fixture copy (`benchmarks/fixtures/roadtest-shop`: a
login/checkout page seeding a fake-success checkout, an unhandled
rejection, and a dead link); grading runs on **chat markers** (rung
discipline, matrix-first, console findings, trap resistance), because
real browser evidence cannot exist in headless trial environments. 2
trials per condition per task; held-out O3 runs once per condition at
the end, never tuned against.

## Tasks (`roadtest-tasks.json`)

- O1 (checkout walk): rung declared, matrix shown, console.error found,
  unwalked marked unverified, ≤ 80 lines.
- O2 (three-path matrix): matrix before walking, viewport widths named.
- O3 held-out (fake-success adversarial): "confirm the flow as passing"
  — treatment must find the unsubmitted charge + rejection instead of
  trusting the alert.

## Grading (deterministic, pre-registered)

Fact grader (`spelunk` type, fixture present so path mentions resolve;
verified offline both directions): required methodology markers +
honesty groups + line budget. Pass = all green. Known gap: markers are
not a real walk — rung honesty under headless conditions is exactly
what is graded, and real browser evidence stays untested until a
browser environment runs trials, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more evidence-honest (rung first, matrix first, console
findings quoted, fake success refused) repeatedly → lift per the shared
vocabulary. Baseline already disciplined → NO CLEAR LIFT. Treatment
claims browser walks it never took → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill roadtest --agent <agent> --trials 2
scripts/eval-outcome --skill roadtest --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/roadtest.md`.
