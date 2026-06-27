import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.models.user import User  # noqa: F401
    from app.models.resume import Resume  # noqa: F401

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from app.routes.auth import auth_bp
    from app.routes.resume import resume_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)

    from app.commands import register_commands
    register_commands(app)

    # Auto-create tables for local SQLite runs
    if app.config.get("SQLALCHEMY_DATABASE_URI", "").startswith("sqlite"):
        with app.app_context():
            db.create_all()

    @app.get("/")
    def index():
        return "Resume Builder is running."

    return app