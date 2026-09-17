# Research protocol: evidence that changes a decision

Use this protocol for multiple sources, a compatibility claim, a technology
choice, or a high-consequence factual question. A single documented API fact
usually needs only the source ladder.

## Question and decision record

| Field | Record |
| --- | --- |
| Question | one falsifiable question, not a broad topic |
| Decision | action, owner, and deadline if one exists |
| Scope | installed version, target version, environment, and user constraints |
| Wrong-answer cost | low, material, or high consequence |
| Required confidence | evidence threshold fitting that consequence |
| Recheck trigger | version, configuration, source, or incident change |

Keep observed facts separate from inference. A release note can establish that
a feature changed; an inference that the repository should upgrade must also
consider local integration, migration cost, and user constraints.

## Evidence card

For each load-bearing source, keep: title, publisher, URL or local path,
version or revision, publication date or session check date, applicable scope,
claim supported, and limitation. A source is not stronger merely because it is
longer or newer; versioned product documentation normally outranks a vendor
blog for exact API behavior.

## Compatibility investigation

1. Identify installed and deployed versions plus local wrapper code.
2. Establish observed contract with tests, types, fixtures, or a minimal
   non-mutating reproduction where possible.
3. Read upstream documentation and migration notes for exactly those versions.
4. Compare behavior, defaults, flags, generated artifacts, and removals.
5. Recommend retain, adapt, upgrade, or defer with verification and rollback
   or exit implications.

## Decision comparison

List only credible candidates. Compare them against task criteria: required
behavior, ecosystem fit, maintenance evidence, security posture, migration
effort, operational cost, and exit cost. Popularity is not a decision rule.

## Claim language

- Confirmed: source and scope directly establish the fact.
- Supported inference: facts support the recommendation, assumptions named.
- Unverified: memory, lower-tier report, or unavailable source; do not build a
  production-critical conclusion on it.

When sources remain in conflict, report both claims and the smallest resolving
experiment. An honest uncertainty is more useful than a confident composite.
