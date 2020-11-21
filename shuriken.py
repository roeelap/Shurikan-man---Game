from consts import SHURIKEN_IMAGE, SCREEN_WIDTH, SHURIKEN_RADIUS, SHURIKEN_STARTING_SLOPE, SHURIKEN_ENDING_SLOPE


class Shuriken:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.radius = SHURIKEN_RADIUS
        self.speed = speed
        self.slope = SHURIKEN_STARTING_SLOPE

    def draw(self, window):
        window.blit(SHURIKEN_IMAGE, (self.x, self.y))

    def is_in_screen(self):
        if self.x < SCREEN_WIDTH and self.x > 0 and self.slope != SHURIKEN_ENDING_SLOPE:
            if self.slope >= SHURIKEN_ENDING_SLOPE:
                self.x += self.speed
                self.y -= int((self.slope *
                                    abs(self.slope)) * 0.1)
                self.slope -= 1
            else:
                self.slope = SHURIKEN_STARTING_SLOPE
            return True
        else:
            return False

