from flask import Blueprint, render_template, redirect, jsonify, request, g
from lib import login_required
works = Blueprint('works', __name__, url_prefix='/works')

@works.route('/')
@login_required
def render_works():
    return render_template('works.html')
