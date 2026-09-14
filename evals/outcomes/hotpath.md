# Outcome benchmark — hotpath

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same slowdown + fixture copy, same agent/model/tools; the only intended
difference is whether the `hotpath` runtime is in context. Baseline is
a strong optimizer prompt (make it faster, no methodology). The agent
works in a fixture copy (`benchmarks/fixtures/hotpath-orders`: per-line
catalog scans with a cold formatting decoy); grading runs on the
**workspace** (deterministic work-count + golden-output checks recorded
pre-cleanup, scope containment) plus report markers, via the
`pilot`-type grader. Wall-clock timing is deliberately NOT graded
(shared runners make it flaky); operation counts are the evidence. 2
trials per condition per task; held-out O3 runs once per condition at
the end, never tuned against.

## Tasks (`hotpath-tasks.json`)

- O1 (structural fix): measure, kill the scans, identical re-measure,
  delta + perf lock test, semantics identical on two workloads.
- O2 (micro-tune bait): "speed up the formatting loop" — treatment
  must profile first and fix the scans instead.
- O3 held-out (faster-by-Friday adversarial): "don't care how" —
  treatment still measures first and proves identical semantics.

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type, verified offline end-to-end with real
runs): scan-count bound + golden totals on two workloads + lock-test
presence + scope kept + report markers. Count and goldens separate
structural fixes from micro-tunes, hardcodes, and rewrites that drift.
Pass = all green. Known gap: counts are not latency — real timing
deltas stay in trial review with conditions, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more measurement-honest (profile named it, one change, delta
reported, correctness held) repeatedly → lift per the shared
vocabulary. Baseline already disciplined → NO CLEAR LIFT. Treatment
micro-tunes, hardcodes, or drifts semantics → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill hotpath --agent <agent> --trials 2
scripts/eval-outcome --skill hotpath --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/hotpath.md`.
