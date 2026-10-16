# Debugging techniques: the toolbox, by situation

Pick by what you're facing; most bugs need two or three of these.

## Reading failures

- **Stack traces and chained exceptions**: identify the throw site and caller path using this runtime's ordering. Python prints the most recent frame last; other runtimes differ. A wrapper exception can hide the original cause. Library frames are evidence, not automatic blame.
- **First error wins**: in cascading failures, debug the earliest error
  in the log, not the loudest last one.
- **Full messages, always**: truncated errors ("TypeError: cannot read
  properties of undefined") hide the property name that names the
  suspect.
- **Orchestration traces**: correlate tool calls, state transitions, request IDs, and observable outputs across the failing path. Existing traces can help; do not claim traditional APM is universally inadequate or request hidden model reasoning. Redact sensitive payloads and check sampling gaps.

## Reproduction engineering

- **Differential search**: what differs between pass and fail cases?
  Input, timing, environment, user, data shape. The difference is the
  mechanism.
- **Bisection on history**: "it used to work": `git bisect` with the
  failing signal as the test. Blame the commit, not the mood. The signal
  must be deterministic and side-effect-safe; honor the exit contract
  (0 good, 1-127 except 125 bad, 125 untestable/skip) and note that
  skipping near the culprit destroys first-bad precision.
- **Bisection on input**: halve the payload/steps until the failure
  flips; the boundary locates the trigger.
- **Deterministic replay**: freeze time, seed RNG, record and replay
  network (fixtures), pin the DB state. Intermittent bugs are
  underdetermined inputs; determine them.
- **Frequency math**: 1-in-20 flake → look at anything that happens
  ~5% of the time: concurrency windows, caches expiring, hash-order,
  date logic near month boundaries.

## Observation (when prints beat debuggers)

- Log at **boundaries** (function entry/exit, queue consume/produce,
  HTTP in/out) with correlation ids: mid-function spam buries signal.
- Inspect **actual state** in the actual store (query the DB, read the
  cache, decode the JWT): assumptions about what "must be" in the
  database are the classic wrong turn.
- Dump the diff between expected and actual objects, not "it looks
  wrong".

## Hypothesis discipline

- State hypotheses as falsifiable predictions: "if the cache is the
  cause, purging it makes the bug vanish *for exactly one request*".
- Cheapest discriminating test first: one log line that splits two
  hypotheses beats an hour of theorizing.
- The favorite-hypothesis check: if you've spent three experiments
  protecting a hypothesis instead of testing it, promote a rival.

## Environment-shaped bugs

- Works locally, fails in prod: env vars, versions, data volume, case
  sensitivity (filesystems, collations), clocks/timezones, proxies/CDN,
  IAM, feature flags. Diff the environments as inputs.
- Content/config pushes are deploys too: treat channel files, remote
  config, and flag flips as first-class suspects with the same causal
  chain as code.
- Works for user A, fails for user B: data shape, permissions, locale,
  role. Take the two accounts and subtract.
- Dead code left live kills: the Knight Capital router carried a defective
  function unused since 2005 until a 2012 deploy re-armed it (212 orders
  became 4M+, >$460M lost); 97 ignored pre-market alert emails were the
  unread evidence. Suspect dormant code paths after any deploy, and read
  the alerts first.

## Intermittent, concurrent, and distributed failures

Read this section when the failure depends on timing, order, load,
environment, or distribution -- not for every bug.

Intermittence is evidence about hidden inputs. Capture the failure rate with a
sample count, but do not treat a small clean run as proof of absence. Compare
pass/fail runs by release, instance, region, identity, payload, sequence,
clock, queue position, cache state, feature flag, and correlated downstream
request. Freeze time, random seed, fixture, and scheduling only where it is
safe and meaningful.

For races and order failures, use event timelines with monotonic timestamps,
request or trace IDs, ownership of mutable state, and the exact ordering
constraint that was violated. Check idempotency, retries, locks, transactions,
visibility, and duplicate delivery before changing a timeout. For distributed
systems, trace a single causal path across boundaries; timestamps from different
clocks are supporting evidence, not a total order.

For environment-shaped bugs, compare an explicit environment inventory:
runtime/library versions, build artifact, operating system, configuration,
secrets presence only, feature flags, schema, permissions, locale/timezone,
network/proxy, storage collation, resource limit, and data volume. Never copy
production secrets into a local environment to "make it match".

## Fix-selection and verification decision framework

Select the narrowest fix that eliminates the root cause while preserving the
contract. A local guard can be correct when the defect is local; a workaround
is not automatically inferior, but must be called mitigation if it leaves the
cause active. Compare candidates:

| Candidate | Accept only if | Reject or escalate if |
| --- | --- | --- |
| Input validation | it owns the contract and returns actionable behavior | it masks a producer or authorization defect |
| Retry/timeout change | transient failure evidence and bounded idempotent behavior exist | it amplifies load or hides a permanent fault |
| State repair/migration | invariant and affected records are identified, reversible path exists | scope/data loss is uncertain |
| Config rollback | change evidence and rollback safety are known | it removes unrelated fixes or violates compatibility |
| Code fix | causal path is evidenced and a failing test can protect it | broad refactor is standing in for diagnosis |
| Mitigation | user/data impact needs immediate reduction and label is explicit | it is presented as confirmed resolution |

Verification runs at three boundaries where applicable: the minimal reproducer,
the affected public behavior, and the nearest regression suite. Confirm the
original failure case first, then an adjacent valid case and a failure case that
must remain rejected. If a fix changes data, auth, money, schema, or external
side effects, route verification planning through backend/proof and obtain the
appropriate approval.

## When you're stuck

- Re-read the original report: confirmed fixes that "fix" a different
  bug than reported happen constantly.
- Explain the mechanism out loud, step by step, to the rubber duck; the
  step you gloss over is the step you don't actually know.
- Question the Infrastructure: is the failure in *your* code at all?
  Check the layer below (platform, provider, DNS) before deep-diving
  the layer above.
- Take the break; the hypothesis list survives the coffee.
