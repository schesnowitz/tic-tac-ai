from . import db 
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    text = db.Column(db.String(200))
    move = db.Column(db.Boolean, default=False)
    bool_move_1 = db.Column(db.Boolean, default=False)
    bool_move_2 = db.Column(db.Boolean, default=False)
    bool_move_3 = db.Column(db.Boolean, default=False)
    bool_move_4 = db.Column(db.Boolean, default=False)
    bool_move_5 = db.Column(db.Boolean, default=False)
    bool_move_6 = db.Column(db.Boolean, default=False)
    bool_move_7 = db.Column(db.Boolean, default=False)
    bool_move_8 = db.Column(db.Boolean, default=False)
    bool_move_9 = db.Column(db.Boolean, default=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    first_name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    notes = db.relationship('Note', backref='user', lazy=True)

class Game(db.Model):
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    moves = db.relationship('Move', backref='game', lazy=True)

class Move(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    player = db.Column(db.String(1))  # 'X' or 'O'
    row = db.Column(db.Integer)
    col = db.Column(db.Integer)
    position = db.Column(db.Integer)