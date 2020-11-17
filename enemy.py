import pygame
from consts import ENEMY_WALK_LEFT, ENEMY_WALK_RIGHT


class Enemy(object):

    def __init__(self, x, y, width, height, x_end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_start = x
        self.x_end = x_end
        self.path = [self.x_start, self.x_end]
        self.walk_count = 0
        self.speed = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 9
        self.visible = True

    def draw(self, window):
        self.auto_path()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.speed < 0:
                window.blit(
                    ENEMY_WALK_RIGHT[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                window.blit(
                    ENEMY_WALK_LEFT[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

            pygame.draw.rect(window, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(
                window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (9 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    def auto_path(self):
        if self.speed > 0:
            if self.x - self.speed > self.x_end:
                self.x -= self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0
        else:
            if self.x + self.speed < self.x_start:
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
            self.visible = False


goblin = Enemy(500, 530, 64, 64, 100)
