import pygame
import os

class Assets():
    def __init__(self):
        self.BGImage = pygame.image.load(os.path.join("assets", "BGImage.png"))
        #self.playerImage = pygame.image.load(os.path.join("assets", "red-box.png"))
        self.playerImage = pygame.image.load(os.path.join("assets", "stolen-subaru-impretza.png"))
