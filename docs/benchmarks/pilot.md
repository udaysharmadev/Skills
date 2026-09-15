# Evidence — pilot

Status: **NO LIFT on available evidence** (2026-09-15, opencode 1.18.31
on muse-spark-1.3, n=2 per condition O1+O2 + held-out O3 once per
condition, zero Codex). O1 1/2 vs 1/2, O2 2/2 vs 2/2, held-out O3 1/1
vs 0/1. Both treatment failures made zero file edits after a harness
`.env` read auto-rejection derailed the run — an environment event the
baseline also encountered (O1 baseline trial 1 was derailed, recovered,
made the edit, and still failed on the missing verification marker).
With the derails excluded the tallies are unchanged and there is no
treatment win anywhere at this n; the held-out split is confounded and
needs a re-run before any regression claim.

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

| task | baseline | treatment | runs |
| --- | --- | --- | --- |
| O1 small feature (ts-dashboard) | 1/2 | 1/2 | opencode 1.18.31, commit `5a031fc`, 2026-09-15T15:34Z |
| O2 small fix (py-notes-api) | 2/2 | 2/2 | same |
| O3 held-out cleanup (ts-dashboard) | 1/1 | 0/1 | same, 15:39Z |

Raw traces: `evals/results/20260915-153948-outcome-pilot-opencode.json`,
`20260915-154053-outcome-pilot-opencode-heldout.json` (gitignored).

Grading notes, stated not hidden: no path/contaminant artifacts fired.
Every failure is the `verif` chat marker — the workspace gates (scope
containment, check exits) passed wherever edits were made, so this page
measures verification-reporting discipline, not edit quality. Both
treatment failures (O1 t1, O3) made zero edits: each run hit the
harness's `.env` read auto-rejection (the fixture contains `.env`; the
agent attempts it, opencode auto-rejects, the run derails) and never
recovered to the edit phase. The O1 baseline trial 1 hit the same
rejection, recovered, edited in scope — and still failed `verif`. O3
baseline passed all gates on real edits.

## Trial environment notes (first live runs, 2026-09-15, opencode)

- Model scoped: muse-spark-1.3-contributor-free (opencode default);
  TMPDIR under the repo; durations 9.4–80.2s; zero Codex.
- Known confound, first seen here: `.env` read auto-rejection derails
  weak runs. Fix candidates (pre-authorize the sandbox read, or drop
  `.env` from the fixture) are tracked; the O3 split does not support
  a regression claim until a clean re-run exists.

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
