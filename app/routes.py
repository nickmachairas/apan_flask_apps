"""Module to handle the routes.

Author: Nick Machairas, 2022
"""

from flask import render_template
from app import app
from app.forms import SearchForm


@app.route('/', methods=['GET', 'POST'])
def home():
    """Render the home page."""
    form = SearchForm()
    search_results = None
    if form.validate_on_submit():
        search_results = form.username.data
    return render_template("home.html", form=form, search_results=search_results)
