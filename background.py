import pygame

from gameObject import GameObject

class Background(GameObject):
    def __init__(self, x, y, width, height, image, game):
        super().__init__(x, y, width, height, image, game)
        self.startX = x
        self.startY = y
        self.setTiles()

    def setTiles(self):
        self.tiles = [[self.image]]
        self.tileWidth = self.width
        self.tileHeight = self.height
        self.surface = self.game.window.window.copy()

    def scroll1(self, x, y):
        self.x += x
        self.y += y
        if self.x < 0 - self.width:
            self.x = self.game.bg2.x + self.width
        elif self.x > self.game.window.width:
            self.x = self.game.bg2.x - self.width
        if self.y < 0 - self.height:
            self.y = self.game.bg2.y + self.height
        elif self.y > self.game.window.height:
            self.y = self.game.bg2.y - self.width

    def scroll2(self, x, y):
        self.x += x
        self.y += y
        if self.x < 0 - self.width:
            self.x = self.game.bg1.x + self.width
        elif self.x > self.game.window.width:
            self.x = self.game.bg1.x - self.width
        if self.y < 0 - self.height:
            self.y = self.game.bg1.y + self.height
        elif self.y > self.game.window.height:
            self.y = self.game.bg1.y - self.width

    def scroll3(self, x, y):
        self.x += x
        self.y += y
        if self.x < 0 - self.width:
            self.x = self.game.bg4.x + self.width
        elif self.x > self.game.window.width:
            self.x = self.game.bg4.x - self.width
        if self.y < 0 - self.height:
            self.y = self.game.bg4.y + self.height
        elif self.y > self.game.window.height:
            self.y = self.game.bg4.y - self.width

    def scroll4(self, x, y):
        self.x += x
        self.y += y
        if self.x < 0 - self.width:
            self.x = self.game.bg3.x + self.width
        elif self.x > self.game.window.width:
            self.x = self.game.bg3.x - self.width
        if self.y < 0 - self.height:
            self.y = self.game.bg3.y + self.height
        elif self.y > self.game.window.height:
            self.y = self.game.bg3.y - self.width
