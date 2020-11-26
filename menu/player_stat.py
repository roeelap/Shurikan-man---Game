import pygame
from consts import COLORS, BUTTON_IMAGES, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT, PIXEL_FONT_SMALL
from menu.button import Button


class PlayerStat:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.level = 0
        self.up_button = Button(self.x, self.y - ARROW_BUTTON_HEIGHT , 'up_arrow')
        self.down_button = Button(self.x + ARROW_BUTTON_WIDTH + 5, self.y - ARROW_BUTTON_HEIGHT , 'down_arrow')
    
    def upgrade_stat(self, player):
        if self.level < 10 or player.upgrade_points > 0:
            self.level += 1
            player.upgrade_points -= 1
    
    def downgrade_stat(self, player):
        if self.level > 0:
            self.level -= 1
            player.upgrade_points += 1

    def show(self, window, mouse, player):
        name = PIXEL_FONT_SMALL.render(str(self.name).replace(
            '_', ' ').capitalize(), True,  COLORS['white'])
        window.blit(name, (self.x, self.y))

        if self.level == 10:   
            level_text = PIXEL_FONT_SMALL.render(('Level: Max'), True,  COLORS['white'])
        else:
            level_text = PIXEL_FONT_SMALL.render(('Level: ' + str(self.level)), True,  COLORS['white'])
        window.blit(level_text, (self.x, self.y - name.get_rect()[3] + ARROW_BUTTON_HEIGHT + 10))
        
        if player.upgrade_points == 0:
            self.up_button.disabled = True
        else:
            self.up_button.disabled = False

        if self.level == 0:
            self.down_button.disabled = True
        else:
            self.down_button.disabled = False

        self.up_button.show(window, mouse)
        self.down_button.show(window, mouse)

        for i in range(self.level):
            pygame.draw.rect(window, (180, i * 18, i * 18), [self.x, self.y - name.get_rect()[3] * 3 - i * 20, ARROW_BUTTON_WIDTH * 2, 20])
            pygame.draw.rect(window, COLORS['black'], [self.x, self.y - name.get_rect()[3] * 3 - i * 20, ARROW_BUTTON_WIDTH * 2, 20], width=2)






