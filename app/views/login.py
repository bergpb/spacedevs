from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_user, logout_user

from app.forms import LoginForm
from app.models import User

login = Blueprint("login", __name__)


@login.route("/login", methods=["GET", "POST"])
def page():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            return redirect(url_for(".login"))

        if not user.compare_password(form.password.data):
            return redirect(url_for(".login"))

        login_user(user)
        return redirect(url_for("home.page"))

    print(form.errors)
    return render_template("pages/login.html", form=form)


@login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for(".page"))
