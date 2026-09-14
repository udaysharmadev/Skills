# recall — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Context Window Pollution (2025/2026 AI Agent literature) | Unbounded context injection is the primary cause of reasoning degradation in long-running agents. Memory must be a governed state machine, not just a vector store. | Demands strict soft caps, compaction rules, and state machine lifecycles for memory entries. | SKILL.md §rules, references/file-formats.md |
| Finite State Machine (FSM) Agent Architecture | Agent knowledge rots at different speeds; treating all memory as equivalent leads to context drift. | Defines the Knowledge Hierarchy: Fact vs Decision vs Lesson vs Status. | SKILL.md §rules |
| Memory TTL (Time-To-Live) strategies | Transient blockers and next steps become fossilized if not given an explicit expiration date. | Enforces a `[TTL: date]` constraint on STATUS entries to prevent append-only rot. | references/file-formats.md |
| v1 campaign audit, Phase 27 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (read-before-write assumed, validator→compact→create ladder lived in gates/stops only) | Prerequisites (files + genuine need) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **Explicit Knowledge Hierarchy** — distinguishes between Facts (true until codebase changes), Decisions (true until context changes), and Lessons (portable, true everywhere).
2. **Decision State Machine** — formalizes decisions into a lifecycle (`[Active]` -> `[Superseded]` -> `[Deprecated]`), forcing agents to transition states rather than just deleting or silently contradicting past choices.
3. **Time-To-Live (TTL) for Transient State** — introduces a mandatory TTL for blockers and next steps in `STATUS.md` to prevent context pollution from forgotten, resolved issues.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Context window pollution / memory governance | "Lost in the Middle" and 2026 context degradation studies |
| Hierarchical agent memory | LangGraph memory tiered storage (2025/2026) |
