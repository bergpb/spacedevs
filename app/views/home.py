from flask import Blueprint, render_template


home = Blueprint("home", __name__)


@home.route("/")
def page():
    return render_template("pages/home.html")
