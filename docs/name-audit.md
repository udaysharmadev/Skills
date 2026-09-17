# Name collision audit

**Status: partial, sampled, not exhaustive.** Method and per-slug status
below; the full exact-name audit (GitHub repo/code search + skills.sh
lookup per slug) is a pre-announcement task tracked in the v1.0 gate.

## Method

1. **Sampled ecosystem check** (2026-09-14): the current skills.sh
   leaderboard top installs (`find-skills`, `vercel-react-best-practices`,
   `web-design-guidelines`, per public install reports): none of the 28
   slugs appear among them.
2. **Watchlist adjacency**: the known namesakes recorded in
   `shared/terminology/names.md` (runwayml, Laravel Blueprint, The
   Sleuth Kit, FrugalGPT, DittoLive) are different categories/domains;
   risk assessed as moderate-or-low.
3. **Pending**: exact-match GitHub code search for `SKILL.md` name
   fields, and per-slug skills.sh search — requires the final pass
   immediately before any public announcement. The check-names script
   additionally blocks a hard blacklist of established names.

## Per-slug status

| Skill | Sampled leaderboard | Known adjacent namesake | Risk | Decision |
| --- | --- | --- | --- | --- |
| concierge | no collision found | generic word | low | keep |
| hotseat | no collision found | generic word | low | keep |
| spelunk | no collision found | generic word | low | keep |
| scout | no collision found | generic word | low | keep |
| distill | no collision found | generic word | low | keep |
| masterplan | no collision found | generic word | low | keep |
| pilot | no collision found | generic word | low | keep |
| recall | no collision found | generic word | low | keep |
| blueprint | no collision found | Laravel Blueprint, bento/blueprint libs | moderate | keep: different ecosystem |
| headroom | no collision found | headroom.js (older) | low | keep |
| polish | no collision found | generic word | low | keep |
| friction | no collision found | generic word | low | keep |
| ditto | no collision found | DittoLive (sync) | low | keep |
| unslop | no collision found | none known | low | keep |
| backend | no collision found | maximally generic | low | keep (suite context disambiguates) |
| roadtest | no collision found | generic word | low | keep |
| harden | no collision found | generic word | low | keep |
| sleuth | no collision found | The Sleuth Kit (forensics) | moderate | keep: different domain |
| proof | no collision found | generic word | low | keep |
| referee | no collision found | generic word | low | keep |
| hotpath | no collision found | perf-community term | low | keep |
| janitor | no collision found | generic word | low | keep |
| frontpage | no collision found | MS FrontPage (dated) | low | keep |
| findable | no collision found | generic word | low | keep |
| frugal | no collision found | FrugalGPT (paper) | low | keep |
| cleared | no collision found | generic word | low | keep |
| runway | no collision found | RunwayML (AI video) | moderate | keep: different category |

"No collision found" above means: not found in the sampled sources on
2026-09-14. It does **not** mean unique. Pre-announcement, run the full
exact-match pass and update this table with dates + sources; any hit on
an established skill goes to the pre-approved alternates list
(`shared/terminology/names.md`) rather than ad-hoc renaming.
