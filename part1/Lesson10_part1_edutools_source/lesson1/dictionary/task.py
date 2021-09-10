from flask import Flask

app = Flask(__name__)

vocab = {
    'cat': 'кошка',
    'python': 'питон',
    'flask': 'фляга',
    'developer': 'разработчик',
    'django': 'вофтпщ',
    'framework': 'фреймворк',
    'package': 'библиотека',
    'library': 'библиотека',
}


if __name__ == '__main__':
    app.run()
