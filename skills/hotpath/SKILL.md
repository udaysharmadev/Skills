---
name: hotpath
description: Performance diagnosis and optimization strictly by measurement — benchmark, change, benchmark again, report the delta. Use when something is slow, when the user mentions performance, speed, latency, memory, bundle size or optimization, before shipping performance-sensitive work, or when a budget exists that must be met. Finds hot paths with evidence (query counts, render counts, waterfalls, allocations), quantifies every optimization, and forbids vibe-based tuning and unmeasured claims.
---

# hotpath — never optimize on vibes

The skill is the discipline: **measure → change one thing → measure the
same way → report the delta or revert.** An optimization without a
before/after number is a rumor. Most "obvious" performance work fixes
code that wasn't hot and misses the query that was.

## Prerequisites

A runnable system plus one measurement path to the complaint (profiler,
APM, query log, bundle analyzer, or even `time` + counters). No
measurement path at all → the first deliverable is instrumentation, not
optimization (see stop conditions).

## Tool selection/fallback

- Layer-native profiler/counters → evidence-grade measurement; this is
  the primary route.
- No profiler but runnable → counters and timing around the suspect
  (`time`, query logs, the bundled `measure-report` for delta honesty);
  state the distortion.
- Nothing runnable or measurable → hypotheses only, each explicitly
  unverified; no code changes as "optimizations".

## When NOT to use

- The answer is wrong, just slow to be wrong → `sleuth`.
- "Will the architecture handle 100×?" → `headroom`.
- The UI looks slow but no measurement exists yet → that's your step 1,
  not a reason to skip measuring.

## Workflow

### 1. Define the target

What's slow, for whom, and what would "fast enough" mean: a number and a
condition ("p95 checkout API < 400ms", "dashboard LCP < 2.5s", "test
suite < 3min"). No target → set one from the user's complaint, stated as
an assumption. Optimizing without a target is how you get 30% faster
things nobody cared about.

### 2. Baseline under fixed conditions

Measure the current state with the tooling for the layer (see
`references/measurement.md`) — realistic data volume, warm/cold state
declared, same machine/conditions you'll re-use. Record the numbers and
**how** they were measured; the method is part of the result. No
measurement capability at all → stop and say what instrumentation is
needed; estimating and "optimizing" blind is forbidden.

### 3. Find the hot path with evidence

Profile, trace, or count — never suspect. Signals that usually locate
it: query count (N+1), slow queries, request waterfalls, bundle size,
render counts, startup cost, CPU/memory hotspots, API latency, cache
miss behavior, repeated work, serialization overhead, oversized
payloads. The measurement output names the culprit — your job is to
explain why it's hot, not to pick it by intuition.

### 4. One change, then re-measure

Make the single most promising change; re-run the **identical**
measurement. Algorithmic/structural fixes first (kill the N+1, cache the
derived value, cut the waterfall); micro-tuning (loop tricks, micro-
caching) only when the profile says the hot path is genuinely CPU-bound
at the micro level.

### 5. Keep or revert

Report the delta. If the gain is marginal and the change adds complexity
— revert it and say so; complexity is a cost paid forever. Move to the
next hot path or stop when the target is met.

## Anti-Patterns (The Banned List)

- **Hallucinated Profiling** — guessing that a loop or function is the bottleneck based on intuition or AI training bias, without running a real profiler or inspecting actual APM/trace data. An unmeasured bottleneck is a hallucination.
- **The Micro-Tuning Trap** — wasting effort on granular, incremental adjustments (e.g., swapping `map` for `for`, or micro-caching variables) when the actual latency lives in structural boundaries (database N+1, network round-trips). Fix the architecture before you fix the syntax.

## Rules

- Produce the report from the bundled helper: `scripts/measure-report
  --baseline N --after M --conditions "..."` — it computes the delta and
  enforces the honesty fields (conditions are required; sub-threshold
  deltas are labeled NOISE, not spun).
- Measurement quality rules: warm up before sampling (JIT, caches),
  enough samples for a stable median (≥3–5, report the spread), use
  percentiles not means for latency, representative data volume, and
  declare local-vs-production caveats — numbers without conditions are
  anecdotes.
- One variable per measurement round — two changes at once means neither
  is proven.
- Micro-benchmarks lie (JIT warmup, cache priming, branch prediction) —
  measure realistically or state the distortion.
- The fix must not break correctness: tests stay green, semantics
  identical (a "faster" endpoint that returns subtly different data is a
  bug with a speed problem).
- Don't optimize cold paths, startup nobody complains about, or code
  that runs once — the profile decides what's hot, not the ego.

## Quality gates

- Target stated with a number before any change.
- Baseline and re-measurements use the identical method/conditions —
  documented.
- Every kept change has a before/after delta in the report; every
  reverted change is listed too.
- Tests green after each change.

## Stop conditions

- Target met → report the deltas, remaining opportunities (ranked, not
  started), stop.
- Measurement impossible in this environment → name the exact
  instrumentation or staging access needed; propose changes as
  hypotheses only, explicitly unverified.
- The hot path is architectural (needs `headroom`) → report the numbers
  that prove it and route the decision.

## Output contract

```text
target:    dashboard LCP < 2.5s (assumption from "feels slow", confirmed)
baseline:  4.8s  (local, throttled 4G profile, 50k-row user, 3 runs median)
changes:
  1. killed N+1 on orders list (eager-load)   4.8s → 2.9s   ✅ kept
  2. hero image 4.2MB → 380KB AVIF            2.9s → 2.2s   ✅ kept — target met
reverted:   memoized table rows (0% delta, added complexity)
remaining:  split main bundle (est. −0.3s, needs build change) — not started
evidence:   profiles + Lighthouse runs in chat, conditions documented
```

Numbers with conditions, or nothing.
