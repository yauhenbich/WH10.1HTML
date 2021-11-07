from flask import Flask

app = Flask(__name__)

vocab = {
    'cat': 'кошка',
    'python': 'питон',
    'flask': 'фляга',
    'developer': 'разработчик',
    'django': 'джанго',
    'framework': 'фреймворк',
    'package': 'библиотека',
    'library': 'библиотека',
}

@app.route("/<key>/")
def translate(key):
    value = vocab.get(key, False)
    if value:
        return f"Значение для ключа {key} - {value}"
    return "Ключ не найден", 404


if __name__ == '__main__':
    app.run()
