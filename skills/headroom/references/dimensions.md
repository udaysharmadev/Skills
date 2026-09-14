# Scale dimensions — read only what the decision touches

Each dimension: the question, the threshold thinking, and when it matters.
Skip dimensions the current scale makes irrelevant — and say you skipped
them (that's proportionality, not laziness).

## Load shape

- **Traffic** — requests/sec now and expected peak; the number everything
  else keys off. Ask; estimate only with shown arithmetic.
- **Traffic pattern** — flat, diurnal (peak ≈ 5–10× average), or spiky
  (viral/batch)? Capacity is sized for the pattern, not the mean; queues
  and load shedding exist for the spikes.
- **Read/write ratio** — decides caching, replicas, denormalization.
  95% reads and 50/50 are different architectures.
- **Latency targets** — interactive (<200ms p50?) vs background? Sets
  how much complexity sync paths may carry.
- **Throughput / data size** — GBs vs TBs changes storage choices more
  than any feature comparison chart.
- **Durability** — how much data loss is acceptable in a disaster (RPO)?
  "Zero" prices the storage architecture before anything else does.

## Capacity estimation (when numbers exist)

Do the arithmetic explicitly, one line per step, units on everything:

```text
avg request = 3 reads + 0.2 writes
peak factor = 5× (diurnal assumption — label it)
users → sessions/hr → req/s at peak:  10k users × 0.5 req/session/hr
  × 5 peak ≈ 1.4 req/s  ← tiny; a $10 managed DB carries this
storage growth = rows/day × row size × 365 (+ indexes ≈ 1.5×)
fan-out = one user action → N service calls (N multiplies load downstream)
```

If the arithmetic shows headroom under 3×, the "Scale" tier stops being
hypothetical and Next-level items get concrete triggers. If it shows
100× headroom, say so — that is the proportionality rule winning.

## Data

- **Consistency** — what actually breaks if two readers disagree for a
  second? Most apps: nothing. Money/inventory: real damage. Choose from
  the failure, not from fashion.
- **Partitioning / sharding** — the thing you do when one machine
  genuinely can't hold or serve the data. Marked Scale until proven
  otherwise.
- **Replication** — read scaling and failover; comes with lag, which
  becomes a consistency question above.

## Coordination

- **Concurrency** — hot rows, double-submit, race conditions on limited
  inventory. Usually solved with constraints + idempotency, not queues.
- **Queues** — for bursty or deferrable work (email, media, webhooks).
  Not for making a fast request slow on purpose.
- **Retries / idempotency** — anything that retries must be safe to
  repeat. Cross-cutting; see `backend`'s disciplines.
- **Backpressure / load shedding** — what happens when producers
  outpace consumers? Rejected work beats silently growing lag; decide
  WHO gets shed (low-priority traffic first) before the overload, not
  during it.
- **Hot keys / hot rows** — one celebrity user, one popular product, one
  counter row: caching and queueing fail at the hot key before they fail
  in aggregate. Name the likely hot keys and their plan.

## Availability

- **Availability goals** — "99%" and "99.99%" are different budgets and
  different teams. Match the goal to what downtime actually costs.
- **Failure domains** — what dies together today? One box, one zone?
  Name the blast radius before promising uptime.
- **Disaster recovery** — backup restore *tested*, RTO/RPO stated.
  Untested backups are hopes, not DR.
- **Multi-region** — Scale level almost always; the lag/cost bill is
  enormous. Data residency laws are the one non-negotiable trigger.

## Protection

- **Rate limiting** — per-IP at minimum, per-token for real APIs.
  Decides abuse survival more than any scaling.
- **Cost** — the constraint that makes proportionality real. A $5 managed
  DB that survives 10k users beats a $500 self-run cluster.

## Operability

- **Caching** — where reads are repetitive; every cache needs an
  invalidation story.
- **Observability** — can you see the thing break? Logs/metrics/traces
  proportional to the architecture's complexity (more moving parts =
  more visibility required).
- **Migration path** — from what exists today, in steps that each ship.
  A design with no incremental path from reality is fiction.

## The proportionality table (rough guide)

| Level | Typical numbers | Appropriate shape |
| --- | --- | --- |
| Now | < 10k users, < 50 req/s, single region | one app process + managed DB + queue for async work; boring everywhere |
| Next | 10k–500k users, 50–2k req/s | read replicas, real caching layer, job workers split out, multi-AZ |
| Scale | beyond, or hard multi-region/data-residency needs | service split along real seams, sharding where data demands, event-driven where coupling hurts |
