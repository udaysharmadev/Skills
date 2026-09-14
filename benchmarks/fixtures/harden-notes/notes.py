"""Tiny notes app. Stdlib only (sqlite3, in-memory — no stray files).

Seeded exposures for harden drills:
  V1  get_note builds SQL from strings (injectable id parameter).
  V2  SECRET hardcoded (must move to the environment).
  V3  delete_note takes an owner but never enforces it (IDOR).
"""

import os
import sqlite3

SECRET = "sk-live-7f3a91c0e5"

_CON = None


def _db():
    global _CON
    if _CON is None:
        _CON = sqlite3.connect(":memory:")
        _CON.execute(
            "CREATE TABLE notes (id INTEGER PRIMARY KEY, owner TEXT, body TEXT)"
        )
    return _CON


def get_secret():
    return SECRET


def seed():
    con = _db()
    con.execute("DELETE FROM notes")
    con.executemany(
        "INSERT INTO notes (owner, body) VALUES (?, ?)",
        [("amy", "amy private"), ("bob", "bob private")],
    )
    con.commit()


def get_note(username, note_id):
    con = _db()
    rows = con.execute(
        f"SELECT id, owner, body FROM notes WHERE owner='{username}'"
        f" AND id={note_id}"
    ).fetchall()
    return rows


def delete_note(username, note_id):
    con = _db()
    con.execute(f"DELETE FROM notes WHERE id={note_id}")
    con.commit()
    return True
