from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
from .import db
from .models import Game
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.schema import SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
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
    last_move_by_ai,
):


    lang_model = OpenAI(temperature=0.0)

    board_layout = (
        f"first row:['1', '2', '3'] second row:['4' ,'5' ,'6']third row:['7', '8', '9']"
    )
    board_state = f"first row:['{gm1}', '{gm2}', '{gm3}']\
second row:['{gm4}' ,'{gm5}', '{gm6}']\
third row:['{gm7}', '{gm8}', '{gm9}']"

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content="You are a master tic tac toe player based on board configuration and the current state of the game return a number 1 - 9 that represents your move."
            ),  # The persistent system prompt
            MessagesPlaceholder(
                variable_name="chat_history"
            ),  # Where the memory will be stored.
            HumanMessagePromptTemplate.from_template(
                "{human_input}"
            ),  # Where the human input will injectd
        ]
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chat_llm_chain = LLMChain(
        llm=lang_model,
        prompt=prompt,
        verbose=True,
        memory=memory,
    )

    ai_response = chat_llm_chain.predict(human_input="board_layout={board_layout} board state={board_state} you are player={current_player}")
    save_llm_move_to_db(ai_response, game_id, current_player, game_int, last_move_by_ai)


def save_llm_move_to_db(
    ai_response, game_id, current_player, game_int, last_move_by_ai
):
    print(f"AI REsp {ai_response}")
    print(f"game id {game_id}")
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

    db.session.commit()
