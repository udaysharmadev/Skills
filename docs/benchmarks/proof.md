# Evidence — proof

Status: **MIXED** (2026-09-15, opencode 1.18.30, n=2 per condition +
held-out once per condition, zero Codex). Treatment shows lift on
red-regression discipline (O1 2/2 vs baseline 0/2); no lift available
on one-test restraint (O2 2/2 both) or held-out honesty markers (O3
0/1 both); no regressions anywhere (treatment never worse).

## Primary claim

The right test at the right boundary, proven red before claimed green
(boundary honesty / regression lock).

## Boundaries

Owns: behavior naming, boundary choice, refactor-proof tests, mocking
discipline, flake disposition, regression locks. Must route elsewhere:
cause unknown → `sleuth`; browser-flow proof → `roadtest`; perf →
`hotpath`. Must not: chase counts/coverage, mock the unit under test,
delete red to get green, estimate runner output.

## Method

- Layer A: 5 trigger cases + one-test-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/proof.md` (PF1–PF5,
  incl. zero-harness failure and make-CI-green adversarial); authored,
  unexecuted.
- Layer C: protocol `evals/outcomes/proof.md` + frozen
  `proof-tasks.json` on the `proof-cart` fixture (stdlib unittest,
  green suite blind to a seeded double-discount bug) via the workspace
  grader — O1 graded on genuine red (`FAILED (failures=`, not green,
  not errors). Verified offline end-to-end (real test runs, all gates).

## Raw results

| task | baseline | treatment | runs |
| --- | --- | --- | --- |
| O1 red regression | 0/2 | 2/2 | opencode 1.18.30, commits `4a00589`/`343ca6c`, 2026-09-15T02:55/15:11Z |
| O2 one-test restraint | 2/2 | 2/2 | same |
| O3 held-out theater | 0/1 | 0/1 | same, 15:15Z |

Raw traces: `evals/results/20260915-025710-*.json`,
`20260915-151329-*.json`, `20260915-151509-*-heldout.json`
(gitignored). Excluded: `025227` (contaminated — pre-containment agent
edited the real fixture) and `025503` (permission-blocked roleplays);
`024958` (pre-pristine-commit harness bug, all-fail artifact).

Grading notes, stated not hidden: O2's added-test gate landed between
the two n-rounds — run-4 O2 trials both modified `tests/test_cart.py`,
so both pass under either grading; the tally is unaffected. O3's
`boundary` marker missed a treatment writing "boundaries" (plural) —
marker brittleness blind review may overturn; the verdict does not
depend on it.

## Limitations (known before first run)

- Scope/marker checks are not test quality: whether the lock would
  catch the bug's return stays in blind review.
- O3 grades honesty markers, not suite color — a truthful red with a
  bug report outranks a padded green by design.
- unittest chosen for universality (pytest not guaranteed in trial
  environments); stack-specific runner behavior untested until trials.

## Trial environment notes (first live runs, 2026-09-15, opencode)

- n=1 per condition so far (protocol needs n=2 for any verdict):
  O1 treatment PASS vs baseline FAIL (boundary line discriminated);
  O2 both PASS (one-test restraint needs no skill advantage here).
  Verdict stays UNVERIFIED.
- The first live workspace trials hardened the harness, not the
  verdicts: pristine-fixture commits (untracked files false-failed
  scope), workdir containment (prompt pin + outer-repo monitor +
  workdir tree after an agent edited the real repo), TMPDIR under the
  repo (opencode auto-rejects /tmp workdirs), and O2's added-test
  gate (doing nothing passed). Raw traces in `evals/results/`
  (gitignored); the contaminated run-2 O1-treatment PASS is
  explicitly invalid and excluded from any future tally.

## Context audit

SKILL.md ~115 lines, 1 reference (boundary picker). Phase 14 added Tool
selection/fallback consolidating the four execution rungs — zero new
always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill proof --agent <agent> --trials 2
scripts/eval-outcome --skill proof --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
