import pygame, sys
from pygame.locals import *
from SplendorFiles.gameController import *
from SplendorFiles.mainMenu import *

pygame.init()
BROWN = (75, 25, 0)
resolution = (1000,750)
screen = pygame.display.set_mode(resolution)
screen.fill(BROWN) # background color
menu = MainMenu(screen)

def start(game, screen):
    game.StartGame()
    #TODO: draw game

def addPlayer(game, screen):
    if not game.Started:
        game.AddPlayer(menu.text)
        menu.ResetText()
        
def null(game, screen):
    return

switcher = { "start" : start, "addPlayer" : addPlayer, "null" : null }
def ActivateButton(game, screen, pressed):
    func = switcher.get(pressed)
    func(game, screen)
    
buttons = menu.Buttons
pygame.display.set_caption('Splendor')
pygame.display.update()
gc = GameController()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not gc.Started:
                menu.UpdateText(screen, event)
                continue
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if menu.TextInputField.collidepoint(mouse):
                menu.TextInputActive = True
                continue
            else:
                menu.TextInputActive = False
                
            pressed = "null"
            for button, rect in buttons.items():
                if rect.collidepoint(mouse):
                    pressed = button
                    ActivateButton(gc, screen, pressed)
                    break

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        pygame.display.update()
