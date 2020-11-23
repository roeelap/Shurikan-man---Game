from consts import SHURIKEN_IMAGE, SCREEN_HEIGHT, SHURIKEN_STARTING_SLOPE
import pygame


class Shuriken:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.slope = SHURIKEN_STARTING_SLOPE
        self.rotation_angle = 0

    def draw(self, window):
        window.blit(pygame.transform.rotate(SHURIKEN_IMAGE,
                                            self.rotation_angle), (self.x, self.y))
        self.rotation_angle -= self.speed * 5

    def is_in_screen(self, background):
        if self.y < SCREEN_HEIGHT and background.x < self.x < background.width and abs(self.speed) > 0.1:
            self.x += self.speed
            if self.y - int((self.slope * abs(self.slope)) * 0.1) >= SCREEN_HEIGHT - 30 and self.slope < 0:
                self.y = SCREEN_HEIGHT - 30
                self.slope = abs(self.slope / 1.8)
                self.speed = self.speed / 2
            else:
                self.y -= int((self.slope * abs(self.slope)) * 0.05)
                self.slope -= 0.5
            return True
        else:
            return False
