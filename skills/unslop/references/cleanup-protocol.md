# Cleanup protocol: prove the change is smaller than its risk

Use this reference for a structural batch, any candidate with uncertain
reachability, or a batch that failed verification. It is not a ceremony for an
obvious, mechanically verified deletion.

## Candidate record

Capture one row before editing:

| Field | Required evidence |
| --- | --- |
| Candidate | precise path and symbol or dependency name |
| Claimed status | dead, duplicated, leaky abstraction, or stale artifact |
| Protected invariant | behavior that must remain unchanged |
| Reachability search | imports, registrations, configuration, build entrypoints, tests, docs, and dynamic mechanisms inspected |
| Risk | public surface, data, security, lifecycle, or toolchain concern |
| Batch decision | ship, defer, keep, or hand off, with why |

For a dependency, distinguish direct import, transitive install, build plugin,
code generator, runtime optional peer, and documented user requirement. A zero
text-search result does not prove it is unused.

## Choose the smallest safe transformation

| Evidence | Preferred action | Avoid |
| --- | --- | --- |
| Proven unreachable code with a passing baseline | delete the smallest complete unit | leaving a commented copy |
| Duplicate, stable implementation | consolidate only the shared behavior | redesigning every caller at once |
| One-use pass-through abstraction | inline or delete after checking error and lifecycle behavior | adding a new abstraction to replace it |
| Large mixed-responsibility unit | move one existing seam with compatibility imports if needed | a directory-wide rewrite |
| Ambiguous dynamic path | keep and document uncertainty | deleting from search absence |
| Generated or vendored artifact | use its generator or owner workflow | manual cleanup |

## Dynamic reachability checklist

Search the mechanisms that exist in the repository, not every item blindly:

- route, command, plugin, task, migration, event, and dependency injection
  registrations;
- string-key lookup, reflection, serialization names, templates, generated
  imports, and configuration-selected modules;
- package scripts, build configuration, deployment manifests, and CI jobs;
- public documentation, examples, and extension points that users may copy.

When the repository supports it, add a temporary targeted observation such as a
test fixture, route enumeration, coverage run, or build graph query. Remove a
temporary probe if it is not a lasting useful test.

## Invariants by transformation

| Change | Protect at minimum |
| --- | --- |
| Merge duplication | input normalization, output shape, error behavior, ordering, and side effects |
| Delete dependency | clean install, build, runtime startup, and the relevant production bundle or image |
| Collapse wrapper | retries, timeouts, cancellation, logging, auth context, and metrics behavior |
| Split a module | public import paths, initialization order, type boundaries, and circular dependency behavior |
| Remove stale configuration | defaults, environment override precedence, deployment manifests, and rollback path |

## Failed-batch response

1. Stop at the first unexpected signal; do not stack another cleanup on it.
2. Save the exact command, error, and candidate record beside the batch log.
3. Determine whether the failure was present in the baseline. If unknown, say
   unknown rather than assigning blame.
4. Revert or isolate the batch, then classify the violated assumption.
5. Keep the finding deferred unless a separately authorized behavioral fix is
   warranted.

## Good report language

- Shipped: the unused adapter had no static or registered dynamic callers; the
  same targeted tests and build passed.
- Deferred: no direct imports exist, but the plugin loader resolves names from
  configuration that could be user-provided; no deletion made.
- Kept: the apparent duplicate implements an older wire version and is an
  intentional compatibility boundary.

Do not claim code is dead because it looks old, code is duplicate because names
match, or behavior is preserved because a formatter ran.
