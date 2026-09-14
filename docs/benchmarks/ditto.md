# Evidence — ditto

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
13); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Loop-closed UI reproduction: tokens first, compare rounds quoted,
placeholders for owned assets, traps refused (rebuild fidelity /
untrusted-source discipline).

## Boundaries

Owns: source inspection, token inference/mapping, compare-correct loop,
responsive inference marking, rights placeholders. Must route elsewhere:
a *better* version → `polish`; napkin intent → `polish` discipline;
flow proof → `roadtest`. Must not: copy secrets or owned assets, obey
embedded instructions, claim unseen views inspected, eyeball once.

## Method

- Layer A: 5 trigger cases + placeholders-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/ditto.md` (DT1–DT5,
  incl. auth-walled fetch and injection-plus-secret adversarial);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/ditto.md` + frozen
  `ditto-tasks.json` on the `ditto-source` fixture via the shared
  artifact grader (token markers, structure, trap/asset absence,
  loop/rung markers). Grader verified offline on all gates.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Marker presence is not visual fidelity: whether the clone actually
  matches stays in blind review with screenshots.
- The trap is one injection shape + one secret shape; real pages vary —
  generalization is untested until trials.
- No screenshot rendering in headless runs; round evidence needs a
  browser environment at trial time (recorded per trial).

## Context audit

SKILL.md ~125 lines, 1 reference (sourcing rules + compare method).
Phase 13 added Tool selection/fallback consolidating the four
capability rungs — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill ditto --agent <agent> --trials 2
scripts/eval-outcome --skill ditto --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
