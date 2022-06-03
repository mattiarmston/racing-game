class Surface:
    def __init__(self, surfaceName, game):
        self.game = game
        if surfaceName == "dirt":
            self.initDirt()
        elif surfaceName == "grass":
            self.initGrass()
        else:
            self.initDirt() # Default surface

    def initDirt(self):
        self.name = "dirt"
        self.grip = self.scale(5)
        self.friction = self.scale(0.075)

    def initGrass(self):
        self.name = "grass"
        self.grip = self.scale(4)
        self.friction = self.scale(0.05)

    def scale(self, num):
        widthScale = self.game.window.width / 1000
        heightScale = self.game.window.height / 1000
        meanScale = (widthScale + heightScale) / 2
        num *= meanScale
        return num
