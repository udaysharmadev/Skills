# Backend checklists: read only the sections your task touches

Each section: the checks that transfer across stacks, with the failure
each prevents.

## API design

- Resource naming consistent with the existing API (plural nouns, no verbs
  in paths unless the codebase does that).
- Consistent error shape: same error envelope everywhere; machine-readable
  code + human message; no stack traces in responses.
- Status codes honest: 400 vs 401 vs 403 vs 404 vs 409 vs 422 used for
  their actual meanings; 500 only for genuinely unexpected failures.
- Pagination on collections whose size or latency requires it; limit and cap
  follow the product contract, while cursor versus offset follows mutation and
  ordering behavior.
- Versioning: breaking change → version bump or explicit compatibility
  window; never silently change response shapes.
- **LLM/Agent Outputs:** Any endpoint accepting or returning LLM-generated data
  must validate it strictly against a schema (e.g., Pydantic, JSON Schema).
  Never trust raw LLM output without a structural boundary check.
- **Retry safety:** State-changing operations that may be retried use the
  mechanism appropriate to their contract: an idempotency key, uniqueness
  constraint, conditional write, durable ledger, or explicit rejection.
  Describe delivery and effect guarantees without claiming generic exactly-once.

## Data modeling and migrations

- Schema serves the queries (look at the actual access patterns before
  finalizing tables/indexes).
- Indexes for the where/join/order-by columns that hot queries use; every
  new query that filters on an unindexed column is a decision, not an
  accident.
- Nullability explicit; defaults thought through for existing rows.
- Migrations: additive-first for live data when practical; recovery may be a
  tested rollback, forward-fix, restore, or backup path. Do not invent a down
  migration when reversal would be less safe.
- Money: integer minor units or decimal types: never floats.
- Time: UTC everywhere internally; timezone conversion at the edge; never
  store local times naive.

## Transactions and concurrency

- Multi-write invariants wrapped in a transaction with the right
  isolation for the failure it prevents.
- Optimistic locking (version column) or explicit conflict handling for
  read-modify-write on contested rows.
- Uniqueness enforced by the database (constraints), not application
  checks: the app-level check is UX, the constraint is correctness.
- Deadlocks designed out, not debugged later: acquire locks in a
  consistent order, keep contested transactions short, and retry the
  whole transaction on deadlock/abort (with a cap) rather than part of
  it: partial retry after a deadlock is silent corruption.

## AuthN / AuthZ / sessions

- Passwords: argon2id/bcrypt with sane params; never reversible storage.
- Sessions/tokens: httpOnly + secure + sameSite cookies for browsers;
  short-lived access + rotation for refresh; logout actually invalidates.
- Authorization check at the object level per request ("this user, this
  record"): route-level middleware alone is not authorization.
- OAuth/OIDC: state + PKCE where applicable; validate issuer/audience on
  tokens; don't build crypto when a provider exists.

## Caching

- Every cache has an invalidation story (TTL is the minimum, an event is
  better); stale-while-revalidate where the stack supports it.
- Cache keys include everything the response depends on (auth scope
  included: cross-tenant cache leaks are a real vulnerability class).
- Don't cache what's cheap to compute; do cache the N+1s and external
  calls you already measured.

## Queues, jobs, async

- Handlers exposed to duplicate delivery are retry-safe through a natural key,
  conditional transition, or explicit deduplication.
- Retries with exponential backoff + jitter; a dead-letter path for
  poison messages; visibility into failure counts.
- Job payloads carry IDs, not blobs: the handler re-reads current state
  instead of acting on stale snapshots.
- DB + event atomicity goes through a transactional outbox: write the
  event row in the same transaction as the state change, relay
  asynchronously. Never publish-then-commit (ghost events on rollback)
  or commit-then-publish (silent loss on crash).

## External APIs and webhooks

- Timeouts and a small retry budget on every outbound call; no unbounded
  hangs. Retry ownership is explicit: the caller owns retries within its
  budget and propagates deadlines downstream: callees never silently
  retry non-idempotent operations on the caller's behalf.
- Circuit behavior on repeated failure: stop calling a failing
  dependency for a bounded cool-down (fail fast + surface degraded
  status) instead of piling latency onto every request; per-dependency,
  not global.
- Backpressure over collapse: bounded queues, shed excess load with an
  explicit signal (`429` + `Retry-After` where HTTP fits), degrade
  read-only paths before write paths. A circuit protects you from a sick
  dependency; backpressure protects you from a healthy flood.
- Webhooks: verify signatures before trusting payloads; respond fast,
  process async; treat delivery as at-least-once.
- **Agent integration:** Reuse the project's existing tool or protocol surface.
  MCP is one option when ecosystem interoperability justifies it, not a
  universal wrapper requirement.

## Multi-tenancy

- Tenant scoping is a data-layer invariant, not a UI filter: every query
  for tenant-owned data carries the tenant condition, enforced by row
  level security or a checked repository layer: one unscoped query is
  a cross-tenant leak.
- Tenant context arrives from the authenticated principal, never from a
  client-supplied id alone.
- Cross-tenant features (admin, support tooling) are explicit, audited
  surfaces with their own authorization.

## Storage and files

- Uploads: validate type/size/content server-side; store outside the
  webroot or in object storage with private-by-default access; never
  trust client filenames (path traversal).
- Serve user content from signed/expiring URLs, not public buckets.
- Large files stream; don't buffer whole uploads in memory.
- External responses validated (shape/enum) before use: upstream API
  changes are an input, not an exception.

## Errors and observability

- Structured logs with request/correlation IDs; levels used meaningfully;
  identifiers not payloads.
- Unhandled paths (panic/crash handlers) return a generic 500 and log the
  detail server-side.
- Health endpoint reflects real dependencies when it matters, liveness vs
  readiness distinguished.
- Metrics for the things you'd ask about at 3am: error rate, latency
  percentiles, queue depth, retry counts.
