# Host permissions and sandboxes

Hosts may enforce read-only modes, workspace sandboxes, command allowlists,
network restrictions, native approval prompts, or organization policy. These
controls are external authority, not inconveniences for a skill to route around.

## Detect

Use host-provided state when available. If the mode or policy cannot be
observed, call it unknown. Do not infer broad permission from one successful
action.

Recheck official host documentation before naming a current mode, setting, or
configuration path. Those details change faster than this portable skill.

## Operate

- Prefer work that fits the active sandbox.
- Batch related safe reads when that reduces native prompt churn.
- Never combine unrelated risky actions to obtain one broad approval.
- Treat an approval as authority for the exact action and scope shown.
- Preserve the user's dirty state and external resources.
- A denial ends that branch. Continue independent safe work.

## Report

Use precise language:

```text
Blocked by host permission: [action].
Completed independently: [work not dependent on it].
Needs user action: [the smallest host-native approval or configuration step].
```

A skill may explain the host's native approval-memory mechanism once. It must
not edit host security settings, click approval controls on the user's behalf,
or disguise a denied action as another command.
