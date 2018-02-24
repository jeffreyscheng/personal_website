from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request, url_for
from flask import redirect
from flask_basicauth import BasicAuth
import os

app = Flask(__name__)


# app.config.from_object(Config)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def landing_home():
    return render_template('home.html')


@app.route('/cv', methods=['GET', 'POST'])
@app.route('/projects', methods=['GET', 'POST'])
@app.route('/art', methods=['GET', 'POST'])
@app.route('/writing', methods=['GET', 'POST'])
def landing_cv():
    return render_template('under_construction.html')


@app.route('/contact', methods=['GET', 'POST'])
def landing_contact():
    return render_template('contact.html')


@app.route('/index', methods=['GET', 'POST'])
def landing_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
