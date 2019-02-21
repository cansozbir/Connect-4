from random import randint as rand

class Game :

    def __init__(self , row_size=6, column_size=7):

        self.board = [[0 for i in range (column_size)] for j in range (row_size)]
        self.turn = 1 if rand(0,1)==1 else 2
        self.amountOfCheckers = 42 #comes with 21 yellow checkers and 21 red checkers for a total of 42 :)
        self.inputColumn = -1  #just for initilization
        self.winner = None
        self.game_over = False


    def getTurn (self):
        return 'Player1' if self.turn==1 else 'Player2'

    def changeTurn (self) :
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def printBoard(self):
        print(self.board)

    def move(self, pos):
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
    def isGameFinished (self):

        for r in range(3):  # test diagonally (birim matris)
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
            self.printBoard()
            if self.winner =='Draw ':
                print('Berabere !')
            else :
                print('Tebrikler,', self.winner, 'kazandi \o/' )



    #TODO neural network ile egit


