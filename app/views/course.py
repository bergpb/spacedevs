from flask import Blueprint, render_template


course = Blueprint("course", __name__, url_prefix="/cursos")


@course.route("/")
def catalogue():
    return render_template("pages/course/catalogue.html")


@course.route("/<slug>")
def single():
    return render_template("pages/course/single.html")