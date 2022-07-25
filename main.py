from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)


@app.route('/')
def main_page():
    candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_card(idx):
    candidate: dict = get_candidate(idx)
    if not candidate:
        return "Такого кандидата не найдено"
    return render_template('candidate_page.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidates_my_name_page(candidate_name):
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/search/<skill_name>')
def search_candidates_my_skill_page(skill_name):
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


app.run()

