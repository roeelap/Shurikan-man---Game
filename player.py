import pygame
from consts import PLAYER_STANDING_IMAGE, PLAYER_WALK_LEFT_IMAGES, PLAYER_WALK_RIGHT_IMAGES, SOUNDS, PLAYER_INVINCIBLE_TIME, COLORS, PLAYER_PORTRAIT, PIXEL_FONT_SMALL, SCREEN_WIDTH
from static_functions import draw_circle_alpha
from operator import itemgetter


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 77
        self.height = 77
        self.speed = 2.5
        self.left = False
        self.right = False
        self.standing = True
        self.walk_count = 3
        self.image = PLAYER_STANDING_IMAGE
        self.hitbox = (0, 0, 0, 0)
        self.max_health = 10
        self.health = self.max_health
        self.hurt_counter = 0
        self.xp = 0
        self.level = 1
        self.xp_to_next_lvl = self.level ** 2 * 10
        self.score = 0
        self.coins = 0
        self.throw_speed = 12
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}
        self.shurikens_owned = ['shuriken']
        self.shuriken_equipped = 'shuriken'

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

        self.draw_shade(window)

        self.walk_count += 1
        self.hitbox = (self.x + 23, self.y + 16, 29, 58)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def draw_shade(self, window):
        self.shade = {'x': self.x + self.width / 2,
                      'y': self.hitbox[1] + self.hitbox[3], 'w': 32, 'h': 12}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

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
        self.hurt_counter = PLAYER_INVINCIBLE_TIME
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
        health_bar_x = SCREEN_WIDTH * 2 // 20
        health_bar_width = SCREEN_WIDTH * 17 // 20
        
        pygame.draw.rect(
            window, COLORS['red'], (health_bar_x, 30, health_bar_width, 30), border_radius=15)
        pygame.draw.rect(
            window, COLORS['green'], (health_bar_x, 30, (health_bar_width) - ((health_bar_width // 10) * (self.max_health - self.health)), 30), border_radius=15)
        pygame.draw.rect(window, COLORS['black'], (SCREEN_WIDTH *
                                                   2 // 20, 30, health_bar_width, 30), width=3, border_radius=15)
        pygame.draw.rect(
            window, COLORS['orange'], (health_bar_x, 60, (health_bar_width) * (self.xp / self.xp_to_next_lvl), 20), border_radius=15)  
        pygame.draw.rect(window, COLORS['black'], (SCREEN_WIDTH *
                                                   2 // 20, 60, health_bar_width, 20), width=2, border_radius=15)
        for i in range(1, 4):
            pygame.draw.line(window, COLORS['black'], (health_bar_x + (health_bar_width * i / 4), 60), (health_bar_x + (health_bar_width * i / 4), 80), width=2)
        
        window.blit(PLAYER_PORTRAIT, (SCREEN_WIDTH // 30, 30))

        health = f'{self.health} / {self.max_health}'
        if self.health == 0:
            health = 'DEAD'
        health_text = PIXEL_FONT_SMALL.render(health, True,  COLORS['white'])
        window.blit(health_text, (130, 35))

        xp = '% ' + str(round(self.xp / self.xp_to_next_lvl * 100, 3))
        xp_text = PIXEL_FONT_SMALL.render(xp, True,  COLORS['white'])
        window.blit(xp_text, (130, 61))

        level = f'Level: {self.level}'
        level_text = PIXEL_FONT_SMALL.render(level, True,  COLORS['white'])
        window.blit(level_text, (25, 80))

        score = f'Score: {self.score}'
        score_text = PIXEL_FONT_SMALL.render(score, True,  COLORS['white'])
        window.blit(score_text, (25, 100))

        coins = f'Coins: {self.coins}'
        coins_text = PIXEL_FONT_SMALL.render(coins, True,  COLORS['white'])
        window.blit(coins_text, (25, 120))

        

    def level_up(self):
        self.level += 1
    
    def earn_xp(self, xp_amount):
        self.xp += xp_amount
        if self.xp >= self.xp_to_next_lvl:
            self.xp -= self.xp_to_next_lvl
            self.level_up()
            self.xp_to_next_lvl = self.level ** 2 * 10
        print(self.xp, self.xp_to_next_lvl)