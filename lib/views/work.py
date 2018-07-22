from flask import Blueprint, render_template, redirect, jsonify, request, g
from lib.models.Work import WorkModel
from lib import login_required
work = Blueprint('work', __name__, url_prefix='/work')

@work.route('/', methods=['GET'])
@login_required
def render_works():
    works_model = WorkModel()
    if request.args.get('title') is not None and request.args.get('year') is not None and request.args.get('cours') is not None:
        works = 1
        return render_template('works.html', works=works)
    if request.args.get('title') is not None and request.args.get('year') is not None:
        works = 2
        return render_template('works.html', works=works)
    if request.args.get('title') is not None and request.args.get('cours') is not None:
        works = 3
        return render_template('works.html', works=works)
    if request.args.get('year') is not None and request.args.get('cours') is not None:
        works = 4
        return render_template('works.html', works=works)
    if request.args.get('title') is not None:
        works = 5
        return render_template('works.html', works=works)
    if request.args.get('year') is not None:
        works = 6
        return render_template('works.html', works=works)
    if request.args.get('cours') is not None:
        works = 7
        return render_template('works.html', works=works)
    works = 9
    return render_template('works.html', works=works)
