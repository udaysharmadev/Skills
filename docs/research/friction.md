# friction — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Usability Heuristics (2025/2026) | Traditional UI heuristics are insufficient for AI agents. Evaluation must include execution trajectories, not just static screens. | Adds a dedicated AI/Agentic UX section to the usability checklist. | references/usability-checklist.md |
| Human-in-the-loop Evaluation Patterns | Users abandon agents that fail silently or get stuck in loops without an escalation path. | Enforces checking for "Graceful Degradation / Escalation" paths in AI UX. | references/usability-checklist.md |
| System Status Visibility (Agentic) | Raw tool-call JSON or massive chain-of-thought dumps destroy usability. Status must be translated to human-readable audit trails. | Adds constraints for "Planning Visibility" and plain-language "Audit Trails". | references/usability-checklist.md |
| v1 campaign audit, Phase 12 (2026-09-14) | Tool fallback scattered, healthy-flow honesty unstated — headless runs could invent walk evidence, clean flows invited padded findings | Tool selection/fallback section (walk → static + unverified ladder), no-findings stop condition (cite walks, never invent) | SKILL.md (Tool selection/fallback, Stop conditions) |

## Key new intelligence encoded

1. **AI/Agentic UX Dimension** — explicitly expands the usability audit to cover the unique friction points introduced by AI interfaces (transparency, escalation, and planning visibility).
2. **Planning Visibility** — requires AI systems to surface their intended execution plan before taking action, allowing users to intercept destructive errors.
3. **Graceful Degradation** — treats the absence of a clear human escalation path as a UX failure, acknowledging that AI loops will eventually get stuck.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| AI Usability Heuristics | 2026 updates to Nielsen's heuristics for agentic systems |
