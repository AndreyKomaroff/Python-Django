# Подключаем необходимые библиотеки
import os
import telebot
from telebot import types

# Подключаем базу данных (в данном пример используется sqlite)
import sqlite3
from sqlite3 import Error

# Создаём соединение с базой данных (example.db)
try:
    conn = sqlite3.connect('example.db')
    print("Connected to SQLite")
except Error as e:
    print(e)

# Создаём курсор для работы с базой данных
cur = conn.cursor()

# Создаём таблицу (если она не существует)
cur.execute('''CREATE TABLE IF NOT EXISTS goals
               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               user_id INTEGER,
               goal TEXT, 
               progress TEXT)''')

# Инициализируем бота
bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    # Создаём соединение с базой данных (example.db)
    try:
        conn = sqlite3.connect('example.db')
        print("Connected to SQLite")
    except Error as e:
        print(e)

    # Создаём курсор для работы с базой данных
    cur = conn.cursor()

    # Создаём таблицу (если она не существует)
    cur.execute('''CREATE TABLE IF NOT EXISTS goals
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   user_id INTEGER,
                   goal TEXT, 
                   progress TEXT)''')

    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_goal = types.KeyboardButton('Добавить цель')
    button_progress = types.KeyboardButton('Обновить прогресс')
    button_view = types.KeyboardButton('Посмотреть все цели')
    markup.add(button_goal, button_progress, button_view)

    # приветственное сообщение
    welcome_message = f'Привет, {message.from_user.first_name}! Я твой фитнес-ассистент. Что ты хочешь сделать?'
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)
    conn.close()

# обработчик команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = 'Этот бот поможет Вам отслеживать цели и прогресс в фитнесе. Для начала работы воспользуйтесь командой /start.'
    bot.send_message(message.chat.id, help_message)

# обработчик команды /goal
@bot.message_handler(func=lambda message: message.text == 'Добавить цель')
def add_goal_command(message):
    # Запрос название цели
    bot.send_message(message.chat.id, 'Введите название вашей цели:')
    bot.register_next_step_handler(message, add_goal)

# обработчик названия цели
def add_goal(message):
    goal = message.text
    user_id = message.chat.id

    # Запрос текущего прогресса
    bot.send_message(message.chat.id, 'Введите ваш текущий прогресс:')
    bot.register_next_step_handler(message, add_progress, goal, user_id)

# обработчик текущего прогресса
def add_progress(message, goal, user_id):
    progress = message.text

    # Добавление цели и текущего прогресса в базу данных
    cur.execute("INSERT INTO goals (user_id, goal, progress) VALUES (?, ?, ?)", (user_id, goal, progress))
    conn.commit()

    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_goal = types.KeyboardButton('Добавить цель')
    button_progress = types.KeyboardButton('Обновить прогресс')
    button_view = types.KeyboardButton('Посмотреть все цели')
    markup.add(button_goal, button_progress, button_view)

    # Сообщение об успешном добавлении цели
    success_message = f'Цель "{goal}" была успешно добавлена!'
    bot.send_message(message.chat.id, success_message, reply_markup=markup)

# обработчик команды /add_progress
@bot.message_handler(func=lambda message: message.text == 'Обновить прогресс')
def add_progress(message):
    user_id = message.chat.id
    cur.execute("SELECT * FROM goals WHERE user_id=?", (user_id,))
    rows = cur.fetchall()
    if len(rows) > 0:
        # если цели существуют, запрашиваем дополнительный ввод для обновления прогресса
        bot.send_message(message.chat.id, 'Выберите цель для обновления прогресса', reply_markup=generate_goals_markup(rows))
        bot.register_next_step_handler(message, update_progress, rows)
    else:
        # если целей нет, сообщаем об этом
        bot.send_message(message.chat.id, 'Вы еще не добавили никаких целей')

    # Создаём курсор для работы с базой данных
    cur = conn.cursor()

    user_id = message.from_user.id

    # Вывод списка целей для пользователя
    cur.execute(f"SELECT id, goal FROM goals WHERE user_id={user_id}")
    goals = cur.fetchall()

    if len(goals) > 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for goal in goals:
            markup.add(types.KeyboardButton(goal[1]))
        markup.add(types.KeyboardButton('Отмена'))
        
        bot.send_message(message.chat.id, 'Выберите цель:', reply_markup=markup)

        # Передача дополнительных параметров через lambda-функцию
        bot.register_next_step_handler(message, lambda msg: update_progress(msg, goals))

    else:
        bot.send_message(message.chat.id, 'У вас пока нет целей. Добавьте цель командой /add_goal')

    # Закрытие соединения с базой данных
    conn.close()


# Обновление прогресса пользователем
def update_progress(message, rows):
    try:
        goal_id = int(message.text)
        if not any(goal_id == row[0] for row in rows):
            raise ValueError
        cur.execute("SELECT * FROM goals WHERE id=?", (goal_id,))
        goal_row = cur.fetchone()
        bot.send_message(message.chat.id, f'Введите новый прогресс для цели "{goal_row[2]}":')
        bot.register_next_step_handler(message, save_progress, goal_id)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный ввод, попробуйте снова')
    
def save_progress(message, goal_id):
    progress = message.text
    cur.execute("UPDATE goals SET progress=? WHERE id=?", (progress, goal_id))
    conn.commit()
    bot.send_message(message.chat.id, 'Прогресс успешно обновлен!')
    
    # Закрытие соединения
    conn.close()

# обработчик названия цели
def update_goal(message):
    # Поиск цели в базе данных
    goal = message.text
    user_id = message.chat.id
    cur.execute("SELECT progress FROM goals WHERE user_id=? AND goal=?", (user_id, goal))
    result = cur.fetchone()

    if result:
        # Запрос нового прогресса
        bot.send_message(message.chat.id, 'Введите ваш новый прогресс:')
        bot.register_next_step_handler(message, update_db, goal, result[0])
    else:
        # Клавиатура
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_goal = types.KeyboardButton('Добавить цель')
        button_progress = types.KeyboardButton('Обновить прогресс')
        button_view = types.KeyboardButton('Посмотреть все цели')
        markup.add(button_goal, button_progress, button_view)

        # Сообщение о том, что цель не найдена
        not_found_message = f'Цель "{goal}" не найдена. Попробуйте еще раз.'
        bot.send_message(message.chat.id, not_found_message, reply_markup=markup)

# обработчик нового прогресса
def update_db(message, goal, old_progress):
    new_progress = message.text

    # Обновление цели в базе данных
    cur.execute("UPDATE goals SET progress = ? WHERE goal = ?", (new_progress, goal))
    conn.commit()

    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_goal = types.KeyboardButton('Добавить цель')
    button_progress = types.KeyboardButton('Обновить прогресс')
    button_view = types.KeyboardButton('Посмотреть все цели')
    markup.add(button_goal, button_progress, button_view)

    # Вывод сообщения об успешном обновлении
    success_message = f'Прогресс "{goal}" был успешно обновлён. Старый прогресс: {old_progress}, новый прогресс: {new_progress}.'
    bot.send_message(message.chat.id, success_message, reply_markup=markup)

# обработчик команды /view
@bot.message_handler(func=lambda message: message.text == 'Посмотреть все цели')
def view_goals_command(message):
    user_id = message.chat.id

    # Получение всех целей из базы данных
    cur.execute("SELECT goal, progress FROM goals WHERE user_id=?", (user_id,))
    result = cur.fetchall()

    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_goal = types.KeyboardButton('Добавить цель')
    button_progress = types.KeyboardButton('Обновить прогресс')
    button_view = types.KeyboardButton('Посмотреть все цели')
    markup.add(button_goal, button_progress, button_view)

    # Обработка результатов запроса
    if result:
        goals_message = 'Ваши цели:'
        for goal, progress in result:
            goals_message += f'\n\n{goal}: {progress}'
        bot.send_message(message.chat.id, goals_message, reply_markup=markup)
    else:
        no_goals_message = 'Вы пока не добавили ни одной цели. Для того, чтобы добавить цель, воспользуйтесь командой /goal.'
        bot.send_message(message.chat.id, no_goals_message, reply_markup=markup)

# запускаем бота
bot.polling()