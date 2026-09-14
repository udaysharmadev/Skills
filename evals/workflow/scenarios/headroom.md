# Workflow scenarios — headroom

Authored 2026-09-14 (v1 campaign, Phase 10, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## headroom

### HR1 normal — growing workload, three levels

- Setup: 10k users today, 10× growth expected in a year, read-heavy workload, single region.
- Task: produce the Now/Next/Scale design.
- D1: all three levels present; each Next/Scale item carries a trigger metric (not a vibe).
- D2: load numbers shown with arithmetic (users → req/s at peak, units on everything).
- D3: at least one explicit "don't do yet" item.
- R1: are the gaps between levels the actual advice (what's deliberately deferred)?

### HR2 hard edge — tiny workload, restraint graded

- Setup: 50-user college project, maybe 500 next year, one developer.
- Task: design it without embarrassment.
- D1: Now level is boring (one app + managed DB or equivalent); no Kafka/Kubernetes/microservices anywhere.
- D2: response says the headroom out loud (e.g. "100× headroom at current arithmetic").
- D3: total response proportionate (no 200-line design doc for a class project).
- R1: did restraint read as competence or as dismissal?

### HR3 capability/failure — no numbers obtainable

- Setup: user cannot provide traffic, data size, or growth ("no idea, just make it scale").
- Task: design without numbers.
- D1: no cargo-cult numbers presented as the user's ("millions of requests" banned).
- D2: delivers the decision framework: the estimate ranges that would flip each choice + what to measure first.
- D3: unknowns labeled as estimates with visible arithmetic, conclusions stress-tested ("survives 10× off" or not, stated).
- R1: is the framework actionable the moment real numbers arrive?

### HR4 restraint — premature distribution request

- Setup: 200 daily users; user asks "should we split into microservices".
- Task: answer the question, not the ambition.
- D1: verdict is "no" with the trigger that WOULD justify the split (metric + threshold), not a lecture.
- D2: offers what to do instead now (modular monolith seams that keep the option cheap).
- D3: no resume-driven patterns smuggled in as "best practice".
- R1: does the "no" preserve the user's dignity and future options?

### HR5 adversarial — "design for a billion users"

- Setup: side project with 100 users; user demands billion-user architecture "to be safe".
- Task: hold proportionality under fantasy-scale pressure.
- D1: no billion-user machinery recommended for today (sharding/event-sourcing/multi-region all land in Scale-or-later with triggers, or "don't do yet").
- D2: arithmetic shown proving the gap (current load vs claimed scale, orders of magnitude apart).
- D3: response doesn't mock; it redirects to the real risks (the single box's actual failure modes).
- R1: did the design stay honest without condescension?
