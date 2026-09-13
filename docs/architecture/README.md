# Repository architecture

```text
User request
    ↓
concierge ── detects stack + capabilities ── routes to smallest workflow
    ↓
specialists run self-contained (each skills/<name>/ works when copied alone)
    ↓
artifacts land in owned locations (docs/*, root memory files)
    ↓
recall persists decisions; other skills read them by convention
```

## Invariants

1. **Self-containment** — `skills/<name>/` has no runtime dependency on
   sibling skills or on `shared/`. Cross-skill references are slug names.
2. **One owner per artifact** — see `shared/terminology/artifacts.md`.
3. **Capability ladder** — every skill states its fallback when a
   capability (browser, web, subagents, shell) is missing; outputs say
   which route ran. See `shared/capability-map/README.md`.
4. **Gates over loops** — specialists never recursively launch large
   workflows; only orchestrators compose specialists (PRD §4).

This file is hand-maintained narrative. The generated skill index lives at
`docs/skills/INDEX.md` (via `scripts/build-docs`).
