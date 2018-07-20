from flask import Blueprint, render_template, request, redirect, url_for, g
from lib.models.User import UserModel
from lib import login_required

user = Blueprint('user', __name__, url_prefix='/user')

@login_required
@user.route('/<int:id>')
def detail(id):
    user_model = UserModel()
    user_id = g.user['']
    pass


