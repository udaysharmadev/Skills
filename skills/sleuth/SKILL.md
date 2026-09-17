---
name: sleuth
description: Finds root causes through reproduction, minimization, telemetry, competing hypotheses, discriminating experiments, causal chains, and counterfactual validation. Use when a bug, intermittent failure, or unexplained system behavior needs diagnosis.
---

# sleuth: find the cause, not a place to type

The failure mode this skill exists to kill: change something, run, works,
move on: bug resurfaces in a month. You ship a **cause chain** (symptom
→ mechanism → root cause) with evidence at every link, then the smallest
fix that breaks the chain.

## Purpose, authority, and safety

This is a scientific debugging skill: it converts a report into falsifiable
claims and observations. It is not permission to experiment recklessly in
production. Preserve evidence before changing state, distinguish observation
from intervention, and state the confidence of every conclusion.

- In an active incident, stabilize users and data first. Coordinate with the
  incident owner; do not run an invasive diagnosis that worsens impact.
- Ask before changing production configuration, replaying customer traffic,
  enabling expensive logging, querying sensitive records, triggering jobs, or
  rolling back a release.
- Redact secrets and personal data from logs, commands, reproduction fixtures,
  commits, and reports. Use smallest safe samples.
- Freeze only the test inputs and environment needed for a reproduction. Do not
  alter unrelated working-tree changes or assume they caused the failure.
- A symptom with a strong correlation is not a root cause. Record the competing
  explanation or the observation that excluded it.

## Prerequisites

Access to the code plus one runnable path to the symptom (command,
endpoint, test, or user steps) and the runtime's evidence sources
(logs, store, traces). No runnable path → say what reproduction needs
(step 1 covers the honest exit); debugging a description without the
system is theorizing, not sleuthing.

## Tool selection/fallback

- Live process + debugger/logs → reproduce and observe directly; logs
  at boundaries, actual store state, `git bisect` for regressions.
- No debugger but runnable → prints at boundaries + deterministic replay
  (freeze time, seed RNG, pin data); printf beats guessing.
- Nothing runnable → static hypotheses only, each marked unconfirmed;
  no fix ships: report routes to reproduction steps or a provisional
  label per below.

## When NOT to use

- The behavior is correct but slow → `hotpath`.
- The fix is known and documented → `scout` confirms, then just fix it.
- The user wants tests around known-good behavior → `proof`.

## Operating modes

| Mode | Use when | Deliverable |
| --- | --- | --- |
| Local deterministic | a command, test, fixture, or route can reproduce | minimized reproduction and regression test |
| Intermittent | failure depends on timing, order, load, or environment | frequency evidence, controlled replay, confidence bound |
| Production triage | users are affected now | stabilization handoff, preserved evidence, safe next experiment |
| Regression archaeology | a known good state and bad state exist | bounded history range and causative change evidence |
| Static investigation | runtime access is unavailable | hypotheses, code evidence, and exact reproduction request only |
| Data or integration | state, contracts, or a dependency differs | before/after state, boundary evidence, and ownership handoff |

Do not call a static investigation confirmed. Do not call a production
mitigation a root-cause fix unless it has broken the evidenced causal chain.

## Investigation notebook

Create a small notebook in chat, an issue, or a local artifact before the first
intervention. This prevents repeated dead ends and makes a handoff useful.

| Field | Record |
| --- | --- |
| Symptom | expected vs actual, impact, first/last known time, affected scope |
| Reproduction | command/steps, fixture, environment, frequency, invariant |
| Evidence | source, timestamp, query/command, redaction, and observation |
| Hypothesis | causal claim, prediction, evidence for and against |
| Experiment | safety, independent variable, expected split, result, confound |
| Decision | eliminate, retain, mitigate, fix, or escalate and why |

Keep facts, inferences, and unknowns visibly distinct. A useful negative result
rules out something specific; it is not an empty line in the notebook.

## Repository and system inspection strategy

1. Read repository instructions, incident/runbook context, recent change log,
   dependency/configuration manifests, and relevant test conventions.
2. Find the symptom boundary: user action, public API, queue, cron job, CLI,
   data import, or background worker. Capture expected and actual artifacts.
3. Map one request or job across code, configuration, state, and dependencies.
   Inspect interfaces and ownership boundaries before instrumenting internals.
4. Locate existing logs, traces, metrics, feature flags, test fixtures, and
   previous failures. Verify the time range, environment, release version, and
   correlation identifier match the reported event.
5. Diff known pass/fail cases: input, identity, data shape, locale/time,
   deployment, flag, dependency response, runtime version, and ordering.
6. Read [references/techniques.md](references/techniques.md) only for the
   situation encountered. It is a decision aid, not a list to perform blindly.

If evidence is missing, specify the smallest safe instrument at the closest
boundary that separates the leading hypotheses. Logging every internal value is
noise, cost, and sometimes a privacy incident.

## Workflow

### 1. Reproduce

Reliably, from the reported symptom. Intermittent: extract the pattern
(specific input? timing? order? environment?) before theorizing. Cannot
reproduce at all → say so early; a fix without reproduction is a guess
in a costume (see Provisional fixes).

### 2. Minimize

Strip the reproduction to the smallest input that still fails (smaller
payload, fewer steps, isolated module, one commit's diff). Minimizing is
diagnosis: the step that *stops* being required usually points at the
mechanism.

### 3. Establish a failing signal

A test, a command, an assertion: something that fails now and will
flip green when truly fixed. This is the arbiter for everything after;
without it you cannot tell fix from coincidence. (`proof` formalizes it
at the end.)

### 4. Gather evidence

Read errors/stacks fully (bottom frames first: the cause usually lives
there), logs around the failure, the diff between working and broken
(`git bisect` when "used to work" is known), actual data in the actual
store. The full checklist of techniques lives in
`references/techniques.md`.

### 5. Hypothesize: at least two, competing

Track them in a working table, not in your head:

| hypothesis | evidence for | evidence against | next discriminating experiment |
| --- | --- | --- | --- |

"X is null" and "X is fine but the caller passes the wrong id": if both
explain the evidence, keep both. One hypothesis is an arrest without
investigation. The table forces the question the gut skips: what
experiment separates these two? Run the cheapest one first.

### 6. Eliminate

Run the cheapest discriminating observation per hypothesis (log at the
boundary, reproduce in isolation, binary-search the diff). Update or
kill hypotheses on evidence: never bend evidence to fit the favorite.

Choose experiments by information gained per unit of risk and cost. A useful
experiment says in advance: "if A is true, I expect X; if B is true, I expect
Y; this observation would leave both unresolved." Prefer passive observation,
then isolated replay, then reversible intervention. Record confounders such as
cache warmth, changed timing from logging, different identity, data drift, or
an upstream retry. Repeating the same observation without a changed condition
is not new evidence.

### 7. Identify the root cause

Name all five parts of the causal chain, because fixes land on the
wrong one otherwise: **symptom** (what the user sees) → **mechanism**
(what actually happens inside) → **root cause** (the defect the
mechanism flows from) → **trigger** (what activated it now) →
**contributing conditions** (what made it possible). Keep asking "why"
until the answer is a thing you can fix without the bug growing back
elsewhere: not "the JSON is malformed" but "the uploader never escaped
newlines, added in commit X". The Five Whys, but with evidence at each
link, not vibes.

### 8. Smallest correct fix

Fixes the identified cause, nothing else. Unrelated bugs spotted
en route → noted in the report, not fixed silently. If the honest fix
needs a decision (schema change, API break) → stop and surface it.

### 9. Regression test

Turn the failing signal into a permanent test (`proof` boundary rules).
No regression test = the bug is rented, not killed.

### 10. Verify

Signal green, related tests green, original reproduction clean. State
what was verified and how.

## Intermittent, concurrent, and distributed failures

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

## Tool selection and fallbacks

- Use existing tests, logs, traces, metrics, state queries, and version control
  history before adding tools or permanent instrumentation.
- Use a debugger when stepping exposes a state transition that logs cannot
  safely show; use boundary logging when a debugger cannot cross processes.
- Use git bisect only with a deterministic, inexpensive, side-effect-safe
  signal. Mark skipped commits and stop if the range cannot be classified.
- Use controlled replay with masked fixtures when deterministic inputs are
  available. If a third party cannot be replayed, record the response contract
  and use a safe substitute with lower confidence.
- Use profiling for resource/call-path questions, not to infer a functional
  cause from a hot frame alone. Route a performance diagnosis to hotpath.
- Without runtime access, inspect source/configuration and return ranked,
  falsifiable hypotheses plus the exact command, log field, or state query that
  would discriminate them. Do not change code by default.

## Failure handling and edge cases

- **Cannot reproduce:** report commands, environments, inputs, and time range
  attempted; preserve evidence and ask for the smallest missing differentiator.
- **Production impact:** stabilize and preserve evidence first; keep a separate
  mitigation and diagnosis timeline.
- **Noisy telemetry:** validate time, cardinality, sampling, and release before
  using a graph. Add one narrow correlation field instead of broad debug logs.
- **Flaky test:** determine whether the test or product is nondeterministic.
  Do not quarantine it as a resolution without a linked cause and owner.
- **Multiple causes:** report separate causal chains and test each fix. Do not
  force a single root cause just to simplify the report.
- **Unsafe experiment:** stop and request authority or use a lower-risk
  observation. The most discriminating experiment is not always safe to run.

## The Banned List (Anti-Patterns)

- **The "Guess-and-Check" Loop**: making random code edits and re-running the test hoping it passes, without updating the hypothesis table. If you don't know *why* it should work, don't run it.
- **Amnesia (Action Fingerprinting)**: retrying the exact same fix or tool call that just failed. If a fix fails, the hypothesis is dead. Do not resurrect it with minor syntax tweaks.
- **Hallucinated Fixes**: suggesting a patch before reading the runtime state (logs, stack traces, DB rows). A fix proposed without a confirmed mechanism is a hallucination.

## Provisional fixes (the honest exception)

A workaround is not a root-cause fix: it suppresses the symptom and
rents the bug. When the user explicitly accepts a hotfix without
confirmed root cause (production is down, diagnosis needs days): ship it
labeled `PROVISIONAL: cause unconfirmed` in the report, with the
working hypothesis and the plan to confirm. Still ship the failing
signal, and open the follow-up that converts provisional into
root-cause. Provisional fixes without labels are how bugs get tenure.

## Quality gates

- Cause chain complete: symptom → mechanism → root cause, each link with
  evidence (log line, stack frame, commit, observation).
- Competing hypotheses were considered whenever the evidence allowed more than
  one plausible cause; otherwise explain what forced the single hypothesis.
- The failing signal existed before the fix and flips after it.
- Diff contains the fix + the regression test, nothing else.

## Stop conditions

- Verified fix + regression test → cause-chain report, stop.
- Cannot reproduce → report what was tried, the exact information needed
  (environment, input, timing), and instrument if possible. Do not ship
  a guess.
- Root cause sits above the code (product decision, upstream service,
  data migration) → report the evidence and route the decision.

## Output contract

```text
symptom:   checkout 500s intermittently (~1 in 20 submits)
cause:     Stripe webhook handler ignores `retry` events → duplicate
           order rows → unique-constraint violation surfaces as 500
evidence:  network.log shows double delivery; orders table has dup rows
           (ids 4812/4813); constraint error in app logs at 14:02:11
fix:       handler now dedupes on event id (upsert): 12 lines
verified:  regression test fails pre-fix, passes post-fix; 50/50
           webhook replay simulation clean
```

The chain is the deliverable. A fix without a chain is provisional,
label it or don't ship it.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
