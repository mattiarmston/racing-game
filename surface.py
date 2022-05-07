class Surface:
    def __init__(self, surfaceName):
        if surfaceName == "dirt":
            self.initDirt()
        elif surfaceName == "grass":
            self.initGrass()
        else:
            self.initDirt() # There are no other surfaces so far

    def initDirt(self):
        self.name = "dirt"
        self.grip = 5
        self.friction = 3.5

    def initGrass(self):
        self.name = "grass"
        self.grip = 4
        self.friction = 3
