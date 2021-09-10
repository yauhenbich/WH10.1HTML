

@app.route("/search/")
def get_cities():
    s = request.args.get("s").lower()
    locations_match = [x for x in locations if s in x.lower()]
    if len(locations_match):
        return ", ".join(locations_match)
    return "Городов не найдено"

