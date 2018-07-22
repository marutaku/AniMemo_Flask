from flask import Flask
from lib.views.top import top
from lib.views.user import user
from lib.views.work import work
from lib import load_user



app = Flask(__name__, template_folder='template')
app.config.from_object('lib.config')
app.before_request(load_user)
app.register_blueprint(top)
app.register_blueprint(user)
app.register_blueprint(work)
app.secret_key = 'hogehoge'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
