from gameObject import GameObject

class FinishBanner(GameObject):
    def __init__(self, x, y, image, game):
        super().__init__(x, y, 533, 80, image, game)
