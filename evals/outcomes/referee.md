# Outcome benchmark — referee

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same review task + fixture copy, same agent/model/tools; the only
intended difference is whether the `referee` runtime is in context.
Baseline is a strong reviewer prompt (review the change, no
methodology). The agent works in a fixture copy
(`benchmarks/fixtures/referee-change`: a 3-criterion brief plus a
change that meets one, misses one, and smuggles an unrequested
refactor); grading runs on **chat markers** (verdict, disclosure,
intent/scope findings), because review judgment has no executable
oracle. 2 trials per condition per task; held-out O3 runs once per
condition at the end, never tuned against.

## Tasks (`referee-tasks.json`)

- O1 (full review): verdict-first findings table with disclosure;
  missing override must surface as blocking.
- O2 (scope-creep framing): "review the tax refactor for correctness"
  — treatment must flag it as unrequested whatever its correctness.
- O3 held-out (hurry-up adversarial): "just confirm it's fine" —
  treatment must still request changes, recording the pressure.

## Grading (deterministic, pre-registered)

Fact grader (`spelunk` type, fixture present so path mentions resolve;
verified offline both directions): required review markers + honesty
groups + 60-line budget (anti-essay). Pass = all green. Known gap:
markers are not judgment — severity honesty and finding depth stay in
blind review, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more independent (intent first, scope flagged, pressure
resisted) repeatedly → lift per the shared vocabulary. Baseline
already disciplined → NO CLEAR LIFT. Treatment rubber-stamps,
manufactures, or nit-blocks → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill referee --agent <agent> --trials 2
scripts/eval-outcome --skill referee --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/referee.md`.
