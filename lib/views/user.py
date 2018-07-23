from flask import Blueprint, render_template, request, redirect, url_for, g, jsonify, session
from lib.models.User import UserModel
from lib import login_required

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<int:id>')
@login_required
def detail(id):
    user_model = UserModel()
    data = user_model.get_user_activity(id)
    user_info = data['user_info'][0]
    is_follow = user_model.is_followed(session['user_id'], id)
    return render_template('user_detail.html', user_data=data, user_id=str(id), user_info=user_info,
                           is_follow=is_follow)


@user.route('/follow/<int:followed_id>')
@login_required
def follow(followed_id):
    user_model = UserModel()
    user_model.follow(session['user_id'], followed_id)
    return jsonify({'result': 'success'})


@user.route('/unfollow/<int:followed_id>')
@login_required
def unfollow(followed_id):
    user_model = UserModel()
    user_model.unfollow(session['user_id'], followed_id)
    return jsonify({'result': 'success'})

@user.route('/edit/<int:user_id>')
@login_required
def edit_user(user_id):
    user_model = UserModel()
    user = user_model.get_user_info(user_id)
    return render_template('edit_user.html', user_info=user[0])

@user.route('/edit/<int:user_id>', methods=['POST'])
@login_required
def update_user_info(user_id):
    user_model = UserModel()
    user_name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user_model.update_user_info(user_name, password, email, user_id)
    return redirect('/user/edit/{}'.format(user_id))
