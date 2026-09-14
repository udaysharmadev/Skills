# Evidence — masterplan

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
06); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Create repository-grounded, dependency-aware vertical execution slices
(plan executability / groundedness).

## Boundaries

Owns: reality inspection, invariants + AgDR decisions, vertical
dependency-noted slices, safety nets, executable definition of done. Must
route elsewhere: vague briefs → `distill`; one-file fixes → implement;
execution → `pilot`. Must not: plan unopened files, microstep, smuggle
migrations into UI slices, invent independence under parallel-build
pressure.

## Method

- Layer A: 5 trigger cases; bundle smoke (C-005) applies.
- Layer B: 5 scenarios `evals/workflow/scenarios/masterplan.md`
  (MP1–MP5, incl. no-down-path migration, missing-module, and
  horizontal-pressure adversarial); authored, unexecuted.
- Layer C: protocol `evals/outcomes/masterplan.md` + frozen
  `masterplan-tasks.json`. Grader verified offline (vertical passes,
  horizontal fails).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Proxies can't judge dependency honesty or slice quality — blind review
  required at release; proxies only gate groundedness and shape.
- Single-turn runs can't test replan-on-scope-change or
  brief-contradiction routing (MP3 partially covers the residue).
- No tool-call telemetry from headless runners.

## Context audit

SKILL.md ~145 lines, 1 reference (plan template), 0 scripts (justified:
judgment + template). Phase 06 added path-status labels,
uncertainty-first sequencing, and IRREVERSIBLE marking inside existing
structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill masterplan --agent <agent> --trials 2
scripts/eval-outcome --skill masterplan --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
