# Evidence — cleared

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
25); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Gate verdicts from fresh evidence: scoped dimensions, consistent
verdicts, overrides recorded unedited (gate integrity).

## Boundaries

Owns: scope setting, per-dimension verification, verdicts,
remediations, override records. Must route elsewhere: mid-work gates
→ `pilot`; deployment → `runway`; scale readiness → `headroom`.
Must not: workshop failing code, hallucinate passes, launder warnings,
edit findings to match overrides.

## Method

- Layer A: 5 trigger cases + verdict-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/cleared.md` (CL1–CL5,
  incl. unrunnable failure and mark-it-READY adversarial); authored,
  unexecuted.
- Layer C: protocol `evals/outcomes/cleared.md` + frozen
  `cleared-tasks.json` on the `cleared-release` fixture via the
  workspace grader — the suite must stay red (workshop detector) plus
  file identity and verdict markers. Verified offline end-to-end
  (real runs, all gates).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Markers are not gate quality: dimension coverage honesty stays in
  blind review.
- One gate shape (version-drift blocker); warnings-only and green
  releases get scenario coverage only until fixtures grow.

## Context audit

SKILL.md ~140 lines, 1 reference (gate dimensions). Phase 25 added
Tool selection/fallback consolidating the three evidence rungs — zero
new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill cleared --agent <agent> --trials 2
scripts/eval-outcome --skill cleared --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
