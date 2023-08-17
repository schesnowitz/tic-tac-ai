  
    def check_whos_turn():

        is_ai_move = None
        if (
            game_move.who_goes_first == "AI-X-First"
            and game_move.current_player_int == 1
            
        ):

            is_ai_move = True

        if (
            game_move.who_goes_first == "AI-O-First"
            and game_move.current_player_int == 1
        ):
            is_ai_move = True


        if (
            game_move.who_goes_first == "Human-X-First"
            and game_move.current_player_int == 1
        ):
            is_ai_move = False
   
        if (
            game_move.who_goes_first == "Human-O-First"
            and game_move.current_player_int == 1
        ):
            is_ai_move = False
        return is_ai_move
    print(f"cpi: {game_move.current_player_int}")





