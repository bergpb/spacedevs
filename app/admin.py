from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_login import current_user
from werkzeug.security import generate_password_hash
from wtforms.fields import PasswordField

from . import db
from .models import Course, Quote, Tag, User


class MyAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login.page"))


class BaseViewAuthRequired(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login.page"))


class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


class UserView(BaseViewAuthRequired):
    form_extra_fields = {"password": PasswordField("Password")}
    form_edit_columns = ("first_name", "last_name", "email")
    column_exclude_list = ["password"]
    edit_modal = True

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data)


class CourseView(BaseViewAuthRequired):
    form_widget_args = dict(description={"id": "editor"})

    create_template = "/components/editor.html"
    edit_template = "components/editor.html"


class TagView(BaseViewAuthRequired):
    pass


class QuoteView(BaseViewAuthRequired):
    pass


def init_app(app):
    admin = Admin(
        app,
        url=app.config.FLASK_ADMIN_URL,
        name=app.config.FLASK_ADMIN_NAME,
        template_mode=app.config.FLASK_ADMIN_TEMPLATE_MODE,
        index_view=MyAdminView(url=app.config.FLASK_ADMIN_URL),
    )

    admin.add_view(UserView(User, db.session))
    admin.add_view(CourseView(Course, db.session))
    admin.add_view(QuoteView(Quote, db.session))
    admin.add_view(TagView(Tag, db.session))
    admin.add_link(LogoutMenuLink(name="Logout", url="/logout"))
