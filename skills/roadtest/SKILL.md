---
name: roadtest
description: Verifies the application in a real browser the way a user would use it — critical-path walks with evidence. Use when UI changes need verification, before release, when the user says check it in the browser, does it actually work, or test the flow, or when anything browser-dependent must be proven beyond reading code. Walks critical paths, captures screenshots, console errors, failed network calls and responsive behavior, and reports every result with evidence. Without browser capability it says exactly that and marks browser behavior unverified — it never pretends.
---

# roadtest — use the app like a user, prove what you saw

Reading code is not using the app. You drive the real thing through its
critical paths and return **evidence**, not impressions: screenshots,
console output, network failures, pass/fail per path. This is a Tier C
capability-dependent skill — without a browser it degrades to explicit
honesty, never to imagination.

## When NOT to use

- Pure logic/data verification → `proof` at the right boundary (faster,
  less flaky).
- Slow-but-correct behavior → `hotpath`.
- How it looks → `polish`; how it feels → `friction`. You answer "does
  it work when a human uses it".

## Capability ladder (state which rung ran)

1. **Browser automation** (full skill) — navigate, interact, inspect
   console/network, screenshot, responsive.
2. **HTTP-level** (no browser) — endpoints exercised directly: status
   codes, payloads, auth behavior. UI behavior **unverified**.
3. **Static inspection** (nothing runs) — code reading only; everything
   dynamic marked **unverified**.

The report's first line names the rung. Rung 2/3 never phrase results
as if the UI was exercised.

## Prerequisites

A runnable app (start command from the repo/PROJECT_CONTEXT) and browser
tooling. No browser tooling → drop to rung 2 and say so. App won't
start → that's finding #1; report the blocker with its error output.

## Critical-path walk (per path)

For each critical path (login, the money flow, the core CRUD loop —
named explicitly before starting):

1. start the application;
2. wait for healthy state (don't test a half-booted app);
3. open the browser at the entry URL;
4. navigate like a user (real clicks/keys, not URL-hacking past state);
5. interact: forms, buttons, navigation — including the wrong-way
   attempt (bad input, back button mid-flow);
6. inspect the rendered result — what actually appeared;
7. inspect the console — **any error is a finding**, warnings assessed;
8. inspect failed network calls — 4xx/5xx, CORS, aborted requests;
9. verify responsive states at ≥ 2 viewports (desktop + 390px phone);
10. capture evidence at each meaningful step (see bundle format);
11. on failure: stop, capture, fix (or route to `pilot`/`sleuth`),
    re-walk;
12. repeat until the path passes or is reported failing.

## The evidence bundle

Format and storage in `references/evidence-bundle.md` — one directory
per run under `docs/reports/roadtest-<slug>/`: per-path result lines,
screenshots, console/network excerpts, environment (URL, viewport,
timestamp). The bundle is the deliverable; claims reference their
evidence files.

## Rules

- **Console errors are failures**, not noise — a flow that "worked" with
  three unhandled rejections is a failing flow.
- **Network failures are failures** — including ones the UI silently
  swallowed.
- Screenshots at the moment of assertion, not after a "refresh until it
  looks right".
- Fresh state per path (new session/storage) unless the path is
  specifically about persistence.
- Don't test what can't run: mark it unverified with the reason.

## Quality gates

- Critical paths named before walking; every one has pass/fail + evidence.
- Console and network inspected on every path (the two things users
  can't see but always feel).
- Responsive checked at ≥ 2 viewports per path.
- Every claim in the report maps to an evidence file; rung 2/3 reports
  contain zero UI-behavior claims.

## Stop conditions

- All paths passed, bundle saved → report, stop.
- A path fails and the fix belongs to implementation → capture evidence,
  route to `pilot`/`sleuth`, re-walk after, stop when green or when
  blocked.
- No browser, app unstartable, or login unavailable → rung 2 at best,
  everything UI marked unverified, name exactly what's missing.

## Output contract

Chat: rung declaration, per-path table (path · result · key evidence),
findings list (console/network/responsive), blockers. On disk: the
evidence bundle under `docs/reports/roadtest-<slug>/`.
