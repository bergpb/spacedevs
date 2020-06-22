from . import views

def init_app(app):
    app.register_blueprint(views.home)
    app.register_blueprint(views.course)
