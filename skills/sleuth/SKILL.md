---
name: sleuth
description: Evidence-driven root-cause debugging — reproduce, minimize, hypothesize, eliminate, then fix the cause rather than the symptom. Use when something is broken or behaves unexpectedly, when a fix keeps not sticking or a bug is intermittent, or the user says debug, figure out why, or trace this. Forbids random edits — no fix ships without a confirmed root cause and a failing signal that proves it.
---

# sleuth — find the cause, not a place to type

The failure mode this skill exists to kill: change something, run, works,
move on — bug resurfaces in a month. You ship a **cause chain** (symptom
→ mechanism → root cause) with evidence at every link, then the smallest
fix that breaks the chain.

## When NOT to use

- The behavior is correct but slow → `hotpath`.
- The fix is known and documented → `scout` confirms, then just fix it.
- The user wants tests around known-good behavior → `proof`.

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

A test, a command, an assertion — something that fails now and will
flip green when truly fixed. This is the arbiter for everything after;
without it you cannot tell fix from coincidence. (`proof` formalizes it
at the end.)

### 4. Gather evidence

Read errors/stacks fully (bottom frames first — the cause usually lives
there), logs around the failure, the diff between working and broken
(`git bisect` when "used to work" is known), actual data in the actual
store. The full checklist of techniques lives in
`references/techniques.md`.

### 5. Hypothesize — at least two, competing

Track them in a working table, not in your head:

| hypothesis | evidence for | evidence against | next discriminating experiment |
| --- | --- | --- | --- |

"X is null" and "X is fine but the caller passes the wrong id" — if both
explain the evidence, keep both. One hypothesis is an arrest without
investigation. The table forces the question the gut skips: what
experiment separates these two? Run the cheapest one first.

### 6. Eliminate

Run the cheapest discriminating observation per hypothesis (log at the
boundary, reproduce in isolation, binary-search the diff). Update or
kill hypotheses on evidence — never bend evidence to fit the favorite.

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

## The Banned List (Anti-Patterns)

- **The "Guess-and-Check" Loop** — making random code edits and re-running the test hoping it passes, without updating the hypothesis table. If you don't know *why* it should work, don't run it.
- **Amnesia (Action Fingerprinting)** — retrying the exact same fix or tool call that just failed. If a fix fails, the hypothesis is dead. Do not resurrect it with minor syntax tweaks.
- **Hallucinated Fixes** — suggesting a patch before reading the runtime state (logs, stack traces, DB rows). A fix proposed without a confirmed mechanism is a hallucination.

## Provisional fixes (the honest exception)

A workaround is not a root-cause fix — it suppresses the symptom and
rents the bug. When the user explicitly accepts a hotfix without
confirmed root cause (production is down, diagnosis needs days): ship it
labeled `PROVISIONAL — cause unconfirmed` in the report, with the
working hypothesis and the plan to confirm. Still ship the failing
signal, and open the follow-up that converts provisional into
root-cause. Provisional fixes without labels are how bugs get tenure.

## Quality gates

- Cause chain complete: symptom → mechanism → root cause, each link with
  evidence (log line, stack frame, commit, observation).
- ≥ 2 hypotheses were alive at some point (or an explanation of why one
  was forced by the evidence).
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
fix:       handler now dedupes on event id (upsert) — 12 lines
verified:  regression test fails pre-fix, passes post-fix; 50/50
           webhook replay simulation clean
```

The chain is the deliverable. A fix without a chain is provisional —
label it or don't ship it.
