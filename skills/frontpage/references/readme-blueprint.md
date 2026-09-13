# README blueprint — the section menu

Not every README needs every section. Pick by project type; order by
reader value.

## Above the fold (mandatory, in this order)

1. **Name + one-line value proposition** — what it is, stated plainly.
   "Fast, offline-first notes app that syncs when it can."
2. **Why it's different** — one or two lines max; comparison detail
   lives further down.
3. **One command to try it** — the copy-paste that gets a working
   example running. If there's no such command yet, the honest v0 says
   what's coming instead of faking it.
4. **The visual** — a screenshot/GIF of the real thing (current build,
   not the 2024 mock), or the skill-map diagram for a bundle. A README
   without a single visual is a wall.

## The menu

| Section | Earns its place when… |
| --- | --- |
| Features | the list is scannable and true — not a feature-dump of aspirations |
| Quick start | install → first success in < 5 minutes; put it high |
| Installation | more than the one-liner: prerequisites, platforms, package managers |
| Usage | real commands with real output; the 80% path first |
| Examples | runnable, tested, linked to files in `/examples` |
| Architecture | the project is non-trivial; link to `docs/architecture/` (blueprint) |
| Configuration | a table: option · default · meaning — generated from the actual config surface |
| Compatibility | only what was tested; versions from CI matrix, not hope |
| Comparison | honest, checkable facts; no invented feature cells for rivals |
| Benchmarks | methodology + numbers you can reproduce; without both, cut it |
| FAQ | the same 3+ questions keep arriving |
| Roadmap | real intent, not wishful marketing |
| Contributing | the repo actually accepts contributions |
| Security | disclosure policy; point at SECURITY.md |
| License | one line + link; the file itself is janitor's check |

## Project-type templates

**CLI/library:** fold → quick start → install → usage → config →
examples → contributing → license.
**Web app:** fold → screenshot/demo → quick start → features → config →
deployment → contributing.
**Skills bundle (like this suite):** fold → the lifecycle map visual →
install one command → per-skill cards/table → compatibility →
principles → FAQ.
**WIP/early:** name → what it is → why → roadmap → "not ready yet,
here's how to follow along". Honesty is the whole brand at this stage.

## Writing rules

- Second person, active voice, present tense: "Run the agent", not "The
  agent can be run".
- One idea per paragraph; scannable beats complete — link out for depth.
- Code blocks specify language; shell examples show expected output
  where success isn't obvious.
- No marketing fog: "blazingly fast" is a claim; "p95 < 80ms (see
  benchmarks)" is a fact. Only one of them is allowed here.
- Versioned claims carry the version: "Requires Node ≥ 20 (tested on
  20.x/22.x)".
- Emojis: at most structural (section markers), never emotional
  decoration.

## The claims audit (walk before shipping)

| Claim type | Valid source |
| --- | --- |
| Version/platform support | manifest engines, CI matrix, executed install |
| Performance numbers | reproducible benchmark, method included |
| Compatibility | tested matrix or explicit "not tested" removal |
| Counts (stars/users/downloads) | live API number, dated — or cut |
| Feature list | demonstrable in the current build |

Every row without a valid source → the claim is cut, not softened.
