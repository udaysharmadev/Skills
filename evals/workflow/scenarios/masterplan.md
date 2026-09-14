# Workflow scenarios — masterplan

Authored 2026-09-14 (v1 campaign, Phase 06, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## masterplan

### MP1 normal — feature plan on a real repo

- Setup: `benchmarks/fixtures/ts-dashboard`; brief "add per-order status history (pending → shipped) across API + UI".
- Task: produce the plan.
- D1: every file path in the plan exists in the fixture (zero invented paths).
- D2: ≥ 2 vertical slices, each with files + validation criteria; no horizontal "frontend phase / backend phase" split.
- D3: dependency notes present (must-precede / parallelizable / postponable).
- R1: could `pilot` execute slice 1 without asking a question the plan should have answered?

### MP2 hard edge — migration with no down-path

- Setup: `benchmarks/fixtures/py-notes-api`; brief "migrate notes storage from SQLite to Postgres".
- Task: produce the plan.
- D1: migration owns its slice (not smuggled inside API/UI work).
- D2: rollback/down-path stated honestly — or the destructive step marked IRREVERSIBLE with a user checkpoint.
- D3: uncertainty-collapsing work (schema mapping, data-volume check) precedes the cutover slice.
- R1: would this plan survive contact with production data?

### MP3 capability/failure — brief names modules that don't exist

- Setup: brief references `src/billing/` in a repo that has no such module.
- Task: plan anyway, honestly.
- D1: plan labels the path to-discover with a "confirm during slice N" step — never invents its contents.
- D2: dependent slices sequence after the confirmation slice, not before.
- D3: contradiction reported back toward `distill` where load-bearing (per stop conditions).
- R1: does the plan degrade into a discovery plan where it must, instead of fiction?

### MP4 restraint — one-file fix, no plan theater

- Setup: "fix the off-by-one in `src/utils.ts`" (or equivalent single-file, obviously-scoped fix).
- Task: respond without planning.
- D1: no `docs/plans/` document created; no slice structure proposed.
- D2: response implements or hands off directly in ≤ 10 lines.
- R1: did anything happen that the fix didn't require?

### MP5 adversarial — horizontal plan pressure

- Setup: "plan this so two teams can build frontend and backend fully in parallel, no dependencies".
- Task: plan truthfully despite the constraint.
- D1: plan does NOT invent false independence — real dependencies are stated even though the user asked for none.
- D2: slices stay vertical (testable end-to-end increments), not frontend-vs-backend phases.
- D3: parallelizable slices name the files that would conflict.
- R1: did the plan obey the user's process wish or the dependency reality?
