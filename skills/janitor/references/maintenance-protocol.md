# Maintenance protocol: repository changes with an audit trail

Use this reference for an actual hygiene change. It does not authorize the
change; it makes an already-authorized change safer to execute.

## Action record

| Field | Capture |
| --- | --- |
| Finding | command-backed observation and current state |
| Target | exact path, ref, tag, setting, or staged set |
| Action class | observe, propose, reversible local, or collaborative/destructive |
| Authorization | user wording and exact operation allowed |
| Preconditions | merge state, protection, ownership, clean tree, or remote access |
| Verification | post-action command and expected state |
| Recovery | undo path, or why history/remote recovery is not simple |

Refresh preconditions immediately before a mutation. A ref changed after audit
is a new target.

## Branch and tag candidates

Before proposing removal, inspect exact ref, merge relationship to intended
base, upstream tracking, unique commits, open reviews if accessible,
protection, and worktree use when visible. Report uncertainty rather than
deleting a ref whose owner or purpose is unknown. Branch and tag deletion
always require explicit approval even when merged.

## Ignore and tracked files

An ignore rule affects future untracked files; it does not remove a tracked
file. Before suggesting index removal, identify whether teammates or builds
need the artifact and whether it contains generated, deployment, or local-state
content. Explain that index removal changes future clones. Verify status and a
targeted clean checkout or build path after an approved change when practical.

## Release and remote metadata

Tags, releases, default branches, protections, workflows, topics, and
descriptions can participate in automation and public trust. Audit them
read-only first. For a remote change, show exact setting and intended value,
affected automation or contributors, then wait for owner approval. Never infer
a release convention from one tag.

## Recovery

If a mutation creates unexpected state, stop further actions. Capture status,
ref state, and command result. Use the least invasive rollback only when it is
authorized and clearly restores recorded state; otherwise present evidence and
ask. Never use force operations as generic cleanup.

## Reporting language

- Candidate: branch is merged into stated base, but no deletion was made.
- Executed: exact approved ignore rule was added; status and targeted build
  passed afterward.
- Deferred: remote protection needs owner decision; no settings changed.

Do not call a finding fixed until its recorded verification shows intended
postcondition.
