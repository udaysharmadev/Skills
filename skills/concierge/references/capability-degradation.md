# Capability degradation

When a capability probe fails mid-route, treat the missing capability as
a change in available evidence — not as a reason to fake the action or
abandon the work.

## Capability rungs

Each capability has a degradation ladder. The skill selects the highest
rung actually available and discloses which rung ran.

### Web research

| Rung | Available | Behavior |
| --- | --- | --- |
| A | Web access confirmed | Full search, page fetching, version verification |
| B | No web access | Use local files: lockfile, node_modules, installed types, changelog |
| C | Local files missing | State: "cannot verify external claim — proceeding with stated assumption" |

At rung B/C: mark external claims as `unverified` rather than confident.
The source hierarchy for `scout` applies: local before remote.

### Browser automation

| Rung | Available | Behavior |
| --- | --- | --- |
| A | Browser confirmed | Full navigation, screenshot, network/console capture |
| B | Static files available | Source inspection, link checking, structured output review |
| C | Neither available | State limitation; describe what evidence would be needed; do not fake |

`roadtest` and `ditto` have their own rung logic — consult their SKILL.md
before assuming B/C is always acceptable.

### Subagents

| Rung | Available | Behavior |
| --- | --- | --- |
| A | Subagents confirmed | Full parallel specialist dispatch |
| B | No subagents | Execute specialists sequentially in this context |
| C | Token budget constrained | Route one specialist; surface the rest as follow-up |

At rung B: `hotseat` is most affected. Sequential persona simulation is
a degraded experience — disclose this to the user.

### GitHub CLI (`gh`)

| Rung | Available | Behavior |
| --- | --- | --- |
| A | `gh` available and authenticated | Full PR/issue/repo actions |
| B | `git` only | Local history, branch, status, blame available |
| C | Read-only filesystem | Directory/file inspection only |

`janitor` and `frontpage` note specific fallback steps for each rung.

## Rules

- Never silently run at a lower rung without disclosing it.
- Never manufacture evidence that requires a capability you don't have.
- If the rung drop makes the user's goal unreachable, say so explicitly
  and propose what *can* be done.
- Re-probe once at the start of a new session; capability availability
  can change (e.g., `gh` login, browser tool enabled).

## When a specialist discovers the rung dropped mid-task

1. State which capability is missing.
2. Identify which rung is now available.
3. Propose the fallback action at that rung.
4. Ask for confirmation before reducing fidelity for safety-sensitive actions
   (e.g., `roadtest` dropping from A to B for a production auth flow).
