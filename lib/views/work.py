from flask import Blueprint, render_template, redirect, jsonify, request, g, session, url_for
from lib.models.work import WorkModel
from lib import login_required
import datetime
work = Blueprint('work', __name__, url_prefix='/works')

@work.route('/', methods=['GET'])
@login_required
def render_works():
    work_model = WorkModel()
    title_query = request.args.get('title')
    year_query = request.args.get('year')
    cours_query = request.args.get('cours')
    if year_query != "" and year_query is not None:
        work_model.is_stored(year_query)
    works = work_model.get_works(title_query, year_query, cours_query)
    today = datetime.date.today()
    return render_template('works.html', works=works, title_query=title_query, year_query=year_query, cours_query=cours_query, current_year=today.year)


@login_required
@work.route('/<int:id>', methods=['GET'])
def show_work(id):
    work_model = WorkModel()
    work = work_model.show_work(id)

    reviews = work_model.get_reviews_by_work(id)

    return render_template('work.html', work=work, reviews=reviews)

@login_required
@work.route('/<int:id>', methods=['POST'])
def post_review(id):
    review_model = WorkModel()
    review_model.post_review(session['user_id'], id, request.form['text'])
    return redirect(url_for('work.show_work', id=id))

