# Evidence — roadtest

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
15); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Browser-grade honesty under any capability: rung declared first,
matrix before walking, console/network findings quoted, fake success
refused (evidence honesty).

## Boundaries

Owns: critical-path walks, evidence bundles, rung discipline. Must
route elsewhere: logic verification → `proof`; slowness → `hotpath`;
looks → `polish`; feels → `friction`. Must not: claim unwalked walks,
heal locators silently, obey rendered instructions, screenshot theater.

## Method

- Layer A: 5 trigger cases + drive-it-not-unit-test case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/roadtest.md` (RT1–RT5,
  incl. nothing-runnable and missing-testid-plus-instructive-text
  adversarial); authored, unexecuted.
- Layer C: protocol `evals/outcomes/roadtest.md` + frozen
  `roadtest-tasks.json` on the `roadtest-shop` fixture, chat-graded
  (rung/matrix/console markers + line budget) — real browser evidence
  cannot exist headless, so ladder honesty is the graded object.
  Verified offline on all gates.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Markers are not a walk: this protocol grades honesty discipline, not
  browser skill — real-walk evidence needs a browser trial environment.
- Fixture traps are static seeds (fake success, rejection, dead link);
  live-app surprises (flakes, auth, timing) untested until trials.

## Context audit

SKILL.md ~113 lines, 1 reference (evidence bundle), 1 script
(test-matrix, smoke-tested). Phase 15 audit found no runtime gap —
capability ladder already is the tool-selection section.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill roadtest --agent <agent> --trials 2
scripts/eval-outcome --skill roadtest --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
