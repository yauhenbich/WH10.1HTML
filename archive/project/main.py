from flask import Flask, request
import json


def import_json(path):
    with open(path, 'r') as f:
        return json.load(f)


app = Flask(__name__)

candidates = import_json("candidates.json")
settings = import_json("settings.json")


@app.route("/")
def get_status():
    """ В зависимости от settings["online"] выводит статус"""
    if settings.get("online"):
        return "Приложение работает"
    return "Приложение не работает"


@app.route("/candidate/<int:cid>")
def get_candidate(cid):
    """  Представление для роута candidate/<x>, который бы выводил данные про кандидата так: """
    for can in candidates:
        if can["id"] == cid:
            return f"""<h1>{can["name"]}</h1>
                        <p>{can["position"]}</p>
                        <img src="{can["picture"]}" width=200/>
                        <p>{can["skills"]}</p>
                        """
    return f"Кандидат {cid} не найден"


@app.route("/list/")
def get_all():
    """Выводит список всех кандидатов:"""
    output = "<h1>Все кандидаты</h1>"
    for can in candidates:
        output += f"<p><p><a href='/candidate/{can['id']}'>{can['name']}</a></p></p>"
    return output


@app.route("/search/")
def search_by_skills():
    """ Создайте представление /search?name=<x> для поиска по совпадению."""
    s = request.args.get("name")
    candidates_match = []

    for can in candidates:

        if settings["case-sensitive"]:  # вариант чувствительный
            if s in can["name"]:
                candidates_match.append(can)
        else:
            if s.lower() in can["name"].lower():  # вариант нечувствительный
                candidates_match.append(can)

    output = f"<h1>найдено кандидатов {len(candidates_match)}</h2>"

    for can in candidates_match:
        output += f"<p><p><a href='/candidate/{can['id']}'>{can['name']}</a></p></p>"

    return output


@app.route("/skill/<skill>/")
def get_by_skill(skill):
    """Выведите тех кандидатов, в списке навыков у которых содержится skill."""

    candidates_match = []
    for can in candidates:
        skills = can["skills"].lower().split(", ")
        if skill.lower() in skills:
            candidates_match.append(can)

    output = f"<h1>найдено кандидатов {len(candidates_match)}</h2>"

    candidates_match_limited = candidates_match[:settings["limit"]]

    for can in candidates_match_limited:
        output += f"<p><p><a href='/candidate/{can['id']}'>{can['name']}</a></p></p>"

    return output


app.run()
