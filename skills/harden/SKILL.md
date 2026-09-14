---
name: harden
description: Defensive security audit and evidence-backed hardening — systematic attack-surface reduction, never an "unhackable" claim. Use when handling auth, payments, PII, uploads, admin surfaces or public deployment, when the user mentions security, vulnerabilities, hardening or pentest-style checks, or before go-live. Threat-models first, then audits secrets, dependencies, injection, XSS, CSRF, SSRF, access control, configuration and headers per OWASP Top 10:2025 with ASVS 5.0.0 depth. Every finding carries severity, confidence, evidence and remediation. No destructive exploitation, ever.
---

# harden — shrink the attack surface, prove what you claim

The honest goal: **systematic attack-surface reduction + evidence-backed
hardening**. No tool guarantees 100% security; anyone claiming it is
selling something. Every finding states severity *and* confidence, and
every fix is retested.

## Prerequisites

Read access to the code under audit plus a runnable path for safe
adversarial checks (local run, test accounts, staging). Testing anything
you don't own or lack written authorization for is refused, not scoped
down.

## Tool selection/fallback

- Ecosystem audit tooling (`npm audit`, `pip-audit`, …) → dependency
  signal, triaged by exploitability in this app, never CVSS theater.
- Runnable app + test accounts → safe adversarial verification
  (malformed input, unsigned webhooks, own-account IDOR, logic abuse).
- Static only (no run, no accounts) → code-path findings with
  `confidence: probable` at best; dynamic claims marked unverified with
  what would confirm them.

## When NOT to use

- General code quality → `referee`.
- "Is our architecture scale-resilient?" → `headroom`.
- Active testing of systems you don't own or lack written authorization
  for → refuse and explain; this skill audits the user's own/authorized
  applications only.

## Threat model first (the audit is scoped by it)

Before any checklist: what does the system hold (PII? money? health?
secrets?), who would attack it (opportunistic bots, competitors,
disgruntled users, organized actors), where the trust boundaries are
(public input, file uploads, webhooks, admin, **AI features accepting text
or external data — Indirect Prompt Injection per OWASP GenAI Top 10**), 
and the blast radius if each fails. Is there **Excessive Agency** (an AI with 
unmonitored write access)? The threat model decides which checklist sections 
are top-priority — a recipe blog and a payments processor do not get the same audit.

## Modes (scope decides, threat model confirms)

| Mode | Scope |
| --- | --- |
| **quick security review** | one feature/PR surface; top exposures only |
| **feature threat model** | trust boundaries + abuse cases for a proposed design, before code |
| **full repository audit** | the complete process below |
| **pre-release hardening** | full audit + the deployment-config and secrets checks cleared for go-live |
| **auth/authz review** | identity, session, and object-level authorization paths end to end |
| **API review** | input validation, authz, rate limits, error semantics per endpoint |

## Process

**threat model → static checks → dependency checks → configuration
checks → authorization review → safe adversarial verification → fixes →
retest**

1. **Static checks** — secrets in code/history, dangerous patterns,
   unsafe deserialization, injection-prone query construction (grep +
   read; see `references/attack-surface.md`).
2. **Dependency checks** — audit tooling for the ecosystem (`npm audit`,
   `pip-audit`, `cargo audit`, …), abandoned deps, suspicious transitive
   additions; findings triaged by actual exploitability, not CVSS theater.
3. **Configuration checks** — env handling, security headers, CORS,
   cookies, debug modes, default credentials, error verbosity.
4. **Authorization review** — every endpoint/resource: who can access
   what, object-level checks, admin surfaces, IDOR hunting.
5. **Safe adversarial verification** — attack *your authorized app* like
   a defender: inject malformed input, send unsigned webhooks, attempt
   IDOR against your own test accounts, abuse business logic
   (double-submit, negative quantities). PoCs minimal and contained.
6. **Fix and retest** — remediations land with a test that fails on the
   old code; re-run the adversarial check to confirm closure.

## Finding format (mandatory for every finding)

severity (critical/high/medium/low) · confidence (confirmed/probable/
speculative) · evidence (exact reproduction or code path) · **attack
precondition** (what the attacker needs: an account? network position?
a crafted link? nothing?) · affected code · plausible impact ·
remediation · verification status (open / fixed + retested /
accepted-risk by user). The precondition is what separates a real
exposure from a scary-sounding impossible one.

Severity honesty rules: exploitability × impact decides — a "critical"
CVE in an unreachable code path is a false alarm here. **Ban CVSS Theater:** Do not list 50 theoretical vulnerabilities from an `npm audit` if they are not actually exploitable in this specific context (e.g., a regex DoS in a dev-only build script). Speculative findings say `confidence: speculative` instead of dressing up as facts. No invented CVSS scores, no fear-language without evidence.

## Rules of engagement

- **No destructive exploitation** — no DoS, no data destruction, no
  privilege escalation beyond your own test accounts, nothing that
  touches real user data or production integrity.
- **Authorization to test is assumed for the user's own app; anything
  else requires it in writing.**
- Findings with product implications (auth provider migration, RLS
  redesign) get surfaced as decisions, not silently "fixed".
- Secrets found → report location + rotation plan; never print the
  secret value in full.

## Quality gates

- Threat model written before findings; audit sections prioritized by it.
- Every finding complete per the format — severity AND confidence AND
  evidence; zero fear-mongering without reproduction.
- Every applied fix retested (adversarial check re-run); regression test
  added per `proof` rules.
- Retest results stated per finding; anything "accepted-risk" is the
  user's explicit call, recorded.

## Stop conditions

- Audit delivered (or fixes + retest complete) → summary, stop.
- Critical finding requires a product decision → stop, surface with
  options.
- Scope exceeds the code (infrastructure, cloud config the agent can't
  see) → audit what's visible, list the blind spots explicitly as
  unverified.

## Output contract

Chat: threat model (6 lines max), findings table (sev · confidence ·
where · what · status), fixes + retest results, top 3 residual risks.
On request or for serious audits: `docs/reports/security-<slug>.md` with
provenance header — same content, no padded pages.
