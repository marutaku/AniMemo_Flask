from flask import Blueprint, render_template, request, redirect, url_for
from lib.models.User import UserModel

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<int:id>')
def detail(id):
    user_model = UserModel()
    

