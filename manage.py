from flask import Flask
from lib.views.top import top
from lib.views.user import user
from lib.views.works import works


app = Flask(__name__, template_folder='/template')
app.config.from_object('lib.config')
app.register_blueprint(top)
app.register_blueprint(user)
app.register_blueprint(works)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
