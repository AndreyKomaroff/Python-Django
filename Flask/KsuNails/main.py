from flask import Flask, render_template, request, g
import sqlite3
import os

# конфигурация
DATABASE = '/tmp/main.db'
DEBUG = True
SECRET_KEY = 'aKL;L83acvpavla832lfaoa495723c;4jja489'
USERNAME = 'admin'
PASSWORD = 'Kamap999!'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'main.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    # Вспомогательная функция для создания таблиц БД
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

#create_db()

def get_db():
    # Соединение с БД, если оно еще не установлено
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    # Закрываем соединение с БД, если оно было установлено
    if hasattr(g, 'link_db'):
        g.link_db.close()

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Блог', 'url_name': 'blog'}
]

@app.route("/")
@app.route("/home")
def home():
    db = get_db()
    return render_template('home.html', title="Главная", menu=menu)

@app.route("/blog")
def blog():
    return render_template('blog.html', title="Блог", menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title="Страница не найдена", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
