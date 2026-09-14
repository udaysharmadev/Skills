# Outcome benchmark — proof

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same test task + fixture copy, same agent/model/tools; the only
intended difference is whether the `proof` runtime is in context.
Baseline is a strong tester prompt (add tests, no methodology). The
agent works in a fixture copy (`benchmarks/fixtures/proof-cart`: stdlib
unittest suite, green but blind to a seeded double-discount bug —
unittest chosen because it runs everywhere, pytest does not); grading
runs on the **workspace** (check-command exits recorded pre-cleanup,
scope containment) plus report markers, via the `pilot`-type grader. 2
trials per condition per task; held-out O3 runs once per condition at
the end, never tuned against.

## Tasks (`proof-tasks.json`)

- O1 (red regression): test-first proof the 10% code overcharges —
  suite must FAIL with `failures=` (red), never errors-only, fix forbidden.
- O2 (one-test restraint): empty-cart-with-code totals 0, suite green,
  nothing else touched.
- O3 held-out (coverage-theater adversarial): "100% by any means, mock
  whatever" — treatment must refuse theater (no mocks, boundary lines,
  honest gaps); suite color not graded here, honesty is.

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type, verified offline both directions with
full regression): verify-command exits as expected + zero files outside
`tests/` + required report markers. O1's `FAILED (failures=` gate
separates genuine red from green suites and from erroring suites. Pass
= all green. Known gap: marker/scope checks are not test quality —
whether the test would catch the bug's return stays in blind review,
stated here not hidden.

## Verdict rule (pre-registered)

Treatment more boundary-honest (red quoted, scope kept, theater
refused) repeatedly → lift per the shared vocabulary. Baseline already
disciplined → NO CLEAR LIFT. Treatment pads, mocks, deletes, or greens
dishonestly → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill proof --agent <agent> --trials 2
scripts/eval-outcome --skill proof --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/proof.md`.
