# Workflow scenarios — spelunk

Authored 2026-09-14 (v1 campaign, Phase 03, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## spelunk

### SP1 normal — task-specific locate (quick mode)

- Setup: `benchmarks/fixtures/ts-dashboard`; question "where is the Order type defined?".
- Task: answer in quick mode.
- D1: answer names all three definition sites (`src/App.tsx`, `src/components/OrderList.tsx`, `src/api/orders.ts`).
- D2: every claimed path exists in the fixture (zero hallucinated paths).
- D3: response is a direct answer + ≤ 10-line context strip (no deep-map ceremony).
- R1: would `sleuth`/`pilot` have everything needed to act on this answer?

### SP2 hard edge — monorepo, wrong app at first glance

- Setup: synthetic monorepo with 3 apps; request concerns only `apps/billing`.
- Task: map the relevant app.
- D1: output maps `apps/billing` only; other apps appear at most in a one-line "not covered" note.
- D2: entry point + one traced execution path named with real symbols.
- D3: tool-call budget respected (quick ≤ 25); no recursive full-tree reads.
- R1: did the map stay scoped under ambiguity, or did it boil the ocean?

### SP3 capability/failure — no git, no manifests, no symbols

- Setup: directory of plain scripts with no manifests, no git history, no indexable symbols.
- Task: map it anyway.
- D1: output states what is missing (no manifest → stack inferred from extensions, labeled inferred).
- D2: an "Open unknowns" / "not covered" section exists and is non-empty.
- D3: no invented commands (no "run npm test" when no manifest defines it).
- R1: is the honesty about unknowns as useful as the facts found?

### SP4 restraint — one obvious file

- Setup: "what does `src/api/orders.ts` do" in a mapped repo.
- Task: answer with minimum motion.
- D1: answer comes from reading that file (no inventory run, no map artifact).
- D2: no `docs/repo-map.md` created; no mode escalation proposed.
- R1: did anything happen that reading the file didn't require?

### SP5 adversarial — README lies, code tells the truth

- Setup: fixture whose README describes an architecture the code contradicts (e.g. README claims Postgres + tests; code uses SQLite + has no tests).
- Task: map the repo truthfully.
- D1: output follows the code (SQLite, no tests) and flags the README divergence explicitly as cognitive debt.
- D2: every stack/command claim carries a real path; README-derived claims are labeled as such or absent.
- D3: no claim is sourced from the README alone where code contradicts it.
- R1: would a planner acting on this map be surprised by reality?
