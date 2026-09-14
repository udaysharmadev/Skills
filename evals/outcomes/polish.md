# Outcome benchmark — polish

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same polish task + fixture copy, same agent/model/tools; the only
intended difference is whether the `polish` runtime is in context.
Baseline is a strong designer prompt (improve the UI, no methodology).
The agent works in a fixture copy (`benchmarks/fixtures/polish-dashboard`:
slop-seeded `index.html` + constraint `tokens.css`); grading runs on the
**artifacts** (captured pre-cleanup) plus chat markers. 2 trials per
condition per task; held-out O3 runs once per condition at the end, never
tuned against.

## Tasks (`polish-tasks.json`)

- O1 (full polish): remove the purple-gradient hero, converge hardcoded
  colors onto `tokens.css` without editing it, add hover/focus + empty
  states, Direction: line first.
- O2 (subtle-polish restraint): empty state for the orders table only;
  nothing structural; Direction: line names the mode.
- O3 held-out ("make it pop" adversarial): user demands gradient +
  glassmorphism + icon spam; treatment must push back with an on-brand
  alternative, not silently comply.

## Grading (deterministic, pre-registered)

Artifact grader (`polish` type in `scripts/eval-outcome`, verified
offline both directions with full regression): forbidden slop strings
absent from artifacts + named token files byte-identical to the fixture +
required state markers present + Direction/chat markers present. Pass =
all green. Known gap: static string checks are not visual judgment
(taste, hierarchy, "deliberate" feel) — that stays in blind review,
stated here not hidden. Byte-strict token identity also fails
formatting-only rewrites; trials must record whether a tokens_changed
failure was semantic or cosmetic.

## Verdict rule (pre-registered)

Treatment more deliberate/restrained (slop removed, tokens kept, states
added, pressure redirected) repeatedly → lift per the shared vocabulary.
Baseline already disciplined → NO CLEAR LIFT. Treatment decorates or
rewrites tokens → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill polish --agent <agent> --trials 2
scripts/eval-outcome --skill polish --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/polish.md`.
