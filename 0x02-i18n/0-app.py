#!/usr/bin/env python3
"""basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """home page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0000", port=5000)
