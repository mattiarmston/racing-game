import pygame
import os

class Assets():
    def __init__(self, game):
        self.game = game
        self.mainFont = pygame.font.SysFont("arial", int(self.scale(70)))
        self.titleFont = pygame.font.SysFont(
            "C059", int(self.scale(70)), italic=True, bold=True
        )
        self.grassImage = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "free-grass.png")),
            (self.game.window.width, self.game.window.height)
        )
        self.titleImage = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "title-image.png")),
            (self.game.window.width, self.game.window.height)
        )
        self.finishBanner = pygame.image.load(os.path.join("assets", "finish-banner.png"))
        self.playerImage = pygame.image.load(os.path.join("assets", "subaru-impretza.png"))
        self.stage1 = pygame.image.load(os.path.join("assets", "stage1.png"))
        self.sixrightdirt = pygame.image.load(os.path.join("assets", "six-right-dirt.png"))
        self.straightdirt = pygame.image.load(os.path.join("assets", "straight-dirt.png"))
        self.dirtTurns = [
            self.sixrightdirt,
        ]

    def scale(self, num):
        widthScale = self.game.window.width / 1000
        heightScale = self.game.window.height / 1000
        meanScale = (widthScale + heightScale) / 2
        return num * meanScale
