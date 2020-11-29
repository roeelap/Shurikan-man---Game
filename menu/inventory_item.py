from static_functions import draw_rotated
from consts import PIXEL_FONT_SMALL, COLORS, BUTTON_WIDTH_SMALL, PIXEL_FONT_SMALL_BUTTON
from menu.button import Button


class InventoryItem:
    def __init__(self, x, y, name, image):
        self.x = x
        self.y = y
        self.width = 18
        self.name = name
        self.image = image
        self.equip_button = Button(
            self.x - BUTTON_WIDTH_SMALL - 10, self.y, 'small', 'Equip')
        self.rotation_angle = 0
        self.is_shown = True

    def show(self, window, mouse, player):
        equipped = self.name == player.shuriken_equipped

        if not equipped:
            self.equip_button.disabled = False
            self.equip_button.inactive_text = PIXEL_FONT_SMALL_BUTTON.render(
                'Equip', True,  COLORS['black'])
        else:
            self.equip_button.disabled = True
            self.equip_button.inactive_text = PIXEL_FONT_SMALL_BUTTON.render(
                'Equipped', True,  COLORS['black'])
            
        self.equip_button.show(window, mouse)

        draw_rotated(window, self.image, (self.x + self.width,
                                          self.y + self.width * 2), self.rotation_angle)
        self.rotation_angle += 5

        name = PIXEL_FONT_SMALL.render(str(self.name).replace(
            '_', ' ').capitalize(), True,  COLORS['white'])
        window.blit(name, (self.x, self.y))

    def update_location(self, x, y):
        self.x = x
        self.y = y
        self.equip_button.update_location(x - BUTTON_WIDTH_SMALL - 10, y)
    
    def show_without_button(self, x, y, window):
        draw_rotated(window, self.image, (x + self.width,
                                          y + self.width * 2), self.rotation_angle)
        self.rotation_angle += 5

        name = PIXEL_FONT_SMALL.render(str(self.name).replace(
            '_', ' ').capitalize(), True,  COLORS['white'])
        window.blit(name, (x, y))


