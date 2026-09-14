# Which skill do I need?

Start from the sentence you would naturally say. If two rows sound right, use
the first one that removes the uncertainty blocking your next action.

| What you are thinking | Start here | Why |
| --- | --- | --- |
| “I have an idea.” | [`hotseat`](../skills/hotseat/) | Challenge demand, feasibility, UX, security, growth, and maintainability before code. |
| “I know what I want, but my prompt sucks.” | [`distill`](../skills/distill/) | Turn the request into a short, checkable brief. |
| “I don’t understand this repo.” | [`spelunk`](../skills/spelunk/) | Find the real entry points, commands, boundaries, and risky areas. |
| “I’m not sure this API works like I remember.” | [`scout`](../skills/scout/) | Verify the installed version and current primary documentation. |
| “I want a serious implementation plan.” | [`masterplan`](../skills/masterplan/) | Produce file-grounded vertical slices with proof and rollback. |
| “I already have the plan—build it.” | [`pilot`](../skills/pilot/) | Execute one verified slice at a time. |
| “This is backend, data, auth, or jobs work.” | [`backend`](../skills/backend/) | Protect server contracts and cross-stack correctness invariants. |
| “Show me how this system fits together.” | [`blueprint`](../skills/blueprint/) | Document real architecture with useful diagrams. |
| “Can this handle 100k users?” | [`headroom`](../skills/headroom/) | Compare today’s load with future thresholds and migration triggers. |
| “Make this UI actually beautiful.” | [`polish`](../skills/polish/) | Improve hierarchy, tokens, states, responsive behavior, and visual character. |
| “It looks okay, but using it sucks.” | [`friction`](../skills/friction/) | Walk the user’s tasks and remove hesitation, dead ends, and accessibility barriers. |
| “Copy this reference interface.” | [`ditto`](../skills/ditto/) | Inspect, implement, screenshot, compare, and correct. |
| “My AI-coded repo has become disgusting.” | [`unslop`](../skills/unslop/) | Establish a behavior baseline, then clean in safe batches. |
| “Write the right tests.” | [`proof`](../skills/proof/) | Choose the cheapest boundary that catches a real regression. |
| “Does the actual browser flow work?” | [`roadtest`](../skills/roadtest/) | Exercise critical paths and keep screenshots, console, and network evidence. |
| “This bug keeps coming back.” | [`sleuth`](../skills/sleuth/) | Reproduce, compare hypotheses, prove the cause, then add a regression test. |
| “Review this change before I merge.” | [`referee`](../skills/referee/) | Check intent and engineering quality with only actionable findings. |
| “Why is this slow?” | [`hotpath`](../skills/hotpath/) | Measure the hot path and keep only proven gains. |
| “Is this secure?” | [`harden`](../skills/harden/) | Threat-model the actual surface and rank evidenced findings honestly. |
| “Clean up the Git/GitHub side.” | [`janitor`](../skills/janitor/) | Audit history, branches, tags, ignores, templates, Actions, and repository metadata. |
| “This README is embarrassing.” | [`frontpage`](../skills/frontpage/) | Rebuild documentation from repository truth and tested commands. |
| “Will search engines and link previews understand this?” | [`findable`](../skills/findable/) | Verify rendered metadata, crawlability, structure, and social cards. |
| “We’re burning too much context.” | [`frugal`](../skills/frugal/) | Remove waste without lowering the evidence bar. |
| “Is this ready to go live?” | [`cleared`](../skills/cleared/) | Run the final evidence-backed release gate. |
| “Deploy it.” | [`runway`](../skills/runway/) | Preflight, deploy at the safest available rung, and verify the live build. |
| “I keep losing project context.” | [`recall`](../skills/recall/) | Preserve durable facts, decisions, status, and lessons in four small files. |

## Three easy distinctions

- **Looks vs works vs feels:** `polish` owns appearance, `roadtest` owns
  browser correctness, and `friction` owns usability.
- **Broken vs slow vs risky:** `sleuth` diagnoses wrong behavior, `hotpath`
  diagnoses performance, and `harden` diagnoses security exposure.
- **Ready vs deployed:** `cleared` decides whether a release may proceed;
  `runway` performs and verifies the deployment.

## Still do not know?

Run `/concierge`. It inspects what exists and routes only the skills the task
actually needs.
