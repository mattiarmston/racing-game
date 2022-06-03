from gameObject import GameObject

class Stage(GameObject):
    def __init__(self, x, y, width, height, image, game, surface):
        super().__init__(x, y, width, height, image, game)
        self.surface = surface
