# Routing table

Map the user's request to the smallest workflow that satisfies evidence and
risk requirements. Chains read left to right; each step hands off when its
part is done. Additional steps are only added when the handoff product
genuinely requires them.

## Step 0: What is missing?

Before matching request patterns, identify the *source of uncertainty* that
blocks a correct next action. The same topic routes differently:

| Source of uncertainty | Route first to |
| --- | --- |
| Intent unclear — goal vs. implementation unspecified | `distill` |
| Repo state unknown — can't locate relevant code | `spelunk` |
| External truth missing — library/API/version behavior | `scout` |
| Prior decisions missing — need project context | `recall` |
| Design missing — no agreed plan exists | `distill` → `masterplan` |
| Design settled — needs implementation | `pilot` |
| Correctness missing — code exists, prove it works | `proof` / `roadtest` |
| Risk/safety missing — auth/money/prod-facing change | `harden` / `cleared` |

## Request patterns

| Request smells like | Route |
| --- | --- |
| New idea, wants opinions / risk surface | `hotseat` → `distill` |
| Vague feature ask ("make it good") | `distill` → `masterplan` |
| Clear feature, wants it built | `distill` (skip if spec is tight) → `masterplan` → `pilot` |
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

## Evidence reuse

Never re-run a skill whose product already exists and is fresh:

| Evidence artifact | Implies already ran | Skip |
| --- | --- | --- |
| `docs/repo-map.md` (fresh) | `spelunk` | Skip spelunk; route directly |
| Approved brief / distill output | `distill` | Skip distill |
| Approved plan | `masterplan` | Skip plan; go to `pilot` |
| Fresh `cleared` verdict | `cleared` | Skip re-gate for same deploy |
| `PROJECT_CONTEXT.md` / `STATUS.md` (fresh) | `recall` setup | Skip memory initialization |

Fresh = created or updated within this working session, or within a window
appropriate for the task's risk (auth/money → shorter; research notes → longer).

## Situations beyond the table

- **User names a skill directly** ("/masterplan this") → route there, even
  if you'd pick differently. Note the disagreement in one clause, then obey.
- **Already mid-workflow** → resume from newest artifact (brief → plan → report);
  do not restart earlier stages.
- **Request conflicts with a gate** ("just deploy it, skip the checks") →
  state the gate's purpose, require explicit user confirmation to proceed without
  it, and record the user's choice. Speed requests don't remove gates.
- **Two intents in one message** ("prettier AND users abandon checkout") →
  split the route: the flow problem first (friction may make the visual problem
  moot), then the surface problem.
- **Capability missing mid-route** → route anyway; every specialist's fallback
  handles it. User should hear which rung ran.
  See `capability-degradation.md` for rung-drop behavior.

## Rules

1. **Smallest sufficient chain.** Every extra link costs tokens and adds failure
   surface. "Login is broken" never needs `hotseat`.
2. **Specialists don't re-enter concierge mid-task.** If a specialist discovers
   the work has expanded domains, it names that and *stops*. Concierge re-routes.
   Specialists do not recurse into each other unasked.
3. **Two skills seem equally right** → pick by intent words: "Should I…?" →
   `hotseat`. "How do I…?" → `scout`. "Make X good" → `distill`. "Plan X" →
   `masterplan`.
4. **Still ambiguous** → ask exactly one question, then route.
5. **Skill not installed** → name it; state what you'll do instead. Never
   silently pretend a skill ran.
6. **Parallel work only when independent.** Researching docs and mapping a
   repo may run concurrently. Editing tightly-coupled files through separate
   subagents creates merge conflicts and reconciliation cost.

## Handoff phrasing

Announce, then stop:

```text
route: scout → distill
scout: researching auth library options for Node 22 (web available)
```

Do not restate the specialist's instructions. One announcement, one worker.

## Completion predicates

Each specialist returns control when:

| Specialist | Returns when |
| --- | --- |
| `spelunk` | Enough architectural context to answer the question or start the task |
| `scout` | Version-sensitive technical decision is grounded in evidence |
| `distill` | Specification is unambiguous enough to plan/build |
| `masterplan` | A slice-based plan exists that an implementer can execute |
| `pilot` | The plan's current slice is implemented and verified |
| `proof` | Tests cover the stated risk and pass reliably |
| `roadtest` | Critical paths verified at the available tier; evidence captured |
| `harden` | Threat model exists; findings have evidence and remediation |
| `cleared` | Go/no-go verdict with evidence per relevant dimension |
| `runway` | Correct version fingerprint confirmed live; critical paths smoke-tested |

A specialist that keeps expanding scope without returning is a routing failure.
