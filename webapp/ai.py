
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from . import db
from .models import Move, Game
import time as time

ai = Blueprint("ai", __name__)  
from .llm import send_to_llm

@ai.route("/")
@ai.route("/play_game_ai/<int:game_id>", methods=["GET", "POST"])
@login_required
def play_game_ai(game_id):

    def board_full():
        if (
            game.str_move_1 != "*"
            and game.str_move_2 != "*"
            and game.str_move_3 != "*"
            and game.str_move_4 != "*"
            and game.str_move_5 != "*"
            and game.str_move_6 != "*"
            and game.str_move_7 != "*"
            and game.str_move_8 != "*"
            and game.str_move_9 != "*"
        ):
            return True
        else:
            return False



    items = [
        "Who Goes First?",
        "AI-X-First",
        "AI-O-First",
        "Human-X-First",
        "Human-O-First",
    ]
    user = current_user
    position = request.form.get("position")
    game = db.session.query(Game).filter_by(id=game_id).first()
    player = "X"
    print(f"last move from ai:  {game.last_mover}")
    print(f"ai -- 1:{game.str_move_1} 2:{game.str_move_2} 3:{game.str_move_3} 4:{game.str_move_4} 5:{game.str_move_5} 6:{game.str_move_6} 7:{game.str_move_7} 8:{game.str_move_8} 9:{game.str_move_9}")

    if game.last_mover == 'ai':
        return redirect(url_for("views.play_game", game_id=game.id))
    else:

        send_to_llm(
                            game_id=game.id,
                            is_ai_move=True,
                            game_int=game.current_player_int,
                            current_player=player,
                            gm1=game.str_move_1,
                            gm2=game.str_move_2,
                            gm3=game.str_move_3,
                            gm4=game.str_move_4,
                            gm5=game.str_move_5,
                            gm6=game.str_move_6,
                            gm7=game.str_move_7,
                            gm8=game.str_move_8,
                            gm9=game.str_move_9,
                            last_move_by_ai=False,
                        ) 
        
        return redirect(url_for("views.play_game", game_id=game.id))