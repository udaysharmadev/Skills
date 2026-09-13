# Contributing

Thanks for helping build the bundle. This repo holds itself to the standard
its skills preach: evidence, verification, no slop.

## The bar

A skill ships only when it meets PRD §19 ("legendary skill"):

- clear trigger and clear non-trigger;
- model-independent workflow with capability fallbacks;
- real output contract and verification loop;
- token-conscious `SKILL.md` (≤ 500 lines, detail in `references/`);
- trigger cases in `evals/trigger/cases.md`;
- known limitations documented;
- no unsupported marketing claim.

If a contribution can't meet the bar yet, say so in the PR — an honest
"not ready" beats a shipped maybe.

## Workflow

1. Fork/branch from `main`.
2. Make your change. Keep each skill folder self-contained (see [AGENTS.md](AGENTS.md)).
3. Run the validators:

   ```bash
   scripts/validate-skills
   scripts/check-names
   scripts/check-links
   scripts/build-docs   # if frontmatter changed
   ```

4. Add trigger cases for any new or changed skill.
5. Open a PR describing what the skill does, when it must trigger, and when it
   must stay quiet.

## Naming

Single lowercase word per skill (PRD §16) — the energy of `ponytail` /
`grill-me` / `impeccable`, never the exact words. Before proposing a new name,
check the collision watchlist in `shared/terminology/names.md`, and expect a
fresh GitHub + skills.sh exact-name audit before anything freezes.

## Reporting problems with a skill's behavior

Open an issue with: the runtime you used (Claude Code, Codex, Cursor,
Antigravity, OpenCode, other), the exact user message, what the skill did,
and what you expected. Transcripts beat summaries.
