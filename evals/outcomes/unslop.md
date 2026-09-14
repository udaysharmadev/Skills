# Outcome benchmark — unslop

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same messy repo + fixture copy, same agent/model/tools; the only
intended difference is whether the `unslop` runtime is in context.
Baseline is a strong cleanup prompt (clean the repo, no methodology).
The agent works in a fixture copy (`benchmarks/fixtures/unslop-shop`:
seeded duplication, dead code, zombie layer, swallowed error, debug
leftover, plus a test-locked legacy quirk to defend); grading runs on
the **workspace** (suite green, slop markers gone, quirk surviving,
net-negative lines, scope kept) plus batch markers, via the
`pilot`-type grader. Tests are excluded from scope: touching the
baseline to keep it green fails. 2 trials per condition per task;
held-out O3 runs once per condition at the end, never tuned against.

## Tasks (`unslop-tasks.json`)

- O1 (batched detox): baseline first, slop gone, quirk kept with
  reason, net-negative, batch log.
- O2 (audit-only restraint): ranked map, repo byte-identical.
- O3 held-out (rewrite-it adversarial): "rewrite from scratch" —
  treatment must detox incrementally; rewrites drop the quirk and the
  batch trail.

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type, verified offline end-to-end with real
runs): suite green + slop-grep clean + quirk grep present + line-count
bound + scope kept (tests untouched) + report markers. Pass = all
green. Known gap: greps are not taste — batch quality and ranking
honesty stay in blind review, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more rescue-honest (baseline quoted, batches verified, quirk
kept, rewrite refused) repeatedly → lift per the shared vocabulary.
Baseline already disciplined → NO CLEAR LIFT. Treatment rewrites,
breaks behavior, games tests, or pads → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill unslop --agent <agent> --trials 2
scripts/eval-outcome --skill unslop --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/unslop.md`.
