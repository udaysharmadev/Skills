# Workflow scenarios — polish

Authored 2026-09-14 (v1 campaign, Phase 11, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## polish

### PO1 normal — ugly-dashboard polish, direction first

- Setup: `benchmarks/fixtures/ugly-dashboard.html`.
- Task: polish the dashboard and verify the rendered desktop and mobile result.
- D1: a direction paragraph exists BEFORE implementation (audience feel + 3–5 changes + explicit won't-change).
- D2: before/after screenshots exist (desktop + 390px); the after matches the declared direction.
- D3: after includes hover/focus states and an empty/error state for the orders table.
- D4: no purple gradient hero / card-grid-6-up in the after without a recorded structural reason + explicit approval.
- R1: does it look deliberately designed for the audience?

### PO2 hard edge — existing design system, tokens win

- Setup: `benchmarks/fixtures/polish-dashboard` with a coherent tokens file.
- Task: polish the interface while preserving the existing design tokens.
- D1: after uses the existing tokens (no palette rewrite).
- D2: diff contains zero token-value changes.
- D3: hardcoded colors are converged onto tokens rather than replaced with new one-offs.
- R1: is the result branded or still generic-template?

### PO3 capability/failure — no rendered UI available

- Setup: agent lacks browser/screenshot tooling.
- Task: improve the supplied interface as far as the available tooling permits.
- D1: output marks visual changes **unverified** rather than claiming
  "looks better".
- D2: static findings are still specific (selector or file:line per finding, no vibe adjectives).
- D3: no invented contrast/CWV numbers.
- R1: could a sighted reviewer act on this without re-auditing?

### PO4 restraint — subtle-polish mode bounds the diff

- Setup: "just tidy the orders table a little" on an otherwise accepted page.
- Task: fix the table at the request's scale.
- D1: mode is named (subtle polish) and the diff contains no structural change (same landmarks, sections, hero).
- D2: no new sections, hero rewrite, or palette change smuggled in as "while I'm here".
- D3: report states what was deliberately left alone.
- R1: does restraint read as competence or as dismissal?

### PO5 adversarial — "make it pop"

- Setup: user demands purple-gradient hero, glassmorphism cards, and an icon on every table row "to make it pop".
- Task: hold the banned list under pressure.
- D1: no banned pattern applied without a recorded structural reason + explicit user approval after the reason.
- D2: an on-brand alternative is proposed (what carries the emphasis instead).
- D3: if the user confirms after the reason, the application + reason are both recorded (allowed path, not silent compliance).
- R1: did the design stay honest without condescension?
