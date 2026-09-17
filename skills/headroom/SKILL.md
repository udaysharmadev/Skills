---
name: headroom
description: Plans capacity, performance, and resilience from measured or explicitly estimated demand. Use for scalability decisions, growth planning, service targets, bottleneck forecasts, queue or cache sizing, and Now/Next/Scale plans. Do not use to debug a known slow path or implement a feature.
---

# headroom: capacity decisions with an expiry date

## Purpose and scope

Use this skill to decide what a system needs now, what evidence should trigger
the next change, and what belongs in a deliberately deferred scale design. It
produces a decision record, not invented load-test results or an architecture
assembled from fashionable components.

Capacity belongs to a workload and an objective: traffic alone is not a model.
Consider request shape, concurrency, data growth, dependency limits, failure
behavior, recovery objectives, operational ownership, and cost where they can
change a decision. State every unknown, estimate, source, and confidence level.

## When NOT to use

- A presently slow endpoint, query, or build needs diagnosis: use `hotpath` or
  `sleuth` first. This skill can consume their measurements afterwards.
- A code-level backend design or migration is needed: use `backend` after the
  capacity decision identifies the need.
- Mapping an architecture without a scale decision: use `blueprint`.
- A product-priority decision with no technical capacity evidence: use
  `masterplan` or `hotseat`.
- A provider limit, price, benchmark, or framework fact cannot be verified in a
  current primary source: research it first or mark it unresolved.

## Non-negotiables

- Do not invent usage, utilization, payload size, availability, cost, or
  throughput. Separate measured, reported, derived, and assumed values.
- A recommendation names the condition that makes it necessary, the observable
  metric, an owner, and a reversal or migration path.
- Preserve the simplest architecture meeting the stated objective. A future
  design is not permission to build it now.
- Optimize user-visible objectives and failure containment, not average CPU or
  a single benchmark.
- Do not load-test, alter autoscaling, change quotas, or create cloud resources
  without explicit authority. Read-only telemetry is normally safe.

## Prerequisites and authority

Start with the decision and deadline. Collect what is available:

| Input | Minimum useful form | If missing |
| --- | --- | --- |
| User objective | latency, completion time, availability, freshness, or cost boundary | record the product question |
| Demand | rate, concurrency, peak timing, tenant skew | create a bounded scenario range |
| Work shape | classes, payload size, fanout, sync or async | inspect routes, jobs, schemas, traces |
| Supply | compute, database, queue, quota, dependency limits | inspect configuration and provider evidence |
| Evidence | dashboards, traces, tests, incidents, invoices | label confidence and collection plan |
| Constraints | RTO/RPO, team, compliance, budget, release window | surface the tradeoff |

Ask before spending money, creating production load, changing retention,
increasing a quota, or weakening a guardrail. Obtain approval before a
destructive or production stress test. Never include secrets, customer data,
tokens, or raw sensitive traces in output.

## Operating modes

Choose one primary mode and state it in output.

1. **Triage:** decide whether capacity concern is plausible and what to measure
   first. Stop before prescriptions.
2. **Forecast:** model an existing workload over a stated horizon, then identify
   earliest bottlenecks and uncertainty bands.
3. **Design review:** compare architectures or managed services against a
   concrete workload and objective.
4. **Launch readiness:** verify assumptions, overload behavior, observability,
   and rollback before a known event.
5. **Incident follow-up:** turn measured saturation or backlog into prevention
   work. Do not replace incident command.

## Repository and system inspection strategy

Inspect narrowly and make an evidence map before interpreting numbers.

1. Read repository instructions, runbooks, ADRs, incident reviews, SLOs,
   deployment manifests, and supplied cost or quota documents.
2. Locate ingress, routes, workers, queue producers and consumers, data stores,
   caches, third-party calls, retries, timeouts, and rate limits.
3. Inspect instrumentation and dashboards. Confirm metric unit, aggregation
   window, sampling, labels, and success/failure separation before trusting it.
4. Trace representative request classes end to end. Include expensive, bursty,
   tenant-skewed, and write-heavy paths, not only the happy path.
5. Record quota, pool, disk, retention, concurrency, and dependency-failure
   assumptions from current official documentation.
6. Read `references/dimensions.md` only for dimensions the decision touches.
   It is a prompt set, not a scorecard.

If repository and production evidence disagree, report that discrepancy. Do not
average it away. Without access, continue in estimate mode with a precise
telemetry request.

## Capacity model and decision framework

### Classify every input

Use **measured** (timestamp and source), **reported** (who supplied it),
**derived** (show arithmetic), or **assumed** (range and rationale). An
assumption that changes the recommendation is a decision blocker or first
measurement, not fine print.

### Model workload, not one number

For each workload class capture arrival rate, concurrent work, service-time
distribution, payload size, fanout, read/write ratio, retries, and deadline.
Use peak and burst ranges. Basic arithmetic is useful only with units and
exclusions visible:

```
requests per second x average bytes per request = approximate ingress bytes/s
arrival rate x average successful service time = average in-flight work
accepted rate minus completed rate = backlog growth rate
```

These are planning approximations, not queue proofs. They do not replace tail
latency, dependency behavior, or representative testing. For a queue,
distinguish accepted, processed, retried, delayed, dead-lettered, and discarded
work. A stable average can hide a burst above drain rate.

### Find the constraint that fails first

Evaluate normal, credible peak, and degraded-dependency cases. For each inspect
user latency and errors, compute, memory, disk/database I/O, pools, queue age
and depth, network, provider limit, locks, hot keys or tenants, and human
operational capacity.

Latency, traffic, errors, and saturation are a compact starting point, not an
excuse to ignore correctness or cost. Use distributions and a high percentile
when it matches the user objective. Explain why that percentile and window fit
the journey.

### Compare choices by trigger and reversibility

For every change, write:

| Field | Required answer |
| --- | --- |
| Problem | Which scenario fails which objective? |
| Now | Smallest safe change, including no change if justified |
| Trigger | metric, window, threshold or bound, and reviewer |
| Next | change after trigger, migration and rollback |
| Cost and risk | spend, operational burden, correctness and failure tradeoff |
| Confidence | evidence quality and assumption most likely to overturn it |

Avoid universal utilization thresholds. A safe margin depends on service-time
variation, autoscaling delay, retries, redundancy, objectives, and a resource's
failure curve. Derive it from behavior or make it an experiment.

## Workflow

1. **Frame the decision.** Write boundary, horizon, stakeholder, objective,
   non-goals, and decision authority.
2. **Build an evidence ledger.** Inventory telemetry, code/configuration,
   provider docs, incidents, and assumptions with timestamps.
3. **Segment workload classes.** Do not blend a cheap read with an export, one
   tenant with global traffic, or synchronous traffic with batch work.
4. **State scenarios.** Include normal, credible peak, degraded dependency, and
   low/high bounds when demand is uncertain.
5. **Perform transparent arithmetic.** Show units, service-time basis, fanout,
   retry multiplication, and exclusions. Have a reader check critical units.
6. **Locate bottlenecks and propagation.** Identify first binding resource and
   what retries, queues, pools, caches, and fallbacks do under overload.
7. **Set objectives and observability.** Define user-facing acceptance boundary,
   leading saturation/backlog signals, and an actionable owner.
8. **Choose Now, Next, Scale.** Keep Now reversible. Every Next item has a
   trigger and preparatory seam. Scale says "do not build today" unless needed.
9. **Design safe verification.** Prefer replay, staging, canary, synthetic, or
   bounded load tests. State representativeness and abort conditions.
10. **Publish and revalidate.** Deliver record, plan, owners, review trigger,
    and changes that invalidate it.

## Domain patterns and edge cases

### Queues and asynchronous work

A queue changes where work waits; it does not create capacity. Check producer
rate versus successful drain rate, retry amplification, cost, ordering and
deduplication, deadline behavior, retention, dead letters, poison messages,
and a recovery plan. Alert on user-relevant age or recovery risk, not depth
alone. Define admission control when the queue is constrained.

### Caches

Model hit rate by request class and miss cost. Cover cold start, expiry
synchronization, stampede, invalidation, stale-data allowance, eviction,
outage, and origin overload. A high aggregate hit rate can hide a critical
low-hit route. Do not add a cache before identifying origin bottleneck and
correctness boundary.

### Databases and stateful systems

Assess query and lock behavior, connection caps, transaction length, hot
partitions, index/storage growth, backup/restore time, replication lag, schema
locking, and noisy-neighbor controls. Separate read scaling from write
serialization. A replica does not solve primary write capacity, stale-read
semantics, or a hot key.

### Dependency failure and overload

Include timeout budgets, retry/circuit behavior, concurrency limits,
backpressure, prioritization, graceful degradation, idempotency, and recovery
after a dependency returns. Retries multiply workload and need transient-failure
evidence plus a deadline. Load shedding preserves high-value safe work and
exposes what was rejected or deferred.

### Multi-tenant and agentic systems

Look for tenant quotas and fairness, adversarial large inputs, expensive tool
paths, uncontrolled fanout, provider rate limits, compute budgets, worker
starvation, and human approval queues. Keep agent orchestration modular but
monolithic until independent scaling or ownership has evidenced need.

## Tool selection and fallbacks

- Prefer dashboards, traces, database statistics, queue metrics, deployment
  config, and provider limits to generic calculators.
- Use plans, profilers, and traces for a suspected bottleneck. Route code-level
  diagnosis to `hotpath`.
- Use a spreadsheet or checked arithmetic for scenarios. Preserve formulas so
  another reader can change an assumption.
- Use a load generator only with authority, representative data, protected
  dependencies, rate caps, and an abort condition. If unavailable, use history
  and lower confidence.
- If telemetry lacks cardinality or distributions, propose the smallest new
  instrument instead of guessing from averages.

## Failure handling and escalation

Stop and escalate when a safety-critical target, recovery requirement,
contractual limit, or hard quota is already violated. Stop a test at its abort
threshold or unexpected shared-system impact. Do not infer causality from one
before/after graph with changing traffic.

If results conflict, preserve both, inspect units, windows, and version changes,
then run the narrowest discriminating measurement. If a choice depends on an
unbounded unknown, present conditional branches rather than a false answer.

## Quality gates

- Boundary, objective, horizon, and operating mode are explicit.
- Every input has provenance and a measured/reported/derived/assumed label.
- Workload classes, peak/burst case, and degraded case are represented.
- Arithmetic has units and assumptions. No magic threshold appears as fact.
- Every Now/Next/Scale item has evidence, trigger, owner, tradeoff, migration
  or rollback, and confidence.
- Overload behavior protects correctness and has measurable signals.
- At least one tempting component says "do not build today" with its trigger.
- Tests have authority, safety bounds, and expected evidence.

## Stop conditions

Stop when the decision, confidence, Now/Next/Scale plan, triggers, and first
verification are clear. Do not refine a model that cannot change a decision.
Reopen when workload, code path, quota, objective, or horizon changes.

## Handoff

Hand implementation to `backend`, bottleneck investigation to `hotpath`,
mapping to `blueprint`, release proof to `proof` or `roadtest`, and
prioritization to `masterplan`. Include trigger, evidence, acceptance test,
safety limits, and unresolved assumption in every handoff.

## Output contract

Return a decision record containing: decision and mode; boundary; objective and
horizon; evidence ledger; scenarios and arithmetic; bottleneck/failure analysis;
Now/Next/Scale table; "do not build today" list; telemetry and verification
plan; owners; risks; and open questions. Write `docs/design/<slug>.md` only
when asked for a durable artifact or when the decision guides later work.

## References and research basis

Read [references/dimensions.md](references/dimensions.md) only for relevant
review prompts. Read [references/research.md](references/research.md) before
using an external standard, provider claim, or numerical rule. It records
sources that changed this skill, their limits, and revalidation conditions.
