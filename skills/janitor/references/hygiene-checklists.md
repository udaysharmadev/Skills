# Hygiene checklists — run the commands, quote the output

## Local audit

### History and commits

```bash
git log --oneline -30                      # convention inference
git rev-list --count HEAD                  # scale
git count-objects -vH                      # repo weight
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  awk '/^blob/ {print $3, $4}' | sort -rn | head    # biggest blobs
```

- Commit convention: style (conventional/none), scopes, capitalization,
  language. Match it in commit mode.
- Blob embarrassments: committed builds, videos, datasets → propose
  removal (authorization gate if history rewrite needed) + `.gitignore`
  + note LFS for legitimately-large assets.

### Branches and tags

```bash
git branch -vv                             # tracking + stale
git branch --merged main                   # deletable candidates
git for-each-ref --sort=-committerdate refs/heads/
  --format='%(refname:short) %(committerdate:relative)'   # ages
git tag --sort=-creatordate | head         # release reality
```

- Merged-but-alive branches → deletion candidates (confirm before
  deleting; never delete others' unmerged work).
- Stale branches (> 30 days, unmerged) → list with age + last message;
  the owner decides.
- Tags: releases shipped without tags, tag chaos (v1 vs 1.0.0) →
  recommend a convention.

### Working tree and ignore

```bash
git status --porcelain                     # persistent noise
git ls-files -i -c --exclude-standard      # tracked-but-ignored (trap!)
```

- `.env`, `.DS_Store`, logs, editor dirs showing up → add to
  `.gitignore` (with approval — it changes repo behavior).
- Files both tracked *and* ignored → the classic zombie; propose
  `git rm --cached` (stages a real change — explain the push effect).

### Churn hotspots

```bash
git log --format=format: --name-only --since="6 months ago" |
  grep -v '^$' | sort | uniq -c | sort -rg | head -10
```

High churn + large file = fragility signal. Hand the pointer to
`unslop`/`spelunk` — the *why* lives there, not here.

## Remote audit (gh authenticated; probe with `gh auth status`)

| Check | Command | Looking for |
| --- | --- | --- |
| Identity | `gh repo view --json name,description,repositoryTopics` | description/topics matching reality |
| Files | `gh api repos/{owner}/{repo}/contents` | license, CONTRIBUTING, SECURITY present |
| Actions | `gh run list --limit 10` | red X's, never-run stale workflows |
| Releases | `gh release list` | releases vs tags coherence |
| PRs/Issues | `gh pr list --limit 20`, `gh issue list` | rot, missing triage, stale branches referenced |
| Protection | `gh api repos/{owner}/{repo}/branches/main --jq .protected` | unprotected main on a shared repo |

- Public security hygiene: security policy file, no committed secrets in
  *recent* public history, secret-scanning status where available.
- Presentation: README first screen honest (frontpage owns content —
  you flag the gap, frontpage fixes it).
- Recommend, don't mutate: repo settings changes are the owner's click.

## Commit message guide (mode 2)

Good subject: imperative mood, ≤ 50 chars, no trailing period, specific
enough that log-skimming works.

```text
fix: debounce search input to stop request flood

Each keystroke fired a full query; fast typists sent dozens of
overlapping requests and responses raced on render. Debounced at
250ms and aborted in-flight requests on new input.
```

Why > what: the diff shows what changed; the message records the
reason, the rejected alternative worth remembering, and the visible
symptom (so `git log --grep` finds it from the incident).
