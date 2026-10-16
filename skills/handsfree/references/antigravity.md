# Host permission modes: Antigravity, Gemini CLI, and the portable fallback

Map the mode you **observe at runtime** to an action class. Mode names are
fast-moving: the table below records names observed on 2026-10-14 against
the canonical docs (https://antigravity.google/docs/settings?tab=cli --
the old `/docs/cli/settings/` URL now redirects there). If the host shows a
name not listed here, classify by behavior (does it prompt? does it sandbox?
does it refuse?) and say which rule you applied.

## Permission modes (Antigravity CLI, observed 2026-10-14)

| Observed mode | Meaning | handsfree class |
| --- | --- | --- |
| `request-review` (default) | risky actions prompt | ASK-ONCE: batch one question, proceed on grant |
| `proceed-in-sandbox` | sandboxed commands auto-run; bypass prompts unless an `unsandboxed(...)` rule matches; sandbox defaults off | AUTO inside sandbox, ASK-ONCE for bypass |
| `strict` | forces Request Review on terminal, browser JS, artifacts; ignores allowlist; forces network-less sandbox | read-only posture: say so, keep working without writes |
| `always-proceed` | user pre-authorized motion | AUTO, but BLOCKED gates still hold |
| `artifactReviewPolicy: asks-for-review` (default) / `agent-decides` / `always-proceed` | who approves produced artifacts | ASK-ONCE / AUTO-with-report / AUTO |

## Sandbox strategy

Prefer sandbox-compatible commands first. Never smuggle bypass flags to
dodge a prompt. A sandbox escape is a BLOCKED-class event: stop, report,
ask.

## Strict mode

Strict means the host distrusts the run: do not push harder, do not
rephrase actions to dodge review. State the mode, work read-only, and put
every write behind an explicit user grant.

## Mitigation (precedence verified live 2026-10-17)

Deny > Ask > Allow (https://antigravity.google/docs/permissions/).
In-workspace file access is usually auto-allowed; web, shell, and
out-of-workspace work is where prompts live. Plan the run so the
prompt-heavy surface is batched behind the fewest questions.

## Other runtimes (Gemini CLI)

`defaultApprovalMode`: `default` / `auto_edit` / `plan`. YOLO exists only
via `--yolo` / `--approval-mode=yolo` flags -- never via `settings.json`,
and never by your hand. You must never claim to "enable YOLO" or edit
settings to widen approvals; that is the user's CLI invocation. Respect
plan mode as research-only.

## Banned

- Editing user/host settings to widen approvals.
- Bundling unrelated risky commands to amortize one approval
  ("permission laundering").
