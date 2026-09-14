# concierge — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Anthropic, Effective context engineering for AI agents (Sep 2025) | Context is finite; harness rules encode model weaknesses and age as models improve | Avoid brittle micro-chains; prefer invariants | SKILL.md §5, routing.md rules |
| Research synthesis on over-routing failures (2026) | Each unnecessary handoff adds a seam where information can degrade | Explicit "smallest chain" rule strengthened | SKILL.md intro, routing.md rule 1 |
| "Route by uncertainty source" pattern (2025–2026 deficit-led routing) | Same noun routes to different specialists depending on what's missing | New "what is missing?" decision table | SKILL.md §5, routing.md §Step 0 |
| OpenAI Agents SDK orchestration docs | Manager vs handoff: keep ownership for bounded subtasks; full handoff when the specialist domain becomes the task | Specialist completion predicates | routing.md completion predicates table |
| Simon Smith on skill-library duplication/discovery | Skill libraries scale into overlap and confusion | Routing should operate from compact manifest, not rediscover skills | SKILL.md notes, routing.md rule 5 |
| v1 campaign audit, Phase 01 (2026-09-14) | Predicate table covered 10/28 skills; `handsfree` had no pattern row; no loop ceiling existed | Router could not tell when 18 specialists were done, misrouted autonomy complaints, and could re-dispatch forever | routing.md completion predicates (28/28), handsfree + direct + none pattern rows, rule 7 loop detection |

## Key new intelligence encoded

1. **Uncertainty-source routing** — "What is missing that blocks correct next action?" table replaces
   topic-noun matching for non-obvious cases
2. **Evidence reuse table** — concrete examples of when to skip re-running a skill
3. **Completion predicates** — each specialist has a defined return condition
4. **Capability rungs** — `capability-degradation.md` gives explicit fallback tiers with disclosure rules
5. **Harness aging note** — skill explicitly avoids brittle if/then chains that become stale
6. **Loop ceiling** — same domain dispatched at most twice per task; the third dispatch is defined as failure
7. **Direct/none as first-class routes** — micro-changes and non-repo requests terminate in concierge instead of entering a chain

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
