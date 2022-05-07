import pygame

from assets import Assets
from settings import window_width, window_height

class Window():
    def __init__(self, game):
        settings = self.getSettings()
        self.game = game
        self.width = settings["window_width"]
        self.height = settings["window_height"]
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ultimate rally")

    def getSettings(self):
        settings = {
            "window_width": 1000,
            "window_height": 1000,
        }
        try:
            settings["window_width"] = int(window_width)
        except ValueError:
            pass
        try:
            settings["window_height"] = int(window_height)
        except ValueError:
            pass
        return settings

    def drawFrame(self):
        self.window.blit(self.game.assets.BGImage, (0,0))
        for item in self.game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        pygame.display.update()

    def menuScreen(self):
        self.window.blit(self.game.assets.titleImage, (0,0))
        startText = self.game.titleFont.render("Press space to play", 1, (7, 44, 166))
        xposition = self.width/2 - startText.get_width()/2
        yposition = self.height/2 - startText.get_height()/2 + 35
        self.window.blit(startText, (xposition, yposition))
        pygame.display.update()
