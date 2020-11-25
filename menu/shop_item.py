from consts import PIXEL_FONT_SMALL, COLORS, BUTTON_WIDTH_SMALL
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
            'Buy', self.x - BUTTON_WIDTH_SMALL - 10, self.y, 'small')
        self.equip_button = Button(
            'Equip', self.x + BUTTON_WIDTH_SMALL * 1.75, self.y, 'small')

    def show(self, window, mouse, player):
        owned = self.name in player.shurikens_owned
        equipped = self.name == player.shuriken_equipped

        if self.price > player.coins:
            self.buy_button.disabled = True
        
        if not owned:
            self.buy_button.show(window, mouse)

        if not equipped and owned:
            self.equip_button.show(window, mouse)

        window.blit(self.image, (self.x, self.y))
        name = PIXEL_FONT_SMALL.render(str(self.name), True,  COLORS['white'])
        window.blit(name, (self.x + self.width * 2, self.y))
        if owned and not equipped:
            price_text = 'Owned'
        elif equipped:
            price_text = 'Equipped'
        else:
            price_text = f'Price: {str(self.price)} coins'
        price_text = PIXEL_FONT_SMALL.render(
            (price_text), True,  COLORS['white'])
        window.blit(price_text, (self.x, self.y + self.width * 2))
