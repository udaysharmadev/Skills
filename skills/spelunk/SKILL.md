---
name: spelunk
description: Maps an unfamiliar repository from a concrete question by finding manifests, entry points, execution paths, dependencies, churn, ownership, and risk. Use for codebase onboarding, impact analysis, or locating where behavior lives before planning or debugging.
---

# spelunk: understand before touching

Your output is context other skills consume. The map must be compact
enough to inject later without tax, and every claim in it must be tied to
a real file path you actually saw.

## When NOT to use

- `PROJECT_CONTEXT.md` at the root already covers the need and is fresh,
  read that instead.
- The question is answerable by reading one obvious file. Just read it.
- Empty or greenfield repository: say that and stop.

## Prerequisites

Filesystem + search only. Git enriches (churn, history) but is optional.
No network required or used.

## Authority and evidence boundary

Spelunk is read-only discovery by default. It maps observed repository state;
it does not authorize edits, run state-changing scripts, infer secrets, or
promote a hypothesis into architecture. If a requested answer needs a runtime,
production, private service, or external source, state the boundary and route
to the appropriate investigation rather than simulating certainty.

For deep, risk-map, monorepo, or stale-map work, keep an evidence record using
[references/evidence-protocol.md](references/evidence-protocol.md): question,
scope, paths read, path traced, observed facts, inferences, unknowns, and
recheck trigger.

## Modes

| Mode | When | Stop rule |
| --- | --- | --- |
| `quick` | Task-specific question ("where is auth?") before acting | answer is supported |
| `deep` | Whole-project understanding; may produce `docs/repo-map.md` | major boundaries and unknowns are mapped |
| `teach` | User is new to the project and wants to learn it | one representative path is explainable |
| `risk-map` | Before refactors or handoffs | evidence-backed hotspots are identified |

Pick the mode from the request; when unsure, default to `quick` and offer
`deep` once. In `deep` and `risk-map` modes, start with the bundled
scanner, `scripts/inventory`, to collect file distribution, largest files,
TODO/FIXME debt, test/source
ratio, git churn hotspots). Read its output selectively; it informs the
map, it is not the map.

In a monorepo, identify repository root, package boundaries, workspace tooling,
and the app that owns the question before reading shared utilities. Do not
mistake a root manifest for the target application's runtime.

## Discovery order (all modes)

1. **Manifests before code.** Identify ecosystems from
   `package.json` / `pyproject.toml` / `go.mod` / `Cargo.toml` /
   `pom.xml` / `build.gradle*` / `Gemfile` / `composer.json` /
   `pubspec.yaml` / etc. Scripts, dependencies and tooling follow from
   these: don't guess them.
2. **Entry points.** `main`/`index` files, server bootstrap, app router
   directories, `Dockerfile`/`Procfile` CMD. Where execution starts tells
   you how everything else hangs together.
3. **Trace one execution path early.** Before broadening, follow a single
   representative request end-to-end (route → middleware → handler →
   service/model → response) with real symbols. This grounds every later
   claim; a map built without one traced path drifts into abstraction.
4. **Routing and config.** Route definitions and config files reveal the
   feature surface without reading implementations.
5. **Precise symbols before text search.** If an index exists (LSP,
   ctags, IDE symbols), resolve the symbol there first; fall back to
   grep, then read only the hits, in ranges, not whole files.
6. **Targeted reads.** Read what the task actually touches. Use ranged reads
   when a whole file would add substantial irrelevant context.

Never: recursive full-directory reads, whole-file dumps of large files, or
"read everything to be safe." Budget overflow → deliver the partial map
with an explicit "not covered" list.

If a search result is ambiguous, trace a real import, registration, route, or
test reference before assigning ownership. Names and directory placement are
leads, not proof of execution path.

## What to record

Full checklist with per-ecosystem detection hints lives in
`references/discovery-map.md`: read it in `deep` mode, or when the
checklist item isn't obvious. Core set:

- languages, frameworks, package manager, key dependencies;
- commands: dev / test / lint / typecheck / build (as actually defined in
  manifests and CI, not guessed);
- entry points and request lifecycle in one sentence;
- modules and their boundaries; data models and where migrations live;
- external services and env vars (names only: never values);
- auth mechanism; state management approach;
- CI/CD; conventions worth respecting; hotspots (large or high-churn
  files, via `git log` when available).

## Mode-specific output

- **quick** returns the direct answer first, then only the context needed to
  act safely.
  Even in quick mode: if the code being touched handles auth, payments, or
  PII, flag the trust boundary in one line: don't wait for `harden` to
  find it.
- **deep** → `docs/repo-map.md` with provenance header
  (`<!-- generated by spelunk on YYYY-MM-DD @ <short-sha>, tree <clean|dirty> -->`),
  sections per the checklist, plus an "Open unknowns" section. Write the file
  only when it has durable value beyond the current conversation.
- **teach** → layered explanation: what the project is → how one request
  flows end-to-end → where things live (with paths) → what the conventions
  are → gotchas. Narrative, path-anchored. The request-lifecycle sentence
  names real symbols: "Request enters `server.ts:createApp()` → routed via
  `routes/index.ts` → `middleware/auth.ts` verifies JWT → handler calls
  `services/user.ts` → responds."
- **risk-map** → four-quadrant fragility view:
  1. **High churn + high complexity** = active friction zone; name files and
     the type of change that keeps touching them.
  2. **High complexity + low churn** = landmine; stable but dangerous when
     eventually touched.
  3. **Test gaps around trust boundaries** = where a silent regression has
     no coverage (auth, payments, data migrations).
  4. **Cognitive debt** = systems where the team's understanding has diverged
     from the implementation (look for: stale comments, TODO-in-prod,
     code that contradicts the README, recent commits that say "I'm not
     sure why this works").
  Each item: file path + why it's risky + which skill should own the fix.
  Feeds `unslop`, `harden`, `sleuth`, and planning skills.

### Stale-map and contradiction handling

Treat a prior map as an index, not repository truth. Recheck its commit/tree
provenance, target package, commands, and the path relevant to the new question.
When map and source disagree, source wins; record the invalidated claim and
refresh only the affected section. If the mismatch changes the task boundary,
return a narrower updated map before planning or editing.

## Tool selection / fallback

- Prefer symbol indexes and repository search, then targeted ranged reads.
- Use the bundled inventory script only when its aggregate view answers the question faster.
- Without Git history, omit churn and ownership claims instead of inferring them.
- Prefer a representative executable path and direct symbols over folder-shape
  narratives. Widen only where a dependency, configuration, or test changes
  the answer.

## Quality gates

- Every factual claim carries a file path and is labeled for its epistemic
  status where it matters: **observed** (you read it), **inferred**
  (deduced: say from what), or **unknown** (goes to "Open unknowns").
  Risk maps additionally flag churn×size hotspots and auth/money/data
  flows as risk zones with reasons.
- Commands listed are the ones defined in the repo (scripts entries, CI
  steps): not generic ecosystem defaults.
- Output contains no detail unrelated to the triggering question or durable map.
- No env var values, secrets, or tokens recorded: names only.
- Every inferred relationship names its supporting observed path; no inference
  is used as an implementation instruction without confirming evidence.
- Deep maps include target package boundary, provenance, open unknowns, and
  recheck trigger so a future reader can judge freshness.

## Stop conditions

- The triggering question is answered (quick) or the map is written
  (deep) / explanation delivered (teach).
- Budget cap reached → ship the partial map + "not covered" list.
- Repository turns out to be something else than expected (e.g. a
  monorepo with 8 apps) → map the relevant app only, note the rest.
- Further scanning will not change answer, risk, or next action → stop; broad
  inventory is not a quality gate.
- Required runtime or access evidence is unavailable → give a bounded map and
  precise verification gap.

## Output contract

See mode outputs above. In `deep` mode, end the chat message with the
one-line summary: `repo-map: <stack> · <maturity> · <top 2 risks noticed>`
,  that line is what `concierge` and planning skills will quote.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
Read [references/discovery-map.md](references/discovery-map.md) in deep mode or
when ecosystem hints are needed. Read [references/evidence-protocol.md](references/evidence-protocol.md)
for monorepos, risk maps, stale maps, or handoff-ready discovery.
