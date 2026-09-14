# Outcome benchmark — backend

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same behavior task + fixture repo (two stacks: Python/FastAPI via
py-notes-api, TypeScript via ts-dashboard), same agent/model/tools; the
only intended difference is whether the `backend` runtime is in context.
Baseline is a strong backend-engineer prompt (validate, scope, verify).
The agent works in a fixture copy; grading is workspace-based (changed
files, check exits) plus report markers. 2 trials per condition per task;
held-out O3 runs once per condition at the end, never tuned against.

## Tasks (`backend-tasks.json`)

- O1 (py-notes-api): 422 validation + pagination (default + cap).
- O2 (ts-dashboard): idempotent order submission under retries.
- O3 held-out (py-notes-api): DB-level duplicate-id prevention + 409.

## Grading (deterministic, pre-registered)

Workspace grader: check exits as expected + zero files outside `scope` +
report markers (`verif`, task substance words). Verified offline:
constraint-based O3 passes, app-level-`if` O3 fails. Substance beyond
the proxies (isolation correctness, true exactly-once under concurrency)
stays in blind review at release — proxies gate shape and honesty, not
deep correctness.

## Verdict rule (pre-registered)

Treatment more correct/scoped/honest repeatedly → lift per the shared
vocabulary. Baseline already solid → NO CLEAR LIFT. Treatment skips
validation, drifts scope, or greens dishonestly → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill backend --agent <agent> --trials 2
scripts/eval-outcome --skill backend --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/backend.md`.
