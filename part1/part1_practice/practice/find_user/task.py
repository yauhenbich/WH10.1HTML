from flask import Flask

app = Flask(__name__)


def load_users():
    from part1.task8.users import users
    return users


# TODO добавить маршрут для получения целочисленного индекса из сегмента урл

def get_user(idx):
    users = load_users()

    if idx < 1 or idx > len(users):
        return ''  # TODO вернуть 404 код ответа и строку 'Не найдено'

    return f''  # TODO вернуть фамилию и имя пользователя с индексом idx - 1


if __name__ == '__main__':
    app.run()
