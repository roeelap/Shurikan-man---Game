from consts import SHURIKEN_IMAGE, SCREEN_HEIGHT, SHURIKEN_STARTING_SLOPE


class Shuriken:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.slope = SHURIKEN_STARTING_SLOPE

    def draw(self, window):
        window.blit(SHURIKEN_IMAGE, (self.x, self.y))

    def is_in_screen(self, background):
        if self.y < SCREEN_HEIGHT and background.x < self.x < background.width and abs(self.speed) > 0:
            self.x += self.speed
            if self.y - int((self.slope * abs(self.slope)) * 0.1) >= SCREEN_HEIGHT - 30 and self.slope < 0:
                self.y = SCREEN_HEIGHT - 30
                self.slope = abs(int(self.slope / 2))
                self.speed = int(self.speed / 2)
            else:
                self.y -= int((self.slope * abs(self.slope)) * 0.1)
                self.slope -= 1
            return True
        else:
            return False
