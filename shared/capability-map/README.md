# Capability map (canonical)

How every skill detects what it can use, and what it does when something is
missing. Skills inline the rows relevant to them.

## Detection order

Detect lazily, on first need — not at skill load. Detection itself must be
cheap (one probe, not five).

## The ladder

**use project-native → use already-installed tool → use tiny bundled helper
→ recommend optional tool → manual fallback**

## Capability tiers

| Capability | Probe | With it | Without it |
| --- | --- | --- | --- |
| Shell/exec | run a trivial command (`git status`) | builds, tests, git, scanners | static inspection only; outputs marked unverified |
| Web research | one search/fetch | primary-source research (`scout`) | offline research from lockfiles/vendored sources, clearly labeled limited |
| Browser automation | navigate to a blank page | `roadtest`-style flows, screenshots, console/network evidence | HTTP-level checks or static inspection; browser behavior marked unverified |
| Subagents | spawn one trivial agent | independent parallel passes (`hotseat` personas, `referee` fresh context) | sequential simulation with explicit anti-anchoring discipline |
| GitHub CLI | `gh auth status` | repo/PR analysis (`janitor`) | local git only; remote analysis skipped, not guessed |
| Filesystem write | create/remove a temp file | artifacts, fixes | propose exact diffs/patches for the user to apply |

## Honesty rules

1. A capability is "available" only after a successful probe this session —
   never because a previous session or the model's memory says so.
2. If a fallback ran instead of the preferred route, the output says which
   route ran.
3. No runtime may hallucinate performing an unavailable action (Agent
   Skills portability contract, PRD §10 — Tier C skills still fail
   gracefully).

## Portability grades (PRD §10)

- **Tier A — fully portable:** filesystem/search/shell only.
- **Tier B — portable with enhancement:** works everywhere, better with
  browser/web/subagents.
- **Tier C — capability-dependent:** primary function needs a capability
  (e.g. real browser interaction), and must degrade to a clearly-labeled
  static fallback.
