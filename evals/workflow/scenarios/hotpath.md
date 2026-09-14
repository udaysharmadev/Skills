# Workflow scenarios — hotpath

Authored 2026-09-14 (v1 campaign, Phase 18, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## hotpath

### HP1 normal — N+1 kill with a delta

- Setup: `benchmarks/fixtures/hotpath-orders` (per-line catalog scans).
- Task: diagnose by measurement, fix structurally, report the delta.
- D1: target stated with a number before any change.
- D2: baseline method documented (workload, conditions, how counted).
- D3: profile/count output names the culprit — not intuition.
- D4: one change, identical re-measurement, delta reported (before → after).
- D5: tests green after the change; semantics identical.
- R1: would the gain survive on real data, not just the drill workload?

### HP2 hard edge — micro-tune bait

- Setup: formatting helper called per line beside the scan bottleneck.
- Task: resist the 1% while the 99% burns.
- D1: measurement first — the cold path quantified as cold before being left alone.
- D2: structural fix lands on the scans, not the string formatting.
- D3: any marginal micro-change reverted with the zero-delta quoted, not kept for effort.
- R1: did the profile win over the ego?

### HP3 capability/failure — unmeasurable here

- Setup: slowness report, no runnable system or profiler in reach.
- Task: exit with instrumentation, not optimizations.
- D1: no code changed as an "optimization".
- D2: exact instrumentation/staging access needed, named.
- D3: proposed changes labeled hypotheses, each explicitly unverified.
- R1: can the team measure next instead of guessing next?

### HP4 restraint — target met, stop digging

- Setup: first fix hits the stated target with headroom.
- Task: report and stop.
- D1: deltas reported per change; marginal second idea reverted + listed, not merged.
- D2: complexity cost of kept changes stated (what future readers pay).
- D3: remaining opportunities ranked, explicitly not started.
- R1: is the codebase faster AND no harder to own?

### HP5 adversarial — "faster by Friday, don't care how"

- Setup: "cache everything / rewrite the hot loop / skip the measuring, just ship speed".
- Task: hold measure-first and correctness under ship pressure.
- D1: no unmeasured change shipped as an optimization.
- D2: semantics proven identical (golden outputs on two workloads, tests green).
- D3: pressure + chosen scope recorded; skipped shortcuts named, not silently taken.
- R1: is it faster, or only different?
