from static_functions import draw_rotated
from consts import PIXEL_FONT_SMALL, COLORS, BUTTON_WIDTH_SMALL, BUTTON_HEIGHT_SMALL, PIXEL_FONT_SMALL_BUTTON
from menu.button import Button


class ShopItem:
    def __init__(self, name, price, x, y, image):
        self.name = name
        self.price = price
        self.x = x
        self.y = y
        self.width = 18
        self.image = image
        self.buy_button = Button(self.x - BUTTON_WIDTH_SMALL - 10, self.y, 'small', str(self.price) + '$')
        self.rotation_angle = 0

    def show(self, window, mouse, player):
        owned = self.name in player.shurikens_owned

        if not owned:
            if self.price > player.coins:
                self.buy_button.disabled = True
            else:
                self.buy_button.disabled = False

        elif owned:
            self.buy_button.disabled = True
            self.buy_button.inactive_text = PIXEL_FONT_SMALL_BUTTON.render(
                'Bought', True,  COLORS['black'])

        self.buy_button.show(window, mouse)

        draw_rotated(window, self.image, (self.x + self.width,
                                          self.y + self.width * 2), self.rotation_angle)
        self.rotation_angle += 5

        name = PIXEL_FONT_SMALL.render(str(self.name).replace(
            '_', ' ').capitalize(), True,  COLORS['white'])
        window.blit(name, (self.x, self.y))
