from flask import Flask

app = Flask(__name__)


def load_users():
    """ Эта функция получает данные, не трогайте ее!"""
    from users import users
    return users


def get_user(uid):  # Написать маршрут тут
    users = load_users()

    if uid < 1 or uid > len(users):
        return ... # Вернуть значение тут

    return ... # Вернуть значение тут


if __name__ == '__main__':
    app.run()
