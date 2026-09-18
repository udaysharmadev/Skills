# Contributing

Thanks for helping improve the bundle. The repository holds contributions to
the same standard as its skills: evidence, restraint, verification, and no
generic instruction padding.

## What belongs here

A useful behavior change usually adds one or more of:

- non-obvious specialist decision logic;
- prevention for a demonstrated failure mode;
- a capability-aware tool or fallback;
- a verification or completion contract;
- restraint—when the skill should not act, should stop, or needs approval.

Do not add “best practices” a capable model already knows. More words are not
more intelligence, and a helper script is justified only when deterministic
execution materially improves reliability.

## Changing research-backed behavior

Include the complete chain in one pull request:

1. **Reason:** the observed weakness or decision that needs to change.
2. **Evidence:** prefer primary/official sources; community anecdotes identify
   failure modes, not ground truth.
3. **Research note:** update `docs/research/<skill>.md` with only sources that
   materially changed the skill and record tempting rejected ideas when useful.
4. **Runtime change:** update `SKILL.md`, a conditional reference, or a helper
   at the layer where the behavior belongs.
5. **Trace:** make the research note’s **Where encoded** field point to current
   reality.

Do not copy source text. Mark fast-moving sources and unresolved uncertainty.
Research notes stay outside runtime context.

## Skill contract

Every changed skill must remain self-contained and satisfy [PRD §8](PRD.md):
purpose, clear trigger and non-trigger, prerequisites, workflow, tool selection
and fallback, quality gates, stop conditions, output contract, and discoverable
references. Keep `SKILL.md` at or below 500 lines; conditional depth belongs in
`references/`.

The public set is frozen at 28. Proposals should improve an existing owner, not
create a near-duplicate skill. Any future change to that set needs an explicit
product decision rather than arriving through an ordinary pull request.

## Before opening a pull request

```bash
scripts/validate-skills
scripts/check-names
scripts/check-links
scripts/build-docs
scripts/check-context
scripts/test-regressions
scripts/run-evals
```

- Add or update trigger cases in `evals/trigger/cases.md` when frontmatter or
  routing behavior changes.
- Regenerate `docs/skills/INDEX.md` after frontmatter changes; never edit it by
  hand.
- Run every changed helper with representative input and include the observed
  output in the pull request.
- Keep each pull request to one coherent concern. Existing benchmark fixtures
  do not need to run unless the change touches evaluation infrastructure.

Use the pull request template. For bugs, exact requests and transcripts are
more useful than summaries; remove secrets and personal data first.
