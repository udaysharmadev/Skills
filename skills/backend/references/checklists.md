# Backend checklists — read only the sections your task touches

Each section: the checks that transfer across stacks, with the failure
each prevents.

## API design

- Resource naming consistent with the existing API (plural nouns, no verbs
  in paths unless the codebase does that).
- Consistent error shape: same error envelope everywhere; machine-readable
  code + human message; no stack traces in responses.
- Status codes honest: 400 vs 401 vs 403 vs 404 vs 409 vs 422 used for
  their actual meanings; 500 only for genuinely unexpected failures.
- Pagination on any collection that can grow: limit default, max cap,
  cursor or offset decision stated (cursor preferred for large/changing
  sets).
- Versioning: breaking change → version bump or explicit compatibility
  window; never silently change response shapes.
- Idempotency for unsafe methods where retries are plausible (payments,
  creation with side effects) — accept an idempotency key or dedupe on a
  natural constraint.

## Data modeling and migrations

- Schema serves the queries (look at the actual access patterns before
  finalizing tables/indexes).
- Indexes for the where/join/order-by columns that hot queries use; every
  new query that filters on an unindexed column is a decision, not an
  accident.
- Nullability explicit; defaults thought through for existing rows.
- Migrations: additive-first (add column/table → backfill → switch reads
  → drop old); down-path written and tested; locks considered for large
  tables (batched backfills, avoid long transactions).
- Money: integer minor units or decimal types — never floats.
- Time: UTC everywhere internally; timezone conversion at the edge; never
  store local times naive.

## Transactions and concurrency

- Multi-write invariants wrapped in a transaction with the right
  isolation for the failure it prevents.
- Optimistic locking (version column) or explicit conflict handling for
  read-modify-write on contested rows.
- Uniqueness enforced by the database (constraints), not application
  checks — the app-level check is UX, the constraint is correctness.

## AuthN / AuthZ / sessions

- Passwords: argon2id/bcrypt with sane params; never reversible storage.
- Sessions/tokens: httpOnly + secure + sameSite cookies for browsers;
  short-lived access + rotation for refresh; logout actually invalidates.
- Authorization check at the object level per request ("this user, this
  record") — route-level middleware alone is not authorization.
- OAuth/OIDC: state + PKCE where applicable; validate issuer/audience on
  tokens; don't build crypto when a provider exists.

## Caching

- Every cache has an invalidation story (TTL is the minimum, an event is
  better); stale-while-revalidate where the stack supports it.
- Cache keys include everything the response depends on (auth scope
  included — cross-tenant cache leaks are a real vulnerability class).
- Don't cache what's cheap to compute; do cache the N+1s and external
  calls you already measured.

## Queues, jobs, async

- Handlers idempotent (they will run twice); dedupe/skip logic on a
  natural key.
- Retries with exponential backoff + jitter; a dead-letter path for
  poison messages; visibility into failure counts.
- Job payloads carry IDs, not blobs — the handler re-reads current state
  instead of acting on stale snapshots.

## External APIs and webhooks

- Timeouts and a small retry budget on every outbound call; no unbounded
  hangs.
- Circuit behavior on repeated failure: stop calling a failing
  dependency for a bounded cool-down (fail fast + surface degraded
  status) instead of piling latency onto every request; per-dependency,
  not global.
- Webhooks: verify signatures before trusting payloads; respond fast,
  process async; treat delivery as at-least-once.

## Multi-tenancy

- Tenant scoping is a data-layer invariant, not a UI filter: every query
  for tenant-owned data carries the tenant condition, enforced by row
  level security or a checked repository layer — one unscoped query is
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
- Webhooks: verify signatures before trusting payloads; respond fast,
  process async; treat delivery as at-least-once.
- External responses validated (shape/enum) before use — upstream API
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
