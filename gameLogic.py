import numpy as np
import train
from random import randint as rand
from keras.models import model_from_json
from keras.utils.vis_utils import plot_model
class Game:
    def __init__(self, row_size=6, column_size=7):
        self.board = np.zeros((row_size, column_size), int)
        self.turn = 1 if rand(0, 1) == 1 else 2
        self.amountOfCheckers = 42 #comes with 21 yellow checkers and 21 red checkers for a total of 42 :)
        self.inputColumn = -1  #just for initilization
        self.winner = None
        self.game_over = False
        self.model = self.getAnExistModel()
        self.twoPlayer = False

    def predict (self, board):
        Y = self.model.predict(board.flatten().reshape((1, 42)))
        return Y[0][self.turn]

    def getAnExistModel(self) :
        try:
            model_file = open('Data/Model/model.json', 'r')
            model = model_file.read()
            model_file.close()
            model = model_from_json(model)
            model.load_weights('Data/Model/weights.h5')
            return model
        except:
            train.main()
            return self.getAnExistModel()

    def getTurn (self):
        if self.turn == 1 :
            return 'Player1'
        else:
            if self.twoPlayer:
                return 'Player2'
            else:
                return 'Computer'

    def changeTurn (self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def move(self, pos, play_yourself=False):
        if (self.twoPlayer == True or self.turn == 1) and not play_yourself:
            column = (pos[0]-50)//100
            if column <0 :
                column=0
            elif column >6:
                column=6
            for row in range(5, -1, -1):
                if self.board[row][column] == 0 :
                    self.board[row][column] = self.turn
                    self.amountOfCheckers -= 1
                    return row, column
            return  -1 , -1
        else :
            #computer's input play_yourself:
            possibleMoves = []
            for column in range (7):
                copy_of_board = np.matrix.copy(pos)
                for row in range (5,-1,-1):
                    if copy_of_board[0][column] != 0 : continue
                    if copy_of_board[row][column] == 0:
                        copy_of_board[row][column] = self.turn
                        possibleMoves.append((row,column,self.predict(copy_of_board)))
                        break
            if possibleMoves == []:
                return
            row, col, prob = possibleMoves[0]
            for i in range (len(possibleMoves)) :
                if possibleMoves[i][2] > prob:
                    row,col ,prob = possibleMoves[i]

            self.board[row][col] = self.turn
            self.amountOfCheckers -= 1
            return row, col

    def moveWithRandomInputs (self) :
        column = rand(0,6)
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.turn
                self.amountOfCheckers -= 1
                return
        self.moveWithRandomInputs()

    def isGameFinished (self):
        for r in range(3):  # test diagonally ()
            for c in range(4):
                if self.board[r][c] == self.turn and self.board[r][c] == self.board[r + 1][c + 1] and self.board[r + 1][c + 1] == self.board[r + 2][
                    c + 2] and self.board[r + 2][c + 2] == self.board[r + 3][c + 3] :
                    self.game_over = True
                    self.winner = self.getTurn()

        if not self.game_over :
            for r in range(5,2,-1):  # test diagonally (ters birim matris)
                for c in range(4):
                    if self.board[r][c] == self.turn and self.board[r][c] == self.board[r - 1][c + 1] and self.board[r - 1][c + 1] == self.board[r - 2][
                        c + 2] and self.board[r - 2][c + 2] == self.board[r - 3][c + 3]:
                        self.game_over = True
                        self.winner = self.getTurn()

        if not self.game_over : # test horizontally
            for r in range(6):
                for c in range(4):
                    if self.board[r][c] == self.turn and self.board[r][c] == self.board[r][c + 1] and self.board[r][c + 1] == self.board[r][
                        c + 2] and self.board[r][c + 2] == self.board[r][c + 3]:
                        self.game_over = True
                        self.winner = self.getTurn()
        if not self.game_over :
            for r in range(3):  # test vertically
                for c in range(7):
                    if self.board[r][c] == self.turn and self.board[r][c] == self.board[r + 1][c] and self.board[r + 1][c] == self.board[r + 2][
                        c] and self.board[r + 2][c] == self.board[r + 3][c]:
                        self.game_over = True
                        self.winner = self.getTurn()

        if not self.game_over :
            if  self.amountOfCheckers == 0 :
                self.winner = 'Draw'
                self.game_over = True
            else :
                self.changeTurn()

        if self.game_over :
            with open("Data/dataset.csv", "a+") as f:
                for row in self.board:
                    for element in row :
                        f.write(str(element) + ',')
                if self.winner == 'Player1':
                    f.write(str(1))
                elif self.winner == 'Player2' or 'Computer':
                    f.write(str(2))
                else:
                    f.write(str(0))
                f.write('\n')
            return True
        else:
            board = self.board
            for i in range(len(board)):
                if 0 in board[i]:
                    return False
            return True

