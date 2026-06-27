from flask import Flask
from app import db


def deploy():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    with app.app_context():
        from app.models.user import User  # noqa: F401
        db.create_all()
