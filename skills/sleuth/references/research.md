Current access pass: 2026-10-14. Publication dates and versions below remain
source claims, not inferred from access date. Previously cited sources not
listed in the current pass are preserved historical provenance, not newly
verified. No agent-effectiveness or compatibility claim follows from this ledger.

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

Publication date: git manual version 2.56.0 (2026-09-28)

Version: 2.56.0 (checked 2026-10-17)

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

## Current decision and source records

Changed artifacts: `SKILL.md` (hypotheses/failure handling) and `techniques.md` (exception/trace interpretation)

Behavior changed: Separate failed intervention from rejected prediction; runtime-specific exception order; competing hypotheses only when plausible; observable traces without hidden reasoning.

Title: Effective Troubleshooting

Author / Organization: Google SRE

Publication date: 2016

Version: SRE book chapter

URL: https://sre.google/sre-book/effective-troubleshooting/

Source type: official docs

What it establishes:
Hypothesis-driven observation supports diagnosis, not guaranteed causation.

What this skill adopts:
Apply the current decision above at the affected boundary; preserve existing
workflow when evidence does not justify change.

What it does NOT establish:
It does not prove this skill improves an agent or validate an unobserved runtime.

Numbers taken from source:
Only version identifiers; no comparative measurement.

Reverify when:
The source, installed version, affected contract or tool capability changes.

Access: fetched 2026-10-14; source-specific breadth and live evaluations remain
pending. Offline fallback: inspect available code/configuration and label
source-sensitive behavior unverified.

Title: traceback

Author / Organization: Python Software Foundation

Publication date: living; retrieved 2026-10-14

Version: 3.15 documentation; target runtime must be detected

URL: https://docs.python.org/3/library/traceback.html

Source type: official docs

What it establishes:
Exception chains and frame order are runtime-specific.

What this skill adopts:
Apply the current decision above at the affected boundary; preserve existing
workflow when evidence does not justify change.

What it does NOT establish:
It does not prove this skill improves an agent or validate an unobserved runtime.

Numbers taken from source:
Only version identifiers; no comparative measurement.

Reverify when:
The source, installed version, affected contract or tool capability changes.

Access: fetched 2026-10-14; source-specific breadth and live evaluations remain
pending. Offline fallback: inspect available code/configuration and label
source-sensitive behavior unverified.

Title: Signals

Author / Organization: OpenTelemetry

Publication date: living; date not established

Version: current concepts documentation

URL: https://opentelemetry.io/docs/concepts/signals/

Source type: official docs

What it establishes:
Traces, logs and metrics are complementary observations.

What this skill adopts:
Apply the current decision above at the affected boundary; preserve existing
workflow when evidence does not justify change.

What it does NOT establish:
It does not prove this skill improves an agent or validate an unobserved runtime.

Numbers taken from source:
Only version identifiers; no comparative measurement.

Reverify when:
The source, installed version, affected contract or tool capability changes.

Access: fetched 2026-10-14; source-specific breadth and live evaluations remain
pending. Offline fallback: inspect available code/configuration and label
source-sensitive behavior unverified.
