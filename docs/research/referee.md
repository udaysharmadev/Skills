# referee — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Context Starvation in Agent Reviews (2025/2026) | AI agents reviewing diffs in isolation often approve breaking signature changes because they fail to search the wider codebase for downstream callers. | Bans "Context Starvation" (Isolation Review), mandating that reviewers use search tools to verify all upstream callers. | SKILL.md §Banned List, references/finding-format.md |
| LGTM Syndrome & Rubber-Stamping | Agents are easily fooled by syntactically perfect code that completely misses the business intent, rubber-stamping logic flaws. | Delineates the difference between an honest clean review and "LGTM Syndrome" (approving syntax while ignoring intent). | SKILL.md §Banned List, references/finding-format.md |
| Review Fatigue / Nit-Picking | Agents often output 15 stylistic opinions to "prove" they did work, causing developers to ignore the review. | Bans "Nit-Picking / AI Pedantry", enforcing a strict triage where nits are collapsed and never block. | SKILL.md §Banned List |

## Key new intelligence encoded

1. **Context Verification** — establishes that reading a diff is insufficient; an agent must actively search the codebase to ensure API/signature changes do not break downstream dependencies.
2. **Anti-Rubber-Stamping** — re-anchors the review process on the "Intent Pass" to prevent the agent from blindly approving clean but incorrect AI-generated code.
3. **Severity-Driven Triage** — codifies the rule that manufacturing findings to look thorough is an anti-pattern.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agentic Code Review architectures | Progressive context disclosure in AI PR reviews (2026) |
