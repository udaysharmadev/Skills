---
name: concierge
description: First-run setup, capability detection, and routing for this coding-skills bundle. Use when the user runs /concierge, asks what these skills can do in this repository, starts work in a repo where the bundle is installed, or brings a request when it is unclear which skill should own it. Detects the project stack, test/build commands, git state and runtime capabilities (shell, web research, browser automation, subagents, GitHub CLI), then routes to the smallest workflow that solves the request — never the whole suite.
---

# concierge — the dispatcher

You are the front desk. Every other skill in this bundle is a specialist;
your job is to look at the repository once, look at the request, and hand
the user to the smallest set of specialists that can solve it. Running
every skill on every request is the failure mode you exist to prevent.

## When NOT to use

- The request maps directly to one specialist ("research upgrade paths"
  → `scout`). Route immediately; skip detection you don't need.
- You already produced a snapshot for this repository **this session** —
  reuse it. Re-detecting unchanged facts wastes tokens.
- The user is mid-task inside a specialist workflow. Do not interrupt.

## Prerequisites

None. Degrades gracefully: with only filesystem access you still produce
a project snapshot and a routing decision; capability lines simply report
what is unavailable.

## Workflow

### 1. Check for existing memory first

If `PROJECT_CONTEXT.md` and `STATUS.md` exist at the repository root, read
them before detecting anything. They are `recall`'s artifacts and usually
answer most of steps 2–3 for free. Only detect what they don't cover or
what looks stale (see file dates / last entries).

### 2. Project fast-pass (target ≤ 15 tool calls)

Look at, in order, only what exists:

- root manifest/config files (`package.json`, `pyproject.toml`, `go.mod`,
  `Cargo.toml`, `pom.xml`, `build.gradle*`, `Gemfile`, `composer.json`,
  `pubspec.yaml`, or similar);
- lockfile names (for dependency-manager identity, not contents);
- directory listing two levels deep;
- CI config (`.github/workflows/`, `.gitlab-ci.yml`, …);
- `git status` + `git log -5 --oneline` if git is available;
- README first ~40 lines.

Extract: languages, frameworks, package manager, test command, lint/type
command, build/dev command, git state, project maturity (blank / early /
established / legacy mess).

### 3. Capability probes (one probe each, only when about to matter)

| Capability | Probe | Used by |
| --- | --- | --- |
| Shell | `git status` or trivial command | most skills |
| Web research | one search/fetch attempt | `scout` |
| Browser automation | navigate to `about:blank` | future QA skills |
| Subagents | spawn one trivial agent | `hotseat`, review |
| GitHub CLI | `gh auth status` | repo-intelligence tasks |

A capability is "available" only after a successful probe **this session**
— never from memory or assumption. If a probe is unavailable to you, mark
the capability `unknown`, not `no`.

### 4. Emit the snapshot

Output the snapshot block (format below). Hard cap: 30 lines. If it
doesn't fit, cut detail, not honesty.

### 5. Route

Pick the route from `references/routing.md` (read it when the request does
not obviously map to one skill). Announce the route in one line, then hand
off. The specialist does the work; you are done.

## Tool selection / fallback

- Prefer reading memory artifacts over fresh detection (cheapest, and
  exactly what they exist for).
- Prefer one cheap probe over assumptions; prefer `unknown` over guessing.
- If filesystem listing is all you have, still produce the snapshot —
  stack facts from manifests only — and mark runtime capabilities
  `unknown`.

## Quality gates

- Every capability listed was actually probed this session.
- Snapshot ≤ 30 lines and contains zero speculative claims ("probably
  React" → check or omit).
- The route names only skills that are actually installed (if a target
  skill is missing, say so and proceed with what exists).
- Total detection cost stays lean: if step 2 exceeded ~15 tool calls, stop
  and deliver what you have.

## Stop conditions

- Route announced and specialist took over → done.
- User's question was fully answered by the snapshot → done.
- Detection blocked (no filesystem access) → say what's missing, stop.

## Output contract

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
"login is broken" → spelunk (quick) → sleuth* → proof → roadtest*
(* not installed yet — bundle phase 4; proceed with manual equivalents)
```

Artifacts: none written. Memory initialization belongs to `recall`; if the
root memory files are missing, suggest `/recall` once, don't create them
unasked.

## References

- `references/routing.md` — request-pattern → workflow chains, conflict
  rules, and handoff phrasing. Read it before routing anything non-obvious.
