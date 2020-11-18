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
        self.walk_count = 0
        self.speed = speed
        self.hitbox = (self.x + 20, self.y + 5, 31, 59)
        self.health = health
        self.alive = True
        self.walk_right_images = walk_right_images
        self.walk_left_images = walk_left_images

    def draw(self, window):
        self.auto_path()

        if self.walk_count + 1 >= 33:
            self.walk_count = 0

        if self.speed < 0:
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
            window, COLORS['green'], (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (9 - self.health)), 10))

        self.hitbox = (self.x + 20, self.y + 5, 31, 59)
        # pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    def auto_path(self):
        if self.speed > 0:
            if self.x - self.speed > self.end_path_x:
                self.x -= self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0
        else:
            if self.x + self.speed < self.start_path_x:
                self.x -= self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0

    def move(self, background_speed, direction):
        self.x += background_speed * direction

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.alive = False
