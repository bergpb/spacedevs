from flask import Blueprint, render_template

from app.models import Course

course = Blueprint("course_page", __name__, url_prefix="/cursos")


@course.route("/")
def catalogue():
    courses = Course.query.all()
    return render_template("pages/course/catalogue.html", courses=courses)


@course.route("/<slug>")
def single(slug):
    course = Course.query.filter_by(slug=slug).first_or_404()
    return render_template("pages/course/single.html", course=course)
