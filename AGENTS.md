# AGENTS.md — guidance for agents working in this repository

This repository is an Agent Skills bundle. Everything in [PRD.md](PRD.md) applies to you while you work here.

## Non-negotiables

1. **Run the validators before claiming done.** `scripts/validate-skills`, `scripts/check-names`, `scripts/check-links`. A clean-looking tree is not evidence.
2. **No slop.** No fake benchmark numbers, no invented compatibility claims, no decorative badges, no filler sections in skill files. If a number is not measured, it does not ship.
3. **Skills are self-contained.** A skill folder under `skills/` must work when copied alone into another repository. Reference sibling skills by slug name only (e.g. "hand off to `masterplan`") — never by relative file path into `../`. Canonical contracts live in `shared/` for humans and tooling, not for runtime cross-loads.
4. **Respect the skill-file contract** (PRD §8): every `SKILL.md` states purpose, triggers, when NOT to use, prerequisites, workflow, tool selection/fallback, quality gates, stop conditions, output contract, and pointers to references. Body ≤ 500 lines; detail goes in `references/`.
5. **Naming:** single lowercase word per skill (PRD §16). `scripts/check-names` enforces it.
6. **Progressive disclosure:** frontmatter description carries the trigger signal; the body carries the workflow; `references/` carries the depth. Do not inline checklists that belong in a reference file.
7. **Paid agents are default-deny.** The eval harness refuses `codex` (and any future billed adapter) unless the human sets BOTH `--allow-paid` and `ALLOW_PAID_AGENT=1` on that run — `scripts/eval_guard.py` exits 4 otherwise. Never set those keys yourself and never invoke a paid agent CLI directly (e.g. `codex exec` in a shell) unless the user explicitly authorized that spend in the current session.

## Before opening a PR

- `scripts/validate-skills` passes
- `scripts/check-names` passes
- `scripts/check-links` passes
- New/changed skills have trigger cases in `evals/trigger/cases.md`
- `scripts/build-docs` regenerated if frontmatter changed

## Dogfooding

Phase 7 of the build sequence means it: use this suite's own methodology (evidence, verification, no slop) on this repository. Anything annoying in real usage gets fixed before launch.
