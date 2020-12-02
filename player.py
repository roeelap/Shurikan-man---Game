from operator import itemgetter
import pygame
from consts import PLAYER_SHOOT_IMAGES, PLAYER_STANDING_IMAGE, PLAYER_STARTING_MAX_HEALTH, PLAYER_STARTING_MAX_SHURIKENS, PLAYER_STARTING_RELOAD_SPEED,\
    PLAYER_STARTING_SHURIKEN_DURABILITY, PLAYER_STARTING_SPEED, PLAYER_STARTING_STRENGTH, PLAYER_STARTING_THROW_SPEED, PLAYER_WALK_LEFT_IMAGES, PLAYER_WALK_RIGHT_IMAGES,\
    SOUNDS, PLAYER_INVINCIBLE_TIME, COLORS, PLAYER_PORTRAIT, PIXEL_FONT_SMALL, SCREEN_WIDTH, PLAYER_MAX_ENERGY
from static_functions import draw_circle_alpha


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 77
        self.height = 77

        self.max_health = PLAYER_STARTING_MAX_HEALTH
        self.speed = PLAYER_STARTING_SPEED
        self.strength = PLAYER_STARTING_STRENGTH
        self.throw_speed = PLAYER_STARTING_THROW_SPEED
        self.reload_speed = PLAYER_STARTING_RELOAD_SPEED
        self.max_shurikens = PLAYER_STARTING_MAX_SHURIKENS
        self.shuriken_durability = PLAYER_STARTING_SHURIKEN_DURABILITY

        self.left = False
        self.right = False
        self.standing = True
        self.walk_count = 3

        self.image = PLAYER_STANDING_IMAGE
        self.hitbox = (0, 0, 0, 0)
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}

        self.health = self.max_health
        self.hurt_timer = 0
        self.shot_timer = -6

        self.energy = PLAYER_MAX_ENERGY

        self.xp = 0
        self.level = 1
        self.xp_to_next_lvl = self.level ** 2 * 10

        self.upgrade_points = self.level - 1
        self.upgrades = {'max_health': 0, 'speed': 0, 'strength': 0,
                         'throw_speed': 0, 'max_shurikens': 0, 'reload_speed': 0, 'shuriken_durability': 0}

        self.score = 0
        self.coins = 0

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

        if self.shot_timer > -3:
            self.shot_timer -= 1
            self.image = PLAYER_SHOOT_IMAGES[self.shot_timer//4]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)

        if self.hurt_timer > 0:
            self.hurt_animation(window)
        else:
            window.blit(self.image, (self.x, self.y))

        self.draw_shade(window)

        self.walk_count += 1
        self.hitbox = (self.x + 23, self.y + 16, 29, 58)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def shoot(self):
        self.shot_timer = 5

    def update_stats(self):
        self.max_health = PLAYER_STARTING_MAX_HEALTH + \
            self.upgrades['max_health'] * 10
        self.speed = PLAYER_STARTING_SPEED + self.upgrades['speed'] / 5
        self.strength = PLAYER_STARTING_STRENGTH + self.upgrades['strength']
        self.throw_speed = PLAYER_STARTING_THROW_SPEED + \
            self.upgrades['throw_speed'] * 2
        self.reload_speed = PLAYER_STARTING_RELOAD_SPEED - \
            self.upgrades['reload_speed'] * 0.5
        self.max_shurikens = PLAYER_STARTING_MAX_SHURIKENS + \
            self.upgrades['max_shurikens']
        self.shuriken_durability = PLAYER_STARTING_SHURIKEN_DURABILITY + \
            self.upgrades['shuriken_durability']

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

    def hit(self, damage):
        if self.hurt_timer == 0:
            if self.health > 0:
                if self.health - damage >= 0:
                    self.health -= damage
                else:
                    self.health = 0
            SOUNDS['player_hit'].play()
            self.hurt_timer = PLAYER_INVINCIBLE_TIME

    def hurt_animation(self, window):
        if 0 <= self.hurt_timer % 6 <= 1:
            window.blit(self.image, (self.x, self.y))
        else:
            hurt_image = self.image.copy()
            hurt_image.fill(
                (255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT)
            window.blit(hurt_image, (self.x, self.y))
        self.hurt_timer -= 1

    def display_player_stats(self, window):
        self.display_health_bar(window)
        self.display_xp_bar(window)
        self.display_xp_text(window)
        window.blit(PLAYER_PORTRAIT, (SCREEN_WIDTH // 30, 30))
        self.display_health_text(window)
        self.display_level_text(window)
        self.display_score_text(window)
        self.display_coins_text(window)
        self.display_energy_bar(window)
        self.display_energy_text(window)

    def level_up(self):
        SOUNDS['level_up'].play()
        self.level += 1
        self.upgrade_points += 1

    def earn_xp(self, xp_amount):
        self.xp += xp_amount
        if self.xp >= self.xp_to_next_lvl:
            self.xp -= self.xp_to_next_lvl
            self.level_up()
            self.xp_to_next_lvl = self.level ** 2 * 10

    def display_health_bar(self, window):
        health_bar_x = SCREEN_WIDTH * 2 // 20
        health_bar_width_max = SCREEN_WIDTH * 17 // 20
        health_bar_width = health_bar_width_max - \
            ((health_bar_width_max // self.max_health)
             * (self.max_health - self.health))
        border_radius = 15
        if self.health > 0:
            pygame.draw.rect(window, COLORS['green'], (health_bar_x,
                                                       30, health_bar_width, 30), border_radius=border_radius)
        pygame.draw.rect(window, COLORS['black'], (SCREEN_WIDTH * 2 // 20,
                                                   30, health_bar_width_max, 30), width=3, border_radius=border_radius)

    def display_xp_bar(self, window):
        xp_bar_x = SCREEN_WIDTH * 2 // 20
        xp_bar_width = SCREEN_WIDTH * 17 // 20
        xp_owned_width = (xp_bar_width) * (self.xp / self.xp_to_next_lvl)
        xp_owned_height_max = 20
        xp_owned_height = xp_owned_height_max
        border_radius = 15
        xp_owned_y_correction = 0
        if xp_owned_width // 2 <= border_radius:
            xp_owned_height = min(xp_owned_width, xp_owned_height_max)
            xp_owned_y_correction = abs(xp_owned_height_max-xp_owned_height)/2
        if self.xp > 0:
            pygame.draw.rect(window, COLORS['orange'], (
                xp_bar_x, 60 + xp_owned_y_correction, xp_owned_width, xp_owned_height), border_radius=border_radius)
        pygame.draw.rect(window, COLORS['black'], (SCREEN_WIDTH *
                                                   2 // 20, 60, xp_bar_width, 20), width=2, border_radius=border_radius)
        for i in range(1, 4):
            pygame.draw.line(window, COLORS['black'], (xp_bar_x + (
                xp_bar_width * i / 4), 60), (xp_bar_x + (xp_bar_width * i / 4), 79), width=2)

    def display_energy_bar(self, window):
        if self.energy < PLAYER_MAX_ENERGY:
            self.energy += 1

        energy_bar_y = 140
        border_radius = 15
        energy_bar_height = self.energy if self.energy >= border_radius else border_radius
        energy_bar_width = 15
        pygame.draw.rect(window, COLORS['cyan'], (
            50, energy_bar_y + PLAYER_MAX_ENERGY - energy_bar_height, energy_bar_width, energy_bar_height), border_radius=border_radius)
        pygame.draw.rect(window, COLORS['black'], (
            50, energy_bar_y, energy_bar_width, PLAYER_MAX_ENERGY), width=2, border_radius=border_radius)

    def display_energy_text(self, window):
        energy_text = PIXEL_FONT_SMALL.render('Energy', True,  COLORS['white'])
        energy_text = pygame.transform.rotate(energy_text, 90)
        window.blit(energy_text, (30, 200))

    def display_coins_text(self, window):
        coins = f'Coins: {self.coins}'
        coins_text = PIXEL_FONT_SMALL.render(coins, True,  COLORS['white'])
        window.blit(coins_text, (25, 100))

    def display_score_text(self, window):
        score = f'Score: {self.score}'
        score_text = PIXEL_FONT_SMALL.render(score, True,  COLORS['white'])
        window.blit(score_text, (25, 80))

    def display_level_text(self, window):
        health_bar_x = SCREEN_WIDTH * 2 // 20
        health_bar_width = SCREEN_WIDTH * 17 // 20

        level = f'Level: {self.level}'
        level_text = PIXEL_FONT_SMALL.render(level, True,  COLORS['white'])
        window.blit(level_text, (health_bar_x + health_bar_width -
                                 level_text.get_rect()[2] - 10, 61))

    def display_xp_text(self, window):
        xp = '% ' + str(round(self.xp / self.xp_to_next_lvl * 100, 2))
        xp_text = PIXEL_FONT_SMALL.render(xp, True,  COLORS['white'])
        window.blit(xp_text, (130, 61))

    def display_health_text(self, window):
        health = f'{self.health} / {self.max_health}'
        if self.health == 0:
            health = 'DEAD'
        health_text = PIXEL_FONT_SMALL.render(health, True,  COLORS['white'])
        window.blit(health_text, (130, 35))
