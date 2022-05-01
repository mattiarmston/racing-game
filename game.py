import pygame

from player import Player

class Game():
    def __init__(self, window, assets):
        self.window = window
        self.assets = assets
        self.BGImage = pygame.transform.scale(
            self.assets.BGImage, (self.window.width, self.window.height)
        )
        self.toDraw = []
        self.lost = False
        self.run = True
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.mainFont = pygame.font.SysFont("arial", 70)
        self.keyBinds = {
            "left": [pygame.K_a, pygame.K_LEFT],
            "right": [pygame.K_d, pygame.K_RIGHT],
            "up": [pygame.K_w, pygame.K_UP],
            "down": [pygame.K_s, pygame.K_DOWN],
        }

    def takeInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        self.keys = pygame.key.get_pressed()
        self.player.move(self.keys, self.keyBinds)

    def initGame(self):
        self.player = Player(self.assets.playerImage, self)
        self.toDraw = [self.player]

    def main(self):
        while self.lost == False:
            self.clock.tick(self.FPS)
            self.window.drawFrame(self)
            self.takeInput()

    def mainMenu(self):
        self.window.menuScreen(self)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.initGame()
                    self.main()
