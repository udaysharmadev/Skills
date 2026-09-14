# Claims registry

Every public quantitative or compatibility statement must have a row here
(schema: `shared/schemas/claim.md`). README facts are generated or
validated against this file. CI (`scripts/check-claims`) blocks missing
evidence for release-critical claims. Last swept: 2026-09-14.

| id | statement | class | evidence | verified | reproduce | stale-if |
|---|---|---|---|---|---|---|
| C-001 | Bundle contains 28 skills | FACT | `skills/` tree + `scripts/validate-skills` | 2026-09-14 | `scripts/validate-skills` | skill set changes |
| C-002 | Each SKILL.md ≤500 lines, self-contained, frontmatter valid | FACT | `scripts/validate-skills`, `scripts/check-names`, `scripts/check-links` | 2026-09-14 | run the three scripts | any skill edit |
| C-003 | `npx skills add udaysharmadev/Skills --all` installs the bundle | MEASURED | clean-dir install log 2026-09-14 (27 skills; see C-004) | 2026-09-14 | clean dir + CLI `--all` | CLI major release or 90 days |
| C-004 | 28-skill install (incl. `handsfree`) succeeds from a clean directory | MEASURED | clean-dir install 2026-09-14: 28/28 folders under `.agents/skills/` incl. `handsfree`, universal + Claude Code targets reported | 2026-09-14 | clean dir + `npx -y skills add udaysharmadev/Skills --all -y`, count `.agents/skills/` | CLI major release, skill-set change, or 90 days |
| C-005 | Trigger routing smoke: Codex 11/12, OpenCode 12/12 | MEASURED | `evals/results/20260914-*.json` (gitignored raw; curated release evidence pending) | 2026-09-14 | `scripts/eval-trigger --tier smoke` | model/agent version change |
| C-006 | Any skill improves outcomes vs same-model baseline | UNVERIFIED | — (Layer C deferred to proof phase; zero trials) | — | per-skill protocol in `evals/outcomes/` | — |
| C-007 | Compatibility beyond Codex/OpenCode routing smoke | UNVERIFIED | `docs/compatibility.md` (Claude hangs, Cursor/Antigravity unavailable) | — | per-runtime harness | runtime availability changes |
| C-008 | skills.sh badge resolves | UNVERIFIED | — (indexing/security review pending; badge must not ship broken) | — | install from skills.sh, confirm listing | listing appears |
| C-009 | Context footprint: SKILL.md ~159KB total, frontmatter ~3525 tok always-on | DERIVED | `scripts/check-context` (byte-estimate method stated in script) | 2026-09-14 | `scripts/check-context` | any skill edit |
| C-010 | `concierge` outcome evidence: MIXED (codex O1 treatment 4/4 vs baseline 1/4; O2/O3 no lift available) | MEASURED | `docs/benchmarks/concierge.md` trial table (raw traces gitignored in `evals/results/`) | 2026-09-14 | `scripts/eval-outcome --skill concierge --agent codex --trials 3` | model/agent version change |
| C-011 | `hotseat` outcome evidence: PROVEN LIFT on debate-structure footprints (treatment 5/5 incl. held-out vs baseline 0/5; strong-critic baseline; ~2× output cost) | MEASURED | `docs/benchmarks/hotseat.md` trial table (raw traces gitignored in `evals/results/`) | 2026-09-14 | `scripts/eval-outcome --skill hotseat --agent codex --trials 2` | model/agent version change |
Prohibited until a row above (or a new row with evidence) allows it:
stars, installs, users, testimonials, benchmark wins, "works on X"
compatibility, token-saving percentages.
