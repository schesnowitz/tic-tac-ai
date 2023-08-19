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
    items = [
        "Who Goes First?",
        "AI-X-First",
        "AI-O-First",
        "Human-X-First",
        "Human-O-First",
    ]
    if request.method == "POST" and request.form.get("new_game"):
        who_goes_first = request.form.get("item").strip()
        if who_goes_first == "AI-X-First":
            game = Game(
                last_mover="human",
                player="X",
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
            flash("Let's Get Ready To Rumble!", category="success")
            return redirect(url_for("ai.play_game_ai", game_id=game.id))
        elif who_goes_first == "AI-O-First":

            
            game = Game(
                last_mover="human",
                player="O",
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
            print(f"Player= {game.player}")
            db.session.commit()
            flash("Let's Get Ready To Rumble!", category="success")
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
    player = "O"
    print(f"last move from views:  {game.last_mover}")

    print(f"views -- 1:{game.str_move_1} 2:{game.str_move_2} 3:{game.str_move_3} 4:{game.str_move_4} 5:{game.str_move_5} 6:{game.str_move_6} 7:{game.str_move_7} 8:{game.str_move_8} 9:{game.str_move_9}")



        
   
  

    if request.method == "POST" and request.form.get("new_game"):
        items = [
            "Who Goes First?",
            "AI-X-First",
            "AI-O-First",
            "ME-X-First",
            "ME-O-First",
        ]
        new_game = request.form.get("new_game")
        who_goes_first = request.form.get("item").strip()
        player = "SC"
        new_game = Game(player=player, user_id=current_user.id, who_goes_first=who_goes_first)
        if (
            who_goes_first == "AI-X-First"
            or who_goes_first == "Human-X-First"
        ):
            new_game.player = "O"
            db.session.add(new_game)
            db.session.commit()
            flash("Let's Play", category="success")
            return redirect(url_for("views.play_game", game_id=new_game.id))
        if (
            who_goes_first == "AI-O-First"
            or who_goes_first == "Human-O-First"
        ):
            new_game.player = "X"
            db.session.add(new_game)
            db.session.commit()
            flash("Let's Play", category="success")
            return redirect(url_for("views.play_game", game_id=new_game.id))
        else:
            flash("Who Goes First?", category="danger")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        

    
    # if game.player == "X":
    #     game.player = "O"

    # else:
    #     game.player == "O"
    #     game.player = "X"

    if request.method == "POST" and request.form.get("position"):
        # loop = True
        # while loop < 10:

        if position == "1":
            game.str_move_1 = player
            game.last_mover = "human" 
        elif position == "2":
            game.str_move_2 = player
            game.last_mover = "human" 
        elif position == "3":
            game.str_move_3 = player
            game.last_mover = "human" 
        elif position == "4":
            game.str_move_4 = player
            game.last_mover = "human" 
        elif position == "5":
            game.str_move_5 = player
            game.last_mover = "human" 
        elif position == "6":
            game.str_move_6 = player
            game.last_mover = "human" 
        elif position == "7":
            game.str_move_7 = player
            game.last_mover = "human" 
        elif position == "8":
            game.str_move_8 = player
            game.last_mover = "human" 
        else:
            position == "9"
            game.str_move_9 = player
            game.last_mover = "human" 
        game.last_mover = "human"  
        db.session.commit()



      


        if (
            game.str_move_1 == "X"
            and game.str_move_2 == "X"
            and game.str_move_3 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_4 == "X"
            and game.str_move_5 == "X"
            and game.str_move_6 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_7 == "X"
            and game.str_move_8 == "X"
            and game.str_move_9 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )

        # X Vertical Wins
        elif (
            game.str_move_1 == "X"
            and game.str_move_4 == "X"
            and game.str_move_7 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_2 == "X"
            and game.str_move_5 == "X"
            and game.str_move_8 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_3 == "X"
            and game.str_move_6 == "X"
            and game.str_move_9 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )

        # X Diagional Wins
        elif (
            game.str_move_1 == "X"
            and game.str_move_5 == "X"
            and game.str_move_9 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_3 == "X"
            and game.str_move_5 == "X"
            and game.str_move_7 == "X"
        ):
            flash('Player "X" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )

        # O Horizontal  Wins
        elif (
            game.str_move_1 == "O"
            and game.str_move_2 == "O"
            and game.str_move_3 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_4 == "O"
            and game.str_move_5 == "O"
            and game.str_move_6 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_7 == "O"
            and game.str_move_8 == "O"
            and game.str_move_9 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )

        # O Vertical Wins
        elif (
            game.str_move_1 == "O"
            and game.str_move_4 == "O"
            and game.str_move_7 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_2 == "O"
            and game.str_move_5 == "O"
            and game.str_move_8 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_3 == "O"
            and game.str_move_6 == "O"
            and game.str_move_9 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )

        # O Diagional WIns
        elif (
            game.str_move_1 == "O"
            and game.str_move_5 == "O"
            and game.str_move_9 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif (
            game.str_move_3 == "O"
            and game.str_move_5 == "O"
            and game.str_move_7 == "O"
        ):
            flash('Player "O" is the winner!', category="success")
            return render_template(
                "pages/game_over.html", game=game, items=items
            )
        elif board_full():
            flash("Tie Game", category="info")

            return render_template(
                "pages/game_over.html", game=game, items=items
            )

        else: 
            return redirect(url_for("ai.play_game_ai", game_id=game.id))

    return render_template("pages/play_game.html", game=game, game_id=game.id)

 