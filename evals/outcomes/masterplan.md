# Outcome benchmark — masterplan

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same brief + fixture repo, same agent/model/tools; the only intended
difference is whether the `masterplan` runtime is in context. Baseline is
a strong planning prompt (real files, validation per slice, rollback).
The agent works in a fixture copy. 2 trials per condition per task;
held-out O3 runs once per condition at the end, never tuned against.

## Tasks (`masterplan-tasks.json`)

- O1 (ts-dashboard): status-history feature — must slice vertically with
  validation, all paths real, ≤ 150 lines.
- O2 (py-notes-api): SQLite→Postgres migration — must own the migration
  slice with down-path or IRREVERSIBLE marking.
- O3 held-out (ts-dashboard): mega-component split — must name App.tsx
  with real paths and slices.

## Grading (deterministic, pre-registered)

Grounded-doc grader: `must_contain` + any-groups + zero contaminants +
every mentioned code path resolves to a real fixture file + `max_lines`
150. Verified offline: a vertical slice-plan passes; a horizontal
frontend-phase/backend-phase plan with no files fails. Verticality beyond
the proxies (dependency honesty, uncertainty-first order) stays in blind
review at release.

## Verdict rule (pre-registered)

Treatment more grounded/executable repeatedly → lift per the shared
vocabulary. Baseline already plans well → NO CLEAR LIFT. Treatment
invents paths or phases → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill masterplan --agent <agent> --trials 2
scripts/eval-outcome --skill masterplan --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/masterplan.md`.
