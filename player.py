import pygame
import logging
import math

from gameObject import GameObject

class Player(GameObject):
    def __init__(self, x, y, image, game):
        super().__init__(x, y, 94, 231, image, game)
        self.y -= self.height
        self.startX, self.startY = self.x, self.y
        self.startCenter = self.image.get_rect().center
        self.originalImage = self.image
        self.speed = 0
        self.accel = self.scale(0.6)
        self.deaccel = self.scale(0.75)
        self.maxSpeed = self.scale(75)
        self.accelerating = False
        self.direction = 0
        self.turningSpeed = 1

    def scale(self, num):
        widthScale = self.game.window.width / 1000
        heightScale = self.game.window.height / 1000
        meanScale = (widthScale + heightScale) / 2
        num *= meanScale
        return num

    def move(self, keys, keyBinds, surface):
        self.updateSpeed(keys, keyBinds)
        self.balanceSpeed()
        self.constrainSpeed()
        self.friction(surface)
        self.turn()
        self.moveSelf()

    def updateSpeed(self, keys, keyBinds):
        self.accelerating = False
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
                        self.accelerating = True
                        logging.info("up    key pressed")
                    if direction == "down":
                        if self.speed - self.deaccel > 0:
                            self.speed -= self.deaccel
                        else:
                            #self.speed = 0
                            self.speed -= self.accel * 2/3
                        logging.info("down  key pressed")

    def balanceTurn(self):
        return

    def balanceSpeed(self):
        if self.speed < 5 and self.accelerating:
            self.speed += 0.1
        if self.speed < 10 and self.accelerating:
            self.speed += 0.075
        if self.speed < 20 and self.accelerating:
            self.speed += 0.05
        elif self.speed > 20:
            self.speed -= 0.05
        elif self.speed > 30:
            self.speed -= 0.1
        elif self.speed > 40:
            self.speed -= 0.15

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
            elif self.x + self.width > self.game.window.width:
                self.x = self.game.window.width - self.width
            if self.y < 0:
                self.y = 0
            elif self.y + self.height > self.game.window.height:
                self.y = self.game.window.height - self.height
