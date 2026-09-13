# Cross-skill handoff contract

Skills cooperate by **slug name**, never by relative path (self-
containment rule, AGENTS.md). The handoff between them is a compact
structured message — not a conversation summary.

## The payload

```text
task:                 <one line — what the requesting skill was solving>
facts established:    <bullets, only facts the next skill cannot re-derive cheaply>
artifact paths:       <files written, owned per shared/terminology/artifacts.md>
decisions:            <locked decisions + one-line why each>
unresolved questions: <open items that may change the next skill's approach>
verification done:    <commands run + results, evidence already produced>
verification needed:  <what the next skill must still prove>
next skill:           <slug>
```

## Rules

1. **≤ 20 lines.** If it needs more, the detail belongs in an artifact
   file the payload points to.
2. **No transcripts.** The next skill receives state, not history.
3. **Verification is directional.** Anything already verified is named
   with its evidence; the receiving skill does not re-prove it (that is
   the frugal contract).
4. **`recall` is not a handoff bin.** Project memory stores durable
   decisions and lessons; session-scoped handoffs travel in the message
   above (chat) or in the artifact files.
5. **Owner boundaries hold.** The payload references artifacts; it never
   asks the receiving skill to write outside its ownership map.

## Worked example

```text
task: dark mode toggle for dashboard (brief docs/briefs/dark-mode.md)
facts: Tailwind 4 + CSS vars; no preference storage today; toggle
       pattern exists in src/components/Toggle.tsx
artifacts: docs/plans/dark-mode.md
decisions: class strategy over media-query; localStorage persistence
unresolved: auth page theming (post-v1)
verification done: baseline build+tests green (14:02, 87 passed)
verification needed: post-implementation suite + browser walk
next skill: pilot
```

Handoff direction flow (reference): `concierge` → specialist →
`referee`/`cleared` gates → `recall` for what must survive the session.
