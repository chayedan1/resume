from app import create_app, db
from app.commands import register_commands
from app.models.user import User

app = create_app()
register_commands(app)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}
