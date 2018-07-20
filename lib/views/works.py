from flask import Blueprint, render_template, redirect, jsonify, request

works = Blueprint('works', __name__, url_prefix='/works')

@works.route('/')
def render_works():
    return render_template('works.html')
