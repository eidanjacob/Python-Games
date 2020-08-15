import pygame
from pygame.locals import *


LTBROWN = (75, 25, 0)
gry = "Colors[gry]"
blk = "Colors[blk]"
wht = "white"
blu = "blue"
grn = "green"
red = "red"
gld = "gold"
Colors = { blk : (0, 0, 0), wht : (255, 255, 255), blu : (0, 0, 255), grn : (0, 255, 0), red : (255, 0, 0), gld : (255, 255, 0), gry : (128, 128, 128) }
colorNames = [blk, wht, blu, grn, red, gld]

class GameInterface:

    def __init__(self, gc, screen):
        self.gameController = gc
        self.screen = screen
        w = screen.get_width()
        h = screen.get_height()
        self.font = pygame.font.SysFont("Arial Narrow", 20)
        self.tableaus = [[int(x) for x in [w * 0.2, 0, w * 0.6, h * 0.15]], \
                         [int(x) for x in [w * 0.2, h * 0.85, w * 0.6, h * 0.15]], \
                         [int(x) for x in [0, h * 0.1, h * 0.15, w * 0.6]], \
                         [int(x) for x in [w - h * 0.15, h * 0.1, h * 0.15, w * 0.6]]]
        self.playerNames = [[int(x) for x in [w * 0.21, h * 0.01]], \
                            [int(x) for x in [w * 0.21, h * 0.86]], \
                            [int(x) for x in [w * 0.01, h * 0.11]], \
                            [int(x) for x in [w - h * 0.14, h * 0.11]]]
        self.playerScores = [[group[0], int(group[1] + h * 0.025)] for group in self.playerNames ]
        self.playerCoins = [int(w * 0.29), int(h * 0.03), int(w * 0.29), int(h * 0.03) + 35, int(w*0.29), int(h * 0.03) + 70, \
                            int(w * 0.29) + 35, int(h * 0.03), int(w * 0.29) + 35, int(h * 0.03) + 35, int(w*0.29) + 35, int(h * 0.03) + 70, \
                            # Player 2
                            int(w * 0.29), int(h * 0.88), int(w * 0.29), int(h * 0.88) + 35, int(w*0.29), int(h * 0.88) + 70, \
                            int(w * 0.29) + 35, int(h * 0.88), int(w * 0.29) + 35, int(h * 0.88) + 35, int(w*0.29) + 35, int(h * 0.88) + 70, \
                            # Player 3
                            int(w * 0.02), int(h * 0.18), int(w * 0.02) + 35, int(h * 0.18), int(w*0.02)+70, int(h * 0.18), \
                            int(w * 0.02), int(h * 0.18) + 35, int(w * 0.02) + 35, int(h * 0.18) + 35, int(w*0.02) + 70, int(h * 0.18) + 35, \
                            # Player 4
                            int(w * 0.91), int(h * 0.18), int(w * 0.91) + 35, int(h * 0.18), int(w*0.91)+70, int(h * 0.18), \
                            int(w * 0.91), int(h * 0.18) + 35, int(w * 0.91) + 35, int(h * 0.18) + 35, int(w*0.91) + 70, int(h * 0.18) + 35]

    def Draw(self):
        self.screen.fill(LTBROWN)
        for i in range(len(self.gameController.Players)):
            # Draw Player Tableaus
            pygame.draw.rect(self.screen, Colors[gry], self.tableaus[i])
            thisPlayer = self.gameController.Players[i]
            label = self.font.render(thisPlayer.Name, True, Colors[blk], Colors[gry])
            self.screen.blit(label, label.get_rect(left = self.playerNames[i][0], top = self.playerNames[i][1]))
            score = self.font.render("Score: " + str(thisPlayer.Score), True, Colors[blk], Colors[gry])
            self.screen.blit(score, score.get_rect(left = self.playerScores[i][0], top = self.playerScores[i][1]))
        
        # draw card stacks
        
        # draw coins
        for i in range(len(self.gameController.Players)):
            for j in range(6):
                col = Colors[colorNames[j]]
                left = self.playerCoins[12*i + 2*j]
                top = self.playerCoins[12*i + 2*j+1]
                pygame.draw.circle(self.screen, col, (left, top), 15)
        
        for i in range(4):
            # Draw cards on table
            continue

        # TODO: draw nobles (after adding them to game)
