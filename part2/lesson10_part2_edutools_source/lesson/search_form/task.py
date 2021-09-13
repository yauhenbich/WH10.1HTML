from flask import Flask, request

app = Flask(__name__)


@app.route()
def draw_form():
    return '<!doctype html>' \
           '<html lang="ru">' \
           '<form method="post"><input type="text" name="search"><input type="submit"></form>'


@app.route()
def process_form():
    return 'Результаты по запросу <i> ... </i>'


if __name__ == '__main__':
    app.run()
