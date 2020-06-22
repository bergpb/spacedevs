from flask import Flask
from dynaconf import FlaskDynaconf
from . import routes


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)

    routes.init_app(app)
    
    return app