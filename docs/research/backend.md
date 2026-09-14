# backend — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Backend Architecture (2025/2026 patterns) | LLMs are non-deterministic and will retry aggressively upon failures. Idempotency is no longer just for payments; it's required for agent safety (Internal Ledgers). | Elevates idempotency from a sub-bullet to a core rule protecting against agent-driven duplication. | SKILL.md §3, references/checklists.md |
| Structured Output Validation | "Syntax-correct" LLM output is not safe. It must be treated as an untrusted boundary crossing. | Formalizes LLM outputs as a trust boundary requiring schema validation (Pydantic/Zod). | SKILL.md §1, references/checklists.md |
| MCP (Model Context Protocol) Adoption | Exposing internal APIs to agents via bespoke REST tools is brittle; MCP is the 2026 standard for agentic integrations. | Adds MCP server requirements for outbound agent APIs. | references/checklists.md |
| v1 campaign audit, Phase 08 (2026-09-14) | Same webhooks bullet in two checklist sections; no outbox/deadlock/retry-ownership/backpressure rules; PRD Prerequisites + Tool-fallback sections absent | Removed duplicate, added outbox atomicity, caller-owned retries with deadline propagation, lock-order + whole-transaction deadlock retry, backpressure-vs-circuit distinction, contract-compliance sections | references/checklists.md, SKILL.md |

## Key new intelligence encoded

1. **LLM outputs as a trust boundary** — explicitly states that agent/LLM generated data must be validated strictly against a schema (Zod/Pydantic) before being trusted by the backend.
2. **Agent-Safe Idempotency** — expands idempotency requirements to cover non-deterministic agent retries, recommending internal ledgers to ensure exactly-once execution.
3. **MCP Integration** — mandates the use of Model Context Protocol (MCP) servers when exposing internal APIs for agent consumption.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agent integration protocols | Model Context Protocol (MCP) ecosystem (2025/2026) |
| Multi-agent orchestration | LangGraph / AutoGen v0.4 patterns |
