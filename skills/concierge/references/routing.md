# Routing table

Map the user's request to the smallest workflow. Chains read left to
right; each step hands off when its part is done. All 27 skills in
this bundle are installed together; if a target skill is missing, the
user installed a subset — say so and proceed with the manual equivalent.

## Request patterns

| Request smells like | Route |
| --- | --- |
| New idea, wants opinions / validation | `hotseat` → `distill` |
| Vague feature ask ("make it good") | `distill` → `masterplan` |
| Clear feature, wants it built | `distill` (skip if spec is already tight) → `masterplan` → `pilot` |
| "How does this repo work" / new to codebase | `spelunk` |
| Library/API/framework question | `scout` |
| "What did we decide" / "catch me up" | `recall` |
| Bug report | `spelunk` (quick) → `sleuth` → `proof` |
| Something is slow | `hotpath` |
| Security ask / handles auth, money, PII | `harden` |
| Review this code / diff / PR | `referee` |
| Add or improve tests | `proof` |
| Verify it works in the browser | `roadtest` |
| UI looks generic / "make it pretty" | `polish` → `friction` → `roadtest` |
| Confusing flows / accessibility | `friction` |
| Copy this design (screenshot/URL) | `ditto` |
| Architecture docs / diagrams | `blueprint` |
| "Will it scale" / architecture choice | `headroom` |
| Backend / API / data work | `backend` |
| "My repo is a mess, help" | `unslop` |
| Git / GitHub hygiene, commit messages | `janitor` |
| README / docs for the project | `frontpage` |
| SEO / discoverability / social previews | `findable` |
| Token usage / context costs too high | `frugal` |
| "Are we ready to ship / go live" | `cleared` |
| Deploy this (any platform) | `runway` |
| Before context reset / handoff | `recall` (session delta) |

## Rules

1. **Smallest sufficient chain.** Every extra link costs tokens and adds
   failure surface. "Login is broken" never needs `hotseat`.
2. **Specialists don't compose.** If a specialist seems to need another
   specialist, that's a signal to come back here — or more often, to just
   do the small extra step inline.
3. **Two skills seem equally right** → pick by the user's *intent words*,
   not the topic. "Should I…?" → `hotseat`. "How do I…?" → `scout`.
   "Make X good" → `distill`. "Plan X" → `masterplan`.
4. **Still ambiguous after intent words** → ask exactly one question
   ("want a critique of the idea, or a plan to build it?"), then route.
5. **Route to a skill that isn't installed** → name it, mark it (planned),
   and state what you'll do instead. Never silently pretend a skill ran.

## Handoff phrasing

Announce, then get out of the way:

```text
route: scout → distill
scout: researching current best practice for auth libraries (web available)
```

Do not restate the specialist's instructions, and do not shadow it — one
announcer, one worker.
