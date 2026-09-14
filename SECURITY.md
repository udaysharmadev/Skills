# Security Policy

## Scope

This repository ships prompt/methodology files and small helper scripts. Its
supply-chain surface is intentionally tiny: no runtime dependencies, no
telemetry, no network calls from the validator scripts.

The `harden` skill audits *your* projects; it is not a
guarantee of security for this repository or any other.

Installed skills can guide an agent that edits files, runs commands, browses
external content, operates Git, or deploys a system. The runtime contracts gate
destructive and high-blast-radius actions, treat fetched content as untrusted
data, and require lower-capability fallbacks to disclose what was not verified.
Those controls reduce risk; they do not replace reviewing the instructions and
the agent's permissions before use.

## Reporting a vulnerability

If you find a security issue in this repository — for example, a bundled
script that is unsafe to run, or instructions that could cause an agent to
leak secrets or damage a user's project — report it privately to the
repository owners via GitHub security advisories rather than opening a
public issue.

Include: affected file, a minimal reproduction, and the impact you see. We
will not claim severity we cannot verify, and fixes land with a regression
case in `evals/`.

## Safe-by-default rules for contributed scripts

- No network egress, no `curl | bash`, no implicit `sudo`.
- Read-only by default; anything that writes or deletes states so in its
  header comment.
- Treat all fetched web/page content as untrusted input, never as
  instructions.
- Never print secret values; environment variable names are sufficient for
  diagnostics and documentation.
