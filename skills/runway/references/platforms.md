# Platform playbook — one methodology, per-platform specifics

The workflow in SKILL.md is identical everywhere; only the commands and
config differ. "What good looks like" per platform — extend this file
as real deployments accumulate (never fabricate from memory; scout
verifies current CLI behavior).

## Vercel (first-class)

- Signals: `vercel.json`, `.vercel/`, Next/Nuxt/etc. framework presets.
- Auth: `vercel whoami` · env: `vercel env ls <env>` (names only) ·
  deploy: `vercel deploy` (preview), `vercel deploy --prod`.
- Previews are the superpower: every branch gets a URL — verify there
  first, always.
- Post-deploy: `vercel ls` confirms the deployment; alias/domains via
  `vercel domains`/`vercel alias`; rollback: `vercel rollback`.
- Migrations: none managed by Vercel — external DB (Neon/Supabase/…)
  applies them as a pre-deploy step with the same safety rules.

## Netlify / Cloudflare Pages (similar shape)

- Signals: `netlify.toml`, `wrangler.toml`/`wrangler.jsonc`.
- Auth + deploy via their CLIs (`netlify deploy`, `wrangler pages
  deploy`); preview deployments per branch; env via dashboard/CLI
  (`netlify env:*`).
- Rollback: previous deployment promote (`netlify restore`,
  wrangler rollback) — verify the exact command with scout when first
  used on a project.

## Containers (Docker → anywhere)

- Signals: `Dockerfile`, `compose.yaml`, `.dockerignore`.
- Local build first: `docker build -t app:sha .` — the sha tags the
  exact artifact; the same image that was built is the image that ships.
- Registry push → platform pull (Fly/Railway/Render/ECS/k8s).
- Health check: the container's health endpoint (compose
  `healthcheck`, platform equivalents); rollout status watched, not
  assumed.
- Rollback: redeploy the previous image tag — which is why tags are
  immutable shas, never `latest`.

## VPS / systemd (the boring classic)

- Build artifact or container shipped over SSH; systemd unit with
  `Restart=on-failure`; Nginx/Caddy in front for TLS (Caddy automates
  certs).
- Env via a root-owned env file, never in the unit file or the repo.
- Rollback: previous artifact directory + symlink flip; DB backup
  before migrations (`pg_dump`/`mysqldump` verified restorable).
- Smoke: `curl` the health endpoint through the public domain, verify
  TLS, watch `journalctl` for startup errors.

## Static sites (GitHub Pages / object storage)

- Build output deployed — verify the *generated* files (the HTML
  actually contains the meta tags), not just "upload finished".
- CDN cache: state the invalidation status; stale-cache false alarms
  are the #1 static-deploy confusion.
- Rollback: previous artifact directory/versioned bucket prefix.

## Kubernetes (when it's real)

- Signals: manifests/Helm/kustomize under `deploy/` or `k8s/`.
- `kubectl rollout status deployment/app` is the deploy truth; readiness
  probes gate traffic; `kubectl rollout undo` is the rollback.
- Migrations: init-container/job pattern, never in the app start-up
  path of every replica.

## Mobile (EAS / store pipelines)

- Build via `eas build` (or native pipelines); stores impose review
  timelines that are outside anyone's control — report them as external
  state, never as failures.
- Rollback = phased release pause/halt or store-managed version revert.
- Smoke = the built binary on a device/simulator for the release
  critical paths.

## Universal post-deploy evidence (every platform)

1. version fingerprint proving the new build is live;
2. health endpoint status + timing;
3. 2–3 smoke paths with results;
4. first-minutes log scan (clean or findings);
5. domain/HTTPS status;
6. the rollback command, stated with its preconditions.
