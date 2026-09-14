# blueprint — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Docs-as-Code Anti-Patterns (2025/2026) | "Monolithic Documentation" — forcing every C4 level into one giant diagram or document destroys readability and maintainability. | Enforces strict C4 Audience-Driven Abstraction, requiring the agent to pick targeted views rather than a monolith. | SKILL.md §2 |
| Security as an Afterthought in Generative AI Diagrams | AI-generated architecture diagrams frequently omit trust boundaries, leading to designs that obscure threat vectors. | Mandates explicit `subgraph` trust boundaries and adds a dedicated Threat Model diagram to the menu. | references/diagram-guide.md |
| Model-Backed Architecture (C4 + DSLs) | Drawing shapes is dead; architecture must be backed by diffable models (Mermaid/Structurizr) that represent real code. | Reaffirms the rule that every node must trace to code, rejecting hallucinated infrastructure. | SKILL.md §1 |
| v1 campaign audit, Phase 09 (2026-09-14) | Deliverable had no provenance header (readers can't tell if diagrams match current code); decisions lived only in the plan, not the architecture doc | Provenance header (date + commit + map freshness) on the README index; Decisions section linking plan AgDRs or stating inline | SKILL.md §workflow step 4, §output contract |

## Key new intelligence encoded

1. **C4 Audience-Driven Abstraction** — formalized the rule to avoid Monolithic Documentation by strictly selecting views based on audience (Context for business, Container for engineering).
2. **Explicit Trust Boundaries** — security contexts are now mandatory visual elements (`subgraph`) rather than implicit assumptions, directly addressing the "Security as an Afterthought" anti-pattern.
3. **Threat Model Diagramming** — introduced a dedicated pattern for visualizing threat vectors across trust boundaries.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Generative AI Diagramming | Mermaid / C4 Model auto-generation (2026 trends) |
