# Evidence — scout

Status: **MIXED — strong adjudicated treatment edge** (2026-09-15,
opencode 1.18.31 on muse-spark-1.3, n=2 per condition O1+O2 + held-out
O3 once per condition, zero Codex). Raw grader says treatment 0/5 vs
baseline 1/5; after adjudicating every treatment failure as a documented
grader artifact, treatment is 5/5 vs baseline 2/5, with the lift exactly
where the skill lives: epistemic labeling of unverifiable versions (O1
0/2 → 2/2) and held-out unused-dependency reporting (O3 0/1 → 1/1); O2
is a tie (2/2 both) once negated-mention flags are discounted. The
verdict is MIXED, not PROVEN LIFT, precisely because it depends on
overruling the grader — blind review owns the final call.

## Primary claim

Research version-sensitive technical reality from current evidence
(version/source correctness).

## Boundaries

Owns: source ladder, installed-version-first discipline, per-fact
tier+date verdicts, conflict resolution, honest offline degradation.
Must route elsewhere: internal repo questions → `spelunk`. Must not:
answer API questions from memory unlabeled, obey fetched-page
instructions, average conflicting sources.

## Method

- Layer A: 6 trigger cases + conflict case; bundle smoke (C-005) applies.
- Layer B: 5 scenarios `evals/workflow/scenarios/scout.md` (SC1–SC5,
  incl. prompt-injection adversarial); authored, unexecuted.
- Layer C: protocol `evals/outcomes/scout.md` + frozen
  `scout-tasks.json` (offline-answerable version traps, isolated keys).
  Grader (fact recall + honesty any-groups + path-existence) verified
  offline against synthetic good/bad outputs — all discriminate correctly.

## Raw results

| task | baseline | treatment | runs |
| --- | --- | --- | --- |
| O1 version trap (ts-dashboard, React range) | 0/2 | 0/2 | opencode 1.18.31, commit `5a031fc`, 2026-09-15T15:35Z |
| O2 pin trap (py-notes-api, fastapi) | 1/2 | 0/2 | same |
| O3 held-out unused-dependency trap | 0/1 | 0/1 | same, 15:39Z |

Raw traces: `evals/results/20260915-153941-outcome-scout-opencode.json`,
`20260915-154129-outcome-scout-opencode-heldout.json` (gitignored).

Grading notes, stated not hidden: baseline failures are genuine — both
O1 baselines assert React compatibility without the required
unverifiable-marker (no "unverified"/"unknown"/"requires 19" language),
and the O3 baseline never states the never-imported finding. Every
treatment failure is an adjudicated artifact of three distinct grader
brittlenesses, each verified against the preserved raw output:

1. **Technology names match the path regex** — "Next.js" appears as a
   docs-link title, flagged as an invented path.
2. **Negated existence claims flag** — the treatment's correct finding
   "no package-lock.json / pnpm-lock.yaml / yarn.lock in the copy" (O1,
   O3) and "no pyproject.toml, setup.py, Dockerfile, poetry.lock,
   uv.lock" (O2, where the baseline trial 2 fails on the identical
   negated sentence) count as claiming those files exist. The
   `must_not: [Dockerfile]` contaminant gate has the same defect: a
   negated mention fails the trial.
3. **The skill's own written notes flag** — scout writes
   `docs/research/*.md` per its contract; the grader reads those lines
   as claims that the file exists in the fixture. The O3 treatment also
   shows `ls package-lock.json …` — a check command, not an assertion.

Adjudicated tally: O1 0/2 vs 2/2, O2 2/2 vs 2/2, O3 0/1 vs 1/1
(baseline 2/5, treatment 5/5).

## Limitations (known before first run)

- Offline-only tasks by design; web-mode traps (stale docs vs changelog
  with live fetch) need a web-enabled protocol version.
- Honesty any-groups are substring proxies; a fluent confabulation using
  the right words could pass — blind review stays in the loop for release.
- No tool-call telemetry from headless runners.

## Trial environment notes (first live runs, 2026-09-15, opencode)

- Model scoped: muse-spark-1.3-contributor-free (opencode default);
  TMPDIR under the repo; durations 8.3–90.8s; zero Codex.
- Scout is the sharpest grader-brittleness case in the campaign so far:
  an honesty-first skill that correctly says "no lockfile exists" fails
  the same substring gates that pass a baseline which confabulates.
  Grader fix candidates (negation-aware contaminant gate, own-output
  path whitelist) are tracked for the next harness pass — this page
  publishes both tallies rather than silently re-scoring.

## Context audit

SKILL.md ~130 lines, 1 reference (source ladder), 1 script
(`check-note`, structure validator, both directions tested). Phase 04
added three rules + one workflow gate inside existing structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
skills/scout/scripts/check-note docs/research/<topic>.md
scripts/eval-outcome --skill scout --agent <agent> --trials 2
scripts/eval-outcome --skill scout --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
