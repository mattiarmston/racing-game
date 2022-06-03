import pygame

from gameObject import GameObject

class Background(GameObject):
    def __init__(self, x, y, width, height, image, game):
        super().__init__(x, y, width, height, image, game)
        self.startX = x
        self.startY = y

    def setAdjacentBG(self, sameRow, sameCol):
        self.sameRow = sameRow
        self.sameCol = sameCol

    def move(self, x, y):
        self.x += x
        self.y += y

    def wrap(self):
        """
        Wrap a background back onto the screen if it scrolls off.
        """
        self.wrapX()
        self.wrapY()

    def wrapX(self):
        if self.x < 0 - self.width:
            self.x = self.sameRow.x + self.width
        elif self.x > self.game.window.width:
            self.x = self.sameRow.x - self.width

    def wrapY(self):
        if self.y < 0 - self.height:
            self.y = self.sameCol.y + self.height
        elif self.y > self.game.window.height:
            self.y = self.sameCol.y - self.width
