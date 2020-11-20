import pygame
from consts import *


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.speed = 5
        self.jumping = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.standing = True
        self.walk_count = 3
        self.image = PLAYER_STANDING_IMAGE
        self.hitbox = (self.x + 17, self.y + 11, 28, 53)
        self.max_health = 9
        self.health = self.max_health
        self.hurt_counter = 0

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 3

        if self.standing:
            self.walk_count = 0

        if self.left:
            self.image = PLAYER_WALK_LEFT_IMAGES[self.walk_count // 3]

        if self.right:
            self.image = PLAYER_WALK_RIGHT_IMAGES[self.walk_count // 3]

        if self.hurt_counter > 0:
            self.hurt_animation(window)
        else:
            window.blit(self.image, (self.x, self.y))

        self.walk_count += 1

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

    def hit(self):
        PLAYER_HIT_SOUND.play()
        self.hurt_counter = PLAYER_INVINCIBLE_TIME
        if self.health > 0:
            self.health -= 1

    def hurt_animation(self, window):
        if self.hurt_counter % 3 == 0:
            window.blit(self.image, (self.x, self.y))
        else:
            hurt_image = self.image.copy()
            hurt_image.fill(
                (255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT)
            window.blit(hurt_image, (self.x, self.y))
        self.hurt_counter -= 1

    def display_health_status(self, window):
        pygame.draw.rect(window, COLORS['red'], (130, 30, 630, 30))
        pygame.draw.rect(
            window, COLORS['green'], (130, 30, 630 - (70 * (self.max_health - self.health)), 30))
        window.blit(PLAYER_PORTRAIT, (40, 30))

        health = f'{self.health} / {self.max_health}'
        if self.health == 0:
            health = 'DEAD'
        health_text = PIXEL_FONT.render(health, True,  COLORS['white'])
        window.blit(health_text, (35, 70))


player = Player(10, 530)
