import pygame
from consts import COLORS
from path import Path


class Enemy:

    def __init__(self, x, y, width, height, path, speed, health, walk_right_images, walk_left_images):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walk_count = 0
        self.walk_count_limit = len(walk_right_images) * 3
        self.speed = speed
        self.path = path
        self.path_limit = Path(self.path.start, self.path.end)
        self.max_speed = abs(speed)
        self.hitbox = (x + 20, y + 5, 31, 59)
        self.health = health
        self.max_health = health
        self.alive = True
        self.walk_right_images = walk_right_images
        self.walk_left_images = walk_left_images

    def draw(self, window):

        # Slow enemy down when punching
        self.speed = self.max_speed if self.speed > 0 else self.max_speed * -1
        if 9 <= self.walk_count//3 <= 11:
            self.speed /= 20

        if self.walk_count + 1 >= self.walk_count_limit:
            self.walk_count = 0

        if self.speed > 0:
            window.blit(
                self.walk_right_images[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        else:
            window.blit(
                self.walk_left_images[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        # drawing the health bar
        self.hitbox = (self.x + 20, self.y + 5, 31, 59)
        pygame.draw.rect(window, COLORS['red'],
                         (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(
            window, COLORS['green'], (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (self.max_health - self.health)), 10))

        # pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    def auto_path(self):
        inbound_left = self.x + self.speed > self.path.end
        inbound_right = self.x + self.speed < self.path.start
        going_left = self.speed < 0
        going_right = self.speed > 0
        if inbound_left and going_left or inbound_right and going_right:
            self.x += self.speed
        else:
            self.turn_around()

    def updatePathLimits(self, background_x):
        self.path.start = self.path_limit.start + background_x
        self.path.end = self.path_limit.end + background_x

    def turn_around(self):
        self.speed *= -1
        self.walk_count = 0

    def move(self, background_speed, direction):
        self.x += background_speed * direction

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.alive = False
