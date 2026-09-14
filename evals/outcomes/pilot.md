# Outcome benchmark — pilot

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same slice + fixture repo, same agent/model/tools; the only intended
difference is whether the `pilot` runtime is in context. Baseline is a
strong implementer prompt (scoped diff, honest verification). The agent
works in a fixture copy; grading happens on the **workspace** (changed
files, check-command exits recorded pre-cleanup), not on chat claims.
2 trials per condition per task; held-out O3 runs once per condition at
the end, never tuned against.

## Tasks (`pilot-tasks.json`)

- O1 (ts-dashboard): empty-state slice — scope `src/components/` +
  `src/App.tsx`; must report verified/unverified honestly.
- O2 (py-notes-api): 422-on-empty-title slice — scope `app/`; touched
  file must still parse (executable check).
- O3 held-out (ts-dashboard): debug-leftover/dead-code removal — scope
  `src/`; no drive-by refactors.

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type in `scripts/eval-outcome`, offline-tested
with synthetic obs incl. drift and red-build cases): all `verify`
commands exit as expected + zero changed files outside `scope` +
required report markers present. Pass = all green. Recorded: changed
file list, check tails, duration. Fixture honesty note: ts-dashboard has
no runnable suite by design (seeded gap), so O1/O3 lean on scope +
presence checks — full test-exit grading needs a runnable-suite fixture
(future fixture work, not hidden).

## Verdict rule (pre-registered)

Treatment more scoped and more honestly verified repeatedly → lift per
the shared vocabulary. Baseline already disciplined → NO CLEAR LIFT.
Treatment drifts scope or greens dishonestly → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill pilot --agent <agent> --trials 2
scripts/eval-outcome --skill pilot --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/pilot.md`.
