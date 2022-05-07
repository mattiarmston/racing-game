import pygame

class GameObject:
    def __init__(self, x, y, width, height, image, game):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scaleSelf(game)
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.game = game
        self.mask = pygame.mask.from_surface(self.image)

    def scaleSelf(self, game):
        widthScale = game.window.width / 1000
        heightScale = game.window.height / 1000
        self.width *= widthScale
        self.height *= heightScale
