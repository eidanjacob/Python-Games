import pygame
from pygame.locals import *


LTBROWN = (75, 25, 0)
GRAY = (128, 128, 128)

class GameInterface:

    def Draw(self, gameController, screen):
        w = screen.get_width()
        h = screen.get_height()
        screen.fill(LTBROWN)
        tableau_locations = [[int(x) for x in [w * 0.2, 0, w * 0.6, h * 0.15]], \
                             [int(x) for x in [w * 0.2, h * 0.85, w * 0.6, h * 0.15]], \
                             [int(x) for x in [0, h * 0.1, h * 0.15, w * 0.6]], \
                             [int(x) for x in [w - h * 0.15, h * 0.1, h * 0.15, w * 0.6]]]
        for i in range(len(gameController.Players)):
            # Draw Player Tableaus
            pygame.draw.rect(screen, GRAY, tableau_locations[i])
        
        # draw card stacks
        
        # draw coins
        
        for i in range(4):
            # Draw cards on table
            continue

        # TODO: draw nobles (after adding them to game)
