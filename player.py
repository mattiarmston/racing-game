import logging

from gameObject import GameObject

class Player(GameObject):
    def __init__(self, image, game):
        super().__init__(50, 50, 1157 / 4, 470 / 4, image, game)
        self.speedX = 0
        self.speedY = 0
        self.accelX = 1
        self.accelY = 1
        self.maxSpeedX = 50
        self.maxSpeedY = 50

    def move(self, keys, keyBinds):
        self.updateSpeed(keys, keyBinds)
        self.constrainSpeed()
        self.moveSelf()

    def updateSpeed(self, keys, keyBinds):
        for direction in keyBinds:
            for key in keyBinds[direction]:
                if keys[key]:
                    if direction == "left":
                        self.speedX -= self.accelX
                        logging.info("left  key pressed")
                    if direction == "right":
                        self.speedX += self.accelX
                        logging.info("right key pressed")
                    if direction == "up":
                        self.speedY -= self.accelY
                        logging.info("up    key pressed")
                    if direction == "down":
                        self.speedY += self.accelY
                        logging.info("down  key pressed")

    def constrainSpeed(self):
        if self.speedX > self.maxSpeedX:
            self.speedX = self.maxSpeedX
        if self.speedX < self.maxSpeedX * -1:
            self.speedX = self.maxSpeedX * -1
        if self.speedY > self.maxSpeedY:
            self.speedY = self.maxSpeedY
        if self.speedY < self.maxSpeedY * -1:
            self.speedY = self.maxSpeedY * -1

    def friction(self):
        return

    def moveSelf(self):
        self.x += self.speedX
        self.y += self.speedY
        if self.x < 0:
            self.x = 0
            self.speedX = 0
        elif self.x + self.width > self.game.window.width:
            self.x = self.game.window.width - self.width
            self.speedX = 0
        if self.y < 0:
            self.y = 0
            self.speedY = 0
        elif self.y + self.height > self.game.window.height:
            self.y = self.game.window.height - self.height
            self.speedY = 0
