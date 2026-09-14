# runway — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| The Execution Layer Gap (2025/2026) | Autonomous agents often suffer from "Blind Fire-and-Forget"—executing a deployment command but failing to observe the resulting remote state before declaring success. | Bans "Blind Fire-and-Forget", enforcing a hard requirement to verify the live URL after the deployment tool exits. | SKILL.md §Banned List |
| Dashboard Hallucinations | AI systems incorrectly assume a workflow succeeded because the deployment agent exited 0, while the actual web server is crash-looping. | Bans "Dashboard Hallucination", forcing the agent to verify the exact build fingerprint on the live endpoint. | SKILL.md §Banned List |
| Enterprise Cosplay | Agents trained on generic "best practices" inject massive unnecessary infrastructure complexity (e.g. k8s canary deploys for static sites). | Explicitly names and bans "Enterprise Cosplay", keeping deployment strategy tethered to the actual platform. | SKILL.md §Banned List |

## Key new intelligence encoded

1. **Visible Execution** — mandates that deployment is not complete when the CLI returns, but only when the live URL serves the new build.
2. **Contextual Infrastructure** — stops agents from over-engineering deployment strategies beyond the needs of the detected platform.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agentic CI/CD | Specialist Agent Networks for deployment verification (2026) |
