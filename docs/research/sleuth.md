# sleuth — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Debugging Anti-Patterns (2025/2026) | The "Guess-and-Check" loop is the primary failure mode of autonomous debugging agents, burning tokens without converging on a root cause. | Explicitly bans guess-and-check edits and "Amnesia" (retrying the same failed action), forcing hypothesis-driven elimination instead. | SKILL.md §Banned List |
| Observability Blind Spots in Agentic Systems | Traditional black-box APM tools cannot debug non-deterministic agent workflows. | Adds "Trace-Based Observability" to ensure agents inspect the entire reasoning and tool-call hierarchy when debugging orchestrations. | references/techniques.md |
| Hallucinated Fixes | Agents without strict runtime grounding default to suggesting plausible but incorrect structural patches. | Bans suggesting any fix before gathering runtime evidence (logs, DB state). | SKILL.md §Banned List |

## Key new intelligence encoded

1. **Anti-Amnesia / Action Fingerprinting** — bans the agent from repeatedly trying identical or trivially tweaked fixes that have already failed, forcing it to kill the underlying hypothesis instead.
2. **Trace-Based Observability** — directs the debugging effort away from shallow HTTP responses and toward deep LLM reasoning traces when diagnosing modern orchestrated systems.
3. **The Banned List** — formalizes the rejection of the "vibe debugging" behaviors that make LLMs untrustworthy maintainers.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agent state observability | OpenTelemetry for LLM traces (2026 standards) |
