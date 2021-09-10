from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search = request.form.get('search', '')  # or request.form['search']

        return f'<h1>Результаты по запросу <i>{search}</i>.</h1>'
    elif request.method == 'GET':
        return '<!doctype html>' \
               '<html lang="ru">' \
               '<form method="post"><input type="text" name="search"><input type="submit"></form>'


if __name__ == '__main__':
    app.run()
