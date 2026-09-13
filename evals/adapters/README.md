# Agent adapters

Invocation capability per agent, with verification status. **Flags are
never invented** — each row is either verified against a live agent or
carries its vendor-docs source and stays `unverified` until first
successful execution.

| Agent | Binary | Invocation | Status | Source / notes |
| --- | --- | --- | --- | --- |
| Codex | `codex` | `codex exec "<prompt>"` | **verified** 2026-09-14 (v0.153.4, model gpt-5.6-sol) | executed live; reads stdin — runner passes stdin=DEVNULL |
| OpenCode | `opencode` | `opencode run "<prompt>"` | **verified** 2026-09-14 (v1.18.30) | executed live |
| Claude Code | `claude` | `claude -p "<prompt>" --output-format json` | flags per [official docs](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using); **execution hangs in the dev environment** (reproduced sandboxed and unsandboxed, stdin closed) — unverified until run in a working environment |
| Cursor | `cursor-agent` | — | **UNAVAILABLE** (not installed) | add invocation after vendor docs check + install |
| Antigravity | — | — | **UNAVAILABLE** (no headless CLI found) | recheck when vendor ships one |

Environment note: all invocations pass `stdin=DEVNULL` — `codex exec`
blocks reading stdin otherwise (learned from its stderr: "Reading
additional input from stdin...").

## Semantics (binding)

- Not installed → **UNAVAILABLE**; the runner exits 3 and writes no
  results. No fake failures.
- Installed but flags not yet exercised → results carry
  `invocation: "unverified"` and are not comparable to verified runs.
- Ambiguous parse of an answer → recorded as observed, never coerced
  into a pass.

## Method note (what a trigger eval measures here)

The prompt surfaces the suite's own skill metadata (name + description
from frontmatter — exactly what a runtime shows the model) and asks for
a routing decision. This measures **routing-given-metadata**, a fair
proxy for trigger behavior; it cannot measure in-runtime automatic
skill activation, which requires per-runtime harness integration
(planned 0.8). This limitation is stated wherever results are shown.
