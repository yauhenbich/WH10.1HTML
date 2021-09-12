@app.route("/all/")
def get_all():
    expenses_str = " ".join([str(x) for x in expenses])
    return expenses_str


@app.route("/max/")
def get_max():
    return str(max(expenses))


@app.route("/min/")
def get_min():
    return str(min(expenses))


@app.route("/avg/")
def get_avg():
    total = sum(expenses)
    avg = round( total / len(expenses))
    return str(avg)
