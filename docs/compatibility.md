# Cross-agent compatibility matrix

**Portability is an empirical claim, not a format assumption.** Cells are
filled only from actual tests or clearly-labeled research — never from
"the Agent Skills format is theoretically portable".

Status semantics:

- ✅ **tested** — executed against a live agent, date recorded
- ◐ **supported with fallback** — works, but degraded vs the primary path
- ? **unverified** — researched/documented, not yet executed here
- — **unavailable** — not installed / no headless capability found

## Local probe results (2026-09-14)

| Agent | Installed | Version | Headless invocation | Routing eval |
| --- | --- | --- | --- | --- |
| Codex | yes | 0.153.4 (gpt-5.6-sol) | ✅ tested (`codex exec`, stdin closed) | ✅ measured — smoke 0.917 accuracy (11/12), 2026-09-14 |
| OpenCode | yes | 1.18.30 | ✅ tested (`opencode run`) | ✅ measured — smoke 1.0 accuracy (12/12), 2026-09-14 |
| Claude Code | yes | 2.1.235 | ? flags documented; **execution hangs in dev env** | ? — pending a working environment |
| Cursor | no | — | — | — unavailable locally |
| Antigravity | no | — | — | — unavailable locally |

## Capability matrix (by agent, when installed)

| Capability | Claude Code | Codex | OpenCode | Cursor | Antigravity |
| --- | --- | --- | --- | --- | --- |
| Skill discovery (skills CLI) | ◐ tested | ? | ? | ? | ? |
| Filesystem | ? | ? | ? | ? | ? |
| Shell | ? | ? | ? | ? | ? |
| Web research | ? | ? | ? | ? | ? |
| Browser automation | ? | ? | ? | ? | ? |
| Subagents | ? | ? | ? | ? | ? |
| Structured output | ? (JSON mode documented, execution hung) | ? | ? | ? | ? |
| Token telemetry | ? | ? | ? | ? | ? |
| GitHub CLI passthrough | ? | ? | ? | ? | ? |
| Artifacts on disk | ? | ? | ? | ? | ? |

The skills themselves are Tier A/B portable by design (pure Markdown +
references; deterministic standard-library scripts; graceful capability
fallbacks in `shared/capability-map/`), but **design intent is not measured
compatibility**. Unknown cells remain unknown until a future proof pass runs the
specific agent/capability and records the date. They do not make the runtime
implementation incomplete.

## Installation compatibility (measured 2026-09-14)

- `npx skills add udaysharmadev/Skills --all -y` → **verified**: all 27
  skills discovered and installed into `./.agents/skills/` of a clean
  directory via the public skills CLI; CLI reports Claude Code as
  symlinked target and broad "universal" agent support. **28-skill
  re-verification (with `handsfree`) is pending — see C-004 in
  [claims.md](claims.md); do not quote 28-install success until it runs.**
- Interactive single-skill install (`npx skills add udaysharmadev/Skills`)
  → same CLI, selection mode; discovery verified, interactive flow
  exercised manually.
