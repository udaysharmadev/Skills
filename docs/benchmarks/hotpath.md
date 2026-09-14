# Evidence — hotpath

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
18); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Measured optimization: profile-named hot paths, one structural change,
identical re-measurement, delta or revert (measurement honesty).

## Boundaries

Owns: target setting, baselines, hot-path evidence, structural fixes,
delta reports. Must route elsewhere: wrong behavior → `sleuth`;
scale questions → `headroom`; architectural needs → decision routing.
Must not: vibe-tune, micro-tune cold paths, hardcode, drift semantics,
estimate numbers.

## Method

- Layer A: 5 trigger cases + no-blind-optimization case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/hotpath.md` (HP1–HP5,
  incl. unmeasurable-here and faster-by-Friday adversarial); authored,
  unexecuted.
- Layer C: protocol `evals/outcomes/hotpath.md` + frozen
  `hotpath-tasks.json` on the `hotpath-orders` fixture via the
  workspace grader — deterministic scan counts + golden totals on two
  workloads separate structural fixes from micro-tunes, hardcodes, and
  drift. Verified offline end-to-end (real runs, all gates).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Counts are not latency: wall-clock deltas need trial environments
  with declared conditions; the fixture proves the discipline, not the
  milliseconds.
- One bottleneck shape (scan-per-lookup); other regimes (waterfalls,
  bundles, GC) get scenario coverage only until fixtures grow.

## Context audit

SKILL.md ~135 lines, 1 reference (measurement toolbox), 1 script
(measure-report). Phase 18 added Prerequisites and Tool
selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill hotpath --agent <agent> --trials 2
scripts/eval-outcome --skill hotpath --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
