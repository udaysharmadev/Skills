# Skills

**27 specialist skills that turn a general coding agent into an experienced product, engineering, design, QA, security and DevOps team.**

One install covers the whole arc of real work — idea debate, research, planning, building, browser verification, security, performance, cleanup, docs, git, and shipping — with routing that picks the *smallest* sufficient workflow instead of running everything.

## Install

Verified with the public [skills CLI](https://skills.sh) on 2026-09-14 (all 27 skills discovered and installed into a clean directory):

```bash
npx skills add udaysharmadev/Skills --all
```

Interactive selection:

```bash
npx skills add udaysharmadev/Skills
```

Then start any new project with `/concierge` — it detects your stack and capabilities, and routes your request to the smallest workflow that solves it.

## What changes after installation

Before — you re-explain process to the agent every session: "research first", "don't claim it works, prove it", "make a plan before coding".

After — 27 specialists carry that process, and a router keeps it lean:

```text
IDEA      THINK           PLAN        BUILD    PROVE             SHIP              REMEMBER
hotseat   scout, distill  masterplan  pilot    proof, roadtest   cleared, runway   recall
                                               sleuth, referee, hotpath
```

| | | |
| --- | --- | --- |
| **`concierge`** — detect + route | **`hotseat`** — 7-persona idea debate | **`spelunk`** — map any codebase |
| **`scout`** — cited research first | **`distill`** — vague ask → sharp brief | **`masterplan`** — vertical-slice plans |
| **`pilot`** — execute plans, verify each slice | **`backend`** — server correctness, any stack | **`blueprint`** — architecture that renders |
| **`headroom`** — scale with proportionality | **`polish`** — kill the AI-generated look | **`friction`** — can a human use it? |
| **`ditto`** — recreate UI from a reference | **`proof`** — the right test at the right boundary | **`roadtest`** — real-browser evidence |
| **`sleuth`** — root cause, not symptom | **`referee`** — independent review | **`hotpath`** — measured optimization |
| **`harden`** — security audit, evidence-backed | **`unslop`** — detox the vibe-coded mess | **`janitor`** — git/GitHub hygiene |
| **`frontpage`** — READMEs from verified facts | **`findable`** — SEO without snake oil | **`frugal`** — token efficiency, honestly measured |
| **`cleared`** — go-live gate | **`runway`** — deploy + verify live | **`recall`** — memory with a context budget |

## Measured, not vibes

This repository is subject to its own rules — no benchmark number that was not run, no compatibility claim that was not tested, no claim of "works everywhere" that was not verified. Current evidence:

| Claim | Status |
| --- | --- |
| Install: `npx skills add udaysharmadev/Skills --all` discovers and installs all 27 skills | **measured** 2026-09-14, skills CLI, clean directory |
| 27/27 skills pass the bundle validators (frontmatter, naming, links, ≤500-line budget) | **measured**, runs on every commit via CI |
| Routing eval, stratified smoke tier (12 cases, 12 distinct skills incl. 1 negative), Codex (gpt-5.6-sol): accuracy **0.917**, single run; sole miss: a trivial-styling request routed to `polish` | **measured** 2026-09-14, raw JSON committed under `evals/results/` |
| Routing eval, same tier, OpenCode: accuracy **1.0** (12/12) | **measured** 2026-09-14, same protocol |
| Routing eval, sibling-confusion suite (20 adjacency pairs), Codex | **measured** 2026-09-14, see `evals/results/` |
| Context footprint: median ≈1,200 tokens per SKILL.md (derived byte estimate), zero outliers; always-on frontmatter descriptions ≈3,500 tokens total | **measured** by `scripts/check-context` |
| Claude Code headless invocation | **unverified** — flags per official docs; execution hangs in the dev environment |
| Cursor / Antigravity | **unavailable** locally — no results claimed |

Every result JSON records agent, version, commit, date, invocation status and raw outputs — see [docs/evaluations.md](docs/evaluations.md).

## Compatibility

Fill-by-evidence matrix per agent and capability: [docs/compatibility.md](docs/compatibility.md). Skills are Tier A/B portable by design (markdown + references, deterministic scripts, explicit capability fallbacks) — and portability is treated as a claim to prove, not assume.

## Documentation

- [Evaluations](docs/evaluations.md) · [Benchmarks](docs/benchmarks.md) · [Naming audit](docs/name-audit.md) · [Handoff contract](docs/handoff.md) · [Architecture](docs/architecture/README.md)
- Product definition: [PRD.md](PRD.md)

## Principles

1. **Evidence before confidence** — verification replaces confidence language; what can't be verified is marked `unverified`.
2. **Universal core, runtime enhancements** — core workflow → capability detection → best available tool → fallback.
3. **No AI slop** — no invented numbers, decorative badges, or rewrites-for-activity.
4. **Save tokens, never save effort** — the quality gate never moves.
5. **Protect user control** — reversible actions autonomous; destructive ones explicitly gated.

## FAQ

**Why 27 skills instead of one big prompt?** A mega-prompt is always-on tax and forgets under pressure. Specialists carry deep checklists in `references/` loaded only when their workflow needs them; the router keeps small tasks cheap.

**Why should I trust the names won't collide with existing skills?** Single-word system enforced by `scripts/check-names`, watchlist + pre-approved alternates in `shared/terminology/names.md`, and a fresh exact-name audit gated before any public announcement ([docs/name-audit.md](docs/name-audit.md) records status honestly).

**Does this work outside Claude Code?** The install is verified once via the skills CLI into a clean directory; per-agent capability cells remain untested by policy and are tracked in [docs/compatibility.md](docs/compatibility.md) — cells stay `?` until tested, by policy.

**Can I install just one skill?** Yes — `npx skills add udaysharmadev/Skills` for interactive selection. Each skill folder is self-contained by contract.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Every skill meets the "legendary" bar (PRD §19) before shipping: clear triggers, capability fallbacks, deterministic verification, token-conscious files, honest limitations. Deterministic CI runs on every PR; live evals are manual and budgeted.

## License

[MIT](LICENSE)
