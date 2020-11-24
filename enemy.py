import pygame
from consts import COLORS, FPS, SOUNDS
from path import Path
from random import choice
from static_functions import draw_circle_alpha


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
        self.hitbox = (self.x + 20, self.y + 15, 31, 59)
        self.health = health
        self.max_health = health
        self.alive = True
        self.walk_right_images = walk_right_images
        self.walk_left_images = walk_left_images
        self.movement_timer = 0
        self.movement_timeout = FPS
        self.can_hit = False

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

        mid_bottom = (self.x + self.width / 2 + correction -
                      5, self.hitbox[1] + self.hitbox[3])
        draw_circle_alpha(
            window, COLORS['black'], (mid_bottom), 38, 12)

        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

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
        pygame.draw.rect(window, COLORS['red'],
                         (self.hitbox[0]-x_axis_fix, self.hitbox[1] - 40, 50, 10))
        pygame.draw.rect(
            window, COLORS['green'], (self.hitbox[0]-x_axis_fix, self.hitbox[1] - 40, 50 - (5 * (self.max_health - self.health)), 10))
        pygame.draw.rect(window, COLORS['black'],
                         (self.hitbox[0]-x_axis_fix, self.hitbox[1] - 40, 50, 10), width=1)

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
