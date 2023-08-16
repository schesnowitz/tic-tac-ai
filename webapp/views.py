from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from . import db
from .models import Move, Game
import time as time
views = Blueprint("views", __name__)
from .llm import send_to_llm


@views.route("/")
# @login_required
def index():
    return render_template("pages/index.html")


@views.route("/new_game/", methods=["GET", "POST"])
@login_required
def new_game():
    items = ["Who Goes First?", "AI-X-First", "AI-O-First", "ME-X-First", "ME-O-First"]
    if request.method == "POST" and request.form.get("new_game"):
        who_goes_first = request.form.get("item").strip()
        # print(who_goes_first)
        if (
            who_goes_first == "AI-X-First"
            or who_goes_first == "AI-O-First"
            or who_goes_first == "ME-X-First"
            or who_goes_first == "ME-O-First"
        ):
            # print(who_goes_first)
            flash("Let's Get Ready To Rumble!", category="success")
            game = Game(
                user_id=current_user.id,
                who_goes_first=who_goes_first,
                str_move_1="*",
                str_move_2="*",
                str_move_3="*",
                str_move_4="*",
                str_move_5="*",
                str_move_6="*",
                str_move_7="*",
                str_move_8="*",
                str_move_9="*",
            )

            db.session.add(game)
            db.session.commit()
            print(game.str_move_1)
            return redirect(url_for("views.play_game", game_id=game.id))
        else:
            flash("Who Goes First?", category="danger")
            return render_template("pages/new_game.html", items=items)

    return render_template("pages/new_game.html", items=items)


@views.route("/play_game/<int:game_id>", methods=["GET", "POST"])
@login_required
def play_game(game_id):
    def board_full():
        if (
            game_move.str_move_1 != "*"
            and game_move.str_move_2 != "*"
            and game_move.str_move_3 != "*"
            and game_move.str_move_4 != "*"
            and game_move.str_move_5 != "*"
            and game_move.str_move_6 != "*"
            and game_move.str_move_7 != "*"
            and game_move.str_move_8 != "*"
            and game_move.str_move_9 != "*"
        ):
            return True
        else:
            return False

    def does_board_has_a_move():
        if (
            game_move.str_move_1 != "*"
            or game_move.str_move_2 != "*"
            or game_move.str_move_3 != "*"
            or game_move.str_move_4 != "*"
            or game_move.str_move_5 != "*"
            or game_move.str_move_6 != "*"
            or game_move.str_move_7 != "*"
            or game_move.str_move_8 != "*"
            or game_move.str_move_9 != "*"
        ):
            return True
        else:
            return False

    user = current_user
    position = request.form.get("position")
    game_move = db.session.query(Game).filter_by(id=game_id).first()
    current_player = ""
    is_ai_move = False
    # print(game_move.who_goes_first)
    # print(board_full())


    items = ["AI-X-First", "AI-O-First", "ME-X-First", "ME-O-First"]
    # this is the AI's first move of the game as player X
    # if game_move.who_goes_first == "AI-X-First" and does_board_has_a_move() == False:
    #     is_ai_move = True
    # time.sleep(1.5)
    # send_to_llm(
    #     gm1=game_move.str_move_1,
    #     gm2=game_move.str_move_2,
    #     gm3=game_move.str_move_3,
    #     gm4=game_move.str_move_4,
    #     gm5=game_move.str_move_5,
    #     gm6=game_move.str_move_6,
    #     gm7=game_move.str_move_7,
    #     gm8=game_move.str_move_8,
    #     gm9=game_move.str_move_9,
    #     current_player=current_player,
    #     game_int=game_move.current_player_int,
    #     is_ai_move=is_ai_move,
    #     game_id=game_id
    # )

    # if game_move.who_goes_first == "AI-O-First" and does_board_has_a_move() == False:
    #     game_move.current_player_int = 2
        # send_to_llm(
        #     gm1=game_move.str_move_1,
        #     gm2=game_move.str_move_2,
        #     gm3=game_move.str_move_3,
        #     gm4=game_move.str_move_4,
        #     gm5=game_move.str_move_5,
        #     gm6=game_move.str_move_6,
        #     gm7=game_move.str_move_7,
        #     gm8=game_move.str_move_8,
        #     gm9=game_move.str_move_9,
        #     current_player=current_player,
        #     game_int=game_move.current_player_int,
        #     is_ai_move=is_ai_move,
        #     game_id=game_id,
        # )

    # if game_move.who_goes_first == "ME-O-First" and does_board_has_a_move() == False:
    #     game_move.current_player_int = 2

    if game_move.current_player_int == 1:
        current_player = "X"
        game_move.current_player_int = 2
    else:
        game_move.current_player_int == 2
        current_player = "O"
        game_move.current_player_int = 1

    # send_to_llm(
    #     gm1=game_move.str_move_1,
    #     gm2=game_move.str_move_2,
    #     gm3=game_move.str_move_3,
    #     gm4=game_move.str_move_4,
    #     gm5=game_move.str_move_5,
    #     gm6=game_move.str_move_6,
    #     gm7=game_move.str_move_7,
    #     gm8=game_move.str_move_8,
    #     gm9=game_move.str_move_9,
    #     current_player=current_player,
    #     game_int=game_move.current_player_int,
    #     is_ai_move=is_ai_move,
    #     game_id=game_id,
    # )
    if request.method == "POST" and request.form.get("new_game"):
        new_game = request.form.get("new_game")
        who_goes_first = ""

        new_game = Game(user_id=current_user.id, who_goes_first=who_goes_first)
        db.session.add(new_game)
        db.session.commit()
        flash("Let's Play", category="success")
        return redirect(url_for("views.play_game", game_id=new_game.id))

    if request.method == "POST" and request.form.get("position"):
        if position == "1":
            game_move.str_move_1 = current_player
        elif position == "2":
            game_move.str_move_2 = current_player
        elif position == "3":
            game_move.str_move_3 = current_player
        elif position == "4":
            game_move.str_move_4 = current_player
        elif position == "5":
            game_move.str_move_5 = current_player
        elif position == "6":
            game_move.str_move_6 = current_player
        elif position == "7":
            game_move.str_move_7 = current_player
        elif position == "8":
            game_move.str_move_8 = current_player
        else:
            position == "9"
            game_move.str_move_9 = current_player

        # print(is_ai_move )
        # if is_ai_move == False:
        db.session.commit()

        if (
            game_move.str_move_1 == "X"
            and game_move.str_move_2 == "X"
            and game_move.str_move_3 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_4 == "X"
            and game_move.str_move_5 == "X"
            and game_move.str_move_6 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_7 == "X"
            and game_move.str_move_8 == "X"
            and game_move.str_move_9 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)

        # X Vertical Wins
        elif (
            game_move.str_move_1 == "X"
            and game_move.str_move_4 == "X"
            and game_move.str_move_7 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_2 == "X"
            and game_move.str_move_5 == "X"
            and game_move.str_move_8 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_3 == "X"
            and game_move.str_move_6 == "X"
            and game_move.str_move_9 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)

        # X Diagional Wins
        elif (
            game_move.str_move_1 == "X"
            and game_move.str_move_5 == "X"
            and game_move.str_move_9 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_3 == "X"
            and game_move.str_move_5 == "X"
            and game_move.str_move_7 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)

        # O Horizontal  Wins
        elif (
            game_move.str_move_1 == "O"
            and game_move.str_move_2 == "O"
            and game_move.str_move_3 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_4 == "O"
            and game_move.str_move_5 == "O"
            and game_move.str_move_6 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_7 == "O"
            and game_move.str_move_8 == "O"
            and game_move.str_move_9 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)

        # O Vertical Wins
        elif (
            game_move.str_move_1 == "O"
            and game_move.str_move_4 == "O"
            and game_move.str_move_7 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_2 == "O"
            and game_move.str_move_5 == "O"
            and game_move.str_move_8 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_3 == "O"
            and game_move.str_move_6 == "O"
            and game_move.str_move_9 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)

        # O Diagional WIns
        elif (
            game_move.str_move_1 == "O"
            and game_move.str_move_5 == "O"
            and game_move.str_move_9 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif (
            game_move.str_move_3 == "O"
            and game_move.str_move_5 == "O"
            and game_move.str_move_7 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template("pages/game_over.html", game_move=game_move)
        elif board_full():
            flash("Tie Game", category="info")

            return render_template("pages/game_over.html", game_move=game_move)

        else:
            return render_template("pages/play_game.html", game_move=game_move)

    return render_template("pages/play_game.html", game_move=game_move)
