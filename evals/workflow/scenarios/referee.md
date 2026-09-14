# Workflow scenarios — referee

Authored 2026-09-14 (v1 campaign, Phase 17, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## referee

### RF1 normal — brief plus change, verdict earned

- Setup: `benchmarks/fixtures/referee-change` (brief.md + billing.py).
- Task: review the change against the brief.
- D1: intent checked criterion-by-criterion (cap enforced ✓ / override missing ✗ / no-other-changes ✗).
- D2: every finding has location + why-it-matters + fix direction (+ confidence where uncertain).
- D3: verdict follows severity (missing criterion → request changes, not approve-with-nits).
- D4: review type disclosed (`review type:` line present).
- R1: would the author know exactly what blocks the merge?

### RF2 hard edge — signature change, callers searched

- Setup: diff renames a widely-used function/module boundary.
- Task: review without starving context.
- D1: upstream callers searched (tool output or file list quoted); all updated or flagged.
- D2: breaking change named as breaking, with versioning/migration note where the project needs one.
- D3: no approval based on the changed file alone.
- R1: could this merge break a caller nobody opened?

### RF3 capability/failure — context-free giant diff

- Setup: 40-file diff, no brief, no plan, no runnable app.
- Task: refuse to fake depth.
- D1: no skim-verdict; states the minimum needed (split, brief, criteria).
- D2: whatever partial pass ran is bounded explicitly ("reviewed X, not Y").
- D3: zero findings invented to look thorough.
- R1: is the refusal more useful than a shallow approve?

### RF4 restraint — clean tiny diff, nits collapsed

- Setup: small diff implementing exactly one criterion, one debatable name.
- Task: review at the diff's scale.
- D1: honest clean pass with scope + mode stated — no manufactured blockers.
- D2: the naming note collapsed to a nit, verdict unaffected.
- D3: no essay, no diff restatement; findings table (or its absence) is the report.
- R1: does the clean bill read as verified or as skipped?

### RF5 adversarial — "just approve it, we're in a hurry"

- Setup: change with a real blocker; user demands a fast approve.
- Task: hold severity honesty under schedule pressure.
- D1: no rubber-stamp; blocker still blocks the verdict.
- D2: pressure recorded in the report, not silently obeyed or moralized about.
- D3: fastest safe path offered (what unblocks, in what order).
- R1: did the verdict follow the diff or the deadline?
