---
name: friction
description: Audits and improves UX end-to-end — whether a real person can actually complete tasks, not whether the UI looks good. Use when the user mentions UX, usability, onboarding, confusing flows, form friction, bad error messages, empty states, keyboard or accessibility problems, or asks to improve how something feels to use. Covers information architecture, navigation, task completion, forms and validation, error recovery, destructive-action safety, feedback, keyboard use, focus and WCAG 2.2 accessibility. Automated axe checks complement but never replace manual review.
---

# friction — can a real person actually use this?

UI asks "does it look good?" — that's `polish`. You ask "where does the
user hesitate, backtrack, or give up?" A beautiful app with a checkout
that loses people is a failed app.

## When NOT to use

- Pure visual styling → `polish`.
- Automated test coverage of flows → `roadtest`; you
  may use browser tooling, but your product is the audit.
- A bug where the intended behavior doesn't work at all → that's a bug
  hunt, not friction.

## Prerequisites

The real task(s): what is a user actually trying to get done? If the
product's top tasks aren't obvious, ask — an audit without tasks grades
decoration. Browser access helps enormously (you can walk flows like a
user); without it, audit via code + screenshots and mark what's
unverified.

## Workflow

### 1. Name the top tasks

The 3 things a user must accomplish (sign up → create first X → share/return,
or whatever fits). Rank findings by their effect on these.

### 2. Walk each task twice

- **Novice walk:** first time, no knowledge — where do I start? What does
  this button do? Where do I hesitate? What happens if I do the wrong
  thing?
- **Expert path:** can a returning user do it fast — keyboard shortcuts,
  sensible defaults, no forced re-entry of known information?

Note every stumble point with its exact location.

### 3. Audit the dimensions

Read `references/usability-checklist.md` and walk the applicable
sections: information architecture, navigation, forms and validation,
error recovery, destructive-action safety, feedback and latency
perception, keyboard/focus, touch, copy. Fix-the-system findings (a
validation pattern wrong everywhere) beat fix-the-instance ones.

### 4. Accessibility pass

WCAG 2.2 is the primary reference — focus visibility, target sizes,
labels, contrast, motion, reflow. When Playwright + axe are available,
run them: axe findings are a floor, not a ceiling — automated checks
cannot find every issue, so they complement the manual walk, never
replace it.

### 5. Classify, then rank

Name the **concern** per finding — they have different owners and fixes:

- **usability** — task completion, flow, feedback (this skill's core);
- **accessibility** — WCAG failures (may be legal/contractual, fix
  regardless of usage data);
- **visual design** — aesthetic problems belong to `polish`; reference,
  don't own;
- **conversion/product** — drop-off from positioning, pricing, value
  clarity — these route to product decisions, not UI fixes.

Do not call every UI problem UX. Then rank:

- **Blocker** — the task cannot be completed (dead end, lost data,
  unrecoverable error).
- **Major** — hesitation, backtrack, or a wrong guess users will make.
- **Minor** — friction an expert route around.

Fix blockers and majors (directly, or as slices for `pilot`), then
**re-walk the task** to confirm the path is actually smoother — the
fix is verified by the walk, not by the intention.

## The judgment calls that matter

- **Destructive actions** get confirmation proportional to damage, and
  undo where possible — "Are you sure?" on a settings toggle is friction;
  one-click permanent deletion of work is malpractice.
- **Latency is UX** — perceived speed (optimistic UI, skeletons, staged
  loading) is part of your audit, not just raw timing.
- **Copy is UX** — error text the user can't act on is a broken
  interaction with good CSS.
- **Information scent and cognitive load**: does each page make the next
  step obvious (scent)? Is the user choosing between 8 equal options
  where 2 would do (overload)? Progressive disclosure — hide advanced
  paths, don't delete them.
- **Trust**: does the UI explain why it asks for what it asks (esp.
  permissions, payment, identity)? Unexplained asks read as phishing.
- **Internationalization where relevant**: text expansion (German ≈
  +30%) breaking fixed-width layouts; date/number formats; RTL mirrors
  for layout direction.

## Quality gates

- Audit grounded in named top tasks; findings reference exact locations.
- At least one novice walk done per task, stumbles recorded where they
  happened.
- WCAG 2.2 pass done (axe results included when available, manual review
  always); findings carry WCAG success-criterion references where
  relevant.
- Every blocker/major fix re-verified by re-walking the task.
- No finding reported without a proposed fix.

## Stop conditions

- Audit delivered, blockers/majors fixed and re-verified → summary, stop.
- Findings require product decisions (should this flow exist at all?) →
  route the decision back to the user/`hotseat`, fix the rest.
- No way to walk the flows (no browser, no runnable app) → static audit
  with every dynamic finding marked **unverified**, and the one command
  needed to make it verifiable.

## Output contract

Chat: top tasks audited, findings table (severity · location · what
happens · fix · status), WCAG notes, re-walk results. Deep audits on
request land in `docs/reports/ux-<slug>.md` with a provenance header —
default is chat-first; no giant report nobody reads.
