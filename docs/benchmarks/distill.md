# Evidence — distill

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
05); zero baseline-vs-skill trials executed — zero-spend policy. This
page publishes no number it cannot point at.

## Primary claim

Turn vague intent into implementation-grade requirements without needless
questions (ambiguity removed, questions minimized).

## Boundaries

Owns: goal extraction, materiality-tested questions (≤5, batched),
repo-first grounding, scaled briefs, numbered assumptions. Must route
elsewhere: unsettled product decisions → `hotseat`; precise requests →
straight to planning; mechanical micro-fixes → just do it. Must not:
interrogate, invent requirements, brief nonexistent surfaces, absorb
smuggled scope.

## Method

- Layer A: 6 trigger cases; bundle smoke (C-005) applies.
- Layer B: 5 scenarios `evals/workflow/scenarios/distill.md` (DI1–DI5,
  incl. contradiction, missing-surface, and scope-smuggling cases);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/distill.md` + frozen
  `distill-tasks.json` (grounding + scale-budget traps on seeded
  fixtures). Grader (recall + honesty groups + path-existence +
  max_lines) verified offline against synthetic outputs.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Single-turn headless runs can't test the interrogation dynamic (max-5
  batching, one-pass confirmation) — only its residue: assumptions over
  questions. Multi-turn harness stays future work.
- Line budgets (200/30/200) are blunt proxies for "scaled right"; blind
  review judges proportionality at release.
- No tool-call telemetry from headless runners.

## Context audit

SKILL.md ~125 lines, 1 reference (brief template + worked example), 0
scripts (justified: judgment + template, nothing to compute). Phase 05
reordered grounding before questions and added the materiality test
inside existing structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill distill --agent <agent> --trials 2
scripts/eval-outcome --skill distill --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
