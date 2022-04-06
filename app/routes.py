"""Module to handle the routes.

Author: Nick Machairas, 2022
"""

from flask import render_template
from app import app


@app.route('/')
def home():
    """Render the home page."""
    return render_template("home.html")
