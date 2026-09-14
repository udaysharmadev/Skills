# Discovery map — the deep checklist

Per-ecosystem detection hints for each checklist section. Use what
applies; skip what doesn't; record "not found / N/A" honestly rather than
omitting silently in deep mode.

## 1. Stack and tooling

| Signal | Where |
| --- | --- |
| JS/TS | `package.json` (deps/scripts), lockfile name (`package-lock` vs `pnpm-lock` vs `yarn.lock` vs `bun.lockb`) |
| Python | `pyproject.toml` / `requirements*.txt` / `setup.py`, poetry/uv/pip markers |
| Go | `go.mod`, `go.sum` |
| Rust | `Cargo.toml`, workspace members |
| JVM | `pom.xml` (Maven), `build.gradle[.kts]` (Gradle) |
| Ruby | `Gemfile`, `.ruby-version` |
| PHP | `composer.json` |
| Flutter/Dart | `pubspec.yaml` |
| Mobile | `*.xcodeproj`, `android/app/build.gradle`, `capacitor.config.*`, `app.json` (Expo) |

Frameworks worth naming explicitly: Next/Nuxt/SvelteKit/Remix, Django/
FastAPI/Flask, Rails, Spring, Laravel, Express/Fastify/Hono, gin/echo/
fiber, Actix/Axum.

## 2. Commands (as actually defined)

- `package.json` → `scripts` block
- Python → `[tool.poetry.scripts]`, `Makefile`, `justfile`, CI steps
- Makefile / `justfile` / `Taskfile.yml` anywhere → list the real targets
- CI (`.github/workflows/*.yml`, `.gitlab-ci.yml`) → the commands CI
  actually runs are the source of truth for test/lint/build
- If a command exists nowhere: record `test=none defined` — do not invent

## 3. Entry points and request lifecycle

- Search for bootstrapping: `createApp`, `new Vue`, `App Router`
  `app/` dir, `def create_application`, `func main()`, `@SpringBoot`,
  `app.listen`, serverless handlers, `Dockerfile` CMD/ENTRYPOINT.
- Follow one representative request end-to-end (route → middleware →
  handler → service/model → response). One sentence, real symbols.

## 4. Modules and boundaries

- Top-level directories + one-line responsibility each.
- Note explicit boundaries: monorepo workspaces, module path rules
  (`internal/` in Go, `src/lib` vs `src/app` conventions), dependency
  direction between the 2–3 biggest modules.

## 5. Data models and migrations

- ORM/schema locations: `prisma/schema.prisma`, `drizzle.config.*`,
  `migrations/`, `alembic/`, `django app/models.py`, `db/schema.rb`,
  `ent/`, SQL files.
- List the 3–6 core entities and their relationships — enough for
  planning, not an ER diagram.

## 6. External services and configuration

- Env var **names** from `.env.example`, config modules, `process.env`
  references, `os.environ` — never values.
- Note which services: database, cache, queue, email, storage, auth
  provider, payments, analytics, LLM APIs.

## 7. Auth and state

- Auth: session vs JWT vs OAuth provider vs platform-managed
  (Clerk/Supabase/Auth0); where verification happens (middleware path).
- State: server state (query/ORM patterns) and client state (store
  libraries) — name the approach and where stores live.

## 8. CI/CD

- Workflows present, what each does in five words, deploy target if
  discoverable (Vercel/Netlify/Fly/Render/K8s/none).

## 9. Conventions

- Naming patterns in 5 random files; test file placement; import style;
  comment language; formatter/linter configs found.

## 10. Hotspots (git available)

```bash
# Top churn:
git log --format=format: --name-only since="6 months ago" \
  | grep -v '^$' | sort | uniq -c | sort -rg | head -10
```

```bash
# Top complexity proxy (size):
git ls-files | xargs wc -l 2>/dev/null | sort -rn | head -10
```

Map files against the churn-vs-complexity quadrant:
- **High churn + high size** = active friction zone. Top refactoring priority.
- **Low churn + high size** = landmine. Stable but dangerous to touch.
- **High churn + low size** = config/route files. Normal, but watch for coupling.

Flag the active friction zones in the map's summary line.
