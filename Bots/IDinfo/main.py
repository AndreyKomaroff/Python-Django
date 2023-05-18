import telebot
import sqlite3
import os

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(content_types=['text'])
def send_id(message):
    user_id = str(message.chat.id)
    nick_name = str(message.from_user.username)
    name = str(message.from_user.first_name)
    surname = str(message.from_user.last_name)

    bot.send_message(message.chat.id, 'Your id: ' + user_id + '\nNickname: ' + nick_name + '\nName: ' + name + '\nSurname: ' + surname)

    with open('user_ids.txt', 'a') as f:
        f.write(user_id + "\n" + nick_name + "\n" + name + "\n" + surname + "\n")
    
    conn = sqlite3.connect('user_ids.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id int, nick_name varchar, name text, surname text)")
    cursor.execute("INSERT INTO users (user_id, nick_name, name, surname) VALUES (?, ?, ?, ?)", (user_id, nick_name, name, surname))
    conn.commit()

bot.polling()