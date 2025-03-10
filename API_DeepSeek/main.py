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

# Загружаем переменные из .env
load_dotenv()
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')  # Токен Telegram-бота

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

# Использование сессии для запросов с прокси в DeepSeek
openai.requestssession = session

# Настраиваем OpenAI API для работы с DeepSeek
openai.api_key = DEEPSEEK_API_KEY
openai.base_url = "https://api.deepseek.com/v1"

# Загрузка промпта из файла
def load_prompt():
    with open("prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

# История сообщений
messages = [{"role": "system", "content": load_prompt()}]

# Функция общения с DeepSeek
def chat_with_bot(user_message):
    messages.append({"role": "user", "content": user_message})
    
    try:
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=messages
        )
        bot_response = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": bot_response})
        return bot_response
    except Exception as e:
        return f"Произошла ошибка: {e}"

# FastAPI приложение
app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/chat/")
async def chat(user_input: UserInput):
    try:
        response = chat_with_bot(user_input.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Telegram-бот команды
async def start(update, context):
    await update.message.reply_text("Привет! Я ваш персональный ассистент. Чем могу помочь?")

async def handle_message(update, context):
    user_message = update.message.text
    response = chat_with_bot(user_message)
    await update.message.reply_text(response)

# Функция запуска Telegram-бота
def run_telegram_bot():
    print("Запуск Telegram-бота...")
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот готов к запуску run_polling()...")
    application.run_polling()

# Функция запуска FastAPI
def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

if __name__ == "__main__":
    # Запускаем FastAPI и Telegram-бота в разных процессах
    fastapi_process = multiprocessing.Process(target=run_fastapi, daemon=True)
    telegram_process = multiprocessing.Process(target=run_telegram_bot, daemon=True)

    fastapi_process.start()
    telegram_process.start()

    # Ожидаем завершения процессов
    fastapi_process.join()
    telegram_process.join()
