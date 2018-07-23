from flask import Blueprint, render_template, redirect, jsonify, request, g, session, url_for
from lib.models.Status import StatusModel
from lib import login_required
status = Blueprint('status', __name__, url_prefix='/status')

@status.route('/watch_later/<int:work_id>', methods=['POST'])
@login_required
def watch_later(work_id):
    status_model = StatusModel()
    status = request.form['status']
    user_id = session['user_id']
    result= status_model.change_status(user_id, work_id, status)
    return jsonify({'result': result})

@status.route('/watched/<int:work_id>', methods=['POST'])
@login_required
def watched(work_id):
    status_model = StatusModel()
    status = request.form['status']
    user_id = session['user_id']
    result= status_model.change_status(user_id, work_id, status)
    return jsonify({'result': result})

@status.route('/favorite/<int:work_id>', methods=['POST'])
@login_required
def favorite(work_id):
    status_model = StatusModel()
    status = request.form['status']
    user_id = session['user_id']
    result= status_model.change_status(user_id, work_id, status)
    return jsonify({'result': result})
