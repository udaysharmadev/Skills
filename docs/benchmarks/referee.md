# Evidence — referee

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
17); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Independent review: intent before quality, scope flagged, pressure
resisted (review independence).

## Boundaries

Owns: intent pass, quality pass, severity-honest findings, verdicts.
Must route elsewhere: live debugging → `sleuth`; architecture →
`headroom`; test strategy → `proof`; approach questions → conversation.
Must not: rubber-stamp, manufacture findings, nit-block, skim giant
context-free diffs.

## Method

- Layer A: 5 trigger cases + blockers-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/referee.md` (RF1–RF5,
  incl. context-free giant diff and hurry-up approve adversarial);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/referee.md` + frozen
  `referee-tasks.json` on the `referee-change` fixture, chat-graded
  (verdict, disclosure, intent/scope markers, 60-line anti-essay
  budget) — review judgment has no executable oracle, so marker
  discipline is the graded object. Verified offline on all gates.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Markers are not judgment: severity honesty and finding depth stay in
  blind review.
- One brief shape (caps + missing override + smuggled refactor);
  generalization untested until trials.

## Context audit

SKILL.md ~135 lines, 1 reference (finding format + checklist). Phase 17
added Prerequisites and Tool selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill referee --agent <agent> --trials 2
scripts/eval-outcome --skill referee --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
