import pygame
import time
import logging

from window import Window
from assets import Assets
from player import Player
from background import Background
from turn import Turn
from stage import Stage
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
        self.defaultSurface = Surface("dirt", self)

    def initGame(self):
        widthScale = self.window.width / 1000
        heightScale = self.window.height / 1000
        self.bg1 = Background(
            0, # x position
            0, # y position
            self.window.width, # width
            self.window.height, # height
            self.assets.grassImage, # image
            self # game
        )
        self.bg2 = Background(
            self.window.width,
            0,
            self.window.width,
            self.window.height,
            self.assets.grassImage,
            self
        )
        self.bg3 = Background(
            0,
            self.window.height,
            self.window.width,
            self.window.height,
            self.assets.grassImage,
            self
        )
        self.bg4 = Background(
            self.window.width,
            self.window.height,
            self.window.width,
            self.window.height,
            self.assets.grassImage,
            self
        )
        self.bg1.setAdjacentBG(self.bg2, self.bg3)
        self.bg2.setAdjacentBG(self.bg1, self.bg4)
        self.bg3.setAdjacentBG(self.bg4, self.bg1)
        self.bg4.setAdjacentBG(self.bg3, self.bg2)
        self.bgs = [self.bg1, self.bg2, self.bg3, self.bg4]
        self.finishBanner = FinishBanner(
            400 * widthScale,
            -10000 * heightScale,
            self.assets.finishBanner,
            self
        )
        #self.turn = Turn(6, "right", "dirt", self.assets.sixrightdirt, self)
        self.turn = Turn(0, "straight", "dirt", self.assets.straightdirt, self)
        self.stage1 = Stage(
            self.window.width * -9,
            self.window.height * -9,
            self.window.width * 10,
            self.window.height * 10,
            self.assets.stage1,
            self,
            Surface("dirt", self)
        )
        self.player = Player(
            self.window.width / 2,
            self.window.height * 19/20,
            self.assets.playerImage,
            self
        )
        self.turns = [self.turn]
        self.toDraw = [
            self.bg1,
            self.bg2,
            self.bg3,
            self.bg4,
            #self.stage1,
            self.turn,
            self.player,
            self.finishBanner
        ]

    def takeInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        self.keys = pygame.key.get_pressed()

    def findSurface(self, obj):
        offset = (int(obj.x - self.stage1.x), int(obj.y - self.stage1.y))
        poi = self.stage1.mask.overlap(obj.mask, offset)
        if poi != None:
            return self.stage1.surface
        return self.defaultSurface

    def oldfindSurface(self, obj):
        for turn in self.turns:
            offset = (int(obj.x - turn.x), int(obj.y - turn.y))
            poi = turn.mask.overlap(obj.mask, offset)
            if poi != None:
                return turn.surface
        return self.defaultSurface

    def scrollBG(self):
        def scroll(x, y):
            for bg in self.bgs:
                bg.move(x, y)
            for bg in self.bgs:
                bg.wrap()

        diffX, diffY = 0, 0
        heightLimit = self.window.height * 6/10
        bottomLimit = self.window.height * 19/20
        leftLimit = self.window.width / 5
        rightLimit = self.window.width * 4/5
        player_direction = self.player.direction % 360
        if self.player.speed != 0:
            if self.player.y < heightLimit and self.player.speed != 0:
                diffY = heightLimit - self.player.y
            if self.player.y + self.player.height > bottomLimit and self.player.speed != 0:
                if self.player.speed > 0:
                    if self.player.direction % 360 > 90 and self.player.direction % 360 < 270:
                        diffY = bottomLimit - (self.player.y + self.player.height)
                elif self.player.speed < 0:
                    if player_direction < 90 or player_direction > 270:
                        diffY = bottomLimit - (self.player.y + self.player.height)
            if self.player.x + self.player.width > rightLimit and self.player.speed != 0:
                diffX = rightLimit - self.player.x - self.player.width
            if self.player.x < leftLimit and self.player.speed != 0:
                diffX = leftLimit - self.player.x
        for item in self.toDraw:
            if type(item) != Background:
                item.x += diffX
                item.y += diffY
        scroll(diffX, diffY)


    def newscrollBG(self):
        def scroll(x, y):
            for bg in self.bgs:
                bg.move(x, y)
            for bg in self.bgs:
                bg.wrap()

        diffX, diffY = 0, 0
        if self.player.speed != 0:
            center = self.player.image.get_rect().center
            diffX = self.player.startX - self.player.x
            diffY = self.player.startY - self.player.y
            #diffX -= self.player.startCenter[0] - center[0]
            print("self.player.startCenter, center:", self.player.startCenter, center)
        #    if self.player.speed != 0:
        #        diffX = self.player.startX - self.player.x - self.player.width
        #    if self.player.speed != 0:
        #        diffX = self.player.startX - self.player.x
        for item in self.toDraw:
            if type(item) != Background:
                item.x += diffX
                item.y += diffY
        scroll(diffX, diffY)


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
