from static_functions import draw_circle_alpha
from operator import itemgetter
from consts import HEALTH_PACK_IMAGE, FPS, HEALTH_PACK_WIDTH, HEALTH_PACK_HEIGHT, COLORS


class HealthPack:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = HEALTH_PACK_WIDTH
        self.hight = HEALTH_PACK_HEIGHT
        self.image = HEALTH_PACK_IMAGE
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}
        self.timer = FPS * 60
        self.is_shown = True
        self.taken = False

    def draw(self, window):
        self.timer -= 1

        if FPS * 3 < self.timer < FPS * 60 or self.timer <= FPS * 3 and self.timer % 10 != 0 and not self.taken:
            window.blit(self.image, (self.x, self.y))
            self.draw_shade(window)

    def draw_shade(self, window):
        self.shade = {'x': self.x + self.width // 2,
                      'y': self.y + self.width // 2 + 30, 'w': 35, 'h': 8}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(window, COLORS['black'], (x, y), w, h)

    def move(self, player_speed, direction):
        self.x -= player_speed * direction
