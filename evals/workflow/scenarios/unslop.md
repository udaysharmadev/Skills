# Workflow scenarios — unslop

Authored 2026-09-14 (v1 campaign, Phase 20, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.
Signature U1–U3 remain as cross-checks.

## unslop

### UN1 normal — shop detox in batches

- Setup: `benchmarks/fixtures/unslop-shop` (seeded duplication, dead code, zombie layer, swallowed error, debug leftover).
- Task: detox Critical + High-leverage ranks, batch by batch.
- D1: behavior baseline captured (suite run quoted) before batch 1.
- D2: findings ranked with file:line each; no style-preference padding.
- D3: each batch independently verifiable (tests green quoted per batch); net line delta negative.
- D4: kept-with-reason list present (legacy export format survives with its reason).
- R1: is the repo safer to touch, with proof?

### UN2 hard edge — load-bearing weirdness stays

- Setup: fixture's legacy pipe-format export covered by tests.
- Task: clean around the quirk, never through it.
- D1: legacy export byte-behavior identical after detox (its tests green, format untouched).
- D2: kept-list names it with the reason; no "simplification" of the format.
- D3: deletion candidates near it verified by search, not memory.
- R1: did restraint protect revenue-adjacent behavior?

### UN3 capability/failure — no runnable baseline

- Setup: messy repo, zero tests, app barely runs.
- Task: build signal before deleting anything.
- D1: batch 0 is a smoke baseline (money-path tests), quoted green.
- D2: zero deletions before the signal exists.
- D3: if the app won't run, fixing that becomes the mission (via `sleuth`), stated outright.
- R1: was the first change a test, not a deletion?

### UN4 restraint — audit-only / already-clean repo

- Setup: "audit the mess first, don't delete anything yet" (or a genuinely clean repo).
- Task: map honestly, touch nothing.
- D1: ranked findings with file:line, zero deletions.
- D2: clean repo → "already clean" stated outright; zero invented findings.
- D3: no performative cleanup to justify the audit.
- R1: is the map trustworthy enough to schedule from?

### UN5 adversarial — "rewrite it cleanly from scratch"

- Setup: user demands a full rewrite ("faster than picking through it").
- Task: refuse the rewrite without refusing the user.
- D1: no giant unverified rewrite shipped; incremental batches instead.
- D2: kept-list items (legacy quirks) survive with reasons — rewrites drop them silently.
- D3: batch log shows what each batch changed + its verification.
- R1: did the code get cleaner without losing what worked?
