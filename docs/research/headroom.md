# headroom — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Scaling / Orchestration (2025/2026) | The "god agent" is dead, but splitting agents into true microservices prematurely is a costly anti-pattern. Orchestrated execution graphs (modular monoliths) are preferred. | Adds the "Premature Microservices" warning specifically for agentic workflows to the scaling dimensions. | references/dimensions.md |
| Team Topologies for AI | AI does not replace the need for stream-aligned stewardship; it amplifies it. Architecture must prioritize human observability and "Bounded Agency". | Encodes Bounded Agency and Team Topologies as core scaling dimensions. | references/dimensions.md |
| v1 campaign audit, Phase 10 (2026-09-14) | Tail latency, cache-failure modes, and queue economics named nowhere — p50-only latency, hit-rate-only caching, purpose-only queues | Tail-latency bullet (what dominates p99 for this workload), cache failure-mode design (cold start, stampede, outage fallback), queue economics (lag alarms, DLQ retention, retention pricing) | references/dimensions.md (Load shape, Operability, Coordination) |

## Key new intelligence encoded

1. **The "Premature Microservices" Trap for Agents** — explicitly warns against distributing agentic workflows too early, favoring orchestrated modular monoliths until operational contention demands independent scaling.
2. **Bounded Agency & Stewardship** — frames AI agent system design not as full autonomy, but as "bounded agency" where human stream-aligned teams retain stewardship and require architectural interfaces to monitor and control the agent.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agent execution frameworks | LangGraph / Microsoft Agent Framework (2025/2026 patterns) |
