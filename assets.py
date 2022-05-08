import pygame
import os

class Assets():
    def __init__(self, game):
        self.game = game
        self.mainFont = pygame.font.SysFont("arial", 70)
        self.titleFont = pygame.font.SysFont("C059", 70, italic=True, bold=True)
        self.BGImage = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "grass-image.png")),
            (self.game.window.width, self.game.window.height)
        )
        self.titleImage = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "title-image.png")),
            (self.game.window.width, self.game.window.height)
        )
        self.finishBanner = pygame.image.load(os.path.join("assets", "finish-banner.png"))
        self.playerImage = pygame.image.load(os.path.join("assets", "subaru-impretza.png"))
        self.sixrightdirt = pygame.image.load(os.path.join("assets", "six-right-dirt.png"))
        self.dirtTurns = [
            self.sixrightdirt,
        ]

    def scaleImage(self, img):
        widthScale = self.game.window.width / 1000
        heightScale = self.game.window.height / 1000
        width = widthScale * img.get_width()
        height = heightScale * img.get_height()
        scaleImg = pygame.transform.scale(
            img,
            (width, height)
        )
        return scaleImg
