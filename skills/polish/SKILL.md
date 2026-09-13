---
name: polish
description: Designs and upgrades user interfaces so they stop looking AI-generated. Use when building or improving any visual interface (web, mobile, dashboard, landing page), when the user says make it pretty, good, professional, modern or clean, mentions design, UI, styling or look-and-feel, or when generated UI has that generic template look. Audits layout, typography, color, spacing, states, motion and responsiveness, then redesigns deliberately inside the project's existing design system. Deliberately anti-slop — no default purple gradients, no random glassmorphism, no card-grid addiction.
---

# polish — make AI interfaces stop looking AI-generated

Generic UI is not a taste problem, it's a decisions problem: default
everything, no hierarchy, decoration instead of intent. You fix it by
understanding the product first, auditing deliberately, and making a
small number of strong decisions — not by sprinkling gradients.

## When NOT to use

- Users can't complete tasks → that's usability, `friction`'s job. Fix
  flow before aesthetics.
- Recreating an existing design from a screenshot/URL → `ditto`.
- The project has no product definition yet → `hotseat`/`distill` first;
  you can't design for an unknown audience.

## Prerequisites

Before touching a pixel, know: what the product is, who uses it, what the
page's single primary action is, the existing design system (tokens,
components, fonts already in the repo) and what's already built you can
reuse. **Existing good design tokens are an asset, not a suggestion** —
rewrite them only if they are actively broken, never for novelty.

## Workflow

### 1. Audit against the checklist

Read `references/audit.md` and walk every applicable dimension (layout,
type, color, spacing, hierarchy, states, motion, responsive, mobile) on
the real rendered UI — screenshots of current state, not imagination.
Note what's actually weak; skip what's already good and say so.

### 2. Decide the direction

One short paragraph before implementing: what should this feel like for
its audience (dense tool for experts? calm consumer product?), what are
the 3–5 changes that get there, what explicitly won't change. This is the
brief you'll verify against.

### 3. Implement within the system

- Typography and spacing from the token scale (establish one if missing —
  then use it everywhere).
- Color: a small role-based palette (background, surface, text, primary,
  danger); contrast verified (AA minimum for text).
- Components reused before rebuilt; consistency beats local cleverness.
- Every interactive element gets its states: hover/focus/active,
  disabled, loading, empty, error. States are where AI UI most often
  stops too early.

### 4. Verify like an engineer, not a vibes-machine

- Screenshot before/after at desktop + mobile widths; compare against the
  direction paragraph.
- Walk empty/loading/error states with real data conditions, not just
  the happy path.
- Keyboard pass: focus visible on every interactive element, tab order
  sane.
- For web: check current Core Web Vitals (LCP, INP, CLS) where
  measurable — large unoptimized hero images and layout shift are design
  bugs too.
- Then hand off: `friction` for usability, `roadtest` (planned phase 4)
  for browser-flow evidence.

## The banned list

- **Default purple gradient** — the uniform of generated UI. Color comes
  from the product's intent, not the model's prior.
- **Random glassmorphism** — blur/transparency needs a structural reason
  (real layering), not vibes.
- **Card-grid addiction** — three identical feature cards is not
  information architecture. Structure content by importance, not symmetry.
- **Gigantic hero because "modern SaaS"** — hero height serves the
  message, not the template.
- **Arbitrary gradients/glows** — decoration must earn its place or go.
- **Icon spam** — an icon per bullet adds noise, not scanability.
- **Token rewrites for novelty** — the existing system wins.
- Each ban has an escape hatch: state the structural reason and the user
  can approve it explicitly.

## Quality gates

- Before/after screenshots exist; the after matches the declared
  direction.
- All states present on changed components (hover/focus/disabled/loading/
  empty/error as applicable).
- Text contrast meets AA; focus visible everywhere.
- Zero banned patterns without an approved reason.
- No unused CSS/one-off styles scattered behind the change — cleanup is
  part of the change.

## Stop conditions

- Direction implemented + verified → report before/after and hand to
  `friction`, stop.
- The real problem is flows, not looks → report that and route to
  `friction`.
- No design system and the user doesn't want one → smallest consistent
  set of tokens for the task at hand, documented in the report.

## Output contract

Chat: the direction paragraph, the audit's top findings (what was weak),
what changed, verification evidence (screenshots, contrast, states,
CWV where measured). On disk: only code/token changes — audit narrative
lives in chat unless the user asks for a document.
