# Outcome benchmark — distill

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy). Numbers appear only after live runs
with full provenance.

## Design

Same vague request + fixture repo, same agent/model/tools; the only
intended difference is whether the `distill` runtime is in context.
Baseline is a strong brief-writer prompt (compact, repo-checked, real
files only). The agent works in a fixture copy. 2 trials per condition
per task; held-out O3 runs once per condition at the end, never tuned
against.

## Tasks (`distill-tasks.json`)

- O1 (ts-dashboard): "bro add dashboard make it good" — must ground in
  real files, carry Non-goals + numbered assumptions, stay ≤ 200 lines.
- O2 (py-notes-api): typo fix, "keep it tiny" — must stay ≤ 30 lines
  (over-specifying is the failure mode).
- O3 held-out (ts-dashboard): per-user login — must scope honestly and
  surface auth/security considerations (auth bites here).

## Grading (deterministic, pre-registered)

Fact-grader extension: `must_contain` + honesty any-groups + zero
contaminants + every mentioned code path resolves to a real fixture file
+ `max_lines` budget (200 / 30 / 200). Pass = all green. Recorded:
duration, output size, line count. Verified offline against synthetic
good/bloat/tiny/no-auth outputs — all discriminate correctly.

## Verdict rule (pre-registered)

Treatment more grounded and better-scaled repeatedly → lift per the
shared vocabulary. Baseline already brief-right → NO CLEAR LIFT.
Treatment hallucinates scope or bloats → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill distill --agent <agent> --trials 2
scripts/eval-outcome --skill distill --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/distill.md`.
