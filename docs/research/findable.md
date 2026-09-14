# findable — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic SEO Anti-Patterns (2025/2026) | Agents trained on SEO templates tend to hallucinate fake structured data (e.g. 5-star `AggregateRating` for a new blog) just to satisfy a JSON-LD schema, feeding misinformation to AI search engines. | Bans "Hallucinated Structured Data" and enforces strict validation of schema.org reality. | SKILL.md §Banned List, references/seo-checklist.md |
| GEO vs SEO Shifts | 2026 Answer Engine Optimization (GEO) penalizes volume-based, keyword-stuffed "slop content." Discoverability is earned via structural clarity and factual citation. | Bans "Slop Content Generation" and forces the agent to focus on machine-legible structure over word-count inflation. | SKILL.md §Banned List |
| The Invisible Meta Tag | Agents often write JS code to append `<meta>` tags on the client-side of SPAs, failing to realize that search crawlers will never see them. | Adds the "Invisible Meta Tags" warning, requiring SSR/prerendering context before attempting SEO fixes. | SKILL.md §Banned List |

## Key new intelligence encoded

1. **Anti-Slop Optimization** — explicitly aligns the skill with 2026 GEO realities, forbidding the generation of filler text to "improve rankings."
2. **Schema Truth Verification** — forces agents to ensure JSON-LD data strictly matches the verifiable, real-world content of the page, preventing hallucinated knowledge graphs.
3. **Rendered-First Audit** — mandates that agents `curl` the live URL to verify meta tags, combating the hallucination of client-side-only fixes.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Generative Engine Optimization (GEO) | AI citation metrics and `llms.txt` standardization (2026) |
