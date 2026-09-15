# Evidence — distill

Status: **NO LIFT** (2026-09-15, opencode 1.18.31 on muse-spark-1.3,
n=2 per condition O1+O2 + held-out O3 once per condition, zero Codex).
Baseline ≥ treatment on every task family: O1 2/2 vs 1/2 (treatment
trial 1 returned a 15-line brief with no non-goals section and no
numbered assumptions), O2 2/2 vs 2/2, held-out O3 0/1 vs 0/1 (both
conditions miss the non-goal marker and the security-surface group). No
artifacts to adjudicate — every failure is a genuine marker miss. The
one treatment regression is a marker-discipline slip at n=1; the O2 tie
is at ceiling.

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

| task | baseline | treatment | runs |
| --- | --- | --- | --- |
| O1 vague spec (ts-dashboard) | 2/2 | 1/2 | opencode 1.18.31, commit `5a031fc`, 2026-09-15T15:35Z |
| O2 short request (py-notes-api) | 2/2 | 2/2 | same |
| O3 held-out contradiction spec | 0/1 | 0/1 | same, 15:38Z |

Raw traces: `evals/results/20260915-153842-outcome-distill-opencode.json`,
`20260915-153858-outcome-distill-opencode-heldout.json` (gitignored).

Grading notes, stated not hidden: no grader artifacts fired on any
distill trial (no path flags after the workdir/dotfile fixes; nothing to
adjudicate). O1 treatment trial 1 is the only treatment failure: a
15-line brief missing the `non-goal` marker and the assumption group.
O3 fails both conditions on the same two gates (no non-goals, no
security/auth surface mentioned) — a genuine held-out miss for both.

## Trial environment notes (first live runs, 2026-09-15, opencode)

- Model scoped: muse-spark-1.3-contributor-free (opencode default);
  TMPDIR under the repo; durations 6.0–36.2s; zero Codex.

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
