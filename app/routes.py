"""Module to handle the routes.

Author: Nick Machairas, 2022
"""

from flask import render_template
from app import app
from app.forms import SearchForm
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port='5432',
    database="uni_small",
    user="postgres",
    password="123")


@app.route('/', methods=['GET', 'POST'])
def home():
    """Render the home page."""
    form = SearchForm()
    search_results = None
    if form.validate_on_submit():
        search_term = form.username.data
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM student WHERE name = '{search_term}';")
        search_results = cur.fetchall()
        cur.close()
    return render_template(
        "home.html", form=form, search_results=search_results)
