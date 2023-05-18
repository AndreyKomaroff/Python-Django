from flask import Flask, render_template, request, g, flash, abort
from fDataBase import FDataBase
import sqlite3
import os

# конфигурация
DATABASE = '/tmp/post.db'
DEBUG = True
SECRET_KEY = 'aKL;L83acvpavla832lfaoa495723c;4jja489'
USERNAME = 'admin'
PASSWORD = 'Kamap999!'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'post.db')))

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

create_db()

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
        {'title': 'Блог', 'url_name': 'blog'},
        {'title': 'Добавить пост', 'url_name': 'add_post'}
]

@app.route("/")
@app.route("/home")
def home():
        return render_template('home.html', title="Главная", menu=menu)

@app.route("/post/<int:id_post>")
def showPost(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(id_post)
    if not title:
        abort(404)
 
    return render_template('post.html', menu=menu, title=title, post=post)

@app.route("/blog")
def blog():
        db = get_db()
        dbase = FDataBase(db)
        return render_template('blog.html', title="Главная", menu=menu, posts=dbase.getPostsAnonce())


@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    db = get_db()
    dbase = FDataBase(db)
 
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['image'], request.form['post'])
            if not res:
                flash('Ошибка добавления статьи', category = 'error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')
 
    return render_template('add_post.html', title="Добавление статьи", menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title="Страница не найдена", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
