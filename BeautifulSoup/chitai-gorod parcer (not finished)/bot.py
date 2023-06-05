import telebot
import os
from main import collect_data

#API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('6009105167:AAE2EB7FFrDTv6xY9VRE2AN3u_wzRlacnis')

@bot.message_handler(commands=['start'])
def return_books(message):
    bot.send_message(message.chat.id, collect_data())
    #books_file_path = os.path.abspath("books_01_06_2023_19_38.json")

    #with open(books_file_path, 'rb') as f:
    #    bot.send_document(message.chat.id, f)


bot.polling()