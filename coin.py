from consts import BRONZE_COINS, SILVER_COINS, GOLD_COINS, COLORS
from static_functions import draw_circle_alpha
from operator import itemgetter


class Coin:

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.radius = 20
        self.height = 20 * 2
        self.kind = kind
        self.spin_count = 0
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}

    def draw(self, window):
        if self.spin_count + 1 >= 16:
            self.spin_count = 0
        if self.kind == "bronze":
            window.blit(BRONZE_COINS[self.spin_count // 2], (self.x, self.y))
        elif self.kind == "silver":
            window.blit(SILVER_COINS[self.spin_count // 2], (self.x, self.y))
        elif self.kind == "gold":
            window.blit(GOLD_COINS[self.spin_count // 2], (self.x, self.y))

        self.spin_count += 1

        self.draw_shade(window)

    def draw_shade(self, window):
        self.shade = {'x': self.x+self.radius,
                      'y': self.y+self.radius+30, 'w': 35, 'h': 8}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(
            window, COLORS['black'], (x, y), w, h)

    def move(self, player_speed, direction):
        self.x -= player_speed * direction
