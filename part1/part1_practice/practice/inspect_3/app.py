from flask import Flask

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<first_name>/')
@app.route('/hello/<first_name>/<last_name>/')
def hello(first_name=None, last_name=None):
    name = 'Anonymous'

    if first_name and last_name:
        name = f'{first_name} {last_name}'
    elif first_name:
        name = first_name

    return f'Hello {name}!'


if __name__ == '__main__':
    app.run()
