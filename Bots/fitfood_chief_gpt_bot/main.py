import openai
from dotenv import load_dotenv
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json
import asyncio
import multiprocessing
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import re
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from urllib.parse import quote_plus

# Загружаем переменные из .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
telegram_token = os.getenv('TELEGRAM_TOKEN')  # Токен Telegram-бота

# Данные для подключения к MySQL
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# Формируем строку подключения к MySQL
MYSQL_PASSWORD = quote_plus(os.getenv('MYSQL_PASSWORD'))
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


# Создаем подключение к базе данных
engine = create_engine(DATABASE_URL, pool_recycle=3600, pool_size=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Определяем модель для хранения сообщений
class Message(Base):
    __tablename__ = "fitfoodchief_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), index=True)
    user_message = Column(Text)
    bot_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Создаем таблицу, если её нет
Base.metadata.create_all(bind=engine)

# Функция для сохранения сообщений в базу
def save_message(user_id, user_message, bot_response):
    db = SessionLocal()
    message = Message(
        user_id=user_id,
        user_message=user_message,
        bot_response=bot_response
    )
    db.add(message)
    db.commit()
    db.close()

# Функция для загрузки конфигурации прокси
def load_proxy_config():
    with open("proxy_config.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Настройка прокси
proxies = load_proxy_config()
session = requests.Session()
session.proxies = proxies

# Настройка повторных попыток
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Использование сессии для запросов с прокси в OpenAI
openai.requestssession = session

# Загрузка промпта из файла
def load_prompt():
    with open("prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

def remove_markdown(text):
    # Удаление заголовков (например ####)
    text = re.sub(r'^\s{0,3}(#{1,6})\s*(.*?)\s*#*\s*(?:\n|$)', r'\2\n', text, flags=re.MULTILINE)

    # Удаление жирного текста, курсива, зачёркиваний и инлайн-кода
    text = re.sub(r'(\*\*|__|\*|_|`|~{1,2})(.*?)\1', r'\2', text)

    return text.strip()

# История сообщений
messages = [{"role": "system", "content": load_prompt()}]

# Функция общения с GPT
def chat_with_bot(user_id, user_message):
    messages.append({"role": "user", "content": user_message})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini", messages=messages
        )
        bot_response = response['choices'][0]['message']['content']
        
        # Очищаем от markdown
        bot_response_clean = remove_markdown(bot_response)

        messages.append({"role": "assistant", "content": bot_response_clean})

        # Сохраняем в базу данных
        save_message(user_id, user_message, bot_response_clean)

        return bot_response_clean
    except Exception as e:
        return f"Произошла ошибка: {e}"

# FastAPI приложение
app = FastAPI()

class UserInput(BaseModel):
    user_id: str
    message: str

@app.post("/chat/")
async def chat(user_input: UserInput):
    try:
        response = chat_with_bot(user_input.user_id, user_input.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Telegram-бот команды
async def start(update, context):
    await update.message.reply_text("Привет, я FitFood Chief — бот тренера Андрея Комарова. Помогу подобрать простые и вкусные ЗОЖ-рецепты, чтобы поддержать энергию и достичь ваших фитнес-целей. Меню составлено из натуральных ингредиентов, сбалансировано по калориям и полезным веществам. С FitFood Chief готовить легко и приятно! Что хотите включить в меню и какие у вас цели?")

async def handle_message(update, context):
    user_id = str(update.message.chat_id)
    user_message = update.message.text
    response = chat_with_bot(user_id, user_message)
    await update.message.reply_text(response)

# Функция запуска Telegram-бота
def run_telegram_bot():
    print("Запуск Telegram-бота...")  # DEBUG
    application = Application.builder().token(telegram_token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот готов к запуску run_polling()...")  # DEBUG
    application.run_polling()

# Функция запуска FastAPI
def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8002, log_level="info")

if __name__ == "__main__":
    # Запускаем FastAPI и Telegram-бота в разных процессах
    fastapi_process = multiprocessing.Process(target=run_fastapi, daemon=True)
    telegram_process = multiprocessing.Process(target=run_telegram_bot, daemon=True)

    fastapi_process.start()
    telegram_process.start()

    # Ожидаем завершения процессов
    fastapi_process.join()
    telegram_process.join()
