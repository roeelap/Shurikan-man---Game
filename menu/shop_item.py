from consts import PIXEL_FONT_SMALL, COLORS, BUTTON_WIDTH_SMALL
from menu.button import Button


class ShopItem:
    def __init__(self, name, price, x, y, image, is_owned, is_equipped):
        self.name = name
        self.price = price
        self.x = x
        self.y = y
        self.width = 18
        self.image = image
        self.is_owned = is_owned
        self.is_equipped = is_equipped
        self.buy_button = Button(
            'Buy', self.x - BUTTON_WIDTH_SMALL - 10, self.y, 'small')
        self.equip_button = Button(
            'Equip', self.x + BUTTON_WIDTH_SMALL * 1.75, self.y, 'small')

    def show(self, window, mouse):
        if not self.is_owned:
            self.buy_button.show(window, mouse)

        if not self.is_equipped and self.is_owned:
            self.equip_button.show(window, mouse)

        window.blit(self.image, (self.x, self.y))
        name = PIXEL_FONT_SMALL.render(str(self.name), True,  COLORS['white'])
        window.blit(name, (self.x + self.width * 2, self.y))
        if self.is_owned and not self.is_equipped:
            price_text = 'Owned'
        elif self.is_equipped:
            price_text = 'Equipped'
        else:
            price_text = f'Price: {str(self.price)} coins'
        price_text = PIXEL_FONT_SMALL.render(
            (price_text), True,  COLORS['white'])
        window.blit(price_text, (self.x, self.y + self.width * 2))
