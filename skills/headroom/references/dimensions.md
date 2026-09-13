# Scale dimensions — read only what the decision touches

Each dimension: the question, the threshold thinking, and when it matters.
Skip dimensions the current scale makes irrelevant — and say you skipped
them (that's proportionality, not laziness).

## Load shape

- **Traffic** — requests/sec now and expected peak; the number everything
  else keys off. Ask; estimate only with shown arithmetic.
- **Read/write ratio** — decides caching, replicas, denormalization.
  95% reads and 50/50 are different architectures.
- **Latency targets** — interactive (<200ms p50?) vs background? Sets
  how much complexity sync paths may carry.
- **Throughput / data size** — GBs vs TBs changes storage choices more
  than any feature comparison chart.

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
- **Backpressure** — what happens when producers outpace consumers?
  Rejected work beats silently growing lag.

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
