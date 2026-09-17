---
name: polish
description: Refines a product interface while preserving its visual language, improving hierarchy, typography, spacing, density, states, responsiveness, keyboard use, focus, motion, and accessibility. Use when the user asks to make an existing web or app interface look intentional and professional.
---

# polish: make AI interfaces stop looking AI-generated

Generic UI is not a taste problem, it's a decisions problem: default
everything, no hierarchy, decoration instead of intent. You fix it by
understanding the product first, auditing deliberately, and making a
small number of strong decisions: not by sprinkling gradients.

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
reuse. **Existing good design tokens are an asset, not a suggestion**,
rewrite them only if they are actively broken, never for novelty.

Also establish the supported viewport range, color themes, locales, data
extremes, input methods, and the implementation boundary. If the request is
only "make it better", inspect the real interface first and return a concise
direction before making a broad visual change. A visual preference is not
evidence that a product problem exists.

## Authority and preservation boundaries

- Preserve working behavior, content intent, URLs, analytics contracts, and
  established component APIs unless the user authorizes a change.
- Do not replace a product's font, color system, component library, or page
  structure merely because another style seems more fashionable.
- Do not claim WCAG conformance from a screenshot, an automated scan, or a
  contrast ratio alone. These are partial evidence.
- Do not use real customer data in screenshots or reports. Mask or use a
  representative fixture.
- Ask before changing copy with legal, pricing, safety, localization, or
  conversion implications; visual polish does not grant editorial authority.
- Treat a design file, screenshot, and live app as different evidence. Name
  which was inspected and what it cannot prove.

## Modes

| Mode | Scope |
| --- | --- |
| **subtle polish** | spacing/type/consistency fixes; no structural change |
| **full redesign** | structure up: layout, hierarchy, then surfaces |
| **dashboard** | density first, scannability, state completeness over decoration |
| **landing page** | hierarchy and one primary action; message before aesthetics |
| **mobile-first** | design the 390px flow, then enhance upward |
| **design-system cleanup** | converge drift onto the existing tokens; add nothing new |

The mode bounds the diff. A "subtle polish" that restructures the page
ignored the mode.

## Repository and rendered-product inspection

Inspect before styling. This protects existing work and reveals whether the
problem is visual, behavioral, content-related, or caused by a missing state.

1. Read repository guidance and locate the relevant route, component tree,
   tokens, global styles, fonts, icon assets, responsive rules, and tests.
2. Identify the existing primitives: spacing scale, type scale, semantic color
   roles, radii, elevation, breakpoints, focus treatment, and motion tokens.
   Record drift instead of declaring a new system from one screen.
3. Render the target route at its supported desktop and narrow widths. Capture
   the initial, loading, populated, empty, error, disabled, validation, and
   long-content states that actually apply.
4. Exercise keyboard-only navigation, visible focus, escape behavior, dialogs,
   menus, and form errors. Inspect semantic elements and accessible names,
   roles, and states where custom controls exist.
5. Test realistic stress: long translated strings, narrow widths, many rows,
   missing images, slow network, zoom, dark theme, and reduced-motion
   preference when applicable.
6. Make an evidence list: observed issue, affected task/user, viewport/state,
   likely cause, confidence, and whether it is visual polish or requires a
   handoff to friction, backend, or hotpath.

If no running interface is available, inspect markup and styles, use supplied
screenshots as static evidence, and label every behavioral or visual result
unverified. Do not pretend a code read is a rendered review.

## Design decision framework

Write a direction paragraph before implementation. It must say the audience,
primary job, hierarchy intent, density, visual character, constraints to keep,
and the smallest set of changes expected to matter. Then decide changes in
this order:

1. **Structure:** task order, grouping, primary action, content hierarchy, and
   information density.
2. **Rhythm:** grid, container, alignment, spacing scale, and responsive
   rearrangement.
3. **Legibility:** typography roles, line length, contrast, data formatting,
   labels, and error copy placement.
4. **Surfaces:** semantic color, borders, elevation, icons, images, and dark
   theme. Decoration needs a product reason.
5. **Feedback:** interactive states, loading, validation, empty/error/success,
   focus, motion, and optimistic-update rollback.

Reject a change when it improves only a pristine screenshot but weakens a
common task, real-data robustness, accessibility, performance, or consistency.
When two directions are plausible, present the tradeoff instead of blending
them into a generic compromise.

## Interaction and state model

For each changed interactive component, specify the user action, enabled
condition, feedback, success, recoverable failure, irreversible failure, and
keyboard behavior. Include:

| State | Required design question |
| --- | --- |
| Default | Can a person identify purpose and priority without hover? |
| Hover and active | Does feedback clarify affordance without becoming the only cue? |
| Focus-visible | Is focus obvious, unobscured, and in meaningful order? |
| Disabled | Is the reason discoverable where it matters? |
| Loading | Does it preserve layout and indicate what remains usable? |
| Empty | Does it explain the absence and a next safe action? |
| Error | Is it specific, adjacent, recoverable, and retained long enough to read? |
| Success | Does it confirm the completed outcome without noisy interruption? |

Use native controls when they fit. Custom widgets require the semantic and
keyboard behavior users expect, not only similar pixels. Respect reduced-motion
preferences; motion should explain a change or feedback, never be compulsory
decoration.

## Workflow

### 1. Audit against the checklist

Read `references/audit.md` and walk every applicable dimension (layout,
type, color, spacing, hierarchy, states, motion, responsive, mobile) on
the real rendered UI: screenshots of current state, not imagination.
Note what's actually weak; skip what's already good and say so.

### 2. Decide the direction

One short paragraph before implementing: what should this feel like for
its audience (dense tool for experts? calm consumer product?), which few
changes get there, and what explicitly will not change. This is the
brief you'll verify against.

### 3. Implement within the system

- Typography and spacing from the token scale (establish one if missing,
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
  measurable: large unoptimized hero images and layout shift are design
  bugs too.
- Then hand off: `friction` for usability, `roadtest`
  for browser-flow evidence.

### 5. Review the implementation diff

Confirm tokens and reusable primitives were extended before adding one-off
values. Check that responsive behavior uses content pressure rather than a
single device stereotype, and that a layout change does not alter semantic
reading or focus order. Remove experimental CSS, dead variants, duplicated
breakpoints, and unused assets created during the polish pass.

For an interface with charts, tables, or dense controls, verify at least one
realistic high-density state. For forms, verify invalid submission, inline
error announcement where applicable, correction, and successful completion.
For a destructive operation, the visual change must not obscure the consequence,
confirmation, or recovery path.

## Accessibility and performance verification protocol

Run this proportionately to the changed surface. Automation finds regressions;
keyboard, screen-reader-aware semantic review, and real rendering find different
classes of problems.

1. **Semantics:** inspect headings, landmarks, native controls, labels,
   accessible names, error/status announcement, and custom widget roles. Avoid
   ARIA where native HTML provides the behavior.
2. **Keyboard:** start from browser chrome, tab forward/backward, operate every
   changed control, open/close overlays, and ensure focus returns sensibly.
   Check that focus is visible and not hidden by sticky UI or a modal.
3. **Visual access:** test contrast in all changed themes, color-independent
   meaning, zoom/reflow, text spacing, narrow viewports, and target reach. Use
   the applicable WCAG criterion, including its scope and exceptions.
4. **Motion:** trigger transitions and asynchronous feedback with reduced motion
   enabled. Verify a state change remains understandable when animation is off.
5. **Runtime quality:** inspect layout shift around images, fonts, async content,
   banners, and skeletons; inspect interaction responsiveness around changed
   handlers. Measure only when the tool/environment supports it and state the
   page, device class, and conditions.
6. **Regression scope:** revisit an adjacent route or component that shares the
   changed token/primitives. A global token edit needs broader evidence than a
   local class adjustment.

If an issue cannot be safely fixed inside the requested visual scope, report it
with reproduction steps and route it. Do not hide accessibility or performance
debt behind a polished screenshot.

## Tool selection/fallback

- Browser/screenshot tooling audits and verifies the real rendered UI at the
  product's supported responsive boundaries.
- No browser tooling → static pass over markup and styles only; every
  visual claim is marked **unverified**, never "looks better".
- Contrast/CWV tooling → quote measured values; otherwise compute from
  accessible data or state as unverified: never invent numbers.

## The banned list

- **Default purple gradient**: the uniform of generated UI. Color comes
  from the product's intent, not the model's prior.
- **Random glassmorphism**: blur/transparency needs a structural reason
  (real layering), not vibes.
- **Card-grid addiction**: three identical feature cards is not
  information architecture. Structure content by importance, not symmetry.
- **Gigantic hero because "modern SaaS"**: hero height serves the
  message, not the template.
- **Arbitrary gradients/glows**: decoration must earn its place or go.
- **Icon spam**: an icon per bullet adds noise, not scanability.
- **Token rewrites for novelty**: the existing system wins.
- The rule underneath every ban: these patterns fail when used as
  **default decoration**: the same treatment can be right when it
  serves the product (a glass surface that communicates real layering,
  a gradient that is the brand). Ban the thoughtlessness, not the
  technique: state the structural reason and the user approves
  explicitly.
- **Vibe Coding (Decoupled Aesthetics & Logic)**: designing based on how a screen *feels* with perfect dummy data, ignoring how it behaves under pressure (long text, 1000 items, empty states). Design must survive reality.
- **The "Blank Canvas" hallucination**: ignoring the project's existing design tokens and rewriting component styles from scratch. Existing tokens are a constraint, not a suggestion.
- **Dark mode is a design surface, not an inversion:** check contrast
  and elevation colors separately in dark theme; pure-inverted palettes
  break shadows and brand accents.

## Quality gates

- Before/after screenshots exist; the after matches the declared
  direction.
- All states present on changed components (hover/focus/disabled/loading/
  empty/error as applicable).
- Text contrast meets AA; focus visible everywhere.
- Zero banned patterns without an approved reason.
- No unused CSS/one-off styles scattered behind the change: cleanup is
  part of the change.
- The changed experience was inspected at every applicable state and supported
  theme/viewport, or each untested condition is named.
- Keyboard/focus and semantics received a pass proportionate to the interaction
  change. Automated results do not substitute for that pass.
- Any claimed contrast, performance, or accessibility result names the tool,
  conditions, and limitation.

## Stop conditions

- Direction implemented + verified → report before/after and hand to
  `friction`, stop.
- The real problem is flows, not looks → report that and route to
  `friction`.
- No design system and the user doesn't want one → smallest consistent
  set of tokens for the task at hand, documented in the report.
- No rendered UI available → static pass only; all visual changes marked
  unverified, stop.

## Output contract

Chat: the direction paragraph, the audit's top findings (what was weak),
what changed, verification evidence (screenshots, contrast, states,
CWV where measured). On disk: only code/token changes: audit narrative
lives in chat unless the user asks for a document.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
