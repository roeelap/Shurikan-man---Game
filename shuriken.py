from operator import itemgetter
from consts import COLORS, SHURIKEN_IMAGE, SCREEN_HEIGHT, SHURIKEN_STARTING_SLOPE
import pygame
from static_functions import draw_circle_alpha


class Shuriken:
    def __init__(self, x, y, radius, speed, bottom):
        self.x = x
        self.y = y
        self.radius = radius
        self.height = radius * 2
        self.speed = speed
        self.slope = SHURIKEN_STARTING_SLOPE
        self.rotation_angle = 0
        self.bottom = bottom
        self.shade = {'x': 0,'y': 0, 'w': 0, 'h': 0}

    def draw(self, window):
        window.blit(pygame.transform.rotate(SHURIKEN_IMAGE,
                                            self.rotation_angle), (self.x, self.y))
        self.rotation_angle -= self.speed * 5

    def draw_shade(self, window, correction):
        self.shade = {'x': self.x + self.width / 2 + correction - 5,
                      'y': self.hitbox[1] + self.hitbox[3], 'w': 38, 'h': 12}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

    def is_in_screen(self, background):
        if self.y < SCREEN_HEIGHT and background.x < self.x < background.width and abs(self.speed) > 0.1:
            self.x += self.speed
            if self.y - int((self.slope * abs(self.slope)) * 0.1) >= self.bottom and self.slope < 0:
                self.y = self.bottom
                self.slope = abs(self.slope / 1.8)
                self.speed = self.speed / 2
            else:
                self.y -= int((self.slope * abs(self.slope)) * 0.05)
                self.slope -= 0.5
            return True
        else:
            return False
