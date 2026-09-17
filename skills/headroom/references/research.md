# headroom research ledger

This ledger identifies sources that materially changed the operating behavior
of this skill. It does not turn examples or defaults into universal thresholds.

## Service signals and tail latency

Title: Monitoring Distributed Systems

Author / Organization: Google SRE

Publication date: 2016

Version: SRE book chapter

URL: https://sre.google/sre-book/monitoring-distributed-systems/

Source type: official docs

What it establishes:
Latency, traffic, errors, and saturation are useful service signals. Tail
latency, separate successful and failed responses, and symptom-oriented alerts
matter more than a convenient average.

What this skill adopts:
Use the four signals as a starting model, require distributions for
user-sensitive latency, and insist that alerts name an urgent, actionable
response.

What it does NOT establish:
It does not supply universal latency percentiles, utilization thresholds, or
capacity targets for another organization.

Numbers taken from source:
No numerical default is adopted.

Reverify when:
The service objective, instrumentation, or operating model changes.

## Overload protection

Title: Using load shedding to avoid overload

Author / Organization: Amazon Web Services

Publication date: 2020

Version: AWS Builder's Library article

URL: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/

Source type: official docs

What it establishes:
Overload can create nonlinear latency degradation and amplify failures. Systems
need intentional admission, prioritization, and shedding behavior.

What this skill adopts:
Model overload behavior, bound retries, specify what work can be rejected or
deferred, and require safe test abort conditions.

What it does NOT establish:
It does not choose a single shedding algorithm or tell every product which
requests have highest value.

Numbers taken from source:
No numerical threshold is adopted.

Reverify when:
The workload's critical paths, deadlines, or dependency behavior changes.

## Queue recovery

Title: Avoiding insurmountable queue backlogs

Author / Organization: Amazon Web Services

Publication date: 2022

Version: AWS Builder's Library article

URL: https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/

Source type: official docs

What it establishes:
Backlogs require planning for recovery rate as well as normal processing rate;
retries and downstream limits can prevent a simple scale-out response.

What this skill adopts:
Represent accepted, completed, retried, delayed, and dead-lettered work;
analyze backlog age, drain/recovery, and admission control rather than depth
alone.

What it does NOT establish:
It does not prescribe a queue product, retention period, or consumer count.

Numbers taken from source:
No numerical default is adopted.

Reverify when:
Queue semantics, producer shape, consumer capacity, or recovery requirements
change.

## Metrics semantics

Title: Metrics

Author / Organization: OpenTelemetry Authors

Publication date: 2026

Version: Current documentation

URL: https://opentelemetry.io/docs/concepts/signals/metrics/

Source type: official docs

What it establishes:
Metrics are aggregated measurements with types, units, temporality, attributes,
and aggregation choices that affect their meaning and cost.

What this skill adopts:
Verify metric unit, aggregation window, labels, sampling, and success/failure
semantics before treating telemetry as capacity evidence.

What it does NOT establish:
It does not select a service objective or make a dashboard accurate by itself.

Numbers taken from source:
None.

Reverify when:
Telemetry SDK, aggregation, cardinality policy, or dashboard query changes.

## Horizontal scaling mechanics

Title: Managing Workloads

Author / Organization: Kubernetes Authors

Publication date: 2026

Version: Current documentation

URL: https://kubernetes.io/docs/concepts/workloads/management/

Source type: official docs

What it establishes:
Workload scaling and availability behavior depend on controller configuration,
readiness, rollout, resource requests, and cluster capacity.

What this skill adopts:
Treat autoscaling as one delayed control in a whole system, and inspect
readiness, quotas, requests, dependencies, and rollout behavior before claiming
that more replicas solve an objective.

What it does NOT establish:
It does not specify a safe replica count, utilization target, or workload model.

Numbers taken from source:
None.

Reverify when:
Kubernetes version, scaling configuration, cluster constraints, or workload
architecture changes.
