import click
from flask import current_app
from app import db


def register_commands(app):
    @app.cli.command("init-db")
    def init_db():
        with current_app.app_context():
            db.create_all()
            click.echo("Database initialized.")
