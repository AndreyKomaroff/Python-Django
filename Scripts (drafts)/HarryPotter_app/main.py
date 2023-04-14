import tkinter as tk

# Список вопросов и ответов
questions = [
    {'question': 'Как называется первая книга "Гарри Поттера"?', 'answers': ['Гарри Поттер и философский камень', 'Гарри Поттер и Мудрость Богов', 'Гарри Поттер и Тайная Комната', 'Гарри Поттер и узник Азкабана'], 'correct_answer': 'Гарри Поттер и философский камень'},
    {'question': 'Кто автор книги "Гарри Поттер и философский камень"?', 'answers': ['Джоан Роулинг', 'Стивен Кинг', 'Джон Толкин', 'С. Лейки'], 'correct_answer': 'Джоан Роулинг'},
    {'question': 'Как звали крылатого коня в серии книг "Гарри Поттер"?', 'answers': ['Фиренце', 'Тобиас', 'Хагрид', 'Гвидо'], 'correct_answer': 'Фиренце'},
    {'question': 'Кто являлся главным учителем защиты от темных искусств в первом году обучения Гарри Поттера в Хогвартсе?', 'answers': ['Куирелл', 'Снейп', 'Макгонагалл', 'Биннс'], 'correct_answer': 'Куирелл'},
    {'question': 'Кто занял должность директора Хогвартса после Альбуса Дамблдора?', 'answers': ['Северус Снейп', 'Долорес Амбридж', 'Минерва Макгонагалл', 'Рубеус Хагрид'], 'correct_answer': 'Северус Снейп'},
    {'question': 'Что делает "Распределяющая шляпа" в Хогвартсе?', 'answers': ['Сортирует новых студентов в одну из четырех коллегий', 'Распределяет студентов по комнатам общежитий', 'Является символом уважения и дисциплины в школе', 'Дает студентам рекомендации по поведению вне Хогвартса'], 'correct_answer': 'Сортирует новых студентов в одну из четырех коллегий'},
    {'question': 'Какую способность имеет героиня Луна Лавгуд?', 'answers': ['Видит привидения', 'Обладает беспрецедентной красотой', 'Владеет магическим исцелением', 'Умеет летать на метле'], 'correct_answer': 'Видит привидения'},
    {'question': 'Кто создал карту бесконечных злодеев в серии книг "Гарри Поттер"?', 'answers': ['Рон Уизли, Фред и Джордж', 'Джеймс Поттер, Сириус Блэк, Питер Петтигрю и Римус Люпин', 'Гермиона Грейнджер', 'Альбус Дамблдор'], 'correct_answer': 'Джеймс Поттер, Сириус Блэк, Питер Петтигрю и Римус Люпин'},
    {'question': 'Какое название носил дневник, в который Том Реддл записывал свои мысли?', 'answers': ['Том Реддл: Секреты темных артефактов', 'Том Реддл: Исследование непознанного', 'Том Реддл: Скелеты в шкафу', 'Том Реддл: За преградой тьмы'], 'correct_answer': 'Том Реддл: Скелеты в шкафу'},
    {'question': 'Кто является главным злодеем в серии "Гарри Поттер"?', 'answers': ['Том Реддл (Волан-де-Морт)', 'Драко Малфой', 'Люциус Малфой', 'Феникс'] , 'correct_answer': 'Том Реддл (Волан-де-Морт)'},
]

# Создание окна и виджетов
window = tk.Tk()
window.title("Тест на тему 'Гарри Поттер'")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Создание элементов интерфейса
question_label = tk.Label(canvas, text='', font=('Arial', 18))
question_label.place(relx=0.5, rely=0.2, anchor='center')

answer_var = tk.StringVar()
answer_var.set('')

answer_a_radio = tk.Radiobutton(canvas, text='', font=('Arial', 14), variable=answer_var, value='', command=lambda: check_answer())
answer_a_radio.place(relx=0.5, rely=0.4, anchor='center')

answer_b_radio = tk.Radiobutton(canvas, text='', font=('Arial', 14), variable=answer_var, value='', command=lambda: check_answer())
answer_b_radio.place(relx=0.5, rely=0.5, anchor='center')

answer_c_radio = tk.Radiobutton(canvas, text='', font=('Arial', 14), variable=answer_var, value='', command=lambda: check_answer())
answer_c_radio.place(relx=0.5, rely=0.6, anchor='center')

answer_d_radio = tk.Radiobutton(canvas, text='', font=('Arial', 14), variable=answer_var, value='', command=lambda: check_answer())
answer_d_radio.place(relx=0.5, rely=0.7, anchor='center')

next_question_button = tk.Button(canvas, text='Следующий вопрос', font=('Arial', 16), command=lambda: next_question())
next_question_button.place(relx=0.5, rely=0.9, anchor='center')

# Счетчик текущего вопроса
current_question = 0

# Обновление вопроса и ответов
def update_question():
    global current_question
    question_label.config(text=questions[current_question]['question'])
    answer_a_radio.config(text='A. {}'.format(questions[current_question]['answers'][0]), value=questions[current_question]['answers'][0])
    answer_b_radio.config(text='B. {}'.format(questions[current_question]['answers'][1]), value=questions[current_question]['answers'][1])
    answer_c_radio.config(text='C. {}'.format(questions[current_question]['answers'][2]), value=questions[current_question]['answers'][2])
    answer_d_radio.config(text='D. {}'.format(questions[current_question]['answers'][3]), value=questions[current_question]['answers'][3])

# Проверка выбранного ответа
def check_answer():
    if answer_var.get() == questions[current_question]['correct_answer']:
        next_question_button.config(state=tk.NORMAL)
    else:
        next_question_button.config(state=tk.DISABLED)

# Переход к следующему вопросу
def next_question():
    global current_question
    current_question += 1
    answer_var.set('')
    next_question_button.config(state=tk.DISABLED)
    if current_question < len(questions):
        update_question()
    else:
        canvas.delete('all')
        result_label = tk.Label(canvas, text='Вы ответили правильно на {} из {} вопросов.'.format(get_correct_answers(), len(questions)), font=('Arial', 24))
        result_label.place(relx=0.5, rely=0.5, anchor='center')

# Получение количества правильно отвеченных вопросов
def get_correct_answers():
    correct_answers = 0
    for question in questions:
        if answer_var.get() == question['correct_answer']:
            correct_answers += 1
    return correct_answers

# Начальное обновление вопроса и ответов
update_question()

# Запуск окна
window.mainloop()