from game.game import BlackjackGame

if __name__ == "__main__":
    # create a game
    game = BlackjackGame()
    # configure the game
    game.configure({'game_num_players': 2, 'game_num_decks': 1})
    # initialize the game
    state, player_id = game.init_game()
    # print the state
    print(state)
    while True:
        # get the action randomly
        action = game.np_random.choice(['hit', 'stand'])
        # step the game
        state, player_id = game.step(action)
        # print the state
        print(state)
        # check if the game is over
        if game.is_over():
            break