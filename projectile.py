import pygame


SHURIKEN = pygame.image.load('./data/player-images/shuriken.png')


class Shuriken:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.radius = 12
        self.facing = facing
        self.velocity = 20 * facing
        self.throw_count = 10

    def draw(self,window):
        window.blit(SHURIKEN, (self.x, self.y))