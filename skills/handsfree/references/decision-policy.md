# Interruption Taxonomy & Decision Policy

This document defines the default behaviors for common execution scenarios under the `handsfree` policy.

| Scenario Category | Default Action | Ask? | Log? | Required Evidence |
|-------------------|----------------|------|------|-------------------|
| **Routine execution** | Just do it. | No | No | N/A (Standard tool operation) |
| **Technical ambiguity** | Research & infer. | No | Only if highly material | Docs, adjacent code, project conventions |
| **Recoverable failure** | Diagnose, correct, retry (bounded). | No | No | Error logs, stack traces |
| **Scope expansion** | Stick to the original requested scope. | No | No | User's initial prompt |
| **Product-intent ambiguity** | Infer if trivial; escalate if material. | Yes (if material) | Yes (to `recall`) | Clear difference in end-user experience |
| **External side effect** | Halt unless explicitly authorized. | Yes | Yes | Explicit user request |
| **Destructive action** | Block (e.g., dropping DB). | Yes | Yes | Verification of intent |
| **Cost-bearing action** | Block (unless pre-authorized). | Yes | Yes | Explicit user authorization |
| **Security-sensitive action** | Defer to `cleared` / `harden`. | Yes | Yes | Security policies |
| **Production action** | Defer to `runway`. | Yes | Yes | Deployment authorization |

## Application Guidelines

1. **Ask = Yes** means this is a Class-3 Human Gate. You must stop, formulate a clear default recommendation if possible, and batch it with any other pending questions.
2. **Log = Yes** means the decision should be summarized at the end of the run and optionally handed to `recall` if it will affect future sessions.
3. If multiple categories apply, the most restrictive (highest Ask/Log requirement) takes precedence.
