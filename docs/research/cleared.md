# cleared — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Release Anti-Patterns (2025/2026) | "Evidence Inflation" occurs when agents promise that a system is ready based on theoretical code reading rather than executing the actual CI/CD checks. | Bans "Evidence Inflation (Hallucinated Passes)", making a fabricated pass an automatic BLOCKED verdict. | SKILL.md §Banned List |
| The Workshop Trap | Agents tasked with reviewing readiness often get distracted by fixing minor bugs they find, turning a binary release gate into a never-ending refactor session. | Bans "The Workshop Trap", enforcing that the agent's role is strictly as an auditor at this stage. | SKILL.md §Banned List |
| v1 campaign audit, Phase 25 (2026-09-14) | Both traces verified encoded; only gap is the missing Tool selection/fallback section (runner → sibling-reports → unrunnable ladder lived in workflow/gates only) | Tool selection/fallback section consolidating the three evidence rungs | SKILL.md (Tool selection/fallback) |

## Key new intelligence encoded

1. **Gate Integrity** — establishes that a readiness check must be a pure, read-only audit of evidence; the agent cannot silently fix code to make the audit pass.
2. **Anti-Laundering** — prevents the agent from summarizing away the user's accepted risks in order to present a "cleaner" final report.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agent deployment criteria | Evidence-backed deployment pipelines (2026) |
