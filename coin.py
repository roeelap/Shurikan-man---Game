from consts import BRONZE_COINS_IMAGES, GOLD_COINS_IMAGES, COLORS, SILVER_COINS_IMAGES, SMALL_COINS_IMAGES
from static_functions import draw_circle_alpha
from operator import itemgetter
from math import sqrt, pow


class Coin:

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
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
            if self.x <= 100 and self.y <= 100:
                self.stored = True

    def pickup_animation(self, window):
        delta = sqrt(pow(abs(self.y - 100), 2)+pow(abs(self.x - 100), 2))
        speed = 1000000 / pow(delta, 2)
        if self.x > 100:
            self.x -= speed
        if self.y > 100:
            self.y -= speed
        window.blit(
            SMALL_COINS_IMAGES[self.kind], (self.x, self.y))

    def draw_shade(self, window):
        self.shade = {'x': self.x+self.radius,
                      'y': self.y+self.radius+30, 'w': 35, 'h': 8}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

    def move(self, player_speed, direction):
        if not self.taken:
            self.x -= player_speed * direction
