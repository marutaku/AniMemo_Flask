from flask import Flask, render_template, redirect, url_for
from lib import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
