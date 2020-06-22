from flask import Blueprint, render_template

from app.models import Course

home = Blueprint("home", __name__)


@home.route("/")
def page():
    courses = Course.query.all()
    return render_template("pages/home.html", courses=courses)
