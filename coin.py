from consts import BRONZE_COINS_IMAGES, COIN_END_PATH_X, COIN_END_PATH_Y, GOLD_COINS_IMAGES, COLORS, SILVER_COINS_IMAGES, SMALL_COINS_IMAGES
from static_functions import draw_circle_alpha
from operator import itemgetter, xor
from math import sqrt, pow


class Coin:

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.pickup_x_delta = self.x
        self.pickup_y_delta = self.y
        self.radius = 20
        self.height = 20 * 2
        self.kind = kind
        self.spin_count = 0
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}
        self.taken = False
        self.stored = False

    def draw(self, window):
        if not self.taken:
            if self.spin_count + 1 >= 16:
                self.spin_count = 0
            if self.kind == "bronze":
                window.blit(
                    BRONZE_COINS_IMAGES[self.spin_count // 2], (self.x, self.y))
            elif self.kind == "silver":
                window.blit(
                    SILVER_COINS_IMAGES[self.spin_count // 2], (self.x, self.y))
            elif self.kind == "gold":
                window.blit(
                    GOLD_COINS_IMAGES[self.spin_count // 2], (self.x, self.y))

            self.spin_count += 1

            self.draw_shade(window)
        else:
            self.radius = 7
            self.pickup_animation(window)
            if self.x <= COIN_END_PATH_X and self.y <= COIN_END_PATH_Y:
                self.stored = True

    def pickup_animation(self, window):
        delta = sqrt(pow(abs(self.y - COIN_END_PATH_Y), 2)+pow(abs(self.x - COIN_END_PATH_X), 2))
        if self.x > COIN_END_PATH_X:
            self.x -= pow(self.pickup_x_delta, 1.3) / delta
        if self.y > COIN_END_PATH_Y:
            self.y -= pow(self.pickup_y_delta, 1.3) / delta
        window.blit(
            SMALL_COINS_IMAGES[self.kind], (self.x, self.y))

    def set_pickup_delta(self):
        self.pickup_x = abs(self.x - COIN_END_PATH_X)
        self.pickup_y = abs(self.y - COIN_END_PATH_Y)

    def draw_shade(self, window):
        self.shade = {'x': self.x+self.radius,
                      'y': self.y+self.radius+30, 'w': 35, 'h': 8}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

    def move(self, player_speed, direction):
        if not self.taken:
            self.x -= player_speed * direction
