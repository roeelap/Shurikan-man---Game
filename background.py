import pygame


class Background:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.image = pygame.image.load('./data/background-images/dungeon.png')

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))


background = Background(0, 0, 1655, 610)