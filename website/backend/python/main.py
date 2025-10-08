from fastapi import FastAPI #импорт класса
from pathlib import Path #для путей
from pydantic import BaseModel #импорт для создания схемы данных
import sqlite3 #импорт SQLite
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent.parent #путь до папки backend
DB_PATH = BASE_DIR / "database" / "app.db" #путь до папки с бд
print("👉 База данных создаётся здесь:", DB_PATH)
DB_PATH.parent.mkdir(parents=True, exist_ok=True) #создаем папку database

def init_db(): #создание функции для базы данных
    print("Создаю таблицу users...")
    conn = sqlite3.connect(DB_PATH) #подключение к базе данных через путь DB_PATH
    cursor = conn.cursor() #создали объект, курсор (метод соединения который создаёт объект курсор, для дальнейшего выполнения SQL-запросов)
    cursor.execute
    ("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT
    )
    """) #создаём таблицу users (если её ещё нет)
    conn.commit() #сохраняем изменения в базе
    conn.close() #закрываем соединение с базой
    print("Таблица users создана или уже существует.")
    
init_db() #вызываем эту функцию

app = FastAPI() #создаем объект с классом FastAPI

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # "*" — разрешить всем, потом можно указать конкретный сайт
    allow_credentials=True,
    allow_methods=["*"],        # разрешаем все методы (POST, GET, OPTIONS)
    allow_headers=["*"],        # разрешаем все заголовки
)

class SignUP(BaseModel): #создаем класс SignUP на проверки данных (на основе BAaseModel)
    userNameUp: str 
    userEmailUp: str
    userPasswordUp: str #схема данных и их типы

@app.post("/sign_up") #связываем объект app с HTTP-методом POST и указываем маршрут
def sign_up(userup: SignUP): #создаем функцию sign_up для POST запроса из маршрута декоратора в которой она примет информацию в переменную userup и преобразует ее через класс SignUp в нужный нам формат
    conn = sqlite3.connect(DB_PATH) #создаем переменную связывающую базу данных с путем DB_PATH
    cursor = conn.cursor() #создаем объект (курсор) (метод для взаимодействия с базой данных через мостик в виде conn)

    cursor.execute("SELECT id FROM users WHERE email = ?", (userup.userEmailUp,)) #отправляем запрос в бд 
    if cursor.fetchone(): #проверяем уникальность email с помощью cursor.execute и метода fetchone (который выдает нам строку из результата поиска)
        conn.close() #закрываем соединение
        return {"ok": False, "detail": "Name already exists"} #если этот email не нашелся, то есть он уникален
    
    cursor.execute( 
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
        (userup.userNameUp, userup.userEmailUp, userup.userPasswordUp) #задаем базе данных вставть полученные данные в нужные места таблицы (name, email, password) делаем это казалось бы лишнее движение для защиты от SQL-инъекций
    )
    conn.commit() #сохраняем изменения в базе данных
    conn.close() #закрываем соединение
    return {"ok": True} #если все будет успешно - получим True

class SignIn(BaseModel): #создаем класс SignIn на основе BaseModel
    userNameIn: str 
    userPasswordIn: str #задаем нужные нам данные и их типы

@app.post("/sign_in") #присваеваем POST-запрос страничке sign_in
def sign_in(userin: SignIn): #создаем функцию sign_in 
    conn = sqlite3.connect(DB_PATH) #создаем переменную с путем до бд (для связи с бд)
    cursor = conn.cursor() #создаем курсор для взаимодействия с бд
    cursor.execute("SELECT id, name, password FROM users WHERE name = ?", (userin.userNameIn,)) #отправляем запрос в бд 
    row = cursor.fetchone() #проверяем существование этого имени в бд
    conn.close() #закрываем соединение

    if not row: #если не будет найдено отправить обратно:
        return {"ok": False, "detail": "User not found"}

    user_id, name, stored_password = row #создаем перемнную со значениями из бд
    if stored_password != userin.userPasswordIn: #если пароль не соответвствует выдавать следующий текст:
        return {"ok": False, "detail": "Wrong password"}

    return {"ok": True, "id": user_id, "name": name} #deли соответствует выдавать







