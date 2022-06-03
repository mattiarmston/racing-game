import pygame
import time
import logging

from window import Window
from assets import Assets
from player import Player
from background import Background
from turn import Turn
from surface import Surface
from finishBanner import FinishBanner

class Game():
    def __init__(self):
        self.window = Window(self)
        self.assets = Assets(self)
        self.finished = False
        self.run = True
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
        self.bg1 = Background(
            -500,
            -500,
            self.window.width,
            self.window.height,
            self.assets.BGImage,
            self
        )
        self.bg2 = Background(
            self.window.width - 500,
            -500,
            self.window.width,
            self.window.height,
            self.assets.BGImage,
            self
        )
        self.bg3 = Background(
            -500,
            self.window.height - 500,
            self.window.width,
            self.window.height,
            self.assets.BGImage,
            self
        )
        self.bg4 = Background(
            self.window.width - 500,
            self.window.height - 500,
            self.window.width,
            self.window.height,
            self.assets.BGImage,
            self
        )
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
        self.bgs = [self.bg1, self.bg2, self.bg3, self.bg4]
        #self.toDraw = [self.bg, self.turn, self.player, self.finishBanner]
        self.toDraw = [self.bg1, self.bg2, self.bg3, self.bg4]

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

    def scrollBG(self):
        self.bg1.scroll1(5, 5)
        self.bg2.scroll2(5, 5)
        self.bg3.scroll3(5, 5)
        self.bg4.scroll4(5, 5)

    def removeBGs(self):
        del self.toDraw[0:4]

    def checkIfFinished(self, obj):
        offset = (int(obj.x - self.finishBanner.x), int(obj.y - self.finishBanner.y))
        poi = self.finishBanner.mask.overlap(obj.mask, offset)
        if poi != None:
            return True
        else:
            return False

    def main(self):
        while self.finished == False:
            self.clock.tick(self.window.fps)
            self.takeInput()
            surface = self.findSurface(self.player)
            self.player.move(self.keys, self.keyBinds, surface)
            self.scrollBG()
            self.window.drawFrame()
            self.finished = self.checkIfFinished(self.player)

    def mainMenu(self):
        self.window.menuScreen()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    logging.info("Initialising game")
                    self.initGame()
                    logging.info("Game initialised")
                    self.main()
                    time.sleep(1)
                    self.finished = False
                    self.mainMenu()
