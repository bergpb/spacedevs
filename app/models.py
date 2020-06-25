from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, login_manager

courses_tags = db.Table(
    "courses_tags",
    db.Column("course_id", db.ForeignKey("courses.id"), nullable=False),
    db.Column("tag_id", db.ForeignKey("tags.id"), nullable=False),
)


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    courses = db.relationship("Course", backref="author")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def fullname(self):
        return f"{self.name}"

    def compare_password(self, password):
        return check_password_hash(self.password, password)

    def __str__(self):
        return self.fullname

    def __repr__(self):
        return self.fullname


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(130), unique=True, index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    video_url = db.Column(db.String(255), nullable=False, unique=True, index=True)
    source_code_url = db.Column(db.String(255), unique=True)
    release_date = db.Column(db.DateTime)
    sub = -db.Column(db.Boolean, default=False)
    quotes = db.relationship("Quote", backref="course")
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tags = db.relationship("Tag", secondary=courses_tags, backref="course")

    def __str__(self):
        return self.name


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.name


class Quote(db.Model):
    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    quote_time = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.title
