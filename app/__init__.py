from dynaconf import FlaskDynaconf
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
dynaconf = FlaskDynaconf()

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "error"
login_manager.login_message = "Você deve fazer o login antes de continuar."


def create_app():
    app = Flask(__name__)
    dynaconf.init_app(app)
    app.config.load_extensions()

    login_manager.init_app(app)
    db.init_app(app)

    return app
