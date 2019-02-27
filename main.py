import pygame
from gameLogic import  Game
from pygame.locals import *

class userInterface:

    def __init__(self):
        self.game = Game()  #game initilization
        pygame.init()
        pygame.font.init()
        self.bigFont= pygame.font.SysFont(None, 60)
        self.mediumFont= pygame.font.SysFont(None, 40)
        self.smallFont = pygame.font.SysFont(None, 26)
        self.run = True  # it's because quit event in playgame method
        self.gameDisplay = pygame.display.set_mode((800,700))
        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0,30,130)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Connect4 Game')
        self.batch_size = 0


    def welcomeScreen (self) :

        skip = False
        self.gameDisplay.fill((66, 111, 155))
        playgame = self.bigFont.render('Play Game', True, (0,0,0))
        about = self.mediumFont.render('About', True, (0, 0, 0))
        quit = self.mediumFont.render('Quit', True, (0, 0, 0))
        author = self.smallFont.render('by can sozbir', True, (0, 0, 0))
        self.gameDisplay.blit(playgame, (300, 250))
        self.gameDisplay.blit(about,(300,310))
        self.gameDisplay.blit(quit,(300,360))
        self.gameDisplay.blit(author, (650, 650))
        while not skip :
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skip=True
                    self.run=False

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if ((pos[0]>290 and pos[0]<530) and (pos[1]>246 and pos[1]<300)):
                        skip = True
                        self.selectEnemy()
                    elif ((pos[0]>298 and pos[0]<400) and (pos[1]>310 and pos[1]<340)):
                        skip = True
                        self.about()
                    elif ((pos[0]>298 and pos[0]<365) and (pos[1]>360 and pos[1]<380)):
                        skip = True
                        self.run = False
            pygame.display.update()

    def about (self) :

        txt = 'Challenge a friend to disc-dropping fun with the classic game of Connect 4!\n' \
              'Drop your red or yellow discs in the grid and be the first to get 4 in a row to win.\n' \
              'If your opponent is getting too close to 4 in a row, block them with your own disc!\n' \
              'Created by Can Sozbir'.split('\n')
        self.gameDisplay.fill((66, 111, 155))
        aboutscreen = []
        for i in range (4):
            aboutscreen.append(self.smallFont.render(txt[i],True,(0,0,0)))
            self.gameDisplay.blit(aboutscreen[i], (80, 20*i+250))

        returnMenu = self.mediumFont.render('Main menu',True,(0,0,0))
        self.gameDisplay.blit(returnMenu,(325,400))
        skip = False
        while not skip :
            self.clock.tick(30)  # This limits the while loop to a max of 10 times per second.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skip = False
                    self.run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if ((pos[0]>320 and pos[0]<480) and (pos[1]>395 and pos[1]<435)):
                        skip = True
                        self.welcomeScreen()
            pygame.display.update()


    def selectEnemy (self):

        skip = False
        self.gameDisplay.fill((66, 111, 155))
        onePlayer = self.mediumFont.render('One player', True, (0, 0, 0))
        twoPlayer = self.mediumFont.render('Two player', True, (0, 0, 0))
        self.gameDisplay.blit(onePlayer, (300, 250))
        self.gameDisplay.blit(twoPlayer, (300, 360))
        while not skip:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skip = True
                    self.run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if ((pos[0] > 290 and pos[0] < 460) and (pos[1] > 246 and pos[1] < 285)):
                        skip = True
                        self.game.twoPlayer = False
                        self.playgame()
                    elif ((pos[0] > 295 and pos[0] < 450) and (pos[1] > 358 and pos[1] < 395)):
                        skip = True
                        self.game.twoPlayer = True
                        self.playgame()
            pygame.display.update()


    def playgame (self) :

        self.gameDisplay.fill(self.blue)
        for row in range(1,7):
            for column in range(1,8):
                pygame.draw.circle(self.gameDisplay, self.white, [column*100, row* 100 ],30)

        while self.run:
            self.clock.tick(30) #This limits the while loop to a max of 30 times per second.
            player1 = self.mediumFont.render('Player1',1,self.red if self.game.turn==1 else (128,128,128))
            player2 = self.mediumFont.render('Player2' if self.game.twoPlayer==True else 'Computer',1,self.yellow if self.game.turn==2 else (128,128,128))
            self.gameDisplay.blit(player1,(50,24))
            self.gameDisplay.blit(player2,(650,24))

            if not self.game.game_over:
                if self.game.twoPlayer or (self.game.turn == 1) :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.run = False

                        if  event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            row,column= self.game.move(pos)
                            if (row == -1 or column == -1 ): continue
                            pygame.draw.circle(self.gameDisplay, self.red if self.game.turn==1 else self.yellow, [(column+1)*100, (row+1)* 100 ],30)
                            self.game.isGameFinished()
                else : # computer's move
                    #time.sleep(0.5)
                    pygame.time.wait(300)
                    row,column= self.game.move(self.game.board)
                    pygame.draw.circle(self.gameDisplay, self.yellow, [(column + 1) * 100, (row + 1) * 100], 30)
                    self.game.isGameFinished()

            else :
                self.endOfGame()
            pygame.display.update()

    def playAgain (self):

        self.game = Game()
        self.welcomeScreen()


    def endOfGame (self) :

        pygame.draw.rect(self.gameDisplay,(200,0,0) if self.game.turn==1 else (255,255,0),(0,0,800,52))
        pygame.draw.rect(self.gameDisplay, (102,204,0), (0,640 , 800, 30))
        pygame.draw.rect(self.gameDisplay, (204, 0, 0), (0,670,  800, 30))
        if self.game.winner =='Draw':
            congrats = self.mediumFont.render('Draw!', 1, (0,0,0))
        elif self.game.winner == 'Player1':
            congrats= self.mediumFont.render(self.game.getTurn()+' wins ! Congrats!', 1,(0,0,0))

        else :
            congrats= self.mediumFont.render(self.game.getTurn()+' wins ! Congrats!' if self.game.twoPlayer==True else self.game.getTurn()+' wins !', 1,(0,0,0))
        quit= self.smallFont.render('Quit',1,(0,0,0))
        playAgain= self.smallFont.render('Play again',1,(0,0,0))
        self.gameDisplay.blit(congrats,(280,15))
        self.gameDisplay.blit(quit,(375,680))
        self.gameDisplay.blit(playAgain,(350,650))

        skip = False
        while not skip :
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skip= True
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[1] > 640:
                        if pos[1] < 670:
                            self.playAgain()
                        else :
                            skip = True
                            self.run = False

            pygame.display.update()


if  __name__ == "__main__":
    game = userInterface()
    game.welcomeScreen()