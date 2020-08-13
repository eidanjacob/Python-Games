import pygame
from pygame.locals import *


LTBROWN = (75, 25, 0)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

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
                             

    def Draw(self):
        self.screen.fill(LTBROWN)
        for i in range(len(self.gameController.Players)):
            # Draw Player Tableaus
            pygame.draw.rect(self.screen, GRAY, self.tableaus[i])
            thisPlayer = self.gameController.Players[i]
            label = self.font.render(thisPlayer.Name, True, BLACK, GRAY)
            self.screen.blit(label, label.get_rect(left = self.playerNames[i][0], top = self.playerNames[i][1]))
        
        # draw card stacks
        
        # draw coins
        
        for i in range(4):
            # Draw cards on table
            continue

        # TODO: draw nobles (after adding them to game)
