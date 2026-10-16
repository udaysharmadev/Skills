---
name: runway
description: Deploys software through the target platform's real release model, sequencing configuration, secrets, data, and code safely, then verifying the immutable release and public behavior. Use when the user asks to deploy, release, publish, roll back, or prove a version is live.
---

# runway: deploy down the runway, verify on the ground

A deploy command can succeed while live behavior remains unverified. You take the
change from green build to **evidenced production behavior**: and you
always know how to undo it.

## Prerequisites

Candidate-bound readiness evidence (a `cleared` verdict when available), a
successful applicable build locally or in the trusted pipeline, and access to
the target platform (CLI authed or CI wired).
Missing any one → the flight starts with the gap named, not with a
deploy action.

## Authority and release modes

Runway may inspect deployment configuration and execute a preview when the
task and platform access permit it. Production release, traffic switching, DNS,
live migration, secret changes, paid capacity, and rollback each require their
own current authorization. Credentials or a successful CLI probe prove access,
not approval.

| Mode | Use when | Result |
| --- | --- | --- |
| Preflight | target or readiness uncertain | release record and blockers; no deploy |
| Preview | non-production target available | immutable preview and evidence |
| Production | explicit release authorization plus green gates | deployed version and rollback readiness |
| Incident recovery | health or smoke fails | contain, diagnose, rollback or forward-fix decision |

Read [references/release-protocol.md](references/release-protocol.md) before a
production action, migration, traffic change, or release failure.

## Tool selection/fallback

- Platform CLI/CI available → drive it, verify the live fingerprint,
  report each step as it happens.
- No CLI/auth but buildable → preflight + local build + env-name check
  only; production marked **unverified**, never claimed.
- Nothing runnable → plan-only: platform pick, env list, rollback
  sketch, and the exact access needed; zero deploy claims.

## When to use

- "deploy this to production"
- "launch the site and verify it works live"
- "preflight only, don't actually deploy anything"

## When NOT to use

- "Are we ready to ship?" → `cleared` (you want its verdict first: a
  BLOCKED gate does not fly).
- Choosing infrastructure for scale → `headroom`.

## Safety rails (before anything moves)

- **Previews/staging:** proceed within authorized scope only after checking
  data, secrets, public exposure and costs. A preview label does not make
  production-connected databases or paid resources safe.
- **Production:** requires the user's explicit go (this message, a
  command they ran, or previously-authorized CI). Expensive or
  irreversible production actions (infrastructure changes, data
  migrations on live data, DNS cutover) are gated even mid-deploy.
- **Secrets:** env var names are handled freely; values are set through
  the platform's own mechanism and never printed, echoed, or committed.
- **Build evidence follows the pipeline.** A candidate-bound successful CI
  build can be sufficient; do not require a redundant local build or a build
  command for an uncompiled static artifact. Identify exactly what will ship.

## Workflow

### 1. Detect platform and pipeline

Read the signals: `vercel.json` / `.vercel/`, `netlify.toml`,
`wrangler.toml`, `fly.toml`, `railway.json`, `render.yaml`, `Dockerfile`
/ `compose.yaml`, k8s manifests, `.github/workflows` deploy jobs, mobile
configs. No platform config → propose one from the project shape
(`references/platforms.md`), get the user's pick before creating
anything.

### 2. Preflight

- candidate-bound readiness evidence has no unresolved critical blocker; use
  an available `cleared` report or perform this scoped preflight directly;
- shipped commit/artifact and exact included files are known; preserve
  unrelated dirty work instead of resetting, stashing or adding everything;
- target platform CLI authenticated (`vercel whoami` etc.: probe, name
  what's missing).

Record target, commit or immutable artifact, authorization, expected
fingerprint, environment names, migration state, health and smoke checks,
observation window, rollback command, and release owner. Unknown items are
preflight gaps, not details to discover during production mutation.

### 3. Build and validate environment

- Use the actual applicable build/pipeline and target configuration. Record
  artifact identity and successful local or trusted CI output; errors stop promotion.
- Environment variables: every required name present in the **target**
  environment (checked via platform CLI, values never displayed).
  Missing → BLOCKED, list the names.
- Database migrations: strategy stated (expand/contract, order),
  destructive ones have tested restoration or an authorized forward-fix
  recovery plan; application rollback must remain compatible with data state.

### 4. Deploy: nearest safe rung first

Preview deployment when available → verify it (build success, URL
responds, key flows pass) → then production (user's go). Announce each
step as it happens. The platform's own CLI/CI is the executor: you
drive it, you don't pretend it.

**Strategy follows the platform, not ambition**: rolling when supported, blue/green or canary (when the platform supports traffic
switching and the change is risky), immutable deploys (container/image
platforms), atomic static swaps (static hosts). A small project on
Vercel gets preview → prod, and that IS professional; inventing canary
infrastructure for it is enterprise cosplay in the other direction.
CDN/cache state is part of the verification: a successful deploy with
stale edge cache means the old version is still live: verify the
fingerprint through the public URL, not the dashboard.

### 5. Verify on the ground (the part that makes it real)

- **Health:** endpoint(s) return 200 in reasonable time; version
  fingerprint confirms the **new** build is actually live (deployed
  hash/version marker: not wishful thinking).
- **Smoke:** the 2–3 critical API/browser paths on the live URL
  (roadtest discipline, light run, evidence captured).
- **Logs:** first minutes scanned for startup errors, unhandled
  exceptions, connection failures.
- **Domain/HTTPS:** correct domain resolves, certificate valid, apex/
  www redirects behave.
- **Post-deploy checks:** any post-deploy migrations/indexing completed.

### 6. Rollback path: stated before it's needed

Name the undo for every layer: previous deployment redeploy (platform
command, verified available), migration down-path (or forward-fix
policy), DNS/cache TTLs if involved. A rollback that has never been
stated is a hope, not a path.

## Anti-Patterns (The Banned List)

- **Blind Fire-and-Forget**: running `git push` or `vercel --prod`, seeing the command exit, and immediately declaring "Deployed successfully!" without waiting for the remote build to finish or verifying the live URL.
- **Dashboard Hallucination**: claiming the deployment is healthy without actually curling the live URL to verify the new version fingerprint, relying instead on wishful thinking or a successful tool invocation.
- **Enterprise Cosplay**: inventing a 5-stage Kubernetes canary deployment strategy for a static blog on Vercel because of training bias toward "best practices." Strategy follows the platform.
- **Silent Failures**: a deploy fails, and you hide the logs. Failed deploy: capture logs, report the failure layer (build/config/infra), fix forward or roll back per the user's call.

## Quality gates

- Preflight complete (candidate-bound readiness, artifact known, target access
  and authorization) before a deploy action; preview risks checked too.
- Applicable build succeeded against the candidate locally or in the trusted
  pipeline before promotion; static artifacts without a build are explicit.
- All required env names verified in the target; zero secret values in
  any output.
- Smoke tests passed on the live URL with evidence; version fingerprint
  confirms the new build.
- Rollback path named (and exercised where the platform allows a dry
  check).
- Release record binds production authorization to target and artifact; access,
  preview, or a different commit never substitutes.
- Verification covers asynchronous or cache state when changed surface needs it.

## Stop conditions

- Live and verified → deploy report, stop.
- Any step fails irrecoverably (quota, missing credentials, platform
  outage) → stop with the exact blocker and the command/access needed.
- Production preflight lacks critical readiness evidence → report the exact
  missing evidence and complete safe preparation. User authorization to deploy
  does not convert unknown critical controls into verified facts. An explicit
  risk decision remains recorded beside the unchanged readiness findings.
- Artifact, target, authorization, or migration state changes after preflight →
  invalidate record and re-run affected checks.

## Output contract

```text
── deploy report ──────────────────────────
platform:   Vercel (vercel.json) · commit 4f2a91c "fix: debounce search"
preflight:  cleared READY (14:02) · git clean · CLI authed
build:      local ✅ (42s) · env: 9/9 names present in prod
staging:    preview 4f2a91c-x.vercel.app: smoke 3/3 ✅
production: live ✅ · fingerprint 4f2a91c confirmed · smoke 3/3 ✅
            logs clean 5min · HTTPS valid · apex→www ✅
rollback:   vercel rollback <prev-deploy> · migrations: none shipped
evidence:   screenshots + log excerpts inline
```

The report is the deploy's flight record: every claim traceable.


## Optional receipt consistency helper

Use `scripts/check-receipt.py` after collecting sanitized release observations,
not in place of collecting them. Run `python3 <skill-folder>/scripts/check-receipt.py receipt.json`.
Fields: `target` (HTTP URL without credentials/query secrets), `expected_build`,
`observed_build`, `observed_at`, `evidence`, `status` (200), and nonempty `smoke`
observations with `name`, boolean `passed`, and `evidence`. Exit 0 means receipt
consistency, 1 means missing/contradictory observations, 2 means invalid input.
The helper does not fetch a URL, authenticate evidence, deploy, authorize, or
prove freshness. `--self-test` safely rejects bogus CLI success and old builds.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
Read [references/platforms.md](references/platforms.md) only after platform
detection. Read [references/release-protocol.md](references/release-protocol.md)
for production authorization, migrations, evidence, and recovery.
