# File formats for the four memory files

Keep these formats boring and diff-friendly. Humans will read and edit
these files; agents must not break them.

## PROJECT_CONTEXT.md

```markdown
# Project context
<!-- generated/maintained by recall — stable facts only, temp state lives in STATUS.md -->

## Stack
- Next.js 15 (App Router) · TypeScript 5 · Tailwind 4 (CSS variables)
- SQLite via Drizzle ORM — chosen 2026-09-01 (single-box deploy)

## Commands
- dev: `npm run dev` · test: `npm test` · lint: `npm run lint`

## Conventions
- Components in `src/components`, server logic in `src/server`
- Feature work goes through briefs in `docs/briefs/`

## External services
- Resend (email) — env: RESEND_API_KEY
- Upstash Redis (rate limiting) — env: UPREDIS_URL
```

Rules: env var **names** only, ever. Every stable fact dated when it was
a decision. Six-month test: if it might not be true in six months, it
belongs in STATUS, not here.

## DECISIONS.md

```markdown
# Decisions
<!-- newest first — one entry per decision, always with the why -->

## [Active] 2026-09-12 — Auth: magic links, no passwords
- Chose magic-link email auth over passwords+OAuth.
- Why: no password storage liability, single flow to maintain.
- Rejected: OAuth-only (email deliverability risk identical, plus
  provider lock-in).
- Revisit when: enterprise users ask for SSO.

## [Superseded] 2026-08-01 — Auth: OAuth-only
- *(superseded 2026-09-12 by: magic links)*
```

Rules: newest first. Every decision acts as a governed state machine 
(`[Active]` -> `[Superseded]` or `[Deprecated]`). The `Revisit when` line 
is what makes a decision living instead of fossilized. Superseded decisions 
get their content pruned but the header and replacement pointer stay: 
history, not deletion.

## STATUS.md

```markdown
# Status
<!-- snapshot, not a log — recall replaces this, never appends -->
<!-- updated 2026-09-14 -->

## Done
- Dark mode shipped (slices 1–3 of plan docs/plans/dark-mode.md)

## In progress
- Avatar upload: presigned URLs work, client resize missing

## Blocked
- Waiting on DNS propagation for staging domain [TTL: 2026-09-16]

## Next
- Avatar upload slice 3 (client-side resize) — brief in docs/briefs/avatar-upload.md
```

Rules: ≤ 40 lines total. Replaced wholesale on each session delta, with
the update date bumped. Blockers and Next steps must carry a `[TTL: YYYY-MM-DD]` 
(Time-To-Live). If a TTL expires without resolution, it gets formally 
escalated or dropped. Detail lives in `docs/` artifacts — STATUS points
at them.

## LEARNINGS.md

```markdown
# Learnings
<!-- expensive lessons only — anything that cost real time to discover -->

## 2026-09-13 — Next.js 15: `cookies()` is async now
- Route handlers and server components must `await cookies()`.
- Symptom we hit: TypeError mid-request, only in prod build.
- Source: verified in Next.js 15 docs; do not "fix" back to sync.
```

Rules: symptom + cause + what not to do again. If it's in the official
docs and easy to re-find, it's not expensive — don't hoard trivia.

## Anti-patterns

1. **The transcript dump** — "User asked X, agent replied Y…" — delete on
   sight.
2. **The everything-file** — one giant CONTEXT.md holding status, history
   and lessons. Four files exist because they rot at different speeds.
3. **Secrets in memory** — env names only; values live in `.env` which is
   gitignored.
4. **Undated entries** — a fact without a date can't be aged or trusted.
5. **Append-only rot** — STATUS.md as an ever-growing log defeats its
   entire purpose.
