from consts import PIXEL_FONT_SMALL, SCREEN_HEIGHT, SCREEN_WIDTH, COLORS


class ShopItem:
    def __init__(self, name, price, x, y, image, is_owned):
        self.name = PIXEL_FONT_SMALL.render(str(name), True,  COLORS['white'])
        self.price = price
        self.x = x
        self.y = y
        self.width = 18
        self.image = image
        self.is_owned = is_owned
    
    def show(self, window):
        window.blit(self.image, (self.x, self.y))
        window.blit(self.name, (self.x + self.width * 2, self.y))
        if self.is_owned:
            price_text = 'Owned'
        else:
            price_text = f'Price: {str(self.price)} coins'
        price_text = PIXEL_FONT_SMALL.render((price_text), True,  COLORS['white'])
        window.blit(price_text, (self.x, self.y + self.width * 2))