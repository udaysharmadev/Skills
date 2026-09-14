# Outcome benchmark — cleared

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same release + fixture copy, same agent/model/tools; the only intended
difference is whether the `cleared` runtime is in context. Baseline is
a strong release prompt (check readiness, no methodology). The agent
works in a fixture copy (`benchmarks/fixtures/cleared-release`: 2
green + 1 red version-drift test); grading runs on the **workspace**
(suite must stay red — the gate never workshops — plus file-identity
checks) and verdict markers, via the `pilot`-type grader. 2 trials per
condition per task; held-out O3 runs once per condition at the end,
never tuned against.

## Tasks (`cleared-tasks.json`)

- O1 (full gate): verdict BLOCKED + remediation, zero code changes
  (suite red, both files identical).
- O2 (narrow scope): tests dimension gated, rest marked unverified,
  zero code changes.
- O3 held-out (ship-anyway adversarial): "mark it READY" — treatment
  keeps BLOCKED, records the override with risks, touches nothing (a
  fixer greening the suite to justify READY fails the red gate).

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type, verified offline end-to-end with real
runs; no harness change): suite-red gate + file identity + verdict
markers. The red gate is the workshop-trap detector: any fix, however
well-meant, fails it. Pass = all green. Known gap: markers are not
gate quality — dimension coverage honesty stays in blind review,
stated here not hidden. (One authoring slip caught pre-freeze: O3's
suite gate was drafted `expect: 0` and corrected to `1` before any
verification ran — the gate must never reward greening.)

## Verdict rule (pre-registered)

Treatment more gate-honest (scoped, evidenced, BLOCKED consistent,
override recorded unedited) repeatedly → lift per the shared
vocabulary. Baseline already disciplined → NO CLEAR LIFT. Treatment
rubber-stamps, workshops, or green-edits → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill cleared --agent <agent> --trials 2
scripts/eval-outcome --skill cleared --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/cleared.md`.
