from fastapi import FastAPI #импорт класса
from pathlib import Path #для путей
from pydantic import BaseModel #импорт для создания схемы данных
import sqlite3 #импорт SQLite

BASE_DIR = Path(__file__).resolve().parent.parent #путь до папки backend
DB_PATH = BASE_DIR / "database" / "app.db" #путь до папки с бд

def init_db(): #создание функции для базы данных
    conn = sqlite3.connect(DB_PATH) #подключение к базе данных через путь DB_PATH
    cursor = conn.cursor() #создали курсор (метод соединения который создаёт объект курсор, для дальнейшего выполнения SQL-запросов)
    cursor.execute
    ("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT)""") #создаём таблицу users (если её ещё нет)
    conn.commit() #сохраняем изменения в базе
    conn.close() #закрываем соединение с базой
    init_db() #вызываем эту функцию

app = FastAPI() #создаем переменную с классом FastAPI

class SignUP(BaseModel): #создаем класс SignUP на проверки данных (на основе BAaseModel)
    userNameUp: str 
    userEmailUp: str
    userPasswordUp: str #схема данных и их типы

@app.post("/sign_up") #
def sign_up(userup: SignUP):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (userup.userEmailUp,))
    if cursor.fetchone():
        conn.close()
        return {"ok": False, "detail": "Email already exists"}
    
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (userup.userNameUp, userup.userEmailUp, userup.userPasswordUp)
    )
    conn.commit()
    conn.close()
    return {"name": userup.userNameUp}

class SignIn(BaseModel):
    userNameIn: str
    userPasswordIn: str

@app.post("/sign_in")
def sign_in(payload: SignIn):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, password FROM users WHERE name = ?", (payload.userNameIn,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"ok": False, "detail": "User not found"}

    user_id, name, stored_password = row
    if stored_password != payload.userPasswordIn:
        return {"ok": False, "detail": "Wrong password"}

    return {"ok": True, "id": user_id, "name": name}










