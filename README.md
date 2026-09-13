# The Vibe Coding Skills OS

**One install turns a general coding agent into something that behaves much closer to an experienced product, engineering, design, QA, security, DevOps and documentation team.**

Works with every practical Agent Skills-compatible runtime: Claude Code, Codex, Cursor, Google Antigravity, OpenCode and friends.

```text
IDEA     THINK          PLAN        BUILD   PROVE            SHIP             REMEMBER
hotseat  scout, distill masterplan  pilot*  proof*, roadtest cleared*, runway* recall
                                                              * planned — see table below
```

## Status: v0.6 — all 27 skills shipped

| Phase | Skills | State |
| --- | --- | --- |
| Foundation | validators, shared contracts, naming system | ✅ shipped |
| Intelligence | `concierge` `hotseat` `spelunk` `scout` `distill` `masterplan` `recall` | ✅ shipped |
| Building | `pilot` `backend` `blueprint` `headroom` | ✅ shipped |
| Experience | `polish` `friction` `ditto` | ✅ shipped |
| Proof | `proof` `roadtest` `sleuth` `referee` `hotpath` `harden` | ✅ shipped |
| Cleanup & public surface | `unslop` `janitor` `frontpage` `findable` `frugal` | ✅ shipped |
| Shipping | `cleared` `runway` | ✅ shipped |

The 27-skill target, contracts and build order are specified in [PRD.md](PRD.md).

## Install

> Repository brand is intentionally TBD until the final naming pass (PRD §16), so `<owner>/<repo>` is a placeholder.

```bash
npx skills add <owner>/<repo> --all
```

Then start every new project with:

```text
/concierge
```

It inspects the project and explains what is available in under a minute of your attention. You can also install skills individually:

```bash
npx skills add <owner>/<repo>          # interactive selection
```

## All 27 skills

| Skill | Job |
| --- | --- |
| `concierge` | Detects stack + runtime capabilities, routes your request to the smallest workflow |
| `hotseat` | Seven specialists destroy and rebuild your idea before you build it |
| `spelunk` | Maps any existing repository deeply — quick, deep or teach mode |
| `scout` | Research before code: cited, version-pinned, primary-source-first |
| `distill` | Turns "bro add dashboard make it good" into an execution-grade brief |
| `masterplan` | A serious implementation plan with vertical slices, rollback and a definition of done |
| `pilot` | Executes plans slice by slice — implement, verify, inspect diff, repeat |
| `backend` | Server-side correctness in any stack: APIs, data, auth, jobs, webhooks |
| `blueprint` | Architecture analysis + diagrams that render (Mermaid + navigable HTML) |
| `headroom` | Scale design with proportionality — Now / Next / Scale, with trigger metrics |
| `polish` | UI design that kills the AI-generated look — deliberate, anti-slop, state-complete |
| `friction` | UX audits: can a real person complete the task? WCAG 2.2 + novice/expert walks |
| `ditto` | Recreates UI from screenshot/URL/design with a screenshot-compare-correct loop |
| `proof` | The right test at the right boundary — behavior-named, regression-locked, mock-disciplined |
| `roadtest` | Real-browser QA with evidence bundles — screenshots, console, network, responsive |
| `sleuth` | Root-cause debugging: reproduce, hypothesize, eliminate, fix the cause, lock it with a test |
| `referee` | Independent review on two axes — intent then quality; actionable findings only |
| `hotpath` | Measured optimization: benchmark, one change, re-measure, report the delta or revert |
| `harden` | Security audit per OWASP Top 10:2025 — severity + confidence, no destructive testing |
| `unslop` | Rescues vibe-coded messes: baseline, de-slop in verified batches, never a big rewrite |
| `janitor` | Git/GitHub hygiene — grounded in real git output, commit messages from real diffs |
| `frontpage` | READMEs from research, not vibes — every claim provable, every snippet executed |
| `findable` | SEO/discoverability verified on rendered HTML — no snake oil |
| `frugal` | Token efficiency: save tokens, never save effort — savings reported honestly |
| `cleared` | The final gate: READY / READY WITH WARNINGS / BLOCKED, every verdict from evidence |
| `runway` | Deploy with verification: preflight → preview → prod → smoke → logs → rollback path |
| `recall` | Persistent high-signal project memory with a strict context budget |

Each skill is a self-contained folder under `skills/` — install one, or all of them.

## Principles

1. **Evidence before confidence.** Never "everything works" because the code looks reasonable. Run what can be run; mark what can't as unverified.
2. **Universal core, runtime enhancements.** No skill fundamentally requires one runtime, MCP server, framework or OS. Core workflow → capability detection → best available tool → fallback.
3. **No AI slop.** No fake benchmarks, no decorative badges, no giant unverified rewrites, no hallucinated packages.
4. **Save tokens, never save effort.**
5. **Protect user control.** Autonomous for reversible actions; explicit gates for destructive ones.

Full principles and the skill-file contract live in [PRD.md](PRD.md) and [shared/principles](shared/principles/).

## Repository layout

```text
skills/       one self-contained folder per skill
shared/       canonical contracts (principles, terminology, capability map)
evals/        trigger/workflow fixtures — wired to a real runner before any claims
docs/         architecture and generated skill index
scripts/      validate-skills, check-names, check-links, build-docs
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Every skill must pass `scripts/validate-skills` and `scripts/check-names`, and meet the "legendary skill" bar in PRD §19 before it ships.

## License

[MIT](LICENSE)
