#!/usr/bin/env python3
"""Refresh the skills.sh install-count badge endpoint data.

Source of truth: the public, unauthenticated skills.sh search API
(the same endpoint the `skills` CLI itself queries):
    GET https://skills.sh/api/search?q=skill&owner=udaysharmadev&limit=200

The response carries a per-skill `installs` field. This script sums the
rows whose `source` is exactly `udaysharmadev/skills` and writes
`assets/skills-sh-endpoint.json` in the shields.io endpoint schema, so the
README badge shows a measured number — never a hand-typed one.

Only ONE HTTP request per run: the search API is rate-limited (429s observed
under burst traffic). Do not loop per-skill queries.

Usage: scripts/update-install-badge.py [--output assets/skills-sh-endpoint.json]
Exit non-zero on network/API failure so scheduled CI fails loudly instead of
committing a stale count.
"""
import argparse
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = "udaysharmadev/skills"
API_URL = "https://skills.sh/api/search?q=skill&owner=udaysharmadev&limit=200"
PACK_URL = "https://www.skills.sh/udaysharmadev/skills"


def fetch_counts():
    req = urllib.request.Request(API_URL, headers={"User-Agent": "Skills-install-badge/1.0"})
    with urllib.request.urlopen(req, timeout=30) as res:
        payload = json.load(res)
    per_skill = {}
    for entry in payload.get("skills", []):
        if entry.get("source") == SOURCE and entry.get("skillId"):
            per_skill[entry["skillId"]] = int(entry.get("installs", 0) or 0)
    if not per_skill:
        raise ValueError(f"no rows for source {SOURCE!r} in API response")
    return per_skill


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(ROOT / "assets" / "skills-sh-endpoint.json"))
    args = ap.parse_args()

    per_skill = fetch_counts()
    total = sum(per_skill.values())
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    endpoint = {
        "schemaVersion": 1,
        "label": "skills.sh installs",
        "message": str(total),
        "color": "blue",
        "cacheSeconds": 86400,
        # Audit trail (ignored by shields.io, read by humans/validators).
        "source": PACK_URL,
        "api": API_URL,
        "updated": now,
        "total": total,
        "perSkill": dict(sorted(per_skill.items())),
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    previous = None
    if out.exists():
        previous = json.loads(out.read_text()).get("total")
    out.write_text(json.dumps(endpoint, indent=2) + "\n")

    print(f"OK: {SOURCE} total installs = {total} across {len(per_skill)} skills (was {previous})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # fail loudly; never commit a stale count
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
