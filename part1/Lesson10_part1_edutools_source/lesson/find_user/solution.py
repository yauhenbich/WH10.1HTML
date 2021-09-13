from flask import Flask

app = Flask(__name__)


def load_users():
    from users import users
    return users

@app.route("/users/<int:uid>/")
def get_user(uid):
    users = load_users()

    if uid < 1 or uid > len(users):
        return 'Не найдено', 404

    requested_user = users[uid-1]
    return f'{requested_user["last_name"]} {requested_user["first_name"]}'

if __name__ == '__main__':
    app.run()
