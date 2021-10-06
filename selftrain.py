from gameLogic import Game
from train import main
game = Game()
n = int(input())
for i in range(n):
    while True:
        if game.isGameFinished():
            main()
            print(i + 1)
            game = Game()
            break
        game.move(game.board, True)
        game.changeTurn()

