# scout — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| SWE-agent 2026 architectural analysis | API version mismatches and hallucinations are a systemic architecture issue, not just bad prompting. "No Source = No Claim" is the standard mitigation. | Agents must treat un-grounded memory as unsafe for API signatures. | SKILL.md §rules |
| Structured Grounding research (Source-Driven Development) | Agents need explicit source hierarchies where official structured specs (like MCP or OpenAPI) override model weights. | Formalizes the "source ladder" and penalizes general web knowledge. | references/source-ladder.md |
| Structure-Aware Chunking best practices | Agents fetching full monolithic index pages lose context; they must fetch the specific endpoint documentation. | Directs the web fetch strategy to target specific sub-pages. | SKILL.md §rules |
| v1 campaign audit, Phase 04 (2026-09-14) | Claim-level verdicts missing (global confidence only); conflict rules lived in the reference unreferenced; note structure unchecked by tooling | Per-fact tier+date rule, SKILL.md pointer to ladder conflict resolution, `scripts/check-note` structure validator wired into the workflow | SKILL.md §rules + §workflow, skills/scout/scripts/check-note |

## Key new intelligence encoded

1. **"No Source = No Claim" rule** — strictly prohibits answering API signature questions from model memory; requires explicit marking of unverified memory.
2. **MCP integration in Source Hierarchy** — adds Model Context Protocol servers to Tier 1, recognizing structured API specs as the highest-fidelity external source.
3. **General knowledge penalization** — explicitly states that general web knowledge must not override official documentation or vendored code.
4. **Targeted documentation fetching** — instructs the agent to fetch the specific endpoint or interface documentation rather than the monolithic index page.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| SWE-agent successor architectures | mini-swe-agent / Open SWE 2026 |
| Grounding techniques | Model Context Protocol (MCP) ecosystem |
