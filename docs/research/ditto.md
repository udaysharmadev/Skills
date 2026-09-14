# ditto — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Design-to-Code mapping (2025/2026) | Recreating UI via raw hex/pixel guessing creates brittle code. Agents must map elements directly to existing Design System tokens (e.g., via MCP). | Replaces the "Infer" step with an "Infer or Map" step, explicitly requiring integration with MCP design system servers where available. | SKILL.md §3 |
| Visual QA loops (Structural vs Pixel diffing) | Traditional pixel-matching fails across responsive viewports and minor browser rendering differences. Modern Visual QA analyzes structural DOM integrity. | Updates the Fidelity dimensions to prioritize structural analysis and semantic token mapping over naive pixel diffing. | SKILL.md §5 |
| v1 campaign audit, Phase 13 (2026-09-14) | Both research traces verified encoded; only gap is the missing tool-selection ladder in the body (browser → static → description-only rungs lived in stops/reference only) | Tool selection/fallback section consolidating the four capability rungs | SKILL.md (Tool selection/fallback) |

## Key new intelligence encoded

1. **Design System Mapping via MCP** — instructs the agent to link the UI recreation to formal design systems (like StitchMCP) rather than hallucinating raw CSS variables, ensuring the cloned UI survives in a production codebase.
2. **Structural Visual QA** — shifts the comparison loop's focus away from brittle pixel-matching toward structural integrity and responsive layout behavior.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Design System MCPs | StitchMCP and Figma agentic pipelines (2026) |
