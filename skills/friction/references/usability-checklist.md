# Usability checklist: walk with a user's hands, not a linter

Grouped by where friction lives. Each: the question to answer on the real
flow, and the classic tell.

## Information architecture and navigation

- Can a first-time visitor identify the product and next action without
  avoidable hesitation?
- Can users find critical actions without avoidable navigation? Tell:
  settings split across three menus by internal team structure, not user
  mental model.
- Labels name user goals ("Billing") not system concepts ("Subscription
  Resource Management").
- Back/breadcrumb exists for anything buried; the user always knows where
  they are.

## Forms and validation

- Inputs ask only for what's needed now; every field has a visible label
  (placeholders are not labels: they vanish on type).
- Validation timing: inline on blur for format, on submit for
  cross-field; never punish-as-you-type.
- Error messages: what happened + how to fix it, attached to the field:
  "Email needs an @: like name@company.com", not "Invalid input".
- Constraints stated before the mistake: "Password: 12+ chars" under the
  empty field, not after failing.
- Progress preserved on failure; back button never destroys form state.

## Error recovery and destructive safety

- Every error has a next step (retry, contact, alternate path): dead-end
  screens are blockers.
- Destructive severity ladder: toggle → instant; delete draft → confirm
  inline; delete account/project → typed confirmation + consequence
  statement; prefer soft-delete with undo wherever possible.
- Undo beats confirmation beats nothing, in that order of preference.
- Session loss: drafts autosaved; timeout warns before expiry.

## Feedback and latency perception

- Every action acknowledges promptly relative to measured latency and user
  expectations.
- Perceptible waits show progress honestly with treatment appropriate to the
  operation.
- Success confirmations state what changed ("Moved to Archive", not "OK").
- Optimistic UI only where failure can roll back visibly.

## Keyboard, focus, and input

- Full task completion keyboard-only: logical tab order, visible focus
  (WCAG 2.4.7), no focus traps without escape (2.1.2), Escape closes
  dialogs.
- Enter submits the form it's in; Enter/Space activates the focused
  control.
- Apply WCAG 2.2 target-size requirements with their documented exceptions.
  Larger targets may be a product heuristic; no hover-only affordances on
  touch devices.

## Accessibility anchors (WCAG 2.2, the recurring ones)

- Text alternatives for meaningful images (1.1.1); contrast 4.5:1 body /
  3:1 large text and UI components (1.4.3 / 1.4.11).
- Reflow at 320px width without 2-D scroll (1.4.10); consistent help and
  identification across pages (3.2.6).
- Accessible authentication: no cognitive-test-only login (3.3.8).
- Status messages announced without stealing focus (4.1.3).
- Run axe when available for the mechanical floor; judge the rest by hand.

## AI / Agentic UX (2026)

- **Planning Visibility:** Does the AI state its intended plan *before* executing destructive or long-running actions?
- **Audit Trails:** Are agent actions logged in plain language (e.g. "Emailed finance@...") rather than raw JSON/tool calls?
- **Graceful Degradation / Escalation:** When the AI gets stuck, is there a clear, immediate escalation path to a human, or does the user get trapped in a loop?
- **Selective Transparency:** Does the UI expose the 'why' behind an AI decision without overwhelming the user with full reasoning traces?

## Copy

- Sentence-case, plain words, no jargon the user didn't introduce.
- Buttons start with verbs and name the outcome ("Create project").
- Empty/error/success copy answers: what happened, so what, now what.

## Response patterns (novice vs expert)

- Novice: guidance where they'll land first-time (empty states with
  actions, examples in placeholders where labels alone are unclear).
- Expert: defaults that skip steps, shortcuts that don't break the
  guided path, bulk actions on repeated operations.
- Never make the expert route the only route, or the guided route a
  maze for the expert.
