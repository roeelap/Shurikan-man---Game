import pygame
from consts import COLORS, FPS, SOUNDS
from path import Path
from random import choice
from static_functions import draw_circle_alpha
from operator import itemgetter


class Enemy:

    def __init__(self, x, y, width, height, path, speed, health, walk_right_images, walk_left_images):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walk_count = 0
        self.walk_count_limit = len(walk_right_images) * 6
        self.speed = speed
        self.path = path
        self.path_limit = Path(self.path.start, self.path.end)
        self.max_speed = abs(speed)
        self.hitbox = (0, 0, 0, 0)
        self.health = health
        self.max_health = health
        self.alive = True
        self.walk_right_images = walk_right_images
        self.walk_left_images = walk_left_images
        self.movement_timer = 0
        self.movement_timeout = FPS
        self.can_hit = False
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}

    def draw(self, window):
        if not self.alive:
            return

        self.auto_path()
        correction = 0

        image_to_blit = self.walk_right_images[self.walk_count //
                                               6] if self.speed > 0 else self.walk_left_images[self.walk_count//6]
        timeout_image = image_to_blit.copy()
        timeout_image.fill(
            COLORS['red'], special_flags=pygame.BLEND_RGBA_MULT)

        if self.movement_timer < self.movement_timeout:
            self.movement_timer += 1
            if 0 <= self.movement_timer % 6 <= 1:
                image_to_blit = timeout_image
        else:
            self.walk_count += 1

        # Slow enemy down when punching
        self.speed = self.max_speed if self.speed > 0 else self.max_speed * -1
        if 9 <= self.walk_count//6 <= 11:
            self.speed /= 20

        if self.walk_count + 1 >= self.walk_count_limit:
            self.walk_count = 0

        if self.speed > 0:
            window.blit(image_to_blit, (self.x, self.y))
        else:
            correction = 15
            window.blit(image_to_blit, (self.x, self.y))

        # drawing the health bar
        self.hitbox = (self.x + 20 + correction,
                       self.y + 15, 31, 60)
        self.draw_health_bar(window)
        self.draw_shade(window, correction)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def draw_shade(self, window, correction):
        self.shade = {'x': self.x + self.width / 2 + correction - 5,
                      'y': self.hitbox[1] + self.hitbox[3], 'w': 38, 'h': 12}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

    def auto_path(self):
        left_limit = min(self.path.start, self.path.end)
        right_limit = max(self.path.start, self.path.end)
        inbound_left = self.x + self.speed > left_limit
        inbound_right = self.x + self.speed < right_limit
        going_left = self.speed < 0
        going_right = self.speed >= 0
        if self.movement_timer >= self.movement_timeout:
            if inbound_left and going_left or inbound_right and going_right:
                self.x += self.speed
            else:
                self.turn_around()

    def draw_health_bar(self, window):
        x_axis_fix = 17 if self.speed > 0 else 5
        x, y = self.hitbox[0]-x_axis_fix, self.hitbox[1] - 18
        w, h = 50, 10
        pygame.draw.rect(window, COLORS['red'],
                         (x, y, w, h))
        pygame.draw.rect(
            window, COLORS['green'], (x, y, w - (5 * (self.max_health - self.health)), h))
        pygame.draw.rect(window, COLORS['black'],
                         (x, y, w, h), width=1)

    def update_path_limits(self, player_speed, direction):
        self.path.start -= player_speed * direction
        self.path.end -= player_speed * direction

    def turn_around(self):
        self.speed *= -1
        self.walk_count = 0

    def move(self, player_speed, direction):
        self.x -= player_speed * direction

    def hit(self, shuriken_speed):
        if self.health > 0:
            choice(SOUNDS['shuriken_hits']).play()
            self.health -= 1
            self.x += int(shuriken_speed / 2)
        else:
            choice(SOUNDS['goblin_deaths']).play()
            self.alive = False
