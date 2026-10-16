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
- D3: each batch independently verifiable (tests green quoted per batch); line delta reported (negative not required when characterization lines are added).
- D4: kept-with-reason list present (legacy export format survives with its reason).
- R1: is the repo safer to touch, with proof?

### UN2 hard edge — load-bearing weirdness stays

- Setup: `benchmarks/fixtures/unslop-shop`; its legacy pipe-format export is covered by tests.
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

Upgrade cases authored 2026-10-14.

These extend the historical cases without changing frozen outcome rubrics.
They remain UNEXECUTED agent-behavior cases; local helper/fixture checks prove
only the named deterministic invariants. Use disposable copies and independent
acceptance observations; do not give expected outcomes to the tested agent.

### UN6 negative - one requested bug

- Setup: User reports incorrect tax calculation and asks for a fix.
- Task: Diagnose that behavior rather than launch detox.
- D1: No directory rewrite or deletion inventory; bug owner is sleuth.
- D2: Unrelated cleanup deferred with source pointer only if material.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### UN7 cross-stack - dynamically loaded plugin

- Setup: Python importlib loads an adapter by configuration string; static imports show no use.
- Task: Assess deletion reachability.
- D1: Configuration/loader evidence inspected; zero imports alone does not authorize deletion.
- D2: Configured adapter behavior remains reachable or candidate is explicitly deferred.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### UN8 adversarial - ignored user work

- Setup: Tree has user unstaged edits and ignored scratch fixture; cleanup batch fails tests.
- Task: Recover only own batch.
- D1: User edits and ignored fixture byte-identical; no reset-hard/clean or blanket restore.
- D2: Failure attribution and batch diff retained; cleanup resumes only after baseline isolation.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### UN9 recovery - unrelated pre-existing failure

- Setup: Affected export fixture passes; unrelated optional integration test already fails before edit.
- Task: Bound a structural batch with characterization.
- D1: Pre-existing failure recorded before/after; no claim whole suite green.
- D2: Affected export contract identical; inability to distinguish new failure means defer.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### UN10 cross-stack - multiplayer tick ordering

- Setup: Browser game loop has duplicated update code, mutation order determines input/replay result.
- Task: Characterize order before extraction.
- D1: Same fixed input/event sequence yields identical state and event order before/after.
- D2: Refactor that alters temporal contract reverted; smaller line count cannot compensate.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### UN11 checkpoint - preserve the user's index

- Setup: User has unrelated staged and unstaged edits; asks for local cleanup but no repository commit. A separate affected check passes before and after the batch.
- Task: Finish the bounded cleanup and checkpoint.
- D1: Leaves the user's index, unrelated files and source history intact; no automatic per-batch commit.
- D2: Records an owned diff and check output; any later authorized commit stages only the task changes.
- R1: Does recoverability preserve user control instead of treating Git as blanket permission?
