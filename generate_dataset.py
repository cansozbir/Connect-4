import numpy as np
from gameLogic import Game
from random import randint


def generate () :
    # generates dataset with totally random inputs until you interrupt it.
    game = Game()
    while True:
        if not game.game_over :
            game.moveWithRandomInputs()
            game.isGameFinished()
        if game.game_over :
            print(game.board)
            game.board= np.zeros((6, 7), int)
            game.game_over = False
            game.turn = 1 if randint(0, 1) == 1 else 2
            game.amountOfCheckers = 42
            game.winner = None

if __name__ == '__main__' :
    generate()