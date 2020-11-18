from consts import SHURIKEN_IMAGE


class Shuriken:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.radius = 12
        self.speed = speed
        self.throw_count = 10

    def draw(self, window):
        window.blit(SHURIKEN_IMAGE, (self.x, self.y))
