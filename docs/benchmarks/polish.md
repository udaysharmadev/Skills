# Evidence — polish

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
11); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Deliberate UI improvement inside the existing design system (slop
removal / restraint, states completeness).

## Boundaries

Owns: visual audit, direction-first redesign, token convergence, state
completeness. Must route elsewhere: task flows → `friction`; recreation
from screenshot/URL → `ditto`; browser-flow proof → `roadtest`. Must
not: rewrite tokens for novelty, apply banned patterns thoughtlessly,
claim visual verification without rendering.

## Method

- Layer A: 5 trigger cases + subtle-tweaks case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/polish.md` (PO1–PO5,
  incl. no-render-toolchain and make-it-pop adversarial); authored,
  unexecuted. Signature P1–P3 remain as cross-checks.
- Layer C: protocol `evals/outcomes/polish.md` + frozen
  `polish-tasks.json` on the `polish-dashboard` fixture with artifact
  grading (slop-hex scan, token byte-identity, state markers, Direction
  line). Grader verified offline on all gates.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Static string checks are not visual judgment: taste, hierarchy, and
  "deliberate" feel stay in blind review.
- Token byte-identity fails formatting-only rewrites; trials must record
  whether a tokens_changed failure was semantic or cosmetic.
- No screenshot rendering in headless runs; before/after evidence needs a
  browser environment at trial time (recorded per trial).

## Context audit

SKILL.md ~145 lines, 1 reference (audit checklist). Phase 11 added Tool
selection/fallback, a no-render stop condition, and a dark-theme audit
bullet — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill polish --agent <agent> --trials 2
scripts/eval-outcome --skill polish --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
