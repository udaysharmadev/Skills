---
name: friction
description: Diagnoses and improves usability by walking real user tasks, finding hesitation, backtracking, errors, recovery gaps, accessibility barriers, and inefficient paths. Use for UX audits, onboarding, forms, navigation, error messages, or confusing flows.
---

# friction: can a real person actually use this?

UI asks "does it look good?": that's `polish`. You ask "where does the
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
product's top tasks aren't obvious, ask: an audit without tasks grades
decoration. Browser access helps enormously (you can walk flows like a
user); without it, audit via code + screenshots and mark what's
unverified.

## Audit authority and evidence boundaries

Friction evaluates task experience; it does not fabricate user research,
conversion metrics, accessibility conformance, or permission to change product
policy. Distinguish observed walk evidence, repository evidence, inference, and
research hypotheses. Do not enter production accounts, create destructive data,
send messages, or expose personal data while walking a task without explicit
authority. Use an isolated identity/fixture, mask evidence, and preserve the
original flow before recommending a change.

## Task charter and severity decision

Create a short charter for every audited task:

| Field | Required answer |
| --- | --- |
| User/job | who is trying to achieve what outcome |
| Entry and precondition | where they start; identity/data/permission needed |
| Success | observable result and stopping point |
| Critical alternatives | error, cancellation, backtrack, empty, recovery |
| Evidence | browser/static rung, viewport, fixture, timestamp/commit |
| Risk | impact of failure: lost work, money, access, trust, time |

Severity is not visual annoyance. Rank by task impact, affected audience,
frequency when known, recoverability, and confidence in the evidence. A
low-frequency inaccessible blocker can outrank a common minor inconvenience.
When frequency is unknown, do not invent it: use task impact and label the
evidence gap.

## Workflow

### 1. Name the critical tasks

Identify the smallest set of tasks that represents the user's real job. Rank
findings by their effect on those tasks.

### 2. Walk each task twice

- **Novice walk:** first time, no knowledge: where do I start? What does
  this button do? Where do I hesitate? What happens if I do the wrong
  thing?
- **Expert path:** can a returning user do it fast: keyboard shortcuts,
  sensible defaults, no forced re-entry of known information?

Note every stumble point with its exact location.

### 3. Audit the dimensions

Read `references/usability-checklist.md` and walk the applicable
sections: information architecture, navigation, forms and validation,
error recovery, destructive-action safety, feedback and latency
perception, keyboard/focus, touch, copy, and **AI/Agentic UX** (planning
visibility, audit trails, escalation). Fix-the-system findings (a
validation pattern wrong everywhere) beat fix-the-instance ones.

### 4. Accessibility pass

WCAG 2.2 is the primary reference: focus visibility, target sizes,
labels, contrast, motion, reflow. When Playwright + axe are available,
run them: axe findings are a floor, not a ceiling: automated checks
cannot find every issue, so they complement the manual walk, never
replace it.

### 5. Classify, then rank

Name the **concern** per finding: they have different owners and fixes:

- **usability**: task completion, flow, feedback (this skill's core);
- **accessibility**: WCAG failures (may be legal/contractual, fix
  regardless of usage data);
- **visual design**: aesthetic problems belong to `polish`; reference,
  don't own;
- **conversion/product**: drop-off from positioning, pricing, value
  clarity: these route to product decisions, not UI fixes.

Do not call every UI problem UX. Then rank:

- **Blocker**: the task cannot be completed (dead end, lost data,
  unrecoverable error).
- **Major**: hesitation, backtrack, or a wrong guess users will make.
- **Minor**: friction an expert route around.

Fix blockers and majors (directly, or as slices for `pilot`), then
**re-walk the task** to confirm the path is actually smoother: the
fix is verified by the walk, not by the intention.

## Turn findings into testable improvements

For each blocker or major, state the causal hypothesis, smallest intervention,
expected changed behavior, owner, and verification method. Prefer a reversible
prototype, copy/structure adjustment, or bounded flow change before a large
redesign when the cause is uncertain. Re-walk with the same charter after a
change; compare task completion, wrong turns, recovery, and accessibility
behavior rather than declaring victory from a nicer screen.

Route work deliberately: visual hierarchy/tokens to polish; a broken contract
to sleuth/backend; browser evidence to roadtest; a user-value or scope decision
to hotseat/distill. Friction owns the task diagnosis and evidence, not every
implementation.

## Accessibility and inclusive-task protocol

Use WCAG success criteria as testable requirements where they apply, but do not
claim full conformance from a partial walk. Combine automated checks, semantic
inspection, keyboard operation, focus/order review, zoom/reflow, contrast,
motion preferences, and representative content. Accessibility testing is both
technical and human evaluation; an automated tool provides a floor.

For each relevant finding, record the affected task, barrier, standard anchor
when known, evidence method, and user impact. Avoid "accessibility issue" as a
catch-all: distinguish semantics, keyboard, focus, visual contrast, timing,
motion, target size, error/status communication, and cognitive burden. If
assistive-technology testing is unavailable, state that evidence limit rather
than simulating a screen-reader experience from code.

## Failure handling and edge cases

- **No runnable UI:** do a static audit only, label dynamic assertions
  unverified, and specify the minimal command/environment needed for a walk.
- **No clear task:** ask for the top job or derive a provisional task from an
  observed primary action and label it an assumption.
- **Conflicting user needs:** document the tradeoff and route a product decision;
  do not optimize one persona invisibly.
- **Sensitive/destructive path:** use the safest fixture and stop at a user
  confirmation boundary. Report the untested production-only step.
- **Finding cannot be reproduced:** record the condition and evidence, classify
  as hypothesis, and propose the smallest discriminating observation.
- **Accessibility/legal requirement:** escalate severity/owner according to the
  project's policy; do not down-rank it because usage data is absent.

## Tool selection/fallback

- Browser tooling → walk the flows like a user (novice + expert); this
  is the primary route.
- No browser but runnable app/screenshots → walk what's walkable, audit
  the rest via code; every dynamic finding marked **unverified** plus
  the one command needed to make it verifiable.
- Playwright + axe → mechanical floor (quote results); manual review
  always judges the rest: axe can never replace the walk.
- Nothing runnable → static audit only; stop per below, never invent
  walk evidence.

## The judgment calls that matter

- **Destructive actions** get confirmation proportional to damage, and
  undo where possible: "Are you sure?" on a settings toggle is friction;
  one-click permanent deletion of work is malpractice.
- **Latency is UX**: perceived speed (optimistic UI, skeletons, staged
  loading) is part of your audit, not just raw timing.
- **Copy is UX**: error text the user can't act on is a broken
  interaction with good CSS.
- **Information scent and cognitive load**: does each page make the next
  step obvious (scent)? Is the user choosing between 8 equal options
  where 2 would do (overload)? Progressive disclosure: hide advanced
  paths, don't delete them.
- **Trust**: does the UI explain why it asks for what it asks (esp.
  permissions, payment, identity)? Unexplained asks read as phishing.
- **Internationalization where relevant**: stress layouts with representative
  longer strings, locale-specific dates and numbers, and RTL direction.

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
- No blockers or majors found → say so with the walks cited; never
  invent findings to justify the audit, stop.

## Output contract

Chat: top tasks audited, findings table (severity · location · what
happens · fix · status), WCAG notes, re-walk results. Deep audits on
request land in `docs/reports/ux-<slug>.md` with a provenance header,
default is chat-first; no giant report nobody reads.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
