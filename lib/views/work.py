from flask import Blueprint, render_template, redirect, jsonify, request, g
from lib.models.Work import WorkModel
from lib import login_required
work = Blueprint('work', __name__, url_prefix='/work')

@work.route('/')
@login_required
def render_work():
    return render_template('works.html')
