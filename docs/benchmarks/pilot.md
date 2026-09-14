# Evidence — pilot

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
07); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Execute work slice-by-slice and prove each slice before moving on (scope
adherence / honest verification).

## Boundaries

Owns: per-slice loop, risk-set verification floor, TDE, diff review,
decision log, completion gate. Must route elsewhere: architecture/scope
changes → `masterplan`; suite strategy → `proof`; slice tests stay here.
Must not: improvise scope, weaken tests to green, spoof APIs, absorb
dirty user state, ping-pong trivia back to planning.

## Method

- Layer A: 5 trigger cases + plan-reality sibling; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/pilot.md` (PI1–PI5,
  incl. pre-existing breakage and "just make it green" adversarial);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/pilot.md` + frozen
  `pilot-tasks.json` with workspace grading (scope + check exits).
  Grader verified offline on synthetic observations.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Fixture suites aren't runnable (seeded gap) → test-exit grading is
  thin until a runnable fixture exists; scope containment carries O1/O3.
- Single-turn runs can't test multi-slice loops, deviation accumulation,
  or replan ping-pong — only single-slice residue. Multi-turn harness
  stays future work.
- Report-marker checks (`verif`) are blunt; blind review judges honesty
  at release.

## Context audit

SKILL.md ~145 lines, 1 reference (completion gate), 0 scripts (justified:
loop discipline + review, nothing deterministic to extract). Phase 07
added decision log, dirty-tree rule, replan materiality, proof boundary —
all inside existing structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill pilot --agent <agent> --trials 2
scripts/eval-outcome --skill pilot --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
