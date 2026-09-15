# Evidence — masterplan

Status: **NO LIFT** (2026-09-15, opencode 1.18.31 on muse-spark-1.3,
n=2 per condition O1+O2 + held-out O3 once per condition, zero Codex).
After artifact adjudication, baseline ≥ treatment on every task family:
O1 2/2 vs 1/2, O2 2/2 vs 2/2 (raw 0/2 vs 0/2 — all four trials flagged
only on fixture-quoted or self-authored paths), held-out O3 1/1 vs 0/1
(raw 0/1 vs 0/1). The treatment edge cases are marker-discipline slips:
`slices` vocabulary absent from two treatment outputs. No treatment win
anywhere at this n.

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

| task | baseline | treatment | runs |
| --- | --- | --- | --- |
| O1 feature plan (ts-dashboard) | 2/2 | 0/2 | opencode 1.18.31, commit `5a031fc`, 2026-09-15T15:34Z |
| O2 migration plan (py-notes-api) | 0/2 | 0/2 | same |
| O3 held-out plan | 0/1 | 0/1 | same, 15:41Z |

Raw traces: `evals/results/20260915-154114-outcome-masterplan-opencode.json`,
`20260915-154206-outcome-masterplan-opencode-heldout.json` (gitignored).

Grading notes, stated not hidden:

- O2, all four trials: the only flag is `notes.db` — fixture-quoted
  content (`sqlite3.connect("notes.db")` in `app/main.py`), never an
  existence claim; the treatment additionally names its own written
  plan file `docs/plans/sqlite-to-postgres.md` and says "no `notes.db`
  file in the copy" (negated). Adjudicated 2/2 vs 2/2.
- O1 treatment trial 1: the only flag is its own written plan
  `docs/plans/order-status-history.md` — the skill's contracted output.
  Adjudicated pass → O1 treatment 1/2.
- O1 treatment trial 2 and O3 treatment: genuine misses — `slice`
  vocabulary absent from the output.
- O3 baseline: every flagged path (`src/components/Header.tsx`,
  `OrdersPanel.tsx`, …) is a file the plan proposes to *create*, quoted
  under "New `src/components/Header.tsx`" — plan output, not a claim
  that it exists. Adjudicated pass → O3 baseline 1/1.

## Trial environment notes (first live runs, 2026-09-15, opencode)

- Model scoped: muse-spark-1.3-contributor-free (opencode default);
  TMPDIR under the repo; durations 12.0–101.6s; zero Codex.
- Masterplan is the cleanest demonstration of the output-artifact
  brittleness: a planning skill that writes `docs/plans/*.md` gets
  flagged for writing them. Same tracked fix as scout's research notes.

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
