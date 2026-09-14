# concierge — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Anthropic, Effective context engineering for AI agents (Sep 2025) | Context is finite; harness rules encode model weaknesses and age as models improve | Avoid brittle micro-chains; prefer invariants | SKILL.md §5, routing.md rules |
| Research: over-routing amplifies errors 17.2× (2026) | Each unnecessary handoff is a seam where information degrades | Explicit "smallest chain" rule strengthened | SKILL.md intro, routing.md rule 1 |
| "Route by uncertainty source" pattern (2025–2026 deficit-led routing) | Same noun routes to different specialists depending on what's missing | New "what is missing?" decision table | SKILL.md §5, routing.md §Step 0 |
| OpenAI Agents SDK orchestration docs | Manager vs handoff: keep ownership for bounded subtasks; full handoff when the specialist domain becomes the task | Specialist completion predicates | routing.md completion predicates table |
| Simon Smith on skill-library duplication/discovery | Skill libraries scale into overlap and confusion | Routing should operate from compact manifest, not rediscover skills | SKILL.md notes, routing.md rule 5 |

## Key new intelligence encoded

1. **Uncertainty-source routing** — "What is missing that blocks correct next action?" table replaces
   topic-noun matching for non-obvious cases
2. **Evidence reuse table** — concrete examples of when to skip re-running a skill
3. **Completion predicates** — each specialist has a defined return condition
4. **Capability rungs** — `capability-degradation.md` gives explicit fallback tiers with disclosure rules
5. **Harness aging note** — skill explicitly avoids brittle if/then chains that become stale

## Rejected / weak ideas

| Idea | Why not adopted |
| --- | --- |
| Static route scores (numeric formula) | Adds complexity without evidence of better decisions; model judgment is flexible |
| Skill manifest generation script | Useful but belongs in separate tooling, not runtime routing |
| Hardcoded "always plan before coding" rule | Contradicted by Anthropic guidance on harness aging |

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| OpenAI Agents SDK orchestration patterns | openai.github.io/openai-agents-python — 2025 |
| Anthropic context engineering | anthropic.com/engineering — Sep 29, 2025 |
| Over-routing error amplification research | Field research synthesis, 2026 |
