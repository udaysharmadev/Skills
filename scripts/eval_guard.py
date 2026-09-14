#!/usr/bin/env python3
"""Paid-agent guard — default-deny gate for billed agent CLIs.

`codex` (and any future paid-quota adapter) must never run because a
default or an automated session chose to. History: on 2026-09-14 the
harness defaults alone produced 186 codex sessions in one day.

Two human-set keys are required TOGETHER, at invocation time:

  1. `--allow-paid` flag on the invoking script, AND
  2. `ALLOW_PAID_AGENT=1` in the environment.

Neither key alone unlocks anything. Agents and automation must never
set these keys on their own initiative — only the user, explicitly
authorizing that specific spend (the equivalent of opening codex
themselves), sets them.

The guard fires only where an agent would actually be invoked:
`--check`, `--list`, and `--dry-run` paths stay ungated (they spawn
nothing). Refusal exits 4 before any subprocess; no results written.
"""
import os
import sys

# Adapters that bill real money per call. Free/local adapters stay out.
PAID_AGENTS = {"codex"}

GUARD_MESSAGE = """\
PAID-AGENT GUARD: refusing to invoke '{agent}' (exit 4).
'{agent}' bills paid quota per call and is default-deny in this repo.
It runs only when a human authorizes THAT run with BOTH keys at once:
  1. --allow-paid          (flag on this very command)
  2. ALLOW_PAID_AGENT=1    (environment variable)
Automation/agents must not set these keys themselves — only the user,
after explicitly deciding to open/spend '{agent}' for this run.
Nothing was invoked; no results were written.
"""


def guard_paid_agent(agent, allow_paid_flag):
    """Refuse paid agents unless both human-set keys are present."""
    if agent not in PAID_AGENTS:
        return
    if allow_paid_flag and os.environ.get("ALLOW_PAID_AGENT") == "1":
        return
    sys.stderr.write(GUARD_MESSAGE.format(agent=agent))
    sys.exit(4)
