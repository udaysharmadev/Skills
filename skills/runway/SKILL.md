---
name: runway
description: Deployment and post-deployment verification — detects the platform, preflights, builds, validates environments, handles migrations, deploys preview/staging first when available, runs health checks and smoke tests, inspects logs, verifies domain/HTTPS and confirms the rollback path. Use when the user says deploy, ship, launch or push to production, mentions Vercel, Netlify, Docker or any hosting, or after cleared has passed. Excellent on Vercel, platform-agnostic by design — and it never fabricates a deploy that didn't happen.
---

# runway — deploy down the runway, verify on the ground

A deploy that isn't verified on the live URL didn't happen. You take the
change from green build to **evidenced production behavior** — and you
always know how to undo it.

## When NOT to use

- "Are we ready to ship?" → `cleared` (you want its verdict first — a
  BLOCKED gate does not fly).
- Choosing infrastructure for scale → `headroom`.

## Safety rails (before anything moves)

- **Previews/staging:** autonomous — deploy freely, verify, report.
- **Production:** requires the user's explicit go (this message, a
  command they ran, or previously-authorized CI). Expensive or
  irreversible production actions (infrastructure changes, data
  migrations on live data, DNS cutover) are gated even mid-deploy.
- **Secrets:** env var names are handled freely; values are set through
  the platform's own mechanism and never printed, echoed, or committed.
- **Never deploy a build that hasn't been built.** Local/green build
  first, always.

## Workflow

### 1. Detect platform and pipeline

Read the signals: `vercel.json` / `.vercel/`, `netlify.toml`,
`wrangler.toml`, `fly.toml`, `railway.json`, `render.yaml`, `Dockerfile`
/ `compose.yaml`, k8s manifests, `.github/workflows` deploy jobs, mobile
configs. No platform config → propose one from the project shape
(`references/platforms.md`), get the user's pick before creating
anything.

### 2. Preflight

- `cleared` verdict fresh and not BLOCKED (re-run if stale);
- git clean and pushed (the deployed commit is knowable);
- target platform CLI authenticated (`vercel whoami` etc. — probe, name
  what's missing).

### 3. Build and validate environment

- Build locally with production config — output errors stop the flight.
- Environment variables: every required name present in the **target**
  environment (checked via platform CLI, values never displayed).
  Missing → BLOCKED, list the names.
- Database migrations: strategy stated (expand/contract, order),
  destructive ones have backup + down-path, applied to staging first
  when staging exists.

### 4. Deploy — nearest safe rung first

Preview deployment when available → verify it (build success, URL
responds, key flows pass) → then production (user's go). Announce each
step as it happens. The platform's own CLI/CI is the executor — you
drive it, you don't pretend it.

**Strategy follows the platform, not ambition** — rolling (default
everywhere), blue/green or canary (when the platform supports traffic
switching and the change is risky), immutable deploys (container/image
platforms), atomic static swaps (static hosts). A small project on
Vercel gets preview → prod, and that IS professional; inventing canary
infrastructure for it is enterprise cosplay in the other direction.
CDN/cache state is part of the verification: a successful deploy with
stale edge cache means the old version is still live — verify the
fingerprint through the public URL, not the dashboard.

### 5. Verify on the ground (the part that makes it real)

- **Health:** endpoint(s) return 200 in reasonable time; version
  fingerprint confirms the **new** build is actually live (deployed
  hash/version marker — not wishful thinking).
- **Smoke:** the 2–3 critical API/browser paths on the live URL
  (roadtest discipline, light run, evidence captured).
- **Logs:** first minutes scanned for startup errors, unhandled
  exceptions, connection failures.
- **Domain/HTTPS:** correct domain resolves, certificate valid, apex/
  www redirects behave.
- **Post-deploy checks:** any post-deploy migrations/indexing completed.

### 6. Rollback path — stated before it's needed

Name the undo for every layer: previous deployment redploy (platform
command, verified available), migration down-path (or forward-fix
policy), DNS/cache TTLs if involved. A rollback that has never been
stated is a hope, not a path.

## Rules

- Each workflow step announced with its result — a deploy log the user
  can follow, not a silence and then "done".
- Verification claims cite live evidence (URL, status, log line,
  screenshot) — "deployed successfully" means the platform confirmed
  AND the smoke tests passed.
- If the platform CLI can't verify something (e.g. CDN cache state),
  the report says **unverified** with what would confirm it.
- Failed deploy: capture logs, report the failure layer (build/config/
  infra), fix forward or roll back per the user's call.

## Quality gates

- Preflight complete (cleared fresh, git clean, CLI authed) before any
  deploy action.
- Build succeeded locally before platform deploy.
- All required env names verified in the target; zero secret values in
  any output.
- Smoke tests passed on the live URL with evidence; version fingerprint
  confirms the new build.
- Rollback path named (and exercised where the platform allows a dry
  check).

## Stop conditions

- Live and verified → deploy report, stop.
- Any step fails irrecoverably (quota, missing credentials, platform
  outage) → stop with the exact blocker and the command/access needed.
- User requests production deploy without a passing `cleared` → state
  the risk once, proceed only on their explicit confirmation, record it.

## Output contract

```text
── deploy report ──────────────────────────
platform:   Vercel (vercel.json) · commit 4f2a91c "fix: debounce search"
preflight:  cleared READY (14:02) · git clean · CLI authed
build:      local ✅ (42s) · env: 9/9 names present in prod
staging:    preview 4f2a91c-x.vercel.app — smoke 3/3 ✅
production: live ✅ · fingerprint 4f2a91c confirmed · smoke 3/3 ✅
            logs clean 5min · HTTPS valid · apex→www ✅
rollback:   vercel rollback <prev-deploy> · migrations: none shipped
evidence:   screenshots + log excerpts inline
```

The report is the deploy's flight record — every claim traceable.
