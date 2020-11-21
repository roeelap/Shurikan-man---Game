from consts import SHURIKEN_IMAGE, SCREEN_WIDTH


class Shuriken:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.radius = 12
        self.speed = speed
        self.throw_count = 10

    def draw(self, window):
        window.blit(SHURIKEN_IMAGE, (self.x, self.y))

    def throw(self):
        if self.x < SCREEN_WIDTH and self.x > 0 and self.throw_count != -20:
            if self.throw_count >= -20:
                self.x += self.speed
                self.y -= int((self.throw_count *
                                    abs(self.throw_count)) * 0.1)
                self.throw_count -= 1
            else:
                self.throw_count = 10
            return True
        else:
            return False

