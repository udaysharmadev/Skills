# unslop — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Codebase Mess Patterns (2025/2026) | "AI Sprawl" occurs because it is cognitively cheaper for an agent's context window to accrete new parallel files than to refactor existing ones. | Adds "AI Sprawl (Accretion by Avoidance)" to the slop catalog to force consolidation. | references/slop-catalog.md |
| Zombie Abstractions | Agents trained on 2015-era enterprise Java patterns tend to hallucinate strategy patterns and abstract base classes for single-implementation functions. | Renames "Premature abstractions" to "Zombie abstractions," directing the agent to flatten these AI-hallucinated layers. | references/slop-catalog.md |
| The Refactor Loop of Death | Agents instructed to "clean up this code" without a behavioral baseline will successfully produce pristine, bug-free code that has completely lost its business logic. | Adds the explicit warning against the "Refactor Loop of Death," making tests a hard prerequisite for any detox operation. | SKILL.md §Rules |

## Key new intelligence encoded

1. **AI Sprawl Diagnosis** — recognizes that unslop's main job is reversing the agentic tendency to write net-new code instead of modifying the old.
2. **Zombie Abstraction Removal** — targets the specific architectural hallucinations (unnecessary interfaces/managers) introduced by AI models.
3. **The Refactor Loop of Death** — enforces the rule that syntactic cleanup without behavioral verification is destruction.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM code-accretion benchmarks | Context-window bloat studies (2026) |
