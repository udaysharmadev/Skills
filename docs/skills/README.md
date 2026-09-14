# The human guide to all 28 skills

This is the browseable guide. It explains the job each skill owns without
duplicating its runtime instructions. For exact trigger metadata, use the
[generated index](INDEX.md).

## Intelligence

### `concierge`

**Use it when:** you do not know where to start.  
**Owns:** project detection, capability probing, and smallest-sufficient routing.  
**Different because:** it routes by what is missing—intent, repository state,
external truth, design, proof, or safety—not just by keywords.  
**Input → output:** a natural request → ≤30-line project snapshot and route.  
**Neighbors:** every specialist, but only when earned.  
[Research](../research/concierge.md) · [Source](../../skills/concierge/)

### `hotseat`

**Use it when:** an idea needs honest pressure before code.  
**Owns:** multi-lens product and engineering debate.  
**Different because:** seven verdicts form independently; synthesis preserves
disagreement, assumptions, MVP cuts, and falsifiable kill criteria.  
**Input → output:** product idea → decision-oriented synthesis and optional idea record.  
**Neighbors:** `distill`, then `masterplan`.  
[Research](../research/hotseat.md) · [Source](../../skills/hotseat/)

### `spelunk`

**Use it when:** the repository is unfamiliar or a risky area is hard to locate.  
**Owns:** compact codebase maps and fragility views.  
**Different because:** manifests, entry points, symbols, and churn lead the
search; observed, inferred, and unknown facts stay distinct.  
**Input → output:** repository or focused question → quick answer, repo map, or risk map.  
**Neighbors:** `sleuth`, `unslop`, `masterplan`, `blueprint`.  
[Research](../research/spelunk.md) · [Source](../../skills/spelunk/)

### `scout`

**Use it when:** an API, library, framework, or platform fact may be stale.  
**Owns:** version-pinned technical research.  
**Different because:** repository and installed source come first; no source
means no claim, and disagreements are resolved by recency × authority.  
**Input → output:** decision question → recommendation, load-bearing facts, uncertainty.  
**Neighbors:** `distill`, `masterplan`, `backend`, `runway`.  
[Research](../research/scout.md) · [Source](../../skills/scout/)

### `distill`

**Use it when:** a request is vague, contradictory, or too conversational to execute.  
**Owns:** compact implementation briefs.  
**Different because:** brief depth scales with blast radius and every
specification must be objectively executable by a downstream agent.  
**Input → output:** rough ask → scope, non-goals, edge cases, acceptance, and proof.  
**Neighbors:** `hotseat` before; `masterplan` after.  
[Research](../research/distill.md) · [Source](../../skills/distill/)

### `masterplan`

**Use it when:** the goal is agreed and the implementation needs sequencing.  
**Owns:** repository-grounded executable plans.  
**Different because:** it records invariants and decision reversals, then cuts
work into vertical slices marked must-precede, parallel, or postponable.  
**Input → output:** brief or clear goal → file-specific slices, rollback, and definition of done.  
**Neighbors:** `scout`, `spelunk`, then `pilot`.  
[Research](../research/masterplan.md) · [Source](../../skills/masterplan/)

### `recall`

**Use it when:** a fact, decision, blocker, or expensive lesson must survive the session.  
**Owns:** four compact project-memory files.  
**Different because:** knowledge types have separate lifecycles, caps, TTLs,
and supersession; transcripts and easy-to-derive facts stay out.  
**Input → output:** durable session delta → context, decisions, status, or learnings update.  
**Neighbors:** `concierge` reads it; any workflow may hand durable decisions to it.  
[Research](../research/recall.md) · [Source](../../skills/recall/)

## Building & architecture

### `pilot`

**Use it when:** an approved plan is ready to build.  
**Owns:** controlled slice-by-slice execution.  
**Different because:** only one slice may be unverified at a time; risk sets the
verification floor and plan deviations are recorded instead of hidden.  
**Input → output:** executable plan → code, tests, updated plan, and build report.  
**Neighbors:** `proof`, `roadtest`, `harden`, `referee`.  
[Research](../research/pilot.md) · [Source](../../skills/pilot/)

### `backend`

**Use it when:** changing APIs, data, auth, migrations, queues, jobs, or webhooks.  
**Owns:** server-side correctness across stacks.  
**Different because:** boundary validation, object authorization, idempotency,
transactions, reversible migrations, and explicit failures are invariants.  
**Input → output:** server behavior request → code, contract delta, migration notes, evidence.  
**Neighbors:** `scout`, `proof`, `harden`, `headroom`.  
[Research](../research/backend.md) · [Source](../../skills/backend/)

### `blueprint`

**Use it when:** people need to understand the system through architecture docs.  
**Owns:** traceable diagrams and navigable architecture deliverables.  
**Different because:** every node maps to code, each diagram answers one
question, and trust boundaries or inferred edges cannot hide.  
**Input → output:** repository map → Mermaid views, architecture index, optional HTML.  
**Neighbors:** `spelunk` before; `headroom` for future-state decisions.  
[Research](../research/blueprint.md) · [Source](../../skills/blueprint/)

### `headroom`

**Use it when:** deciding whether or how a system should scale.  
**Owns:** proportional system design.  
**Different because:** Now/Next/Scale recommendations carry visible arithmetic
and trigger metrics; at least one tempting thing must be marked “do not do yet.”  
**Input → output:** workload and constraints → staged design and migration triggers.  
**Neighbors:** `blueprint`, `backend`, `hotpath`.  
[Research](../research/headroom.md) · [Source](../../skills/headroom/)

## Product experience

### `polish`

**Use it when:** the interface works but looks generic, inconsistent, or AI-generated.  
**Owns:** visual direction, design-system fit, states, and responsive finish.  
**Different because:** it bans thoughtless defaults, not techniques; real data,
dark mode, semantics, contrast, and before/after screenshots are part of design.  
**Input → output:** rendered UI → focused visual changes and verification evidence.  
**Neighbors:** `friction`, then `roadtest`.  
[Research](../research/polish.md) · [Source](../../skills/polish/)

### `friction`

**Use it when:** users hesitate, backtrack, abandon, or cannot access a flow.  
**Owns:** end-to-end usability and accessibility.  
**Different because:** novice and expert walks expose different failures, while
usability, accessibility, visual design, and conversion stay separate concerns.  
**Input → output:** top user tasks → ranked findings, fixes, and re-walk evidence.  
**Neighbors:** `polish`, `roadtest`, product decisions via `hotseat`.  
[Research](../research/friction.md) · [Source](../../skills/friction/)

### `ditto`

**Use it when:** a screenshot, URL, or design export is the target.  
**Owns:** close UI reproduction.  
**Different because:** design tokens are inferred or mapped before code, then
nine fidelity dimensions drive at least two compare-and-correct rounds.  
**Input → output:** visual references → implementation, tokens, explained differences.  
**Neighbors:** `roadtest`; `polish` when improvement matters more than matching.  
[Research](../research/ditto.md) · [Source](../../skills/ditto/)

## Proof & engineering

### `proof`

**Use it when:** behavior needs tests or a bug needs a regression lock.  
**Owns:** test-boundary selection and durable coverage.  
**Different because:** it pushes tests to the cheapest boundary that catches the
real failure and proves new tests fail without the implementation.  
**Input → output:** behavior and risk → boundary map, tests, runner evidence.  
**Neighbors:** `sleuth` before a bug fix; `roadtest` for browser behavior.  
[Research](../research/proof.md) · [Source](../../skills/proof/)

### `roadtest`

**Use it when:** the real browser must prove a critical path works.  
**Owns:** browser-flow evidence.  
**Different because:** paths × viewports × states are chosen before walking;
console, network, screenshots, deep links, refresh, and locator healing are visible.  
**Input → output:** runnable app and paths → evidence bundle with pass/fail per path.  
**Neighbors:** `polish`, `friction`, `sleuth`, `cleared`.  
[Research](../research/roadtest.md) · [Source](../../skills/roadtest/)

### `sleuth`

**Use it when:** behavior is wrong, intermittent, or repeatedly “fixed.”  
**Owns:** evidence-driven root-cause diagnosis.  
**Different because:** competing hypotheses and discriminating experiments must
produce a symptom → mechanism → root cause → trigger → conditions chain.  
**Input → output:** reproducible failure → smallest fix, regression test, causal report.  
**Neighbors:** `proof`, `roadtest`; `hotpath` if behavior is correct but slow.  
[Research](../research/sleuth.md) · [Source](../../skills/sleuth/)

### `referee`

**Use it when:** a diff, PR, or completed change needs an independent gate.  
**Owns:** intent and engineering-quality review.  
**Different because:** it checks acceptance before polish, searches callers, and
reports only actionable findings with severity, confidence, and fix direction.  
**Input → output:** brief plus complete diff → approve, approve with findings, or request changes.  
**Neighbors:** follows `pilot`; may route gaps back to `masterplan` or `proof`.  
[Research](../research/referee.md) · [Source](../../skills/referee/)

### `hotpath`

**Use it when:** latency, memory, bundle size, or runtime cost is the problem.  
**Owns:** measured performance diagnosis.  
**Different because:** one variable changes per round and every kept change has
the same-condition before/after delta; complexity with no gain is reverted.  
**Input → output:** numeric target → profiles, measured changes, keep/revert report.  
**Neighbors:** `headroom` for architectural limits; `sleuth` for wrong behavior.  
[Research](../research/hotpath.md) · [Source](../../skills/hotpath/)

### `harden`

**Use it when:** auth, money, PII, uploads, admin, public exposure, or security is in scope.  
**Owns:** defensive threat modeling, audit, remediation, and retest.  
**Different because:** exploitability × impact decides severity, confidence is
separate, attack preconditions are mandatory, and destructive exploitation is forbidden.  
**Input → output:** owned/authorized surface → threat model and evidence-backed findings.  
**Neighbors:** `proof` for regression tests; `cleared` consumes the result.  
[Research](../research/harden.md) · [Source](../../skills/harden/)

## Cleanup & public surface

### `unslop`

**Use it when:** accidental complexity has made a repository frightening to change.  
**Owns:** behavior-preserving detox.  
**Different because:** cleanup starts from a runnable baseline, ranks real cost
instead of style preferences, and records load-bearing weirdness it deliberately keeps.  
**Input → output:** messy repository → small verified batches and a net-change report.  
**Neighbors:** `spelunk`, `proof`, `referee`; `polish` for visual slop.  
[Research](../research/unslop.md) · [Source](../../skills/unslop/)

### `janitor`

**Use it when:** Git history, branches, tags, ignores, releases, or GitHub hygiene need attention.  
**Owns:** repository hygiene and commit intent.  
**Different because:** every finding comes from current Git/remote evidence and
history rewriting, force pushes, or deletion always remain user decisions.  
**Input → output:** repository or staged diff → ranked audit or convention-matched commit message.  
**Neighbors:** `frontpage`, `harden`, `unslop`.  
[Research](../research/janitor.md) · [Source](../../skills/janitor/)

### `frontpage`

**Use it when:** the README is missing, stale, overloaded, or embarrassing.  
**Owns:** the project’s human-facing documentation experience.  
**Different because:** install and usage snippets run for real, factual claims
have sources, and a project gets only the sections it earns.  
**Input → output:** repository truth and target reader → README plus focused docs.  
**Neighbors:** `janitor`, `blueprint`; `findable` for public-web metadata.  
[Research](../research/frontpage.md) · [Source](../../skills/frontpage/)

### `findable`

**Use it when:** a public website needs correct search and social discovery.  
**Owns:** rendered metadata, semantics, crawlability, structured data, and previews.  
**Different because:** confirmed technical issues, content opportunities, and
speculative growth ideas are separated; only the first is treated as a fix.  
**Input → output:** rendered public pages → evidence table and verified metadata changes.  
**Neighbors:** `frontpage`, `friction`, `hotpath`.  
[Research](../research/findable.md) · [Source](../../skills/findable/)

### `frugal`

**Use it when:** context, tool output, or repeated discovery is consuming too much budget.  
**Owns:** token efficiency without quality loss.  
**Different because:** task-critical evidence is protected; only optional and
wasteful context is cut, and every saving is measured, derived, estimated, or unknown.  
**Input → output:** costly workflow → leak list, changes, honest savings, unchanged gate.  
**Neighbors:** `recall`, `spelunk`, any long workflow.  
[Research](../research/frugal.md) · [Source](../../skills/frugal/)

## Shipping

### `cleared`

**Use it when:** a feature, release, or project needs a go-live decision.  
**Owns:** final production-readiness gating.  
**Different because:** every applicable dimension carries fresh evidence,
unverified is never pass, and every warning or blocker has an owner and action.  
**Input → output:** scope and definition of done → READY, READY WITH WARNINGS, or BLOCKED.  
**Neighbors:** consumes `proof`, `roadtest`, `harden`; precedes `runway`.  
[Research](../research/cleared.md) · [Source](../../skills/cleared/)

### `runway`

**Use it when:** the release is cleared and must be deployed.  
**Owns:** preflight, deployment, live verification, and rollback evidence.  
**Different because:** strategy follows the platform and risk; the public URL
must expose the new fingerprint before a deploy counts as successful.  
**Input → output:** cleared release and platform → flight record with live smoke evidence.  
**Neighbors:** `cleared` before; `roadtest` for live critical paths.  
[Research](../research/runway.md) · [Source](../../skills/runway/)

## Autonomy

### `handsfree`

**Use it when:** the agent keeps interrupting safe reversible work with
"continue?" prompts and permission ceremony.  
**Owns:** the autonomy policy — what runs silently, what checkpoints, what
asks once, what stays blocked.  
**Different because:** it is a governor, not a bypass: model ceremony is
eliminated, host enforcement is reported by layer, and fewer questions via
skipped gates counts as a regression.  
**Input → output:** an authorized task → verified outcome with autonomous
decisions, checkpoints, and pending gates stated.  
**Neighbors:** wraps any execution; never cancels `cleared`, `runway`, or
`janitor` history gates.  
[Research](../research/handsfree.md) · [Source](../../skills/handsfree/)
