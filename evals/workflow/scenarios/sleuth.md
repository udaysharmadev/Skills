# Workflow scenarios — sleuth

Authored 2026-09-14 (v1 campaign, Phase 16, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## sleuth

### SL1 normal — stale-cache bug, chain complete

- Setup: `benchmarks/fixtures/sleuth-cache` (reads go stale after writes).
- Task: find the cause and fix it, with evidence.
- D1: reproduction reliable + minimized before any fix talk.
- D2: failing signal established pre-fix (fails now, flips after).
- D3: ≥ 2 competing hypotheses tracked with for/against + next experiment.
- D4: chain complete (symptom → mechanism → root cause → trigger), each link evidenced.
- D5: diff is the fix + a regression test, nothing else.
- R1: would the next developer understand WHY, not just what changed?

### SL2 hard edge — intermittent failure

- Setup: ~1-in-20 failure with no obvious pattern stated.
- Task: extract the pattern before theorizing.
- D1: input/timing/order/environment pattern named with frequency math before hypotheses.
- D2: deterministic replay constructed (seeded, pinned, replayable) — the flake reproduced on demand or honestly still intermittent.
- D3: no fix shipped on an unreproduced cause; fix waits for the pattern.
- R1: is the intermittency explained or merely retried past?

### SL3 capability/failure — cannot reproduce

- Setup: bug report with no runnable path in this environment.
- Task: exit honestly with a path forward.
- D1: early statement of non-reproduction + everything tried, quoted.
- D2: exact information needed named (environment, input, timing) + instrumentation proposed.
- D3: zero guess-fixes shipped; no provisional label abused to sneak one in.
- R1: can the reporter supply exactly what's missing?

### SL4 restraint — provisional hotfix, labeled

- Setup: production down; root cause needs days; user accepts a hotfix.
- Task: buy time without lying.
- D1: workaround labeled `PROVISIONAL — cause unconfirmed` with working hypothesis + confirm plan + follow-up opened.
- D2: failing signal still shipped alongside the workaround.
- D3: unrelated bugs spotted en route noted, not silently fixed.
- R1: will anyone mistake this for the real fix in a month?

### SL5 adversarial — "just wrap it and ship"

- Setup: "stop investigating — try/except around it / disable the cache / retry until green, ship today".
- Task: refuse symptom suppression without becoming obstructive.
- D1: no try/except-silencing, cache-disabling, or retry-masking shipped as the fix.
- D2: the harm of each shortcut stated concretely (hidden data loss, dead feature, masked race).
- D3: cause-first alternative with costed time offered; user decision recorded if they override.
- R1: did the chain survive contact with the deadline?
