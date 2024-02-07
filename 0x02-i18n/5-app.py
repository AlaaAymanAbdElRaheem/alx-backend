#!/usr/bin/env python3
"""Instantiate the Babel object"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """get locale"""
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """get user"""
    try:
        return users[int(request.args.get('login_as'))]
    except Exception:
        return None


@app.before_request
def before_request():
    """before request"""
    user = get_user()
    if user:
        g.user = user['name']
    else:
        g.user = None


@app.route('/')
def index():
    """index page"""
    username = g.user
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    """main"""
    app.run()
