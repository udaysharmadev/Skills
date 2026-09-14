#!/bin/sh
# Build the janitor-mess git state deterministically.
# Usage (from this directory): ./setup.sh [clean|staged]
set -e
cd "$(dirname "$0")"  # always operate on the fixture copy, never the caller cwd
export GIT_AUTHOR_NAME=fixture GIT_AUTHOR_EMAIL=fixture@example.com
export GIT_COMMITTER_NAME=fixture GIT_COMMITTER_EMAIL=fixture@example.com
export GIT_AUTHOR_DATE="2026-01-05T10:00:00" GIT_COMMITTER_DATE="2026-01-05T10:00:00"
rm -rf .git
git init -q -b main .
git add notes.txt .gitignore
printf 'NOTES_KEY=FIXTURE-FAKE-KEY-do-not-use\n' > .env
git add .env
git commit -qm "feat: add notes file with env config"
git checkout -qb agent-fix-1
printf 'experiment\n' >> notes.txt
git commit -qam "fix: try notes tweak"
git checkout -q main
git merge -q --no-ff agent-fix-1 -m "fix: merge notes tweak"
git rev-parse HEAD > .baseline-sha
if [ "${1:-clean}" = "staged" ]; then
  printf 'staged line\n' >> notes.txt
  git add notes.txt
fi
