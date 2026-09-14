# Debugging techniques — the toolbox, by situation

Pick by what you're facing; most bugs need two or three of these.

## Reading failures

- **Stack traces bottom-up** — the top frame says where it threw; the
  bottom app frames say why your code got there. Library-internal frames
  are a trail, not the culprit.
- **First error wins** — in cascading failures, debug the earliest error
  in the log, not the loudest last one.
- **Full messages, always** — truncated errors ("TypeError: cannot read
  properties of undefined") hide the property name that names the
  suspect.
- **Trace-Based Observability (2026)** — for agentic or orchestrated systems, traditional APMs hide the bug. Read the full execution trace (tool calls, state transitions, reasoning steps), not just the final HTTP 500.

## Reproduction engineering

- **Differential search** — what differs between pass and fail cases?
  Input, timing, environment, user, data shape. The difference is the
  mechanism.
- **Bisection on history** — "it used to work": `git bisect` with the
  failing signal as the test. Blame the commit, not the mood.
- **Bisection on input** — halve the payload/steps until the failure
  flips; the boundary locates the trigger.
- **Deterministic replay** — freeze time, seed RNG, record and replay
  network (fixtures), pin the DB state. Intermittent bugs are
  underdetermined inputs; determine them.
- **Frequency math** — 1-in-20 flake → look at anything that happens
  ~5% of the time: concurrency windows, caches expiring, hash-order,
  date logic near month boundaries.

## Observation (when prints beat debuggers)

- Log at **boundaries** (function entry/exit, queue consume/produce,
  HTTP in/out) with correlation ids — mid-function spam buries signal.
- Inspect **actual state** in the actual store (query the DB, read the
  cache, decode the JWT) — assumptions about what "must be" in the
  database are the classic wrong turn.
- Dump the diff between expected and actual objects, not "it looks
  wrong".

## Hypothesis discipline

- State hypotheses as falsifiable predictions: "if the cache is the
  cause, purging it makes the bug vanish *for exactly one request*".
- Cheapest discriminating test first — one log line that splits two
  hypotheses beats an hour of theorizing.
- The favorite-hypothesis check: if you've spent three experiments
  protecting a hypothesis instead of testing it, promote a rival.

## Environment-shaped bugs

- Works locally, fails in prod: env vars, versions, data volume, case
  sensitivity (filesystems, collations), clocks/timezones, proxies/CDN,
  IAM, feature flags. Diff the environments as inputs.
- Works for user A, fails for user B: data shape, permissions, locale,
  role. Take the two accounts and subtract.

## When you're stuck

- Re-read the original report — confirmed fixes that "fix" a different
  bug than reported happen constantly.
- Explain the mechanism out loud, step by step, to the rubber duck; the
  step you gloss over is the step you don't actually know.
- Question the Infrastructure: is the failure in *your* code at all?
  Check the layer below (platform, provider, DNS) before deep-diving
  the layer above.
- Take the break; the hypothesis list survives the coffee.
