import pygame
import time

from window import Window
from assets import Assets
from player import Player
from turn import Turn
from surface import Surface
from finishBanner import FinishBanner

class Game():
    def __init__(self):
        self.window = Window(self)
        self.assets = Assets(self)
        self.finished = False
        self.run = True
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.keyBinds = {
            "left": [pygame.K_a, pygame.K_LEFT],
            "right": [pygame.K_d, pygame.K_RIGHT],
            "up": [pygame.K_w, pygame.K_UP],
            "down": [pygame.K_s, pygame.K_DOWN],
        }
        self.defaultSurface = Surface("grass", self)

    def initGame(self):
        widthScale = self.window.width / 1000
        heightScale = self.window.height / 1000
        self.finishBanner = FinishBanner(
            400 * widthScale, 50 * heightScale, self.assets.finishBanner, self
        )
        self.turn = Turn(6, "right", "dirt", self.assets.sixrightdirt, self)
        self.player = Player(
            self.window.width / 2,
            self.window.height,
            self.assets.playerImage,
            self
        )
        self.turns = [self.turn]
        self.toDraw = [self.turn, self.player, self.finishBanner]

    def takeInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        self.keys = pygame.key.get_pressed()

    def findSurface(self, obj):
        for turn in self.turns:
            offset = (int(obj.x - turn.x), int(obj.y - turn.y))
            poi = turn.mask.overlap(obj.mask, offset)
            if poi != None:
                return turn.surface
        return self.defaultSurface

    def checkIfFinished(self, obj):
        offset = (int(obj.x - self.finishBanner.x), int(obj.y - self.finishBanner.y))
        poi = self.finishBanner.mask.overlap(obj.mask, offset)
        if poi != None:
            return True
        else:
            return False

    def main(self):
        while self.finished == False:
            self.clock.tick(self.FPS)
            self.takeInput()
            surface = self.findSurface(self.player)
            self.player.move(self.keys, self.keyBinds, surface)
            self.window.drawFrame()
            self.finished = self.checkIfFinished(self.player)

    def mainMenu(self):
        self.window.menuScreen()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.initGame()
                    self.main()
                    time.sleep(1)
                    self.mainMenu()
