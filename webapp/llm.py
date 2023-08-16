from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
from .import db
from .models import Game
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


import os


def send_to_llm(
    game_id,
    is_ai_move,
    game_int,
    current_player,
    gm1,
    gm2,
    gm3,
    gm4,
    gm5,
    gm6,
    gm7,
    gm8,
    gm9,
):
    print(game_int)
    if game_int == 1:
        game_symbol = "X"
    else:
        game_symbol = "O"

    lang_model = OpenAI(temperature=0.9)
    # current_player = f"O"
    board_layout = (
        f"first row:['1', '2', '3'] second row:['4' ,'5' ,'6']third row:['7', '8', '9']"
    )
    board_state = f"first row:['{gm1}', '{gm2}', '{gm3}']\
second row:['{gm4}' ,'{gm5}', '{gm6}']\
third row:['{gm7}', '{gm8}', '{gm9}']"

    prompt_llm = PromptTemplate(
        input_variables=["board_layout", "board_state", "current_player"],
        template="You are a master tic tac toe player. the board is laid out in this \
        fasion: {board_layout}  it is your move which is represented by: {current_player} \
        what is your move based on the current board state of: {board_state}.\
        ONLY RETURN A NUMBER 1 to 9 that represents your move",
    )
    

    
    if is_ai_move:
        ai_response = chain = LLMChain(llm=lang_model, prompt=prompt_llm, verbose=True)
        save_llm_move_to_db(ai_response, game_id, current_player)
       

def save_llm_move_to_db(ai_response, game_id, current_player):
    move = db.session.query(Game).filter_by(id=game_id).first()
    if ai_response == "1":
        move.str_move_1 = current_player
    elif ai_response == "2":
        move.str_move_2 = current_player
    elif ai_response == "3":
        move.str_move_3 = current_player
    elif ai_response == "4":
        move.str_move_4 = current_player
    elif ai_response == "5":
        move.str_move_5 = current_player
    elif ai_response == "6":
        move.str_move_6 = current_player
    elif ai_response == "7":
        move.str_move_7 = current_player
    elif ai_response == "8":
        move.str_move_8 = current_player
    else:
        ai_response == "9"
        move.str_move_9 = current_player

        # db.session.commit()
        print(ai_response)