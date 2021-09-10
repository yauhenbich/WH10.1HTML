from flask import Flask, request
import json

app = Flask(__name__)


def get_index():
    return "", 200

def get_employees():
    return "", 200

def get_employee(uid):
    return "", 200

if __name__ == '__main__':
    app.run()

