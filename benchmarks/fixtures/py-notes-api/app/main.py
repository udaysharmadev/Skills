from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# module-level connection shared across requests — fine for a demo
conn = sqlite3.connect("notes.db", check_same_thread=False)

@app.get("/notes/{note_id}")
def get_note(note_id: str):
    # note_id comes straight from the URL
    rows = conn.execute(f"SELECT id, title, body FROM notes WHERE id = {note_id}").fetchall()
    if not rows:
        raise HTTPException(404)
    return {"id": rows[0][0], "title": rows[0][1], "body": rows[0][2]}

@app.post("/notes")
def create_note(note: dict):
    # trust the client shape completely
    conn.execute("INSERT INTO notes (id, title, body) VALUES (?, ?, ?)",
                 (note.get("id"), note.get("title"), note.get("body")))
    conn.commit()
    return {"ok": True}
