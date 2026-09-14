# Outcome benchmark — headroom

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same workload brief, same agent/model/tools; the only intended difference
is whether the `headroom` runtime is in context. Baseline is a strong
designer prompt (proportionate recommendation with reasons). No fixture:
design tasks need numbers, not repos. 2 trials per condition per task;
held-out O3 runs once per condition at the end, never tuned against.

## Tasks (`headroom-tasks.json`)

- O1 (tiny: 50 users → maybe 500): must reason with triggers, state
  restraint explicitly, stay ≤ 60 lines. Premature machinery is the
  failure — caught structurally where possible (see limitation).
- O2 (growing: 10k → 200k, read-heavy): triggers + Next-level substance,
  ≤ 120 lines.
- O3 held-out (large, spiky, global): triggers + overload/partition
  substance, ≤ 150 lines.

## Grading (deterministic, pre-registered)

Fact-grader without fixture (path check vacuous; fixed this phase after
offline testing exposed the crash): `must_contain` + honesty any-groups
+ `max_lines`. Verified offline: boring-with-triggers passes; K8s-bloat
without triggers fails. Known gap: endorsement-vs-mention for rejected
tech (saying "don't use Kubernetes" contains the word) — needs blind
review at release, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more proportional (triggers + restraint + arithmetic)
repeatedly → lift per the shared vocabulary. Baseline already boring →
NO CLEAR LIFT. Treatment distributes prematurely → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill headroom --agent <agent> --trials 2
scripts/eval-outcome --skill headroom --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/headroom.md`.
