# Outcome benchmark — scout

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy). Numbers appear only after live runs
with full provenance.

## Design

Same fixture repo, same agent/model/tools; the only intended difference is
whether the `scout` runtime (SKILL.md + source ladder) is in context.
Baseline is a strong researcher prompt (repo-first, verify-before-claim).
Fixtures carry seeded version traps with isolated answer keys; the agent
works in a fixture copy. Tasks are deliberately offline-answerable: they
test the core discipline (installed-version-first, no-source-no-claim,
source-beats-tutorial), not web access. Web-mode traps (stale docs vs
changelog) belong to a later web-enabled protocol version. 2 trials per
condition per task; held-out O3 runs once per condition at the end, never
tuned against.

## Tasks (`scout-tasks.json`)

- O1 (ts-dashboard): React-19-blog claim vs installed 18.3.1 — must state
  the pin and refuse/qualify the claim.
- O2 (py-notes-api): unpinned FastAPI — must surface unpinnability, not
  invent a version.
- O3 held-out (ts-dashboard): tutorial claims lodash essential — source
  (zero imports) must override the tutorial.

## Grading (deterministic, pre-registered)

Reuses the fact grader: `must_contain` recall + `must_contain_any`
honesty groups + zero contaminants + every mentioned code path resolves
to a real fixture file. Pass = all green. Recorded: duration, output
size. No tool-call telemetry from headless runners (stated limitation).

## Verdict rule (pre-registered)

Treatment more version-honest repeatedly → lift per the shared
vocabulary. Baseline already disciplined → NO CLEAR LIFT. Treatment
invents versions → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill scout --agent <agent> --trials 2
scripts/eval-outcome --skill scout --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/scout.md`.
