from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from wtforms.fields import PasswordField
from flask_admin import Admin

from . import db
from .models import Course, Quote, Tag, User


class UserView(ModelView):
    form_extra_fields = {"password": PasswordField("Password")}
    form_edit_columns = ("first_name", "last_name", "email")
    column_exclude_list = ["password"]
    edit_modal = True

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data)


def init_app(admin: Admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Course, db.session))
    admin.add_view(ModelView(Quote, db.session))
    admin.add_view(ModelView(Tag, db.session))
