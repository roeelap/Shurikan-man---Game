import pygame
from consts import PLAYER_STANDING, PLAYER_WALK_LEFT, PLAYER_WALK_RIGHT


class Player:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.standing = True
        self.walk_count = 3
        self.hitbox = (self.x + 17, self.y + 11, 28, 53)

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 3

        if not self.standing:
            if self.left:
                window.blit(
                    PLAYER_WALK_LEFT[self.walk_count // 3], (self.x, self.y))
            elif self.right:
                window.blit(
                    PLAYER_WALK_RIGHT[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            if self.left:
                window.blit(PLAYER_WALK_LEFT[0], (self.x, self.y))
            elif self.right:
                window.blit(PLAYER_WALK_RIGHT[0], (self.x, self.y))
            else:
                window.blit(PLAYER_STANDING, (self.x, self.y))
                self.standing = True
                self.walk_count = 3

        self.hitbox = (self.x + 17, self.y + 11, 28, 53)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move_right(self):
        self.x += player.speed
        self.left = False
        self.right = True
        self.standing = False

    def move_left(self):
        self.x -= self.speed
        self.left = True
        self.right = False
        self.standing = False


player = Player(10, 530, 64, 64)
