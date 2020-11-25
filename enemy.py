import pygame
from consts import BOTTOM_BORDER, COLORS, GOBLIN_PATH_TIMEOUT, GOBLIN_SPAWN_TIMEOUT, SOUNDS, TOP_BORDER
from random import choice
from operator import itemgetter
from static_functions import draw_circle_alpha


class Enemy:

    def __init__(self, x, y, width, height, speed, health, walk_right_images, walk_left_images):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walk_count = 0
        self.walk_count_limit = len(walk_right_images) * 6
        self.speed = speed
        self.vertical_speed = self.speed / 2
        self.max_speed = abs(speed)
        self.hitbox = (0, 0, 0, 0)
        self.health = health
        self.max_health = health
        self.alive = True
        self.walk_right_images = walk_right_images
        self.walk_left_images = walk_left_images
        self.spawn_timer = 0
        self.path_refresh_timer = GOBLIN_PATH_TIMEOUT
        self.hit_timer = 0
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}

    def draw(self, window):
        if not self.alive:
            return

        correction = 0
        timeout_image = None

        image_to_blit = self.walk_right_images[self.walk_count //
                                               6] if self.speed > 0 else self.walk_left_images[self.walk_count//6]

        if self.spawn_timer < GOBLIN_SPAWN_TIMEOUT or self.hit_timer > 0:
            timeout_image = image_to_blit.copy()
            timeout_image.fill(
                COLORS['red'], special_flags=pygame.BLEND_RGBA_MULT)
        if self.spawn_timer < GOBLIN_SPAWN_TIMEOUT:
            self.spawn_timer += 1
            if 0 <= self.spawn_timer % 6 <= 1:
                image_to_blit = timeout_image
        else:
            self.walk_count += 1

        if self.hit_timer > 0:
            image_to_blit = timeout_image
            self.hit_timer -= 1

        # Slow enemy down when punching
        self.speed = self.max_speed if self.speed > 0 else self.max_speed * -1
        if 9 <= self.walk_count//6 <= 11:
            self.speed /= 20

        if self.walk_count + 1 >= self.walk_count_limit:
            self.walk_count = 0

        if self.speed > 0:
            window.blit(image_to_blit, (self.x, self.y))
        else:
            correction = 15
            window.blit(image_to_blit, (self.x, self.y))

        # drawing the health bar
        self.hitbox = (self.x + 20 + correction,
                       self.y + 15, 31, 60)
        self.draw_health_bar(window)
        self.draw_shade(window, correction)

        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def draw_shade(self, window, correction):
        self.shade = {'x': self.x + self.width / 2 + correction - 5,
                      'y': self.hitbox[1] + self.hitbox[3], 'w': 38, 'h': 12}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

    def auto_path(self, player_shade, background_width):
        if self.spawn_timer >= GOBLIN_SPAWN_TIMEOUT:
            if self.path_refresh_timer >= GOBLIN_PATH_TIMEOUT:
                self.path_refresh_timer = 0
                if self.shade['x'] > player_shade['x'] and self.speed >= 0:
                    self.horizontal_turn_around()
                if self.shade['x'] < player_shade['x'] and self.speed < 0:
                    self.horizontal_turn_around()
                if self.shade['y'] > player_shade['y'] and self.vertical_speed >= 0:
                    self.vertical_turn_around()
                if self.shade['y'] < player_shade['y'] and self.vertical_speed < 0:
                    self.vertical_turn_around()
            else:
                self.path_refresh_timer += 1

            inbound_y = self.shade['y'] + 0.5 * \
                self.shade['h'] > player_shade['y'] and self.shade['y'] < player_shade['y'] + \
                0.5 * player_shade['h']
            if BOTTOM_BORDER > self.y + self.vertical_speed > TOP_BORDER and not inbound_y:
                self.y += self.vertical_speed
            if 0 < self.x + self.speed + self.width < background_width:
                self.x += self.speed

    def draw_health_bar(self, window):
        x_axis_fix = 17 if self.speed > 0 else 5
        x, y = self.hitbox[0]-x_axis_fix, self.hitbox[1] - 18
        w, h = 50, 10
        border_radius = int(h/2)
        pygame.draw.rect(window, COLORS['red'],
                         (x, y, w, h), border_radius=border_radius)
        pygame.draw.rect(
            window, COLORS['green'], (x, y, w - (5 * (self.max_health - self.health)), h), border_radius=border_radius)
        pygame.draw.rect(window, COLORS['black'],
                         (x, y, w, h), width=1, border_radius=border_radius)

    def horizontal_turn_around(self):
        self.speed *= -1
        self.walk_count = 0

    def vertical_turn_around(self):
        self.vertical_speed *= -1
        self.walk_count = 0

    def move(self, player_speed, direction):
        self.x -= player_speed * direction

    def hit(self, shuriken_speed, coins, shuriken_type):
        if self.health > 1:
            self.hit_timer = 3
            try:
                choice(SOUNDS[f'{shuriken_type}_hits']).play()
            except:
                choice(SOUNDS['shuriken_hits']).play()
            self.health -= 1
            self.x += int(shuriken_speed / 2)
            print(self.health)
        else:
            from coin import Coin
            choice(SOUNDS['goblin_deaths']).play()
            x, y, h = itemgetter('x', 'y', 'h')(self.shade)
            coins.append(
                Coin(x - 20, y - 4 * h, choice(["bronze", "silver", "gold"])))
            self.alive = False
