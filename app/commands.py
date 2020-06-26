import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from app import db as database
from app.models import User


@click.group()
def db():
    """ Managment Database  """
    pass


@db.command("create")
@click.option("--name", help="Your name", required=True)
@click.option("--email", help="Your e-mail address", required=True)
@click.option("--password", help="Your password", required=True)
@with_appcontext
def create(name, email, password):
    """ Create account """
    user = User(
        name=name,
        email=email,
        password=generate_password_hash(password),
        is_admin=True,
    )
    database.session.add(user)
    database.session.commit()


def init_app(app):
    app.cli.add_command(db)
