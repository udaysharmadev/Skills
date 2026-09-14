# masterplan — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| "Plan-Then-Execute" Agent Architecture (2025/2026) | Separating planning from execution dramatically reduces agent hallucination and looping. Plans must be written for the *executor agent*, not just humans. | Frames `masterplan` explicitly as the Planner creating an "Executable Plan" for `pilot`. | SKILL.md §introduction |
| Machine-Readable Task Structures (MCP / Open SWE) | Loose task descriptions ("delivers X") confuse executor agents. Tasks must be verb-led actions with measurable validation criteria. | Replaced vague slice deliverables with strict Action + Validation Criteria fields. | references/plan-template.md |
| AgDR (Agent Decision Records) | Standard ADRs are too slow for agent loops, but architecture choices still need rationale tracking in case the agent guesses wrong. | Embedded the AgDR structure into the Decisions section of the plan. | SKILL.md §3 |
| v1 campaign audit, Phase 06 (2026-09-14) | Paths lacked epistemic status (verified-or-nothing hid uncertainty); no ordering rule put unknown-resolving work first; irreversible steps had no explicit marking | confirmed/probable/to-discover path labels, uncertainty-collapses-first sequencing, IRREVERSIBLE slice marking with user checkpoint | SKILL.md §workflow steps 2+4, §quality gates |

## Key new intelligence encoded

1. **Planner/Executor Separation** — formally acknowledges that `masterplan` writes plans intended for `pilot` to execute systematically, shifting the audience from human developer to downstream agent.
2. **Verb-Led Executable Slices** — slices now require a specific Action instruction rather than a passive outcome description.
3. **Agent Decision Records (AgDR)** — architecture decisions made during planning are explicitly recorded with their alternatives and failure conditions to provide durable context for the executor.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agentic software documentation | "Shift Left" documentation trends (2025/2026) |
| Planner-Executor architectures | LangGraph / SWE-agent multi-agent patterns |
