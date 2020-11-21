from consts import SHURIKEN_IMAGE, SCREEN_WIDTH


class Shuriken:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.radius = 12
        self.speed = speed
        self.y_change = 10

    def draw(self, window):
        window.blit(SHURIKEN_IMAGE, (self.x, self.y))

    def is_in_screen(self):
        if self.x < SCREEN_WIDTH and self.x > 0 and self.y_change != -20:
            if self.y_change >= -20:
                self.x += self.speed
                self.y -= int((self.y_change *
                                    abs(self.y_change)) * 0.1)
                self.y_change -= 1
            else:
                self.y_change = 10
            return True
        else:
            return False

