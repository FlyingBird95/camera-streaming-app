from flask import render_template

from .blueprint import main_blueprint


@main_blueprint.get("/")
def get_index():
    return render_template("index.html")