# frontpage — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Documentation Failures (2025/2026) | Agents trained on popular open-source repositories often hallucinate "professional" CI/CD badges that don't exist and link nowhere. | Bans "Hallucinated Badges", requiring the agent to verify that the CI pipeline actually exists before adding the visual flair. | SKILL.md §Banned List |
| Theoretical Quickstarts | Agents invent commands (like `npm install <repo>`) for packages that have never been published, providing plausible but broken instructions. | Forbids "Theoretical Quickstarts," mandating that all usage instructions must be executed in a real shell by the agent before being written into the README. | SKILL.md §Banned List, SKILL.md §Workflow |
| Template Bloat | Agents tend to fill out massive 10-section documentation templates even when documenting a 50-line script, hiding the actual project under boilerplate. | Bans "Template Bloat", forcing the structure to scale proportionately to the codebase. | SKILL.md §Banned List |
| v1 campaign audit, Phase 22 (2026-09-14) | All three traces verified encoded; only gap is the missing Tool selection/fallback section (snippet-execution and link-check ladders lived in workflow steps only) | Tool selection/fallback section consolidating the four verification rungs | SKILL.md (Tool selection/fallback) |

## Key new intelligence encoded

1. **Context Engineering for Docs** — shifts README generation from "filling out a template" to "documenting verified reality."
2. **Anti-Hallucination Guardrails** — explicitly targets the visual and procedural hallucinations (badges and un-published package commands) that AI models default to.
3. **Execution-Backed Claims** — enforces that the agent must act as the first user, running its own quickstart instructions.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM docs verification | Automated instruction execution via containers (2026) |
