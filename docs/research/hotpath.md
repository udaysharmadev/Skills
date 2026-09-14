# hotpath — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Micro-Tuning Traps (2025/2026) | AI agents easily fall into "incrementalism traps," wasting tokens on granular syntax tweaks (loop unrolling, bitwise ops) instead of finding structural bottlenecks. | Adds "The Micro-Tuning Trap" to the Banned List, enforcing structural "regime shifts" over syntax tweaking. | SKILL.md §Banned List, references/measurement.md |
| Hallucinated Profiling / Evaluation Crisis | Agents often guess what is slow based on their training priors rather than actual runtime metrics, leading to misaligned optimizations. | Explicitly bans "Hallucinated Profiling," requiring actual APM or trace evidence before any optimization is attempted. | SKILL.md §Banned List |

## Key new intelligence encoded

1. **Anti-Hallucinated Profiling** — establishes that an unmeasured bottleneck is a hallucinated bottleneck; agents must prove a hot path exists with empirical data before changing code.
2. **Regime Shifts over Micro-Tuning** — shifts the agent's optimization strategy away from minor code-golfing toward structural and architectural optimizations guided by distributed traces.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Evaluator models for performance | Trace-based bottleneck detection via LLM (2026) |
