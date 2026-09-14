---
name: blueprint
description: Produces architecture documentation with diagrams that render — system context, containers, components, request flow, sequence, data flow, deployment and failure paths as Mermaid sources, assembled into a navigable, print-friendly HTML deliverable under docs/architecture/. Use when the user asks for architecture docs, diagrams of how the system works, onboarding material for a codebase, a design document for a proposed feature, or visibility before a major refactor. Analyzes the real repository first and never fabricates infrastructure to make diagrams look impressive.
---

# blueprint — architecture you can actually read

Diagrams exist to answer questions. You pick the few diagrams this system
actually needs, ground every node in real code, and ship them as an
artifacts set a team can navigate: markdown for the repo, HTML for humans.

## When NOT to use

- "Where does X live?" → `spelunk` quick mode.
- "Will this scale? What should the architecture become?" → `headroom`
  decides; you can document the outcome.
- A single small diagram inside a README → just write inline Mermaid,
  skip the full deliverable.

## Prerequisites

Repository access. Analysis reuses `spelunk` deep mode when a fresh
`docs/repo-map.md` exists (verify it's recent); otherwise run a deep pass
first — you cannot diagram what you haven't mapped.

## Workflow

### 1. Analyze

From the repo map + targeted reads: the real components, real data stores,
real external dependencies, real request paths. **Every node in every
diagram must correspond to something you saw in the code** — a service
that isn't running anywhere doesn't go in a box.

### 2. Choose the diagrams that help (C4 Abstraction)

Avoid the "Monolithic Documentation" anti-pattern. Pick 3–5 diagrams targeted 
at specific audiences (Context for business, Container/Component for engineering). 
The menu in `references/diagram-guide.md` maps the question to the diagram type. 
For each major component on a diagram, the README notes its reasoning in
one line — responsibility, boundary, dependency direction, data it owns,
failure mode, and **explicit trust boundaries** (where security contexts change). 
A box without a reason is decoration. Common picks:

- new team onboarding → system context + container view + one request
  sequence;
- before refactor → component view + the two flows being touched;
- design doc for a feature → proposed sequence + data model delta;
- reliability review → failure path + deployment.

### 3. Write the Mermaid sources

One `.mmd` file per diagram in `docs/architecture/`, ≤ ~30 nodes each
(split rather than shrink text). Labels name real things (`api/index.ts`,
`Postgres`, `Stripe webhook`) — no "Service Layer Abstraction". Validate
each with the bundled checker: `scripts/validate-mermaid docs/architecture/*.mmd`
(catches unknown diagram types, unbalanced brackets, duplicate node ids
— the failures that break rendered docs). Static checks don't prove
rendering: render once via mermaid-cli when available and say whether
you did.

### 4. Assemble the deliverable

- `docs/architecture/README.md` — index: one paragraph per diagram (what
  question it answers, when to read it), mermaid blocks inline (GitHub
  renders them natively), plus **Assumptions** and **Risk callouts**
  sections.
- `docs/architecture/architecture.html` — from `assets/template.html`:
  same content, navigable sidebar, zoomable diagrams, print-friendly.
  Fill every template placeholder; delete unused sections rather than
  shipping empty ones.

### 5. Verify and report

Spot-check rule: pick the two most load-bearing nodes across your
diagrams and re-verify them in code (the module exists, the connection is
real). Report what was verified vs. inferred.

## Honesty rules

- **Never fabricate infrastructure** — no invented queues, replicas,
  CDNs, or "future" components drawn as if they exist. Proposed things go
  in a clearly-marked *Proposed* diagram or dashed nodes.
- Uncertain edges get labeled `(inferred)` in the README, not silently
  drawn.
- If the architecture is genuinely one app + one database, say that in
  one honest diagram instead of decorating it into a microservices saga.

## Quality gates

- Every diagram node traceable to code (spot-checked ≥ 2 load-bearing
  nodes; result reported).
- Each diagram answers one question a reader actually has; README states
  that question above each diagram.
- Assumptions + risk callouts sections exist and are non-empty (or
  explicitly state "none found — which itself is worth trusting only
  after this much reading").
- ≤ 5 diagrams unless the user asked for a specific larger set; HTML has
  no empty placeholder sections.

## Stop conditions

- Deliverable written + spot-checks reported → done.
- Repo too small to warrant the full set (single-file scripts) → say so,
  produce the one honest diagram, stop.
- Repo map is stale (> 30 days / visibly wrong) → re-run `spelunk` deep
  first.

## Output contract

```text
docs/architecture/
  README.md             ← index + inline diagrams + assumptions + risks
  architecture.html     ← navigable, print-friendly deliverable
  context.mmd           ← one file per diagram (kebab-case names)
  containers.mmd
  request-flow.mmd
```

Chat summary: the diagram list with each one's question, the 1–2 risk
callouts that matter most, and the spot-check results.
