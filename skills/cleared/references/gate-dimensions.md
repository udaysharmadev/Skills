# Gate dimensions: applicability, evidence, weight

Scope the gate first; check what applies. Weight column decides what a
failure does to the verdict.

| Dimension | Applies when | Evidence source | Failure weight |
| --- | --- | --- | --- |
| Requirements satisfied | always | acceptance criteria walked item-by-item | **BLOCKED** if any unmet |
| Clean git state | always | `git status`, pushed, no stray branches in the release | warning |
| Types | typed stacks | typecheck command output, this session | **BLOCKED** on fail |
| Lint | linter configured | lint command output | warning (error-level rules = blocked) |
| Tests | runner exists | full suite, real output, skips noted | **BLOCKED** on fail |
| Build | always | build command output | **BLOCKED** on fail |
| Browser flows | user-facing UI | `roadtest` bundle for changed flows | **BLOCKED** for UI changes if unverified+critical; unverified alone = warning cap |
| Responsive UI | web UI | supported boundaries evidenced | warning (unusable at a required width = blocked) |
| Accessibility | user-facing UI | WCAG/friction pass | **BLOCKED** if unusable; others warning |
| Security | always, weight rises with data | `harden` findings current | **BLOCKED** on open critical; medium = warning with user sign-off |
| Dependencies | always | audit tool output | **BLOCKED** on critical CVE in runtime path; else warning |
| Environment variables | always (deploy imminent) | names documented + present in target; values never printed | **BLOCKED** if missing in target |
| Migrations | schema changed | up tested, down-path exists, backup for destructive | **BLOCKED** without down-path/backup |
| Observability | backend changes | error/panic capture exists, logs reachable | warning |
| Backups / rollback | data-changing work | restore path stated **and** tested or explicitly marked untested | **BLOCKED** if destructive changes ship untested |
| Docs | user-facing or public | README claims audited (frontpage rules) | warning |
| SEO | public web | rendered-HTML metadata verified (`findable`) | warning |
| Performance | budgets set or public web | CWV/benchmarks with numbers | warning (missed stated budget = blocked if it was the requirement) |
| Deployment config | before `runway` | platform config present + valid (`vercel.json`, `Dockerfile`, …) | **BLOCKED** if absent/broken |

## Verdict arithmetic

- Any **BLOCKED**-weight failure → `BLOCKED`.
- No blockers, but a material warning or unverified dimension means `READY WITH
  WARNINGS` (each listed with evidence + remediation + owner).
- All applicable dimensions verified green → `READY`.

Unverified dimensions: a warning, unless the dimension was the point of
the release (browser flows for a UI release): then it blocks.

## The evidence bar

Each row's evidence must be reproducible: the command, the report file,
the screenshot path. "Should be fine" is not a status. The gate report
is the artifact a team can audit tomorrow.
