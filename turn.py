from gameObject import GameObject
from surface import Surface

class Turn(GameObject):
    def __init__(self, sharpness, direction, surface, image, game):
        super().__init__(0, 0, 1000, 1000, image, game)
        self.sharpness = sharpness
        self.direction = direction
        self.surface = Surface(surface)
        self.name = str(sharpness) + " " + direction
