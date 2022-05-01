import pygame

from assets import Assets

class Window():
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ultimate rally")

    def drawFrame(self, game):
        self.window.blit(game.BGImage, (0,0))
        for item in game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        pygame.display.update()

    def menuScreen(self, game):
        self.window.blit(game.BGImage, (0,0))
        startText = game.mainFont.render("Press space to play", 1, (0, 0, 0))
        xposition = self.width/2 - startText.get_width()/2
        yposition = self.height/2 - startText.get_height()/2
        self.window.blit(startText, (xposition, yposition))
        pygame.display.update()

