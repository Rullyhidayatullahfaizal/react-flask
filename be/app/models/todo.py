from app import db
from datetime import datetime
from sqlalchemy import CheckConstraint


class ToDo(db.Model):
    __tablename__ = 'todos'
    __table_args__ = (
        CheckConstraint("length(name) > 0", name="ck_todos_name_not_empty"),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
