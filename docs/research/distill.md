# distill — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Requirements Engineering for LLMs (2025/2026 research) | LLMs are capable of proactive ambiguity detection (semantic, linguistic, functional) rather than just passive transcription. | Replaces "gap check" with active "ambiguity detection" targeting specific requirement failures. | SKILL.md §2 |
| BDD evolution / Executable Specifications (2026 trends) | Industry is moving away from brittle manual Gherkin (Given/When/Then) toward AI-native "agent-executable specifications" where the requirement itself is verifiable by a downstream agent. | Replaces "Acceptance criteria" with "Agent-executable specifications" to signal the shift in audience (agent, not just human QA). | SKILL.md, references/brief-template.md |
| Less is More (Agentic framework research) | High-quality, structurally precise requirements are critical for successful distillation into coding tasks. | The template requires actionable, verifiable facts over product philosophy. | references/brief-template.md |

## Key new intelligence encoded

1. **Active Ambiguity Detection** — formalized the gap check to specifically look for undefined boundaries, contradictory constraints, and missing definitions of "good".
2. **Agent-Executable Specifications** — deprecated standard "Acceptance criteria" in favor of criteria written explicitly for a downstream agent to verify without human judgment.
3. **Audience shift** — explicitly grounds the brief as an interface between agents (distiller → planner/implementer) rather than just a human-readable document.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| AI-native BDD alternatives | 2025–2026 software testing frameworks (TestMu, etc.) |
| LLM Requirements Engineering | NLP requirements ambiguity research |
