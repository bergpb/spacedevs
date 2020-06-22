from pytest import fixture
from app import create_app
from app import db

from app.models import Course, User, Tag
from datetime import datetime
from werkzeug.security import generate_password_hash


@fixture
def app():
    app = create_app()
    app.testing = True
    return app


@fixture
def create_database(app):
    with app.app_context():
        db.create_all()

        yield db

        db.session.remove()
        db.drop_all()


@fixture(autouse=True)
def seeds(create_database):
    user = User(
        first_name="Marcus",
        last_name="Pereira",
        email="contato@marcuspereira.xyz",
        password=generate_password_hash("12345"),
        is_admin=True,
    )

    db.session.add(user)
    db.session.commit()

    course = Course(
        name="Curso de test",
        slug="curso-de-test",
        description="alguma coisa...",
        duration=300,
        video_url="http://fake:4000",
        source_code_url="http://fake:4000",
        release_date=datetime.utcnow(),
        author_id=user.id,
    )

    db.session.add(course)
    db.session.commit()