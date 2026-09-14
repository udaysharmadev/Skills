# Workflow recipes

Skills compose through small, explicit handoffs. These recipes are examples,
not rituals: skip any step whose output already exists or whose question is not
blocking the work.

## Build from an idea

```text
hotseat
→ distill
→ scout, only where an external choice needs current evidence
→ masterplan
→ pilot
→ proof
→ roadtest, where a UI exists
→ referee
→ cleared
→ runway
→ recall, for decisions worth keeping
```

The idea is challenged before it becomes scope. The brief fixes what “done”
means; research resolves unstable external facts; the plan becomes verified
slices. Testing, browser evidence, and independent review precede the release
gate. Deployment is a separate act, and only durable decisions enter memory.

## Rescue vibe-coded spaghetti

```text
spelunk → unslop → proof → referee
```

First map what is load-bearing. Then establish a behavior baseline and remove
accidental complexity in small batches. Tests protect the result; review catches
cleanup that quietly changed intent. Use `polish` separately if the mess is
visual rather than structural.

## Fix a hard bug

```text
sleuth → proof → roadtest, if the trigger is browser-dependent
```

Diagnosis produces a failing signal and a causal chain. `proof` turns that
signal into permanent regression protection. `roadtest` is earned only when the
browser is part of the mechanism or the user-visible verification.

## Build a polished frontend

```text
polish → friction → roadtest
```

Visual hierarchy and component states come first. The novice and expert task
walk then tests whether the interface is usable, not merely attractive. The
final browser pass proves the critical paths, console, network, and viewports.

If the task is “match this screenshot,” replace `polish` with `ditto`.

## Prepare an open-source launch

```text
janitor → frontpage → findable → cleared
```

Repository truth and hygiene come before the landing page. `frontpage` turns
that truth into documentation; `findable` handles machine-readable discovery
where a public site exists; `cleared` checks the applicable release dimensions.

## Review architecture

```text
spelunk → blueprint → headroom
```

`spelunk` maps what exists. `blueprint` makes the current boundaries and flows
legible. `headroom` evaluates what should change at measured thresholds. Do not
draw the future as if it already exists.

## Change a backend contract safely

```text
scout, if the framework/API behavior is version-sensitive
→ backend
→ proof
→ harden, for auth/data/trust-boundary changes
→ referee
```

Current external facts are pinned before code. Backend invariants guide the
implementation, tests sit at the contract boundary, security reviews the
changed attack surface, and review checks consumers and migration safety.

## When one skill is enough

- A precise library question: `scout`.
- A readable map of an unfamiliar repo: `spelunk`.
- A commit message from an already-staged diff: `janitor`.
- A performance investigation with no planned refactor: `hotpath`.
- A final readiness decision without deployment: `cleared`.
- A session handoff with durable decisions: `recall`.

The smallest sufficient workflow is a design rule. More specialists do not
automatically mean a better result.

## Autonomous execution

```text
handsfree + pilot
handsfree + sleuth
handsfree + unslop
```

When you already know what needs to be built, fixed, or cleaned up, and you do not want the agent to stop for permission to run tests, inspect files, or make routine engineering decisions. The workflow runs continuously until it hits a human-level product decision, a destructive risk, or completion.
