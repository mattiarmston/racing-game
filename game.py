import pygame

from window import Window
from assets import Assets
from player import Player
from turn import Turn

class Game():
    def __init__(self):
        self.window = Window(self)
        self.assets = Assets(self)
        self.BGImage = pygame.transform.scale(
            self.assets.BGImage, (self.window.width, self.window.height)
        )
        self.titleImage = pygame.transform.scale(
            self.assets.titleImage, (self.window.width, self.window.height)
        )
        self.toDraw = []
        self.lost = False
        self.run = True
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.mainFont = pygame.font.SysFont("arial", 70)
        self.titleFont = pygame.font.SysFont("C059", 70, italic=True, bold=True)
        self.keyBinds = {
            "left": [pygame.K_a, pygame.K_LEFT],
            "right": [pygame.K_d, pygame.K_RIGHT],
            "up": [pygame.K_w, pygame.K_UP],
            "down": [pygame.K_s, pygame.K_DOWN],
        }

    def initGame(self):
        self.turn = Turn(6, "right", "dirt", self.assets.sixrightdirt, self)
        self.player = Player(self.assets.playerImage, self)
        #self.turns
        self.toDraw = [self.turn, self.player]

    def takeInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        self.keys = pygame.key.get_pressed()
        self.player.move(self.keys, self.keyBinds)

    def findSurface(self, obj):
        return

    def main(self):
        while self.lost == False:
            self.clock.tick(self.FPS)
            self.takeInput()
            self.window.drawFrame()

    def mainMenu(self):
        self.window.menuScreen()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.initGame()
                    self.main()
