import pygame
from consts import PLAYER_STANDING_IMAGE, PLAYER_WALK_LEFT_IMAGES, PLAYER_WALK_RIGHT_IMAGES, SOUNDS, PLAYER_INVINCIBLE_TIME, COLORS, PLAYER_PORTRAIT, PIXEL_FONT_SMALL, SCREEN_WIDTH


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 77
        self.height = 77
        self.speed = 2
        self.left = False
        self.right = False
        self.standing = True
        self.walk_count = 3
        self.image = PLAYER_STANDING_IMAGE
        self.hitbox = (self.x + 17, self.y + 11, 28, 53)
        self.max_health = 10
        self.health = self.max_health
        self.hurt_counter = 0
        self.score = 0
        self.coins = 0
        self.throw_speed = 12

    def draw(self, window):
        if self.walk_count + 1 >= 54:
            self.walk_count = 3

        if self.standing:
            self.walk_count = 2

        if self.left:
            self.image = PLAYER_WALK_LEFT_IMAGES[self.walk_count // 6]

        if self.right:
            self.image = PLAYER_WALK_RIGHT_IMAGES[self.walk_count // 6]

        if self.hurt_counter > 0:
            self.hurt_animation(window)
        else:
            window.blit(self.image, (self.x, self.y))

        self.walk_count += 1
        self.hitbox = (self.x + 23, self.y + 16, 29, 58)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move_right(self):
        self.x += self.speed
        self.left = False
        self.right = True
        self.standing = False

    def move_left(self):
        self.x -= self.speed
        self.left = True
        self.right = False
        self.standing = False

    def move_up(self):
        self.y -= self.speed
        self.standing = False

    def move_down(self):
        self.y += self.speed
        self.standing = False

    def hit(self):
        SOUNDS['player_hit'].play()
        self.hurt_counter = PLAYER_INVINCIBLE_TIME * 60
        if self.health > 0:
            self.health -= 1

    def hurt_animation(self, window):
        if 0 <= self.hurt_counter % 6 <= 1:
            window.blit(self.image, (self.x, self.y))
        else:
            hurt_image = self.image.copy()
            hurt_image.fill(
                (255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT)
            window.blit(hurt_image, (self.x, self.y))
        self.hurt_counter -= 1

    def display_player_stats(self, window):
        pygame.draw.rect(window, COLORS['red'], (SCREEN_WIDTH * 2 // 20, 30, SCREEN_WIDTH * 17 // 20, 30))
        pygame.draw.rect(
            window, COLORS['green'], (SCREEN_WIDTH * 2 // 20, 30, (SCREEN_WIDTH * 17 // 20) - ((SCREEN_WIDTH * 17 // 200) * (self.max_health - self.health)), 30))
        pygame.draw.rect(window, COLORS['black'], (SCREEN_WIDTH * 2 // 20, 30, SCREEN_WIDTH * 17 // 20, 30), width=3)
        window.blit(PLAYER_PORTRAIT, (SCREEN_WIDTH // 30, 30))

        health = f'{self.health} / {self.max_health}'
        if self.health == 0:
            health = 'DEAD'
        health_text = PIXEL_FONT_SMALL.render(health, True,  COLORS['white'])
        window.blit(health_text, (130, 35))

        score = f'Score: {self.score}'
        score_text = PIXEL_FONT_SMALL.render(score, True,  COLORS['white'])
        window.blit(score_text, (25, 80))

        coins = f'Coins: {self.coins}'
        coins_text = PIXEL_FONT_SMALL.render(coins, True,  COLORS['white'])
        window.blit(coins_text, (25, 100))
