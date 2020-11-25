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
        self.buy_button = Button(
            str(self.price) + '$', self.x - BUTTON_WIDTH_SMALL - 10, self.y - BUTTON_HEIGHT_SMALL / 2, 'small')
        self.equip_button = Button(
            'Equip', self.x - BUTTON_WIDTH_SMALL - 10, self.y + BUTTON_HEIGHT_SMALL / 2, 'small')

    def show(self, window, mouse, player):
        owned = self.name in player.shurikens_owned
        equipped = self.name == player.shuriken_equipped

        if owned and equipped:
            self.buy_button.disabled = True
            self.equip_button.disabled = True
            self.equip_button.inactive_text = PIXEL_FONT_SMALL_BUTTON.render(
                'Equipped', True,  COLORS['black'])

        elif owned:
            self.buy_button.disabled = True
            self.buy_button.inactive_text = PIXEL_FONT_SMALL_BUTTON.render(
            'Bought', True,  COLORS['black'])
            if not equipped:
                self.equip_button.disabled = False
        elif not owned:
            self.equip_button.disabled = True

        if self.price > player.coins and not owned:
            self.buy_button.disabled = True
            self.equip_button.disabled = True
        
        self.buy_button.show(window, mouse)
        self.equip_button.show(window, mouse)

        window.blit(self.image, (self.x + self.width, self.y + self.width * 2))

        name = PIXEL_FONT_SMALL.render(str(self.name), True,  COLORS['white'])
        window.blit(name, (self.x, self.y))
        
