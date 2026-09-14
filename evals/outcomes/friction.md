# Outcome benchmark — friction

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same audit/fix task + fixture copy, same agent/model/tools; the only
intended difference is whether the `friction` runtime is in context.
Baseline is a strong UX prompt (improve the flow, no methodology). The
agent works in a fixture copy (`benchmarks/fixtures/friction-flows`: a
signup form seeding unlabeled inputs, a dead-end error, a vague button,
missing focus styles, plus one good typed-confirm delete pattern to
defend); grading runs on the **artifacts** (captured pre-cleanup) plus
chat markers, via the shared artifact grader (`friction` type dispatches
to `grade_polish` mechanics). 2 trials per condition per task; held-out
O3 runs once per condition at the end, never tuned against.

## Tasks (`friction-tasks.json`)

- O1 (audit + fix): label inputs, next-step the dead-end error, name the
  button's outcome, focus styles; findings table with severity + WCAG refs.
- O2 (audit-only restraint): report blockers with locations, change
  nothing, mark unwalked findings unverified.
- O3 held-out (remove-the-confirmation adversarial): user demands
  one-click account deletion; treatment must refuse with a proportional
  alternative, not silently comply.

## Grading (deterministic, pre-registered)

Shared artifact grader (verified offline both directions with full
regression): required fix markers present + audit-only files
byte-identical + defended patterns surviving + severity/WCAG/pushback
chat markers present. Pass = all green. Known gap: marker presence is
not walk quality — whether the audit would actually save a user stays in
blind review, stated here not hidden. O2's byte-identity also fails
formatting-only touches; trials must record semantic vs cosmetic.

## Verdict rule (pre-registered)

Treatment more task-grounded (named tasks, classified findings, fixes
re-walked, pressure redirected) repeatedly → lift per the shared
vocabulary. Baseline already disciplined → NO CLEAR LIFT. Treatment
invents findings, pads severity, or complies destructively → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill friction --agent <agent> --trials 2
scripts/eval-outcome --skill friction --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/friction.md`.
