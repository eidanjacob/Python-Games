import pygame, sys
from pygame.locals import *

blk = "black"
gry = "gry"
Colors = { blk : (0, 0, 0), gry : (128, 128, 128) }

class MainMenu:

    def __init__(self, screen):
        self.rectangles = {}
        self.screen = screen
        self.font = pygame.font.SysFont("Arial Narrow", 25)
        self.textColor = Colors[blk]
        self.fillColor = Colors[gry]
        self.w = screen.get_width()
        self.h = screen.get_height()
        self.CreateButtons()
        self.TextInputField = pygame.draw.rect(screen, self.fillColor, [int(x) for x in [self.w * 0.55, self.h * 0.65, self.w * 0.2, self.h * 0.1]])
        self.TextInputActive = False
        self.text = ""

    def UpdateText(self, event):
        if not self.TextInputActive:
            return
        elif event.key is pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif len(self.text) < 12:
            self.text += event.unicode

        self.RenderText()

    def ResetText(self):
        self.text = ""
        self.RenderText()

    def RenderText(self):
        rendered = self.font.render(self.text, True, self.textColor, self.fillColor)
        pygame.draw.rect(self.screen, self.fillColor, [int(x) for x in [self.w * 0.55, self.h * 0.65, self.w * 0.2, self.h * 0.1]])
        self.screen.blit(rendered, rendered.get_rect(center=self.TextInputField.center))

    def CreateButtons(self):
        start = self.StartButton()
        add = self.AddPlayerButton()
        self.Buttons = { "start" : start, "addPlayer" : add }

    def StartButton(self):
        startButton = pygame.draw.rect(self.screen, self.fillColor, [int(x) for x in [self.w * 0.25, self.h * 0.45, self.w * 0.2, self.h * 0.1]])
        text = self.font.render("Start Game", True, self.textColor, self.fillColor)
        text_rect = text.get_rect(center = startButton.center)
        self.screen.blit(text, text_rect)
        return startButton

    def AddPlayerButton(self):
        addPlayerButton = pygame.draw.rect(self.screen, self.fillColor, [int(x) for x in [self.w * 0.25, self.h * 0.65, self.w * 0.2, self.h * 0.1]])
        text = self.font.render("Add a Player", True, self.textColor, self.fillColor)
        text_rect = text.get_rect(center = addPlayerButton.center)
        self.screen.blit(text, text_rect)
        return addPlayerButton
