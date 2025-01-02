from flask import render_template

from src import app


@app.route("/")
def home_page():
    return render_template("home.html")
