from gameLogic import  Game
import pygame
from pygame.locals import *

class userInterface:

    def __init__(self):
        self.game = Game() # game initilization
        pygame.init()
        pygame.font.init()
        self.bigFont= pygame.font.SysFont(None, 60)
        self.mediumFont= pygame.font.SysFont(None, 40)
        self.smallFont = pygame.font.SysFont(None, 26)
        self.run = True  # it's because quit event in playgame method
        self.gameDisplay = pygame.display.set_mode((800,700))
        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (20,26,183)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Connect4 Game')

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
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skip=True
                    self.run=False

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if ((pos[0]>290 and pos[0]<530) and (pos[1]>246 and pos[1]<300)):
                        skip = True
                        self.playgame()
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


    def playgame (self) :
        self.gameDisplay.fill(self.blue)


        for row in range(1,7):
            for column in range(1,8):
                pygame.draw.circle(self.gameDisplay, self.white, [column*100, row* 100 ], 30)

        while self.run:
            self.clock.tick(30) #This limits the while loop to a max of 10 times per second.
            player1 = self.mediumFont.render('Player1',1,self.red if self.game.turn==1 else (128,128,128))
            player2 = self.mediumFont.render('Player2',1,self.yellow if self.game.turn==2 else (128,128,128))

            self.gameDisplay.blit(player1,(50,24))
            self.gameDisplay.blit(player2,(650,24))
            if not self.game.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False

                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        row,column= self.game.move(pos)
                        if row != -1 and column != -1:
                            pygame.draw.circle(self.gameDisplay, self.red if self.game.turn==1 else self.yellow, [(column+1)*100, (row+1)* 100 ],30)
                            self.game.isGameFinished()

            else :
                self.endOfGame()
            pygame.display.update()

    def playAgain (self):
        self.game = Game()
        self.welcomeScreen()


    def endOfGame (self) :
        pygame.draw.rect(self.gameDisplay,(120,120,155),(0,0,800,52))
        pygame.draw.rect(self.gameDisplay, (0,200,0), (0,640 , 800, 30))
        pygame.draw.rect(self.gameDisplay, (190, 20, 20), (0,670,  800, 30))
        if self.game.winner =='Draw':
            congrats = self.mediumFont.render('Draw!', 1, (0,0,0))

        else:
            congrats= self.mediumFont.render(self.game.getTurn()+' wins ! Congrats!', 1,self.red if self.game.turn==1 else self.yellow)
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