# Slop catalog — what to hunt, where it hides, why it costs

Ranked by how often it wrecks vibe-coded projects. Evidence rule applies
to every entry: file:line or it isn't a finding.

## Correctness-adjacent (usually Critical)

- **Swallowed errors** — empty catch blocks, `.catch(() => {})`,
  `except: pass`, errors logged then ignored. The bug you can't see is
  the one that ships.
- **Duplicated schemas/models** — the same entity defined in 3 places
  (DB schema, API type, frontend interface) already drifting apart. One
  change updates one copy; production disagrees.
- **Dead auth/validation paths** — checks that never run (middleware
  mounted on a route that bypasses it, client-side-only validation for
  money math).
- **Copy-pasted logic with a "fix" in one copy** — the pagination bug
  exists twice; someone fixed one instance.

## Structural (usually High leverage)

- **Mega-components / god-files** — a 2,000-line React component or
  1,500-line service file holding five responsibilities. Split by the
  seams that already exist, not by a new architecture.
- **Duplicated logic** — the same transformation in several files;
  consolidate toward one home.
- **Premature abstractions** — base classes with one subclass, strategy
  patterns with one strategy, "flexible" config for one use. Inline
  them; add abstraction when the second real case appears.
- **Needless indirection** — wrapper-of-wrapper calls, event buses for
  two listeners, "managers" that manage nothing. Flatten.
- **Giant utility files** — `utils.ts` as a landfill; split by domain or
  dissolve into actual modules.

## Dead weight (usually Medium)

- **Dead code** — unreachable branches, functions nothing calls
  (verified by search, not vibes), feature-flag remnants.
- **Abandoned files** — `new_version_final_v2.ts`, half-migrated
  modules, `old/` directories that linger.
- **Unused dependencies** — imports gone, packages remain (check the
  lockfile truth, and dev-vs-runtime distinction).
- **Stale comments** — describing code that no longer exists; comment
  blocks from a previous architecture.
- **Debugging leftovers** — `console.log("HERE")`, commented-out
  experiments, hardcoded test tokens (also a `harden` finding).
- **Scattered config** — the same constant in five files; env vars read
  in random modules.

## Generated-slop signatures (Medium unless structural)

- **Type escape hatches** — `any`-cascades, `as unknown as X`, `@ts-ignore`
  clusters where the types were hard instead of wrong.
- **Inconsistent naming for the same concept** — `user`/`account`/
  `profile` interchangeably; pick per the domain, align gradually.
- **Inconsistent patterns** — three data-fetching styles, two state
  systems, four ways to show a loading spinner. Standardize on one,
  migrate in batches.
- **Card-grid UI slop / decorative junk** → `polish`'s territory; note
  it, route it.
- **Hallucination residue** — references to packages that were never
  installed, APIs that don't exist (guarded by `try/catch` so "it
  works"), dead endpoints still called.

## The "keep it" list (slop that's load-bearing)

- Quirks other code depends on (a "wrong" sort order the UI assumes).
- Vendored/generated code — flag the convention, don't hand-edit
  generated files.
- Migration paths mid-flight (old + new coexisting on purpose).

Record these in the report as **kept — load-bearing**, or the next
well-meaning cleanup will break them.
