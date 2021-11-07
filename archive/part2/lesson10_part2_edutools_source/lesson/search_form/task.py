from flask import Flask, request

app = Flask(__name__)


@app.route('/search/', methods=['GET'])
def draw_form():
    return '<!doctype html>' \
           '<html lang="ru">' \
           '<form method="post"><input type="text" name="search"><input type="submit"></form>'


@app.route('/search/', methods=['POST'])
def process_form():
    search = request.form['search']
    return f'<h1>Результаты по запросу <i>{search}</i></h1>'


if __name__ == '__main__':
    app.run()
