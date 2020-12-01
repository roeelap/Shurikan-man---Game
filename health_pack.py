from operator import itemgetter
from static_functions import draw_circle_alpha
from consts import HEALTH_PACK_IMAGE, FPS, HEALTH_PACK_WIDTH, HEALTH_PACK_HEIGHT, COLORS


class HealthPack:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_y = y
        self.end_y = y - 10
        self.y_speed = -0.5
        self.width = HEALTH_PACK_WIDTH
        self.hight = HEALTH_PACK_HEIGHT
        self.image = HEALTH_PACK_IMAGE
        self.shade = {'x': 0, 'y': 0, 'w': 0, 'h': 0}
        self.timer = FPS * 10
        self.is_shown = True
        self.taken = False

    def draw(self, window):
        self.timer -= 1

        self.y += self.y_speed
        if self.y == self.end_y or self.y == self.start_y:
            self.y_speed *= -1

        if FPS * 3 < self.timer < FPS * 10 or self.timer <= FPS * 3 and self.timer % 7 != 0 and not self.taken:
            window.blit(self.image, (self.x, self.y))

        self.draw_shade(window)

        if self.timer == 0:
            self.taken = True

    def draw_shade(self, window):
        self.shade = {'x': self.x + self.width // 2,
                      'y': self.start_y + self.width // 2 + 22, 'w': 35, 'h': 8}
        x, y, w, h = itemgetter('x', 'y', 'w', 'h')(self.shade)
        draw_circle_alpha(window, COLORS['black'], (x, y), w, h)

    def move(self, player_speed, direction):
        self.x -= player_speed * direction
