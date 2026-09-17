# sleuth research ledger

## Source 1

Title: Signals

Author / Organization: OpenTelemetry project

Publication date: Living documentation

Version: Current documentation

URL: https://opentelemetry.io/docs/concepts/signals/

Source type: official docs

What it establishes:
Traces, metrics, and logs provide complementary observations of system behavior.

What this skill adopts:
Use telemetry to discriminate among competing hypotheses and connect symptom, mechanism, root cause, and fix.

What it does NOT establish:
Telemetry correlation does not by itself prove causation.

Numbers taken from source:
No retry or hypothesis-count threshold is adopted.

Reverify when:
Observability guidance or system evidence changes.

## Hypothesis-driven troubleshooting

Title: Effective Troubleshooting

Author / Organization: Google SRE

Publication date: 2016

Version: SRE book chapter

URL: https://sre.google/sre-book/effective-troubleshooting/

Source type: official docs

What it establishes:
Troubleshooting is an iterative hypothesis-and-test process. Triage, system
knowledge, telemetry, safe experiments, and notes help avoid spurious
correlation and premature conclusions.

What this skill adopts:
Maintain competing falsifiable hypotheses, choose discriminating experiments,
record negative results and confounders, and stabilize user impact before deep
diagnosis in an incident.

What it does NOT establish:
It does not prove a local fix is safe in a particular production system or
replace incident-management authority.

Numbers taken from source:
No fixed experiment count or reproduction threshold is adopted.

Reverify when:
The operating model, incident process, or system architecture changes.

## Regression localization

Title: git-bisect

Author / Organization: Git project

Publication date: 2026

Version: Current documentation

URL: https://git-scm.com/docs/git-bisect

Source type: official docs

What it establishes:
Git bisect can use good/bad revisions and a test command to localize a change
range, including handling commits that cannot be classified.

What this skill adopts:
Use bisection only with a deterministic, inexpensive, side-effect-safe signal,
and report skipped commits and the remaining uncertainty.

What it does NOT establish:
It does not prove that the first bad commit is the root cause, particularly
when configuration, data, or a dependency changed separately.

Numbers taken from source:
None.

Reverify when:
Repository history, test determinism, or relevant deployment/configuration
history changes.
