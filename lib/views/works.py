from flask import Blueprint, render_template, redirect, jsonify, request, g
from lib import login_required
works = Blueprint('works', __name__, url_prefix='/works')

@login_required
@works.route('/')
def render_works():
    return render_template('works.html')
