# Evidence — headroom

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
10); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Design scale proportionally with explicit trigger points (capacity
reasoning / restraint).

## Boundaries

Owns: workload numbers, dimension walk, Now/Next/Scale + triggers,
don't-do-yet list. Must route elsewhere: documenting what exists →
`blueprint`; slow endpoints → `hotpath`; implementation → `backend`.
Must not: cargo-cult numbers, resume-driven design, scale redesign for
correctness bugs.

## Method

- Layer A: 5 trigger cases + boring-brief case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/headroom.md` (HR1–HR5,
  incl. no-numbers and billion-user adversarial); authored, unexecuted.
- Layer C: protocol `evals/outcomes/headroom.md` + frozen
  `headroom-tasks.json` (tiny/growing/large). Grader verified offline.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
timestamp per trial, failures preserved.

## Limitations (known before first run)

- No fixture grounding: tasks are pure briefs; arithmetic honesty is
  proxied by digit/trigger presence, not recomputation.
- Endorsement-vs-mention gap for rejected tech (documented above).
- Usefulness of the gaps-between-levels stays in blind review.
- No tool-call telemetry from headless runners.

## Context audit

SKILL.md ~100 lines (smallest runtime in the suite), 1 reference
(dimensions). Phase 10 added tail-latency, cache-failure, and queue-
economics depth to the reference only — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill headroom --agent <agent> --trials 2
scripts/eval-outcome --skill headroom --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
