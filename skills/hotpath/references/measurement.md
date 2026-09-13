# Measurement toolbox — by layer, with the traps

Use what exists (project-native → installed tool → tiny bundled helper
→ recommend optional → manual). State the tool and conditions with every
number.

## Web frontend

- **Lighthouse / Core Web Vitals** (LCP, INP, CLS) — lab numbers with
  throttling declared; field data (RUM) is truth when available.
- **DevTools Performance panel** — flame charts for long tasks, INP
  attribution, layout shifts.
- **Bundle analysis** (`webpack-bundle-analyzer`, `vite-bundle-visualizer`,
  `source-map-explorer`) — what's actually in the payload; the 300KB
  "utility" nobody imports directly.
- **Network panel** — waterfalls: sequential requests that could
  parallelize, oversized payloads, missing compression/cache headers.
- Traps: lab throttle ≠ user devices; extensions skew runs; measure the
  production build, never dev mode.

## Backend / API

- **Query counting** — ORM logs, APM traces, or middleware timing; the
  N+1 shows up as 1 request → 200 queries.
- **Slow query log / `EXPLAIN ANALYZE`** — missing indexes and seq scans
  name themselves; compare planned vs actual rows.
- **APM/tracing** (OpenTelemetry, Sentry perf, provider APMs) — p50/p95/
  p99 per endpoint; p99 is where the intermittently angry users live.
- **Load tools** (`autocannon`, `hey`, `k6`, `ab`) — keep load below the
  saturation point you're trying to measure latency at, or numbers
  invert.
- Traps: local DBs with 12 rows lie about query plans; cold caches;
  connection-pool exhaustion masquerading as "slow DB".

## Application / language runtime

- **Profilers over timers** — cProfile/py-spy (Python), --cpu-prof/clinic
  (Node), pprof (Go), perf/flamegraph (Rust/C), JFR/async-profiler (JVM).
  CPU-bound or IO-bound stops being a debate.
- **Allocation/GC pressure** — most "memory leaks" are retention via
  forgotten listeners/maps/closures; heap snapshots diffed over time
  find the retainer.
- Traps: micro-benchmarks and JIT warmup; measuring debug builds;
  optimize-what-you-can-see (no profiler = guesswork).

## Data layer

- **Row counts and table growth** — the query fast at 10k rows dies at
  10M; test at realistic volume (seed it if needed — say so).
- **Index usage** — `EXPLAIN` every hot query; an index that exists but
  isn't used is a finding, not a plan.
- **Lock/transaction contention** — traces showing latency clusters at
  writes point here.

## CI / build / startup

- **Timing the phases** — `time` per step, build-tool profiling modes
  (`vite build --profile`, webpack stats), test-runner slow-report
  flags. Parallelize/cache the biggest phase, not the loudest one.

## Universal rules

1. Same conditions both sides of a change (machine, data, warmup, load).
2. Median/percentiles over single runs; report the spread.
3. The measurement method ships in the report — reproducible or it's an
   anecdote.
4. Realistic data volume — seeding up to production-like scale is part
   of the work, stated in the report.
