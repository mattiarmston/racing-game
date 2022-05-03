import pygame
import logging
import math

from gameObject import GameObject

class Player(GameObject):
    def __init__(self, image, game):
        super().__init__(500, 500, 470 / 4, 1157 / 4, image, game)
        self.originalImage = self.image
        self.speed = 0
        self.accel = 10
        self.maxSpeed = 50
        self.direction = 0
        self.turningSpeed = 5
        self.turningAccel = 5

    def move(self, keys, keyBinds):
        self.updateSpeed(keys, keyBinds)
        self.constrainSpeed()
        self.friction()
        self.turn()
        self.moveSelf()

    def updateSpeed(self, keys, keyBinds):
        for direction in keyBinds:
            for key in keyBinds[direction]:
                if keys[key]:
                    if direction == "left":
                        self.direction += self.turningSpeed
                        logging.info("left  key pressed")
                    if direction == "right":
                        self.direction -= self.turningSpeed
                        logging.info("right key pressed")
                    if direction == "up":
                        self.speed += self.accel
                        logging.info("up    key pressed")
                    if direction == "down":
                        self.speed -= self.accel
                        logging.info("down  key pressed")

    def constrainSpeed(self):
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif self.speed < self.maxSpeed * -1:
            self.speed = self.maxSpeed * -1

    def friction(self):
        surfaceFriction = 6
        if self.speed > surfaceFriction:
            self.speed -= surfaceFriction
        elif self.speed < -surfaceFriction:
            self.speed += surfaceFriction
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
            self.speed = 0
        elif self.x + self.width > self.game.window.width:
            self.x = self.game.window.width - self.width
            self.speed = 0
        if self.y < 0:
            self.y = 0
            self.speed = 0
        elif self.y + self.height > self.game.window.height:
            self.y = self.game.window.height - self.height
            self.speed = 0
