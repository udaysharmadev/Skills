# The Vibe Coding Skills OS

**One install turns a general coding agent into something that behaves much closer to an experienced product, engineering, design, QA, security, DevOps and documentation team.**

Works with every practical Agent Skills-compatible runtime: Claude Code, Codex, Cursor, Google Antigravity, OpenCode and friends.

```text
IDEA     THINK          PLAN        BUILD   PROVE            SHIP             REMEMBER
hotseat  scout, distill masterplan  pilot*  proof*, roadtest cleared*, runway* recall
                                                              * planned — see table below
```

## Status: v0.1 — under active development

| Phase | Skills | State |
| --- | --- | --- |
| Foundation | validators, shared contracts, naming system | ✅ shipped |
| Intelligence | `concierge` `hotseat` `spelunk` `scout` `distill` `masterplan` `recall` | ✅ shipped |
| Building | `pilot` `backend` `blueprint` `headroom` | 🚧 planned |
| Experience | `polish` `friction` `ditto` | 🚧 planned |
| Proof | `proof` `roadtest` `sleuth` `referee` `hotpath` `harden` | 🚧 planned |
| Cleanup & public surface | `unslop` `janitor` `frontpage` `findable` `frugal` | 🚧 planned |
| Shipping | `cleared` `runway` | 🚧 planned |

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

## The shipped seven

| Skill | Job |
| --- | --- |
| `concierge` | Detects stack + runtime capabilities, routes your request to the smallest workflow |
| `hotseat` | Seven specialists destroy and rebuild your idea before you build it |
| `spelunk` | Maps any existing repository deeply — quick, deep or teach mode |
| `scout` | Research before code: cited, version-pinned, primary-source-first |
| `distill` | Turns "bro add dashboard make it good" into an execution-grade brief |
| `masterplan` | A serious implementation plan with vertical slices, rollback and a definition of done |
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
