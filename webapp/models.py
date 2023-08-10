from . import db 
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    text = db.Column(db.String(5000))
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    move = db.Column(db.Boolean, default=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    first_name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    notes = db.relationship('Note', backref='user', lazy=True)
