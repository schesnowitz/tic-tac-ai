from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from . import db
from .models import Move
views = Blueprint('views', __name__)
from .tic_tac import get_move

@views.route("/")
# @login_required
def index():
    return render_template("pages/index.html")

@views.route("/tictac", methods=["GET", "POST"])

@login_required
def tictac():
    if request.method == "POST":
        # initialize_board()
        position = request.form.get("position")
        match position:
            case '1':
                value = 1
            case "2":
                value = 2
            case "3":
                value = 3               
            case "4":
                value = 4
            case "5":
                value = 5
            case "6":
                value = 6                
            case "7":
                value = 7
            case "8":
                value = 8
            case "9":
                value = 9


            

        move = Move(position=value)
        db.session.add(move)
        db.session.commit()
    
    return render_template("pages/tictac.html", value=value)