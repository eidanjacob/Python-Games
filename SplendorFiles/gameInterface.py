import pygame
from pygame.locals import *


LTBROWN = (75, 25, 0)

class GameInterface:

    def Draw(self, gameController, screen):
        screen.fill(LTBROWN)
        for player in gameController.Players:
            # Draw Player Tableaus

        # draw card stacks

        # draw coins

        for i in range(4):
            # Draw cards on table
