from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='template')

# FIXME This is dummy code

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def slash():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
