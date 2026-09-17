# cleared research ledger

## Source 1

Title: Secure Software Development Framework (SSDF) Version 1.1

Author / Organization: NIST

Publication date: 2022-02-03

Version: SP 800-218

URL: https://csrc.nist.gov/pubs/sp/800/218/final

Source type: standard

What it establishes:
Software-release practices should be selected and evidenced according to risk and context.

What this skill adopts:
Choose gate dimensions by artifact type and risk; critical unverified requirements cannot silently pass.

What it does NOT establish:
It does not define one universal release checklist or guarantee production readiness.

Numbers taken from source:
Version 1.1 is the adopted reference version.

Reverify when:
NIST publishes a newer final SSDF version or project risk changes.

## Build provenance

Title: Security levels

Author / Organization: SLSA

Publication date: 2026

Version: SLSA specification 1.2 current guidance

URL: https://slsa.dev/spec/v1.0/levels

Source type: standard

What it establishes:
Build provenance describes the build platform, process, and inputs. Trust and
tamper resistance depend on how provenance is generated and verified.

What this skill adopts:
Bind release evidence to the candidate artifact/commit, distinguish a current
artifact from a remembered green result, and avoid treating provenance presence
as a universal security guarantee.

What it does NOT establish:
It does not require every project to meet a named SLSA level or replace
application, recovery, or acceptance testing.

Numbers taken from source:
No SLSA level is adopted as a release threshold.

Reverify when:
The build platform, artifact provenance, distribution process, or SLSA
specification changes.
