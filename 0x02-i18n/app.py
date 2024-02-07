#!/usr/bin/env python3
"""Instantiate the Babel object"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
import datetime


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
def get_locale() -> str:
    """get locale"""
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    elif g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    elif request.headers.get('locale') in app.config['LANGUAGES']:
        return request.headers.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> pytz.timezone:
    """get timezone"""
    if request.args.get('timezone'):
        try:
            return pytz.timezone(request.args.get('timezone'))
        except Exception:
            return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])

    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user.get('timezone'))
        except Exception:
            return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])

    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


def get_user() -> dict:
    """get user"""
    try:
        return users[int(request.args.get('login_as'))]
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """before request"""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@app.route('/')
def index() -> str:
    """index page"""
    username = g.user.get('name') if g.user else None
    date_time = datetime.datetime.now(get_timezone())
    current_time = format_datetime(date_time)
    return render_template(
        'index.html', username=username, current_time=current_time)


if __name__ == "__main__":
    """main"""
    app.run()
