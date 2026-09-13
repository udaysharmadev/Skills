---
name: frontpage
description: Generates world-class READMEs and project documentation grounded in what the repository actually is. Use when creating or rewriting a README, when the user says the README is bad, missing, outdated or embarrassing, before open-sourcing, when install/usage instructions don't work, or when docs need extracting out of an overloaded README. Researches the real project first (code, install process, tests, architecture), writes only provable claims — never invented stars, users, benchmarks or compatibility — and verifies every snippet by running it.
---

# frontpage — the README is the product's front page

GitHub renders this file as your landing page. It gets one screen to
answer: what is this, why should I care, how do I try it. You write it
from **research, not vibes** — and every claim in it is provable.

## When NOT to use

- The codebase itself is the mess → `unslop` first; a great README on a
  broken project is a lie with formatting.
- Architecture documentation → `blueprint` (you may *link* to it).
- Repo hygiene (badges, license files, topics) → `janitor`.

## Prerequisites

Research before writing anything (the PRD rule: understand the actual
project):

- what the code does — `spelunk` quick/deep pass, entry points read;
- current README (what's wrong with it — outdated, missing, oversold);
- the install process **executed**, not assumed;
- supported platforms/versions — from manifests and CI, not memory;
- tests/benchmarks that exist (only those may be cited);
- related projects (for honest positioning, if the user wants it);
- the target user (who lands on this page and what they need in 30
  seconds).

## Workflow

### 1. Pick the structure that fits

`references/readme-blueprint.md` has the full section menu with when
each earns its place. Above the fold, always, in order: **what it is
(one line) · why it's different · one command to try it · the skill/map
visual if this is a bundle**. Everything else is chosen, not stuffed —
a small CLI tool with 15 sections is wearing someone else's clothes.

### 2. Write with the capabilities that help

- Markdown tables for enumerable facts (options, compatibility).
- Mermaid diagrams where structure matters (GitHub renders them).
- Collapsible detail (`<details>`) for advanced/rare paths — keep the
  main line scannable.
- **Tested snippets only**: every install/usage command is actually run
  against a clean checkout before it ships; the versions in examples
  match what currently works.
- TOC when the README earns it (> ~150 lines), links verified.
- Badges only for things that exist and pass — no decorative
  build-passing on a repo without CI.

### 3. Verify

- Every link resolves — checked, not assumed; external links verified
  for 200s where the network allows.
- Quickstart executed end-to-end on a clean clone.
- Claims audit: walk the README and mark every factual claim
  (versions, platforms, counts, timings) with its source — manifest,
  CI config, measurement. No source → cut the claim.

### 4. Extract when overloaded

README growing past ~250 lines → extract deep material into `docs/`
(architecture, advanced config, recipes) and leave a pointer. The front
page stays scannable; the depth lives one click away.

## The no-invention rules (non-negotiable)

Never invent or round up: stars, user counts, download numbers,
benchmarks, testimonials, compatibility ("works on Windows" — was it
tested?), performance figures, security guarantees. **If a number is
not proven, it does not get published.** Comparison tables: facts that
can be checked, or the section goes.

## Quality gates

- Above the fold answers what/why/try-it within one screen.
- Quickstart commands executed for real; example versions match reality.
- Zero unproven claims (the audit in step 3 is the evidence).
- Every link resolves; anchors match headings.
- Structure fits the project — sections exist because they earned
  their place, not because the template has them.

## Stop conditions

- README written/rewritten + verified → summary of claims audit, stop.
- The project has nothing installable yet → write the honest v0
  (what/why/roadmap, no fake quickstart), say what to add when it
  becomes runnable.
- Research contradicts the requested content ("write we have 10k
  users") → refuse the fabricated part, ship the true version, note
  the refusal.

## Output contract

On disk: `README.md` (+ `docs/` extractions with pointers). Chat:
structure chosen and why, the claims audit (claim → source table),
verification evidence (quickstart run, link check), what was
deliberately left out.

Dogfood note: this suite's own README is maintained by this skill —
the bar applies to us first.
