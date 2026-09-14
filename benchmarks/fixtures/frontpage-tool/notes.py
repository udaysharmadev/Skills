"""Tiny notes CLI. Stdlib only. Usage: python3 notes.py [--help | add TEXT | list]."""
import argparse
import json
import os

STORE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")


def _load():
    if not os.path.exists(STORE):
        return []
    with open(STORE) as f:
        return json.load(f)


def _save(notes):
    with open(STORE, "w") as f:
        json.dump(notes, f)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Tiny file-backed notes CLI.")
    ap.add_argument("action", nargs="?", default="list", help="add or list")
    ap.add_argument("text", nargs="?", default="", help="note text for add")
    args = ap.parse_args(argv)
    if args.action == "add":
        notes = _load()
        notes.append(args.text)
        _save(notes)
        print(f"added note #{len(notes)}")
    elif args.action == "list":
        for i, note in enumerate(_load(), 1):
            print(f"{i}. {note}")
    else:
        ap.error(f"unknown action {args.action!r}")


if __name__ == "__main__":
    main()
