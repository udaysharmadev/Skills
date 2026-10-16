![28 Skills for Vibe Coding](assets/banner.png)

# Skills

### 28 specialists for the engineering work around vibe coding.

Twenty-eight research-backed specialists for the work between “I have an
idea” and “it is live in production.” Each skill owns one job, carries its own
restraints and verification contract, and loads only when it is relevant.

Each package has a workflow and verification contract. The current upgrade
repairs demonstrated gaps; cross-runtime behavior and comparative outcomes
remain empirical questions. See the [28-row upgrade ledger](docs/upgrade-ledger.md).

[![skills.sh installs](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fudaysharmadev%2FSkills%2Fmain%2Fassets%2Fskills-sh-endpoint.json&style=for-the-badge)](https://www.skills.sh/udaysharmadev/skills)

```bash
npx skills add udaysharmadev/Skills --all
```

Try a direct request such as “Use sleuth to find why this value stays stale
after a write.” You should receive a reproduction, a causal explanation, a
scoped fix and its check output. `/concierge` is optional when the owner is unclear.

> Building one feature, fixing one bug, or cleaning one frightening repo: you
> do not need to memorize 28 commands. Use the owner you know, or ask concierge.

## From idea to production

```mermaid
flowchart LR
    A["IDEA<br/>hotseat"] --> U["UNDERSTAND<br/>spelunk"]
    U --> R["RESEARCH<br/>scout"]
    R --> S["SPEC<br/>distill"]
    S --> P["PLAN<br/>masterplan"]
    P --> B["BUILD<br/>pilot · backend"]
    B --> D["DESIGN<br/>polish · friction · ditto"]
    D --> V["PROVE<br/>proof · roadtest · referee"]
    V --> C["CLEAN<br/>unslop · janitor · frugal"]
    C --> H["SHIP<br/>cleared · runway"]
    H --> M["REMEMBER<br/>recall"]
    B -. "architecture" .-> X["blueprint · headroom"]
    V -. "diagnose" .-> Y["sleuth · hotpath · harden"]
```

This is a map, not a mandatory chain. Most requests need one skill. Larger
workflows compose only where the next specialist needs the previous one’s
output.

## Why this is different

### Research-backed depth

Every skill received an individual research pass. Its provenance note records
the lessons that changed behavior, where those lessons were encoded, rejected
ideas, and knowledge that should be refreshed as the field moves. The
[research index](docs/research/README.md) keeps that evidence browseable without
putting it into runtime context.

### Specialist judgment

These are not “act like an expert” prompts.

- `sleuth` keeps competing hypotheses alive until an experiment separates them.
- `headroom` attaches a trigger metric to every scaling recommendation, and
  tells you what not to build yet.
- `harden` separates severity, confidence, exploit preconditions, and impact.
- `unslop` protects load-bearing weirdness instead of rewriting everything clean.
- `frugal` optimizes successful-task token cost, never raw token count.
- `runway` verifies the deployed fingerprint through the public URL, not the
  command’s exit code.

### Progressive disclosure

Twenty-eight skills do not become one enormous system prompt. Discovery sees
compact names and descriptions; the relevant `SKILL.md` loads on demand; only
its necessary references or helper scripts load after that. This follows the
[Agent Skills specification](https://agentskills.io/specification).

### Restraint is part of the product

Every skill says when not to use it, when to stop, what it cannot verify, and
which actions need the user’s approval. No rewrite for activity. No security
theater. No deploy that quietly becomes an infrastructure migration.

### One portable core

The core is Markdown, self-contained skill folders, conditional references,
small standard-library helpers, and explicit fallbacks. Richer runtimes can add
browsers, web research, subagents, or GitHub access; missing capabilities reduce
the evidence available, not the honesty of the answer. See the
[compatibility matrix](docs/compatibility.md).

## Just talk normally

| You say | The likely owner |
| --- | --- |
| “I want to build a GitHub doom-scroller.” | [`hotseat`](skills/hotseat/) |
| “I don’t understand this repo.” | [`spelunk`](skills/spelunk/) |
| “Bro, make this dashboard stop looking AI generated.” | [`polish`](skills/polish/) |
| “I’ve vibe coded for three weeks and now I’m afraid to touch it.” | [`unslop`](skills/unslop/) |
| “Why does checkout fail only sometimes?” | [`sleuth`](skills/sleuth/) |
| “Can this handle 100k users?” | [`headroom`](skills/headroom/) |
| “Check everything before I ship.” | [`cleared`](skills/cleared/) |
| “Deploy it, then prove the new version is live.” | [`runway`](skills/runway/) |

Still unsure? `/concierge` is the front door. The beginner-friendly
[skill chooser](docs/choosing-a-skill.md) covers the rest.

## The 28 specialists

### Think

- [`concierge`](skills/concierge/): inspect the project and route the smallest sufficient workflow.
- [`handsfree`](skills/handsfree/): stop babysitting the agent. Routine decisions are autonomous; only real human gates interrupt you.
- [`hotseat`](skills/hotseat/): stress-test an idea through seven genuinely different lenses.
- [`spelunk`](skills/spelunk/): map an unfamiliar repository without reading it blindly.
- [`scout`](skills/scout/): replace stale API memory with version-pinned evidence.
- [`distill`](skills/distill/): turn a vague request into a compact, executable brief.
- [`masterplan`](skills/masterplan/): produce vertical slices grounded in files that exist.
- [`recall`](skills/recall/): preserve decisions and expensive lessons without dumping transcripts.

### Build

- [`pilot`](skills/pilot/) — execute an approved plan one verified slice at a time.
- [`backend`](skills/backend/) — protect server contracts, data integrity, auth, jobs, and migrations.
- [`blueprint`](skills/blueprint/) — document real architecture with diagrams that render.
- [`headroom`](skills/headroom/) — design for today, the next threshold, and eventual scale.

### Experience

- [`polish`](skills/polish/) — give interfaces hierarchy and character without generated-UI clichés.
- [`friction`](skills/friction/) — find where real users hesitate, backtrack, or fail.
- [`ditto`](skills/ditto/) — recreate a reference UI through repeated visual comparison.

### Prove

- [`proof`](skills/proof/) — put regression protection at the cheapest boundary that catches the bug.
- [`roadtest`](skills/roadtest/) — walk critical paths in a real browser and keep the evidence.
- [`sleuth`](skills/sleuth/) — establish a causal chain before touching the fix.
- [`referee`](skills/referee/) — review intent first, engineering quality second.
- [`hotpath`](skills/hotpath/) — measure, change one thing, measure again, keep or revert.
- [`harden`](skills/harden/) — reduce attack surface with scoped, evidence-backed findings.

### Clean & publish

- [`unslop`](skills/unslop/) — remove accidental complexity in small behavior-preserving batches.
- [`janitor`](skills/janitor/) — keep Git history and the GitHub surface honest and navigable.
- [`frontpage`](skills/frontpage/) — build READMEs from verified repository facts.
- [`findable`](skills/findable/) — fix crawlability and metadata without ranking promises.
- [`frugal`](skills/frugal/) — cut context waste while keeping the quality gate fixed.

### Ship

- [`cleared`](skills/cleared/) — issue a readiness verdict backed by fresh evidence.
- [`runway`](skills/runway/) — deploy at the platform’s natural level and verify it live.

For inputs, outputs, neighbors, and research links for every skill, use the
[human skill guide](docs/skills/README.md). The generated
[skill index](docs/skills/INDEX.md) mirrors the frontmatter exactly.

Try the [reproducible local failure gallery](docs/demo-gallery.md): a stale
cache, an owner-boundary bug and duplicated payment effects, with retained
failing seeds and correction checks. They demonstrate local behavior without
claiming comparative skill superiority.

## A few worth meeting properly

<details>
<summary><strong>hotseat</strong> does not manufacture seven agreeable opinions</summary>

The selected lenses form verdicts before comparison. The moderator preserves
real disagreement and ends with assumptions, an MVP cut line and falsifiable
decision criteria. It does not manufacture consensus or numerical thresholds.
</details>

<details>
<summary><strong>polish</strong> bans the default, not the technique</summary>

Glass, gradients, cards, and motion are not inherently wrong. Thoughtless
decoration is. The skill starts from the product, existing tokens, real data,
interaction states, and screenshots at desktop and mobile widths.
</details>

<details>
<summary><strong>sleuth</strong> will not rent the bug</summary>

A fix needs a failing signal, competing hypotheses, a five-part causal chain,
and a regression test. Emergency workarounds remain visibly provisional.
</details>

<details>
<summary><strong>recall</strong> remembers less on purpose</summary>

Facts, decisions, current status and hard-won lessons age at different speeds.
Memory uses a task-sized retrieval budget, refresh conditions, supersession
and no transcript dumps.
</details>

## Install

Install the complete bundle:

```bash
npx skills add udaysharmadev/Skills --all
```

Choose skills interactively instead:

```bash
npx skills add udaysharmadev/Skills
```

The public full-bundle command was rechecked on 2026-10-14 with
`skills@1.7.2` in a disposable project: all 28 folders installed. Each selected
local package was also installed independently with its resources and helper
permissions checked. These are packaging checks; native host activation remains
separate. [Installation evidence](docs/compatibility.md).

Install just one owner:

```bash
npx skills@1.7.2 add udaysharmadev/Skills --skill sleuth --agent codex --copy --yes
```

The individual command's shape was exercised against local package sources;
the public bundle check used the default branch. Interactive selection has
historical evidence only and was not re-exercised during this upgrade.

After installation, run:

```text
/concierge
```

## How the bundle stays lean

```mermaid
flowchart TD
    A["Agent starts"] --> B["28 names + descriptions are discoverable"]
    B --> C["Relevant skill activates"]
    C --> D["That skill's SKILL.md loads"]
    D --> E["Only necessary references, scripts, or assets load"]
    E --> F["Evidence-backed output or an explicit unverified gap"]
```

Each `skills/<name>/` folder works when copied alone. Runtime skills refer to
neighbors by slug, never by repository-relative paths. The repository’s
`shared/` directory is for maintainers and validators, not a hidden runtime
dependency. Read the [architecture overview](docs/architecture/README.md) and
[handoff contract](docs/handoff.md) for the full model.

## Research, not prompt folklore

The research notes separate four kinds of evidence: official truth, research
evidence, implementation patterns, and community failure signals. Each note
records what changed the skill and where the idea landed in runtime files.
Fast-moving claims are marked for refresh; tempting but weak ideas are recorded
when relevant instead of quietly returning later.

Browse the [research provenance index](docs/research/README.md).

Verified sources behind current decisions include WCAG 2.2, Core Web
Vitals thresholds, EARS requirement syntax, the Knight Capital SEC
findings, Playwright locator semantics, the git-bisect exit contract,
Fowler's expand/migrate/contract pattern, and Google's code-review
guidance. Each ledger records what was confirmed, what changed runtime
behavior, and what was deliberately left unencoded.

## Trust and safety

These skills can guide agents that edit code, run commands, browse external
content, operate Git, and deploy systems. Destructive and high-blast-radius
actions are explicitly gated; fetched content is treated as untrusted data;
capability fallbacks state what could not be verified. The source is fully
inspectable, but this bundle is not a security guarantee. See
[SECURITY.md](SECURITY.md).

## Documentation

- [Documentation home](docs/README.md)
- [Which skill do I need?](docs/choosing-a-skill.md)
- [Workflow recipes](docs/workflows.md)
- [Architecture](docs/architecture/README.md)
- [Compatibility](docs/compatibility.md)
- [Maintainer evidence and historical audits](docs/evaluations.md)

All 28 packages are present. The [release report](docs/release-readiness.md)
distinguishes structural checks, independent review, observed demonstrations
and unverified live comparisons. The [follow-up implementation
record](docs/upgrade/followup-implementation.md) tracks later repairs on the
current branch. No benchmark superiority is claimed here.

## Contributing

Behavior changes need evidence, not another paragraph of generic “best
practices.” Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull
request.

MIT licensed. See [LICENSE](LICENSE).
