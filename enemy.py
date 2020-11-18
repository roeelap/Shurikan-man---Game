from background import Background
import pygame
from consts import COLORS


class Enemy(object):

    def __init__(self, x, y, width, height, end_path_x, speed, health, walk_right_images, walk_left_images):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start_path_x = x
        self.end_path_x = end_path_x
        self.trail = [self.start_path_x, self.end_path_x]
        self.walk_count = 0
        self.walk_count_limit = len(walk_right_images) * 3
        self.speed = speed
        self.hitbox = (self.x + 20, self.y + 5, 31, 59)
        self.health = health
        self.max_health = health
        self.alive = True
        self.walk_right_images = walk_right_images
        self.walk_left_images = walk_left_images

    def draw(self, window):
        self.auto_path()

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
        pygame.draw.rect(window, COLORS['red'],
                         (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(
            window, COLORS['green'], (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (self.max_health - self.health)), 10))

        self.hitbox = (self.x + 20, self.y + 5, 31, 59)
        # pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    def auto_path(self):
        inbound_left = self.x + self.speed > self.trail[1]
        inbound_right = self.x + self.speed < self.trail[0]
        going_left = self.speed < 0
        going_right = self.speed > 0
        if inbound_left and going_left or inbound_right and going_right:
            self.x += self.speed
        else:
            self.turn_around()

    def updatePathLimits(self, background_x):
        self.trail = [self.start_path_x+background_x,
                      self.end_path_x+background_x]

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
