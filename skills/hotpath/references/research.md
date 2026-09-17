# hotpath research ledger

## Source 1

Title: Benchmarking

Author / Organization: Go project

Publication date: Living documentation

Version: Current documentation

URL: https://pkg.go.dev/testing#hdr-Benchmarks

Source type: official docs

What it establishes:
Benchmarking requires repeatable workloads and reports measured execution behavior.

What this skill adopts:
Define metric and workload, control noise, compare equivalent conditions, and keep only demonstrated improvements.

What it does NOT establish:
It does not prescribe a universal sample count, warmup count, or acceptable regression threshold.

Numbers taken from source:
No numerical threshold is adopted.

Reverify when:
The project benchmark framework or workload changes.

## Query-plan evidence

Title: Using EXPLAIN

Author / Organization: PostgreSQL Global Development Group

Publication date: 2026

Version: PostgreSQL 18 documentation

URL: https://www.postgresql.org/docs/current/using-explain.html

Source type: official docs

What it establishes:
EXPLAIN exposes planned query operations and estimates; estimates can differ
with data statistics and platform conditions, and plan cost omits some elapsed
time contributors.

What this skill adopts:
Inspect actual query behavior with representative parameters and data, compare
estimated/actual rows where available, and avoid presenting planner cost as an
end-to-end latency measurement.

What it does NOT establish:
It does not make every sequential scan wrong or prescribe an index for a query.

Numbers taken from source:
No cost, row-count, or timing default is adopted.

Reverify when:
Database version, schema, statistics, workload, or query parameters change.

## Interaction responsiveness

Title: Optimize Interaction to Next Paint

Author / Organization: web.dev

Publication date: 2026

Version: Current article

URL: https://web.dev/articles/optimize-inp

Source type: official docs

What it establishes:
Interaction responsiveness depends on input delay, processing, and presentation
delay, and needs context-specific measurement.

What this skill adopts:
Inspect interaction traces and long tasks rather than inferring UI performance
from load time or a single framework operation.

What it does NOT establish:
It does not prove field responsiveness from one local trace or choose a
framework-specific fix.

Numbers taken from source:
No numerical target is adopted.

Reverify when:
The interaction path, device class, or measurement methodology changes.
