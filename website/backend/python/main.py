from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def init_db():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.post("/authorization")
async def authorization(request: Request):
    data = await request.json()
    username = data.get("userName")
    password = data.get("userPassword")

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    return {"message": "User saved", "username": username}