# Release protocol: authorize, observe, recover

Use this reference for production, traffic changes, migrations, or a failed
release. Preview work uses the entrypoint unless it exposes material risk.

## Release record

Capture target, immutable artifact or commit, explicit authorization, method,
environment names, migration sequence, fingerprint, health and smoke checks,
observation boundary, rollback method, and owner. Rebuild record if target,
artifact, authorization, or migration state changes.

## Migration sequencing

Prefer compatible expand, deploy, backfill, contract sequencing when old and new
versions overlap. A destructive migration needs backup/restore or approved
forward-fix plan before release. Green build does not prove data compatibility.

## Evidence boundary

Record command or CI result, release identifier, public response fingerprint,
smoke outcomes, logs, cache or async completion signal, and observation end.
Dashboard green is deployment evidence, not product behavior evidence.

## Incident decision

Contain traffic expansion first. Roll back only when prior artifact and data
compatibility are known; otherwise propose forward fix, maintenance action, or
owner escalation. Preserve evidence, expose no secret values, and do not repeat
unchanged deployment attempts.
