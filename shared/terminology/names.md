# Naming system (canonical)

Copied from PRD §16. Enforced mechanically by `scripts/check-names`.

## Six rules

1. **Short** — one word. Two only when a single word genuinely cannot carry
   the meaning.
2. **Understandable** — a real word developers already use for the job
   (`polish`, `proof`, `harden`, `recall`).
3. **Memorable** — `polish` > `comprehensive-frontend-design-improvement`.
4. **Personality** — the energy of `ponytail`, `not-ai`, `archify`,
   `grill-me`, `impeccable`. Those exact names are taken; steal the energy,
   never the words.
5. **Consistent** — single lowercase words across the suite, `^[a-z][a-z0-9]+$`.
6. **Ownable** — no exact name already established by a popular
   skill/project.

## The v1 twenty-seven

`concierge` `hotseat` `spelunk` `scout` `distill` `masterplan` `pilot` `recall`
`blueprint` `headroom` `polish` `friction` `ditto` `unslop` `backend`
`roadtest` `harden` `sleuth` `proof` `referee` `hotpath` `janitor`
`frontpage` `findable` `frugal` `cleared` `runway`

## Collision watchlist (higher-risk slugs)

Single common words trade ownability for style. These have known namesakes
in adjacent spaces and get extra scrutiny in the final audit:

| Slug | Known namesake | Risk |
| --- | --- | --- |
| `runway` | RunwayML (AI video) | different category, moderate |
| `blueprint` | Laravel Blueprint, blueprintjs | different ecosystems, moderate |
| `sleuth` | The Sleuth Kit (forensics) | different domain, moderate |
| `frugal` | FrugalGPT (paper) | different category, low |
| `ditto` | DittoLive (sync) | different domain, low |
| `pilot` | generic word | low |

## Pre-approved alternates

If the final exact-name audit kills a primary, swap in its alternate rather
than inventing a new name ad hoc:

- `blueprint` → `birdseye`
- `runway` → `liftoff`
- `frugal` → `thrifty`
- `sleuth` → `autopsy`
- `ditto` → `mimic`
- `headroom` → `capacity`
- `janitor` → `steward`
- `distill` → `sharpen`
- `referee` → `crosscheck`
- `cleared` → `greenlight`
- `spelunk` → `deepdive`
- `recall` → `elephant`
- `hotseat` → `warroom`

## Final audit protocol (before any public folder freezes)

Fresh exact-name check against: GitHub repositories, GitHub code search for
`SKILL.md`, skills.sh, and the major Agent Skills mirrors. Only then freeze.
