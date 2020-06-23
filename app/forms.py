from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[Email(), DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Logar")
