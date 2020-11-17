import pygame
from player import player


class Background:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = player.velocity
        self.image = pygame.image.load('./data/background-images/dungeon.png')

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move_right(self):
        self.x += self.velocity
        player.left = True
        player.right = False
        player.standing = False

    def move_left(self):
        self.x -= self.velocity
        player.left = False
        player.right = True
        player.standing = False


background = Background(0, 0, 1650, 610)
