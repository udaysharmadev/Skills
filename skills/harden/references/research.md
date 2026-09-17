# harden research ledger

This ledger records the sources that alter this skill's behavior. It is not a
claim that every control, risk category, or testing method applies to every
system.

## Application Security Verification Standard

Title: Application Security Verification Standard

Author / Organization: OWASP Foundation

Publication date: 2025

Version: 5.0.0

URL: https://owasp.org/projects/asvs

Source type: standard

What it establishes:
ASVS provides a versioned basis for specifying and verifying web application
security controls, including architecture/threat modeling, authentication,
access control, validation, cryptography, and logging.

What this skill adopts:
Select control families from the threat model, version any ASVS identifiers in
reports, and require evidence plus retesting rather than checklist completion.

What it does NOT establish:
It does not determine a system's threat model, prove a scanner finding is
reachable, or produce a universal severity score.

Numbers taken from source:
Version 5.0.0 is the reviewed stable reference.

Reverify when:
OWASP releases a newer stable ASVS or a regulated scope imposes another control
baseline.

## API and authorization risks

Title: OWASP API Security Top 10 and Authorization Cheat Sheet

Author / Organization: OWASP Foundation

Publication date: 2023-2026

Version: API Security Top 10 2023 and current cheat-sheet guidance

URL: https://api-security.owasp.org/editions/2023/en/0x00-header/

Source type: official docs

What it establishes:
Object/property/function authorization, business-flow access, resource use,
configuration, inventory, and unsafe upstream API consumption are material API
risk classes. Authorization should be deny-by-default and least-privilege.

What this skill adopts:
Map subject, object, action, context, and enforcement point for sensitive paths;
require controlled negative authorization checks where safely possible.

What it does NOT establish:
It does not prescribe a specific authorization model, response code, ORM, or
database policy for every application.

Numbers taken from source:
The Top 10 category count is not used as an audit score.

Reverify when:
OWASP updates the API risk edition or the system's identity model changes.

## Threat-modeling method

Title: Threat Modeling Cheat Sheet

Author / Organization: OWASP Foundation

Publication date: 2026

Version: Current Cheat Sheet Series guidance

URL: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html

Source type: official docs

What it establishes:
Threat modeling benefits from identifying assets, actors, boundaries, and attack
scenarios. STRIDE is one illustrative method among multiple valid approaches.

What this skill adopts:
Model assets, actors, boundaries, entry points, assumptions, and attack chains
before using category checklists. Treat STRIDE as a prompt set, not a ritual.

What it does NOT establish:
It does not make every STRIDE category relevant to every component or replace
authorized testing and concrete implementation evidence.

Numbers taken from source:
None.

Reverify when:
The system gains a new trust boundary or a more specific domain threat model is
available.

## Secure software development lifecycle

Title: Secure Software Development Framework

Author / Organization: National Institute of Standards and Technology

Publication date: 2022-02

Version: SP 800-218 Revision 1.1

URL: https://csrc.nist.gov/pubs/sp/800/218/final

Source type: standard

What it establishes:
SSDF describes high-level secure software development practices that can be
integrated with existing lifecycle approaches to reduce vulnerabilities and
improve response to them.

What this skill adopts:
Treat security as design, implementation, verification, deployment, and
remediation evidence rather than a final scanner-only stage.

What it does NOT establish:
It does not mandate a particular CI provider, scanning product, evidence format,
or release decision.

Numbers taken from source:
Version 1.1 identifies the reviewed publication.

Reverify when:
NIST supersedes SP 800-218 or the organization's secure-development policy
changes.

## Agentic and generative AI security

Title: OWASP Top 10 for LLM and Generative AI Applications

Author / Organization: OWASP Gen AI Security Project

Publication date: 2025

Version: 2025 edition

URL: https://genai.owasp.org/llm-top-10/

Source type: official docs

What it establishes:
Prompt injection, improper output handling, supply-chain risks, data/model
poisoning, excessive agency, and unbounded consumption are relevant risk areas
for LLM and agentic systems.

What this skill adopts:
Treat retrieved content, prompts, model output, memory, and tool results as
untrusted; minimize tool functionality, permissions, and autonomy; enforce
authorization in downstream systems; bound cost and side effects.

What it does NOT establish:
It does not mean every AI feature needs a separate platform, that prompt filters
are sufficient authorization, or that all agents require human approval for
every reversible action.

Numbers taken from source:
The top-ten list is not used as a maturity score.

Reverify when:
The agent/tool architecture, model provider, or OWASP GenAI guidance changes.

## Security telemetry

Title: ASVS Security Events guidance

Author / Organization: OWASP Foundation

Publication date: 2025

Version: ASVS 5.0 taxonomy

URL: https://cornucopia.owasp.org/taxonomy/asvs-5.0/16-security-logging-and-error-handling/03-security-events

Source type: official docs

What it establishes:
Authentication operations and failed authorization attempts are relevant
security events; sensitive data should not be logged merely to make events rich.

What this skill adopts:
Require security-review findings to consider both observable security signals
and log-data minimization.

What it does NOT establish:
It does not require logging every user action or retaining logs indefinitely.

Numbers taken from source:
None.

Reverify when:
The system's logging/privacy policy or relevant ASVS guidance changes.
