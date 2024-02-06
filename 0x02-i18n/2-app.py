#!/usr/bin/env python3
"""Instantiate the Babel object"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """index page"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
