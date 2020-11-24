from consts import PIXEL_FONT_SMALL, COLORS, CHECKBOX_WIDTH 
from menu.button import Checkbox


class ShopItem:
    def __init__(self, name, price, x, y, image, is_owned):
        self.name = PIXEL_FONT_SMALL.render(str(name), True,  COLORS['white'])
        self.price = price
        self.x = x
        self.y = y
        self.width = 18
        self.image = image
        self.is_owned = is_owned
        self.want_to_buy = False
        self.checkbox = Checkbox(self.x - self.width - CHECKBOX_WIDTH, self.y)

    def show(self, window, mouse):
        if not self.is_owned:
            self.checkbox.show(window, mouse)
        else:
            self.checkbox = None
        window.blit(self.image, (self.x, self.y))
        window.blit(self.name, (self.x + self.width * 2, self.y))
        if self.is_owned:
            price_text = 'Owned'
        else:
            price_text = f'Price: {str(self.price)} coins'
        price_text = PIXEL_FONT_SMALL.render((price_text), True,  COLORS['white'])
        window.blit(price_text, (self.x, self.y + self.width * 2))