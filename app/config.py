import os
from pathlib import Path


def _default_sqlite_uri() -> str:
    base_dir = Path(__file__).resolve().parent.parent
    db_path = base_dir / "instance" / "app.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return "sqlite:///" + db_path.as_posix()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", _default_sqlite_uri())
    SQLALCHEMY_TRACK_MODIFICATIONS = False