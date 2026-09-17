---
name: backend
description: Design, change, debug, or review server-side behavior when an API, database, authentication or authorization path, background job, webhook, external dependency, migration, cache, concurrency invariant, or production reliability concern is in scope. Use this skill for backend work in any stack; inspect the repository before choosing framework-specific patterns.
---

# backend: server-side engineering without framework cosplay

Build backend behavior that stays correct when requests duplicate, users race,
dependencies fail, schemas evolve, and operators need to understand an incident.
The deliverable is not merely code that returns the happy-path response. It is a
verified contract, with its data, security, recovery, and operational behavior
made explicit.

## Purpose and boundaries

Use this skill when a task changes or evaluates any of these surfaces:

- HTTP, RPC, GraphQL, CLI, webhook, queue, cron, or agent-tool boundary;
- persistent data, migrations, indexes, transactions, or consistency rules;
- authentication, session, authorization, tenancy, or sensitive-data handling;
- asynchronous work, event delivery, retries, external calls, caches, or files;
- service observability, health behavior, reliability, or failure recovery.

Do not use it for a purely visual client change, a product decision with no
accepted behavior, an unexplained failure with no reproduced cause, or an
architecture-sizing decision. Route those respectively to the relevant product,
debugging, or architecture skill. A small server edit still uses this skill when
it crosses a trust or data boundary, but it uses the narrowest applicable mode.

## When NOT to use

- Pure visual or client-only work with no server, data, or trust boundary.
- Product discovery before behavior and success conditions are accepted.
- An unexplained defect before a reliable failing signal or cause investigation.
- Architecture sizing or topology selection before an implementation decision.

## Non-negotiable posture

- Inspect the actual stack and existing conventions before proposing code.
- Preserve compatible behavior unless the task explicitly authorizes a break.
- Treat every external value as untrusted, including webhooks, queue payloads,
  environment-derived configuration, file metadata, and model output.
- Make invariants true at the strongest practical layer. A database constraint
  beats a best-effort application check; an authorization query beats a hidden
  client control.
- State uncertainty plainly. A migration not run against a database, or a
  production behavior not observed, is unverified rather than complete.

## Prerequisites and authority

Before making a change, establish:

1. the user-visible behavior or invariant that must change or remain true;
2. repository access and the narrowest runnable verification path;
3. whether the task affects persistent data, identities, external systems,
   secrets, production configuration, or money;
4. the authorization boundary for any irreversible or external action.

Code and tests inside the requested workspace are normal implementation work.
Creating production data, rotating credentials, applying an irreversible live
migration, changing identity-provider settings, sending a real webhook, or
publishing a service requires the user's explicit authority and the platform's
own approval path. Never broaden an approval from one environment, tenant, or
operation to another.

## Operating modes

Choose the smallest mode that can prove the requested outcome. A task may
upgrade mode when inspection reveals a wider blast radius.

| Mode | Use when | Minimum deliverable |
| --- | --- | --- |
| Contract change | API, tool, webhook, or job behavior changes | input, output, errors, compatibility and boundary test |
| Data change | schema, query, state transition, or migration changes | invariant, migration/recovery plan, query or DB evidence |
| Identity change | authn, authz, session, role, or tenant behavior changes | threat-aware access matrix and negative authorization tests |
| Async integration | queue, event, cron, cache, webhook, or dependency changes | delivery/failure model, retry ownership, idempotency evidence |
| Reliability change | timeout, fallback, rate limit, health, or observability changes | failure-mode evidence and operational signal |
| Review or diagnosis | code exists or behavior fails | evidence-backed findings or causal chain before a patch |

For a request spanning modes, name the primary mode and list the secondary
surfaces. Do not hide an auth or migration change inside a generic feature pass.

## Repository inspection strategy

Start with a backend-scoped map. Read only enough to establish the real flow:

1. Identify language, framework, package manager, and commands from manifests,
   CI, container/deployment files, and repository instructions.
2. Find the entry boundary: route registration, RPC resolver, consumer, cron,
   tool handler, or worker bootstrap.
3. Trace one representative request or message from boundary through validation,
   identity, authorization, service logic, persistence, and response/event.
4. Read the affected model/schema, migration history, tests, error formatter,
   and existing observability conventions before changing them.
5. Search all callers, sibling endpoints, consumers, and compatibility clients
   when a public contract or shared helper changes.
6. Inspect recent history only when it can explain a convention, regression, or
   compatibility promise. Do not infer behavior from a filename or framework.

Record a compact discovery line before editing:

```text
stack: FastAPI + SQLAlchemy + Alembic | boundary: POST /orders | auth: OIDC session
data: PostgreSQL | tests: pytest | affected invariant: one paid order per payment id
```

If evidence conflicts, preserve the conflict in the work record and resolve it
with a runtime observation, maintainer decision, or explicitly labeled
assumption. Never choose the tidier interpretation silently.

## Decision framework

### Define the contract before the implementation

For every changed boundary, write the smallest useful contract:

| Concern | Decide and verify |
| --- | --- |
| Caller and identity | Who can call it, how identity is established, and what is not trusted |
| Input | Schema, required/optional fields, limits, normalization, and invalid-input result |
| Output | Success shape, status/result semantics, ordering, pagination, and stable identifiers |
| Failure | Expected domain errors versus unexpected faults, retryability, and user-safe messaging |
| State effect | Records read/written, invariant protected, transaction boundary, and event/cache effect |
| Compatibility | Existing callers, old data, rollout window, deprecation, and rollback/forward-fix path |
| Operations | Timeout/deadline, logs, metrics/traces, alert-worthy failure, and recovery owner |

Use a project-established contract format if one exists. Do not introduce
versioning, pagination, or an error envelope merely because another project
uses it. Introduce it when the actual contract needs it.

### Choose the strongest invariant layer

Apply this order where practical:

1. database constraint, transaction, or storage access control;
2. server-side authorization and validation at the trusted boundary;
3. service-level domain rule and state transition;
4. client validation or UX guardrail.

The lower layers improve usability; they do not replace the higher ones. For
example, use client validation for feedback, server validation for trust, and a
unique constraint for a uniqueness invariant.

### Choose concurrency deliberately

The right tool follows the contested state, not fashion:

| Situation | Usually consider | Evidence needed |
| --- | --- | --- |
| Independent append-only writes | constraint plus normal transaction | duplicate and ordering behavior |
| Read-modify-write on one record | optimistic version check or conditional update | concurrent loser behavior |
| Multi-record invariant | transaction with chosen isolation or ordered locks | conflict, abort, and retry behavior |
| State machine transition | conditional transition from allowed prior state | duplicate/out-of-order transition test |
| Cross-process work claim | durable lease or queue semantics | expiry, handoff, and duplicate worker behavior |

Serializable isolation and locks are not blanket upgrades. PostgreSQL, for
example, can abort serializable transactions and requires an application-level
retry path. Read the data/concurrency checklist before using either.

### Choose retry and delivery semantics honestly

First identify who retries: browser/client, gateway, SDK, job runtime,
webhook sender, worker, or operator. Then choose the smallest mechanism that
makes the requested effect safe:

- no automatic retry when an operation is unsafe and outcome cannot be known;
- idempotency key or durable request record for a retried command whose first
  outcome may be unknown;
- natural unique key or conditional state transition for duplicate delivery;
- transactional outbox when one business change and one published event must
  not diverge;
- explicit dead-letter, replay, or manual-recovery path for poison work.

Do not claim exactly-once delivery unless the concrete system proves that
property end to end. Usually the accurate model is at-least-once delivery plus
idempotent effect.

### Choose migration recovery before writing DDL

Classify the migration:

| Change | Preferred recovery posture |
| --- | --- |
| Additive, unused field/table | ordinary rollback may be reasonable |
| Backfill or new read/write path | expand, backfill, verify, switch, then contract later |
| Destructive rewrite/drop | backup or restore evidence plus tested forward-fix; explicit checkpoint |
| Large-table constraint/index | inspect lock/runtime behavior; stage or use supported online path |

Never promise a down migration that would destroy newly written data or make
recovery less safe. A forward-fix or restore plan can be the correct answer.

## Execution workflow

### 1. Frame the change

State the user outcome, affected contract/invariant, primary mode, known risk,
and verification route. If the request is ambiguous in a way that changes
permissions, data semantics, or public compatibility, ask one focused question
before writing. Otherwise make and label the least risky assumption.

### 2. Build the change map

Use the inspection strategy above. Identify boundary, trust changes, state
owners, readers/writers, external dependencies, and existing tests. For a
public API, list known consumers from repository search and published docs.

### 3. Write the invariant and failure model

Use plain language first: "A member may cancel only their own pending order;
the refund event is emitted once after the cancellation commits." Then list
the states that are allowed, rejected, retryable, or compensatable. This is
the point to read the applicable section of [the checklist](references/checklists.md).

### 4. Select implementation boundaries

Place validation at the trusted ingress, authorization at object access,
transactions around multi-write invariants, and dependency handling at the
outbound boundary. Reuse the repository's schema library, ORM, error shape,
and telemetry conventions before adding a new abstraction or dependency.

### 5. Implement the narrow vertical slice

Change the smallest coherent path from input to durable effect to observable
result. Keep a migration, API contract change, and authorization rule legible
in the diff. Do not fold unrelated cleanup into a security or data change.

### 6. Add boundary-appropriate proof

- API/tool contract: exercise success, malformed, unauthorized, forbidden,
  missing, duplicate, and conflict cases that apply.
- Data change: apply the migration in an appropriate scratch database and
  verify representative existing/new rows plus the recovery path.
- Concurrent or duplicate path: make the competing requests/messages happen,
  not merely inspect code that appears safe.
- External dependency: test timeout, failure, retry, and degradation behavior
  with a controllable fake or authorized test endpoint.
- Background work: verify the durable handoff, duplicate delivery, poison
  path, and operator-visible signal that apply.

Use project-native tests first. Direct HTTP or CLI transcripts are acceptable
additional evidence when a harness is absent.

### 7. Review security and data exposure

Check the changed path for object-level authorization, mass assignment,
unbounded resource consumption, unsafe upstream-data use, secret/PII logging,
tenant leakage, unsafe file handling, and error disclosure. For a broad or
high-risk review, route to the security specialist rather than pretending this
pass replaces a threat model.

### 8. Verify observability and operations

Ensure the change exposes enough signal to answer: what failed, for whom,
where in the dependency chain, and whether retries or queues are accumulating.
Use existing structured log fields and tracing conventions. Do not add noisy
payload logging as a substitute for correlation identifiers and metrics.

### 9. Reconcile compatibility and rollout

For public or persisted behavior, confirm old callers/data remain safe during
the rollout window. Document deprecation, migration sequencing, cache effects,
and the exact recovery action if the new behavior fails after release.

### 10. Stop with evidence

Run the agreed tests and relevant static checks. Inspect the final diff for
unrelated behavior, leaked values, missing callers, and undocumented contract
changes. State unverified surfaces with the exact missing capability.

## Domain-specific rules

Read only the relevant checklist section, not the entire file by default:

| If the task touches | Read in [references/checklists.md](references/checklists.md) |
| --- | --- |
| Endpoint/RPC/tool contract | API design |
| Schema, query, backfill, money, time | Data modeling and migrations |
| Contended writes or state transitions | Transactions and concurrency |
| Login, roles, sessions, tenant data | AuthN / AuthZ / sessions and Multi-tenancy |
| Cache | Caching |
| Jobs, events, webhooks, cron | Queues, jobs, async and External APIs and webhooks |
| Upload/download or external payload | Storage and files |
| Logs, health, metrics, tracing | Errors and observability |

Use the source ledger only when a decision depends on a standard, a
version-sensitive behavior, or a quantitative claim. It records what each
source establishes and what it does not.

## Tool selection and fallbacks

- Use the repository's framework, schema, ORM, migration, queue, and test
  tools before installing a new dependency or copying a generic pattern.
- Use a local/scratch database and controllable dependency fake before a live
  environment. Live production access is evidence only when explicitly allowed.
- When no integration harness exists, exercise the boundary directly with the
  least invasive client available and retain the transcript as evidence.
- When a dependency or database cannot run here, validate static portions,
  state the exact dynamic gap, and do not claim the missing behavior passed.

## Failure handling and edge cases

- A test reveals a different root cause: stop expanding the patch, preserve
  the failing evidence, and diagnose before adding another workaround.
- A migration cannot run locally: do not apply it elsewhere. Verify syntax or
  dry-run support if available, mark runtime evidence unverified, and state the
  exact database access needed.
- A dependency cannot be safely exercised: use a controllable fake, contract
  test, or authorized sandbox. Do not probe a third party with production data.
- A public contract breaks an unknown consumer: prefer an additive transition,
  adapter, or explicit user decision over a silent incompatible release.
- A security finding needs a product decision: present concrete options and
  residual risk. Do not silently weaken authorization or logging requirements.
- An external operation would create spend, user-facing messages, production
  state, or irreversible data: stop at the approval boundary and continue only
  independent local work.

## Quality gates

Before declaring backend work complete, confirm the applicable gates:

- Stack and affected execution path were observed, not assumed.
- Contract and protected invariant are stated in the change or report.
- Every new trusted boundary validates input and every object access has an
  appropriate authorization decision.
- Concurrency, duplicate delivery, and migration recovery were considered
  whenever state can race, repeat, or persist.
- Compatibility, cache invalidation, async side effects, and observability
  are covered when the change reaches them.
- Tests or direct observations exercise the risky behavior, including negative
  cases, and all reported results are fresh.
- No secret, credential, raw sensitive payload, or invented operational claim
  appears in the code, logs, test artifact, or report.

## Stop conditions and handoffs

Stop when the requested behavior and applicable gates have evidence. Hand off
only the information another specialist cannot cheaply re-derive:

```text
backend handoff
contract/invariant: <one sentence>
changed surfaces: <paths and public effects>
evidence: <commands and results>
recovery: <rollback, forward-fix, or restore posture>
unverified: <exact limitation>
next owner: <skill or human decision>
```

Route a reproduced unknown defect to debugging, a scale design decision to
architecture planning, broad attack-surface work to security review, and final
release confidence to the release gate. Do not continue into another skill's
decision just because the backend change exposed it.

## Output contract

Deliver code, migrations, and tests in the project's existing conventions.
The final report contains:

1. discovery line and mode;
2. contract/invariant delta and compatibility note;
3. changed paths and data/external effects;
4. verification commands with observed results;
5. recovery/rollout note for persisted or public changes;
6. unverified items, follow-ups, and any approval still required.

Example:

```text
mode: async integration + data change
invariant: one fulfillment event per paid order, even if the worker retries
contract: POST /payments now records payment id before enqueueing fulfillment
recovery: additive outbox table; replay is safe by event id; no destructive DDL
verified: pytest tests/payments -q: 18 passed; duplicate-delivery test passed
unverified: production queue visibility requires staging credentials
```

## Research basis

Read [references/research.md](references/research.md) for the source ledger
when a decision depends on a standard, a framework-version fact, or a measured
claim. It must never be used to turn a pattern into a universal rule.
