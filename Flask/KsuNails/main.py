from flask import Flask, render_template

app = Flask(__name__)

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Блог', 'url_name': 'blog'}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Главная", menu=menu)

@app.route("/blog")
def blog():
    return render_template('blog.html', title="Блог", menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title="Страница не найдена", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
