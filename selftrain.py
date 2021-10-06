from gameLogic import Game
from train import main
game = Game()
n = int(input())
for i in range(n):
    while True:
        game.isGameFinished()
        if game.game_over:
            main()
            print(i + 1)
            game = Game()
            break
        game.move(game.board, True)
        game.changeTurn()

