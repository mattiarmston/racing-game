import pygame
import logging
import math

from gameObject import GameObject

class Player(GameObject):
    def __init__(self, x, y, image, game):
        super().__init__(x, y, 94, 231, image, game)
        self.y -= self.height
        self.originalImage = self.image
        self.speed = 0
        self.accel = self.scale(10)
        self.deaccel = self.scale(5)
        self.maxSpeed = self.scale(30)
        self.direction = 0
        self.turningSpeed = 5

    def scale(self, num):
        widthScale = self.game.window.width / 1000
        heightScale = self.game.window.height / 1000
        meanScale = (widthScale + heightScale) / 2
        num *= meanScale
        return num

    def move(self, keys, keyBinds, surface):
        self.updateSpeed(keys, keyBinds)
        self.constrainSpeed()
        self.friction(surface)
        self.turn()
        self.moveSelf()

    def updateSpeed(self, keys, keyBinds):
        for direction in keyBinds:
            for key in keyBinds[direction]:
                if keys[key]:
                    if direction == "left":
                        if self.speed != 0:
                            self.direction += self.turningSpeed
                        logging.info("left  key pressed")
                    if direction == "right":
                        if self.speed != 0:
                            self.direction -= self.turningSpeed
                        logging.info("right key pressed")
                    if direction == "up":
                        self.speed += self.accel
                        logging.info("up    key pressed")
                    if direction == "down":
                        if self.speed - self.deaccel > 0:
                            self.speed -= self.deaccel
                        else:
                            #self.speed = 0
                            self.speed -= self.deaccel
                        logging.info("down  key pressed")

    def constrainSpeed(self):
        self.speed = min(self.speed, self.maxSpeed)
        self.speed = max(self.speed, self.maxSpeed * -1)

    def friction(self, surface):
        if self.speed > surface.friction:
            self.speed -= surface.friction
        elif self.speed < -surface.friction:
            self.speed += surface.friction
        else:
            self.speed = 0

    def turn(self):
        originalCenter = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.originalImage, self.direction)
        newCenter = self.image.get_rect().center
        offsetX = originalCenter[0] - newCenter[0]
        offsetY = originalCenter[1] - newCenter[1]
        self.x += offsetX
        self.y += offsetY
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def moveSelf(self):
        if self.speed != 0:
            radians = math.radians(self.direction)
            diffX = math.sin(radians) * self.speed
            diffY = math.cos(radians) * self.speed
            self.x -= diffX
            self.y -= diffY
            if self.x < 0:
                self.x = 0
                self.speed = - 0.5
            elif self.x + self.width > self.game.window.width:
                self.x = self.game.window.width - self.width
                self.speed = - 0.5
            if self.y < 0:
                self.y = 0
                self.speed = - 0.5
            elif self.y + self.height > self.game.window.height:
                self.y = self.game.window.height - self.height
                self.speed = - 0.5
