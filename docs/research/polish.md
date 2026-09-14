# polish — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| "AI Design Slop" Anti-Patterns (2025/2026) | Generative UI often lacks systemic rules, leading to "vibe coding" that breaks under real data constraints or ignores accessibility standards. | Bans "Vibe Coding" and mandates "Stress Testing (Data Scaling)". | SKILL.md §banned, references/audit.md |
| Semantic A11y in Generative UI | AI tools frequently produce visually appealing but semantically broken layouts (e.g., using `<div>` instead of `<h1>`). | Enforces strict Semantic Structure rules in the Reach audit. | references/audit.md |
| Constrained Generation vs Blank Canvas | Agents guessing at design systems produce generic templates. Agents forced to use existing tokens produce branded, cohesive UI. | Explicitly bans the "Blank Canvas" hallucination, elevating existing design tokens to a hard constraint. | SKILL.md §banned |

## Key new intelligence encoded

1. **Anti-Slop "Vibe Coding" Ban** — explicitly rejects UI designs that only work with perfect, symmetrical dummy data, requiring designs to survive data scaling and empty states.
2. **Semantic A11y Enforcement** — adds semantic HTML validation to the audit to prevent visually polished but structurally broken outputs.
3. **Constrained Generation** — reinforces that existing design tokens are not suggestions, but hard boundaries that the agent must not overwrite for novelty.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Generative UI slop identifiers | 2026 design system evolution |
