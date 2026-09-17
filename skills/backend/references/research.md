# backend research ledger

This ledger records sources that changed the skill's behavior. It is not a
generic reading list and it does not make a source's pattern mandatory outside
the conditions stated below.

## HTTP semantics and retry safety

Title: HTTP Semantics

Author / Organization: IETF HTTP Working Group

Publication date: 2022-06

Version: RFC 9110 / Internet Standard 97

URL: https://datatracker.ietf.org/doc/rfc9110/

Source type: standard

What it establishes:
HTTP method idempotency concerns intended effect, and clients should not
automatically retry a non-idempotent request unless they know its semantics are
safe or can know it was not applied.

What this skill adopts:
Identify retry ownership and operation semantics before adding retries. Require
an explicit idempotency or outcome-detection mechanism for retryable commands
whose first outcome can be unknown.

What it does NOT establish:
It does not make POST universally unsafe, make PUT safe for every application
side effect, or prove exactly-once delivery through a distributed system.

Numbers taken from source:
None.

Reverify when:
The service uses a non-HTTP protocol or a newer relevant HTTP standard changes
the operational advice.

## API authorization and input control

Title: OWASP API Security Top 10

Author / Organization: OWASP Foundation

Publication date: 2023

Version: 2023 edition

URL: https://api-security.owasp.org/editions/2023/en/0x00-header/

Source type: standard

What it establishes:
Object-level authorization, property-level authorization, resource limits,
business-flow access, configuration, inventory, and unsafe API consumption are
important API risk classes.

What this skill adopts:
Review changed boundaries for object-level authorization, unsafe mass/property
assignment, resource limits, business-flow abuse, and unsafe upstream data.

What it does NOT establish:
It is an awareness and verification aid, not a substitute for a threat model or
proof that every listed risk applies to every endpoint.

Numbers taken from source:
The 2023 edition contains ten risk categories; the skill does not score an API
by how many categories it mentions.

Reverify when:
OWASP publishes a new stable API Security Top 10 edition.

## Application control verification

Title: Application Security Verification Standard

Author / Organization: OWASP Foundation

Publication date: 2025

Version: 5.0.0

URL: https://owasp.org/projects/asvs

Source type: standard

What it establishes:
ASVS provides versioned verification requirements for application controls,
including server-side input validation and authentication/authorization.

What this skill adopts:
Validate untrusted input at a trusted service boundary and use ASVS as a
risk-selected verification reference for security-sensitive backend work.

What it does NOT establish:
It does not prescribe a framework, schema library, migration policy, or a
universal security-complete checklist for all applications.

Numbers taken from source:
Version 5.0.0 is the selected reference version.

Reverify when:
OWASP releases a newer stable ASVS version or the task has regulatory controls
that supersede this baseline.

## PostgreSQL concurrency and migration behavior

Title: PostgreSQL concurrency control and explicit locking documentation

Author / Organization: PostgreSQL Global Development Group

Publication date: 2025

Version: PostgreSQL 17 documentation

URL: https://www.postgresql.org/docs/17/explicit-locking.html

Source type: official docs

What it establishes:
Locks can deadlock, PostgreSQL aborts one transaction to resolve a deadlock,
consistent lock order reduces risk, transactions should stay short, and some
DDL operations acquire strong locks. Serializable work can also require retry
after serialization failure.

What this skill adopts:
Choose isolation and locking from the actual invariant; avoid long transactions;
test contention behavior; retry whole aborted transactions only when their
effects are safe to retry; inspect lock behavior for large-table changes.

What it does NOT establish:
It does not make PostgreSQL-specific lock advice portable to every datastore or
justify serializable isolation for ordinary CRUD.

Numbers taken from source:
None.

Reverify when:
The target datastore, database version, or ORM migration behavior differs from
the observed PostgreSQL case.

## Resilient dependency and event patterns

Title: Circuit Breaker, Retry, and Transactional Outbox patterns

Author / Organization: Microsoft Learn / Azure Architecture Center

Publication date: 2025-2026

Version: Current documentation and sample guidance

URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

Source type: official docs

What it establishes:
Retries and circuit breakers have different roles, retry layers can amplify
failure, and a transactional outbox can atomically record local state plus a
durable event for later at-least-once relay.

What this skill adopts:
Make retry ownership explicit, stop retrying failures that are not transient,
use circuit breaking only where a failing dependency can cascade, and use an
outbox when one durable state change and one published event must not diverge.

What it does NOT establish:
It does not require every service to use a circuit breaker, queue, event bus, or
outbox. Existing platform capabilities can make an application-level pattern
unnecessary.

Numbers taken from source:
None. Thresholds and retry budgets must be derived from the dependency and
service objective, not copied from a pattern example.

Reverify when:
The platform, dependency contract, or delivery mechanism changes.

## Observability vocabulary

Title: OpenTelemetry Semantic Conventions

Author / Organization: OpenTelemetry

Publication date: 2026

Version: 1.44.0

URL: https://opentelemetry.io/docs/specs/semconv/

Source type: official docs

What it establishes:
OpenTelemetry defines evolving semantic conventions for HTTP, database,
messaging, and related telemetry.

What this skill adopts:
Reuse the repository's telemetry conventions and retain enough correlation and
dependency signal to diagnose the changed path without logging raw sensitive
payloads.

What it does NOT establish:
It does not require OpenTelemetry adoption or make every available attribute
useful for every service.

Numbers taken from source:
Version 1.44.0 identifies the reviewed specification snapshot.

Reverify when:
The project changes telemetry stack or a relevant semantic convention evolves.
