
@app.route('/')
def get_index():
    return "Тут будет главная", 200

@app.route('/employees/')
def get_employees():
    return "Тут будет главная", 200

@app.route('/employees/<int:uid>/')
def get_employee(uid):
    return "Тут будет информация об одном из сотрудников", 200
