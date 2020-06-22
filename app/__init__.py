from dynaconf import FlaskDynaconf
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)

    db.init_app(app)

    from . import admin, routes

    admin_registered = Admin(app)
    routes.init_app(app)
    admin.init_app(admin_registered)

    return app
