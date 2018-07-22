from flask import Blueprint, render_template, url_for, request, redirect
from lib.models.User import UserModel

top = Blueprint('top', __name__, url_prefix='/')

@top.route('/')
def index():
    return render_template('index.html')

@top.route('/login', methods=['POST'])
def login():
    user_name = request.form['name']
    password = request.form['password']
    user_model = UserModel()
    if user_model.login(user_name, password):
        #TODO Session
        return redirect('/works')
    else:
        return render_template('index.html', error='ユーザー名、またはパスワードが違います')

@top.route('register', methods=['GET'])
def render_register():
    return render_template('register.html')

@top.route('register', methods=['POST'])
def register():
    user_name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    image_path = None
    user_model = UserModel()
    result = user_model.register_user(user_name, email, password, image_path)
    if type(result) == bool:
        return render_template('index.html')
    elif type(result) == str:
        print(result)
        return render_template('register.html', error=result)
    else:
        return render_template('register.html', error='Some Error was happen')



