from app import db


class Resume(db.Model):
    __tablename__ = "resumes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    target_position = db.Column(db.String(120), nullable=True)
    visibility = db.Column(db.String(16), default="private", nullable=False)
    is_default = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    owner = db.relationship("User", backref=db.backref("resumes", lazy="dynamic"))
