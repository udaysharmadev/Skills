# Capacity dimensions

Read only the dimensions that can change the current decision.

## Workload

Record observed values where available and label estimates:

- traffic rate and peak-to-average shape;
- concurrency and burst duration;
- read and write mix;
- request fan-out and payload size;
- data volume, growth, retention, and index overhead;
- latency and availability objectives;
- recovery point and recovery time objectives;
- budget and operational staffing.

Show arithmetic with units. A sample estimate is not a capacity fact.

## Bottlenecks

For each likely bottleneck, record:

- resource or dependency;
- evidence of current utilization;
- failure behavior as saturation approaches;
- the metric that would trigger action;
- the cheapest change that creates headroom;
- new cost, consistency, and operational failure modes.

Consider compute, memory, storage, database locks, connections, queues, network,
third-party quotas, hot keys, and human on-call capacity.

## Architecture choices

Use the failure that must be prevented to choose among:

- vertical scaling, horizontal scaling, and workload isolation;
- caching and invalidation;
- batching, queues, and backpressure;
- replication, partitioning, and sharding;
- stronger or weaker consistency;
- single-region and multi-region deployment;
- modular monolith and separately deployed services.

Do not add a mechanism merely because a growth scenario can be imagined.

## Now, Next, Scale

| Horizon | Content |
| --- | --- |
| Now | simplest design that meets current measured needs |
| Next | one low-regret preparation plus a measurable trigger |
| Scale | larger change, evidence that would justify it, migration path, and cost |

A scenario multiplier may be useful for sensitivity analysis, but it must be
labeled as a scenario chosen for the current task, not a universal forecast.

## Failure and recovery

If reliable workload data is missing, return the smallest safe design and the
measurement needed next. If a recommendation depends on an untested assumption,
state the counterfactual that would reverse it.
