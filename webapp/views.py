from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from . import db
from .models import Note
views = Blueprint('views', __name__)

@views.route("/")
# @login_required
def index():
    return render_template("pages/index.html")

@views.route("/tictac", methods=["GET", "POST"])

@login_required
def tictac():
    if request.method == "POST":
        move = request.form.get("move")
        print((move))
        # bool_move = True
        if move == "true":
            move_bool = True
            print(f"{move} seems to be True")
        else:
            move_bool = False
            print(f"{move} seems to be False")
        text = request.form.get("text")
            
            
        print(f"this is it {move_bool}")
        note = Note(
                    text=text,
                    move=move_bool,
                    user_id=current_user.id,
                )
        db.session.add(note)
        db.session.commit()

    return render_template("pages/tictac.html")