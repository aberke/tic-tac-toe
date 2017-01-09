# -*- coding: utf-8 -*-
"""
    Tic-Tac-Toe
    -----------

    Play from command line:
        $ python main.py
"""

from game import (
    Game,
    GameException,
)

QUIT = "q"
RESTART = "restart"
QUIT_RESTART_PROMPT = "You can quit: '{}' or restart: '{}'".format(QUIT, RESTART)


def prompt_next_token(game):
    print game
    print "Ready for token: {}".format(game.next_token)
    print "Enter column ({})".format("/".join([str(i) for i in game.indices]))


def prompt_quit_or_restart():
    print QUIT_RESTART_PROMPT


def play():
    """ Main play loop for game """
    game = Game()
    print "New game of tic-tac-toe is ready to be played!"
    print QUIT_RESTART_PROMPT
    prompt_next_token(game)

    while True:
        user_input = raw_input()

        if user_input == QUIT:
            print "quitting..."
            break

        elif user_input == RESTART:
            print "restarting game..."
            game = Game()
            prompt_next_token(game)

        elif user_input in ["h", "help"]:
            print QUIT_RESTART_PROMPT

        elif user_input.isdigit():

            try:
                game.handle_token(user_input)
            except GameException as error:
                print error
                continue

            winner = game.get_winner()
            if winner:
                print game
                print str(winner) + " is the winner!"
                print QUIT_RESTART_PROMPT
            else:
                prompt_next_token(game)


if __name__ == "__main__":
    play()
