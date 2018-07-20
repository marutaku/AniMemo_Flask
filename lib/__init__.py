from functools import wraps
from flask import request, redirect, url_for, g, session
from lib.database.Users import User
def login_required(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('index', next=request.path))
        return f(*args, **kwargs)

def load_user():
    user_id = session.get('user_id')
    user_db = User()
    if user_id is None:
        g.user = None
    else:
        g.user = user_db.get_user_by_id(user_id)
        print(g.user)
