from operator import itemgetter
import pygame
from consts import BROKEN_SHURIKENS, COLORS, SCREEN_HEIGHT, SHURIKEN_MAX_SHADE_WIDTH, SHURIKEN_MIN_SHADE_WIDTH, SHURIKEN_STARTING_SLOPE
from static_functions import draw_circle_alpha


class Shuriken:

    def __init__(self, x, y, radius, speed, strength, bottom, image, name):
        self.x = x
        self.y = y
        self.radius = radius
        self.height = radius * 2
        self.image = image
        self.name = name
        self.speed = speed
        self.strength = strength
        self.slope = SHURIKEN_STARTING_SLOPE
        self.rotation_angle = 0
        self.bottom = bottom
        self.distance_from_bottom = abs(self.bottom-self.y)/2
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}
        self.hit_animation_counter = 0
        self.has_hit = False
        self.broken = False
        self.broken_info = []

    def draw(self, window):
        if not self.has_hit:
            self.distance_from_bottom = int(abs(self.bottom-self.y)/2)
            window.blit(pygame.transform.rotate(
                self.image, self.rotation_angle), (self.x, self.y))
            self.rotation_angle -= self.speed * 5
            self.draw_shade(window)
        else:
            if self.hit_animation_counter < 10:
                self.hit_animation_counter += 1
                new_info = []
                for broken_shuriken in self.broken_info:
                    image, x, y, x_speed, y_speed = broken_shuriken[0], broken_shuriken[
                        1], broken_shuriken[2], broken_shuriken[3], broken_shuriken[4]
                    window.blit(image, (x, y))
                    x, y = x + x_speed, y + y_speed
                    new_info.append([image, x, y, x_speed, y_speed])
                self.broken_info = new_info
            else:
                self.broken = True

    def hit(self):
        self.has_hit = True
        for index, image in enumerate(BROKEN_SHURIKENS[self.name]):
            x_speed, y_speed = 0, 0
            if index == 0:
                x_speed, y_speed = 1, -1
            if index == 1:
                x_speed, y_speed = 1, 1
            if index == 2:
                x_speed, y_speed = -1, 1
            if index == 3:
                x_speed, y_speed = -1, -1
            self.broken_info.append([image, self.x, self.y, x_speed, y_speed])

    def draw_shade(self, window):
        shade_width = self.distance_from_bottom
        if shade_width < SHURIKEN_MIN_SHADE_WIDTH:
            shade_width = SHURIKEN_MIN_SHADE_WIDTH
        if shade_width > SHURIKEN_MAX_SHADE_WIDTH:
            shade_width = SHURIKEN_MAX_SHADE_WIDTH
        self.shade = {'x': self.x + self.radius,
                      'y': self.bottom, 'w': shade_width, 'h': 9}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

    def is_in_screen(self, background):
        if self.y < SCREEN_HEIGHT and background.x < self.x < background.width and abs(self.speed) > 0.1 and not self.has_hit:
            self.x += self.speed
            if self.y - int((self.slope * abs(self.slope)) * 0.1) >= self.bottom-17 and self.slope < 0:
                self.y = self.bottom-17
                self.slope = abs(self.slope / 1.8)
                self.speed = self.speed / 2
            else:
                self.y -= int((self.slope * abs(self.slope)) * 0.05)
                self.slope -= 0.5
            return True
        if not self.has_hit or self.broken:
            return False
        return True
