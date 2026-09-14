# harden — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| OWASP GenAI Top 10 (2025/2026) | Prompt injection is no longer a chatbot curiosity; it is a systemic vulnerability akin to RCE, especially via Indirect Prompt Injection (IPI) from external documents. | Elevates "Indirect Prompt Injection" to A03 (Injection) and treats external data processed by agents as untrusted. | references/attack-surface.md |
| Excessive Agency Risks | Granting agents standing write-access without human-in-the-loop gates is a critical architectural failure. | Adds "Excessive Agency" to the A04 (Insecure Design) checklist. | references/attack-surface.md |
| Anti-CVSS Theater | Security audits that spam 50 generic CVEs from package scanners ignore contextual exploitability and cause alert fatigue. | Bans "CVSS Theater", requiring findings to be prioritized by actual reachability and impact rather than generic scores. | SKILL.md §Finding format |
| v1 campaign audit, Phase 19 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (authorization assumed-but-unstated, scanner→adversarial→static ladder scattered) | Prerequisites (code + runnable path + authorization line) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **OWASP GenAI Top 10 Integration** — explicitly adds modern agentic attack vectors (Indirect Prompt Injection, Excessive Agency) to the core threat model.
2. **Anti-CVSS Theater** — forces the agent to differentiate between a theoretical CVE in a dev-dependency and an actually exploitable runtime vulnerability.
3. **Agentic Blast Radius** — expands threat modeling to include the damage an autonomous agent could cause if its context window is poisoned.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM Vulnerability frameworks | OWASP Top 10 for Agentic Applications (2026) |
