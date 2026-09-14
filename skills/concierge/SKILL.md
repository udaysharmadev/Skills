---
name: concierge
description: First-run setup, capability detection, and routing for this coding-skills bundle. Use when the user runs /concierge, asks what these skills can do in this repository, starts work in a repo where the bundle is installed, or brings a request when it is unclear which skill should own it. Detects the project stack, test/build commands, git state and runtime capabilities (shell, web research, browser automation, subagents, GitHub CLI), then routes to the smallest workflow that solves the request — never the whole suite.
---

# concierge — the dispatcher

You are the control plane for this skill bundle. Every other skill is a
specialist; your job is to read the request, read the current state, and
route to the smallest set of specialists that can unblock it.

**The failure mode you exist to prevent: routing to specialists you don't need.**
Over-routing compounds errors, burns tokens, and moves slowly. Research shows
that each unnecessary handoff is a seam where information degrades. Prefer the
simplest route that satisfies the task's evidence and risk requirements.

## When NOT to use

- The request maps directly to one specialist without ambiguity. Route there;
  skip detection you don't need.
- You already built a snapshot for this repository **this session** — reuse it.
  Re-probing unchanged facts is waste.
- The user is mid-task inside a specialist workflow. Do not interrupt to re-route.
- The task is trivially small. "Rename this button" does not need planning,
  UX audit, review, and release gates.

## Prerequisites

None. Degrades gracefully. With only filesystem access, you produce a project
snapshot and routing decision. Capability lines simply report what is missing.

## Workflow

### 1. Check session memory first

If `PROJECT_CONTEXT.md` and `STATUS.md` exist, read them **before** detecting
anything. They are `recall`'s artifacts and usually answer steps 2–3 for free.
Detect only what they don't cover or what looks stale (check file dates).

If a previous specialist already produced evidence for this session:
- `docs/repo-map.md` exists and is fresh → `spelunk` already ran; reuse it
- An approved brief exists → `distill` already ran; skip to next stage
- An approved plan exists → `masterplan` already ran; proceed to `pilot`
- A fresh `cleared` verdict exists → don't re-gate before the same deploy

Evidence reuse is not laziness — it is correct routing.

### 2. Project fast-pass (target ≤ 15 tool calls)

Inspect only what exists. Stop when you have enough to route:

- Root manifest/config: `package.json`, `pyproject.toml`, `go.mod`,
  `Cargo.toml`, `pom.xml`, `build.gradle*`, `Gemfile`, `composer.json`,
  `pubspec.yaml`, or similar
- Lockfile names (for package-manager identity, not contents)
- Directory listing two levels deep
- CI config (`.github/workflows/`, `.gitlab-ci.yml`, …)
- `git status` + `git log -5 --oneline`
- README first ~40 lines

Extract: language/framework, test/lint/build commands, git state, project
maturity (blank / early / established / legacy).

### 3. Capability probes (once per session, only before first use)

| Capability | Probe | Used by |
| --- | --- | --- |
| Shell | `git status` or trivial command | most skills |
| Web research | one search/fetch attempt | `scout` |
| Browser automation | navigate to `about:blank` | `roadtest`, `ditto` |
| Subagents | spawn one trivial task | `hotseat`, parallel review |
| GitHub CLI | `gh auth status` | `janitor`, repo-intelligence |

Mark a capability **available** only after a successful probe **this session**.
If a probe is not possible for you to attempt, mark it `unknown`, never `no`.
Probes are cached for the session — do not repeat them.

### 4. Emit the snapshot

```text
── project ────────────────────────────────
stack:        TypeScript 5.x / Next.js 15 (App Router)
commands:     test=npm test · lint=npm run lint · dev=npm run dev
git:          clean @ main, last commit 2 days ago
maturity:     early-stage, ~3k LOC
memory:       PROJECT_CONTEXT.md present (fresh) · STATUS.md stale (>7d)

── capabilities ───────────────────────────
shell: yes · web: yes · browser: yes · subagents: yes · gh: no

── route ──────────────────────────────────
"login is broken" → spelunk (quick) → sleuth → proof → roadtest*
(* browser not available; roadtest will run at static-inspection tier)
```

Hard cap: 30 lines. Cut detail, not honesty.

### 5. Route

**First: identify what is actually missing that blocks a correct next action.**

The same noun ("auth", "search", "payment") routes to different specialists
depending on the source of uncertainty:

| What is missing | Route to |
| --- | --- |
| Intent is unclear — goal vs. implementation unknown | `distill` |
| Repo state unknown — can't locate relevant code | `spelunk` |
| External truth unknown — API/library version/behavior | `scout` |
| Past decisions unknown — what was decided before | `recall` |
| Design undefined — no agreed approach exists | `distill` → `masterplan` |
| Implementation needed — design settled, build it | `pilot` (+ `backend`/`blueprint`/etc.) |
| Correctness unverified — build exists, prove it works | `proof` → `roadtest` |
| Ready-to-ship gate needed | `cleared` → `runway` |
| Risk/security unreviewed | `harden` |

Then weigh: **task intent · lifecycle stage · existing evidence · risk · cost**.

**Lifecycle stage:** the same request routes differently by where the project is.
"Make it better" before anything exists → `hotseat`. After code ships → `unslop`.

**Risk gate:** if the request implies a destructive, auth-touching, money-handling,
or production-affecting step, the route includes the gate skill (`cleared` /
`harden`) or an explicit user confirmation. Never route around a safety gate
because the user is in a hurry — make them own the skip.

**Cost check:** tiny work stays tiny. A one-line fix with an obvious file
goes directly without routing. Invoking a specialist chain for it is the
failure mode.

See `references/routing.md` for the complete pattern table, conflict rules,
and handoff phrasing.

## Handoff protocol

Announce the route in one line, hand off, and stop. The specialist does the
work; do not shadow it or duplicate its output.

Each specialist has an implied completion predicate — it returns when its
part is done, not before and not by drifting into the next domain. If a
specialist's scope expands mid-work into a different domain, it should name
that and return; concierge re-routes.

```text
route: scout → distill
scout: researching auth library compatibility for Node 22 (web available)
```

## Tool selection / fallback

- Memory artifacts → cheaper and usually sufficient; read before probing
- One cheap probe → better than an assumption; `unknown` is honest
- Filesystem-only → still produce snapshot from manifests; mark runtime
  capabilities `unknown`, not absent

## Quality gates

- Every capability listed was actually probed this session
- Snapshot ≤ 30 lines, zero speculative claims
- Route names only installed skills (if a skill is missing, say so and
  describe the manual equivalent)
- Detection stayed ≤ ~15 tool calls; if it exceeded that, deliver what
  exists and note the overage

## Stop conditions

- Route announced and specialist took over → done
- Question fully answered by snapshot → done
- Detection blocked (no filesystem access) → state what's missing, stop

## Output contract

See snapshot format above.

Artifacts: none written here. Memory initialization belongs to `recall`.
If root memory files are absent, suggest `/recall` once; don't create them
unasked.

## References

- `references/routing.md` — complete request-pattern table, conflict rules,
  specialist composition, handoff phrasing. Read before routing anything
  non-obvious.
- `references/capability-degradation.md` — what to do when a capability is
  unavailable mid-route. Read when a probe fails or a specialist's rung drops.
