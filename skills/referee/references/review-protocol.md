# Review protocol: scope a verdict to its evidence

Use this reference for a public contract, persistence, authorization,
concurrency, migration, deployment, or multi-package change. Ordinary bounded
diffs can use the entrypoint and finding format alone.

## Coverage record

Record acceptance criteria, diff range, files read, relevant callers or
consumers searched, tests and commands observed, repository instructions,
runtime surfaces considered, and exclusions. A verdict can be strong inside a
small scope; it must not imply coverage outside that scope.

## Impact map

For each changed boundary, identify only applicable items:

| Boundary | Check |
| --- | --- |
| Public API or event | clients, serialization, docs, versioning, compatibility |
| Data or migration | existing rows, backfill, rollback, ordering, deployment sequence |
| Authorization | identity source, object access, failure disclosure, audit trail |
| Async or retry path | idempotency, timeout, cancellation, duplicate effects, observability |
| Configuration | defaults, overrides, secrets handling, manifests, safe fallback |
| Dependency upgrade | lockfile, supported range, generated code, breaking behavior |

## Evidence policy

State fact when source, diff, test, or reproduction demonstrates it. State
inference when evidence supports but does not prove it. State unknown when the
needed caller, runtime, or configuration is unavailable. Severity follows
consequence and confidence together: a high-consequence possibility can merit
investigation, but should name confirmation needed.

## Review recovery

If criteria, complete diff, history, test output, or consumer code is missing,
list exact missing evidence and its effect on verdict. Do not fill the report
with generic advice. Resume only after evidence arrives or issue a bounded
review that labels the exclusion.

## Root-cause grouping

When locations fail for one reason, report root cause first, affected locations,
and one repair direction. Separate findings only when their fixes or acceptance
consequences differ.
