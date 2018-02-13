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
def landing_home():
    return render_template('under_construction.html')


if __name__ == '__main__':
    app.run()
