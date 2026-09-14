# spelunk — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Behavioral code analysis (2025 engineering blogs) | Technical debt isn't just "bad code" — it's code that actively causes friction. Churn × complexity quadrant pinpoints it. | Maps discovery to organizational impact rather than just static analysis. | SKILL.md risk-map mode, discovery-map.md hotspots |
| Cognitive debt discussions (2025 tech leadership) | The gap between implementation and team understanding is as dangerous as tech debt. | Adds a new failure mode to hunt for during discovery. | SKILL.md risk-map mode |
| Outside-in discovery patterns | Starting with the request lifecycle grounds exploration in real-world behavior, not abstract architecture. | Makes "teach" mode concrete rather than hand-wavy. | SKILL.md teach mode |

## Key new intelligence encoded

1. **Churn × Complexity quadrant** — formalizes the behavioral analysis of the codebase, distinguishing active friction zones from stable landmines.
2. **Cognitive debt tracking** — explicitly looks for signs that the codebase has outgrown the team's mental model (stale comments, TODO-in-prod).
3. **Trust-boundary surfacing in quick mode** — ensures that even fast answers highlight critical security/auth/PII boundaries if they are in play.
4. **Concrete request lifecycle narrative** — requires naming real symbols and paths in teach mode, rather than just abstract descriptions.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Behavioral code analysis | CodeScene and related 2025 methodologies |
| Cognitive debt in engineering | Modern tech leadership discourse |
