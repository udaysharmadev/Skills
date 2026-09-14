# janitor — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Git Anti-Patterns (2025/2026) | Autonomous agents create "multi-concern" changes and squash them into single commits, destroying the atomic history necessary for bisecting regressions. | Bans "Blind Squashing" and mandates atomic commits by concern. | SKILL.md §Banned List |
| AI Branch Sprawl | Rapid agentic experimentation litters repositories with abandoned, unmerged branches, confusing automated tooling and humans alike. | Adds "Orphaned Branch Sprawl" to the Banned List and hygiene checklist as a primary cleanup target. | SKILL.md §Banned List, references/hygiene-checklists.md |
| Commit Message Vibe Coding | Agents summarize the diff line-by-line rather than explaining the architectural intent, rendering the git log useless for RCA. | Forbids diff narration in favor of business intent ("Why > what"). | SKILL.md §Banned List |

## Key new intelligence encoded

1. **Context Preservation** — forces agents to respect the repository's history by breaking down large, generated code blocks into atomic commits.
2. **AI Sprawl Cleanup** — directs the agent to actively hunt down and propose the deletion of abandoned experimental branches created by other agents.
3. **Intent-Driven Commit Messages** — halts the practice of LLM-generated diff narration in favor of writing the missing "why" context.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agent-assisted PR automation | Structured PR generation (2026) |
