import pygame
from consts import COLORS, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT, PIXEL_FONT_SMALL, FPS
from menu.button import ArrowButton
from static_functions import draw_rect_with_alpha


class PlayerStat:
    def __init__(self, name, x, y, upgrade_dict):
        self.name = name
        self.x = x
        self.y = y
        self.level = upgrade_dict[self.name]
        self.level_delta = 0
        self.next_rect_y = self.y - 50
        self.up_button = ArrowButton(
            self.x, self.y - ARROW_BUTTON_HEIGHT - 5, 'up_arrow')
        self.down_button = ArrowButton(
            self.x + ARROW_BUTTON_WIDTH + 5, self.y - ARROW_BUTTON_HEIGHT - 5, 'down_arrow')
        self.is_confirmed = True
        self.bar_timer = 0

    def upgrade_stat(self, player, window):
        if self.level + self.level_delta <= 20 or player.upgrade_points > 0:
            self.is_confirmed = False
            player.upgrade_points -= 1
            self.level_delta += 1

    def downgrade_stat(self, player):
        if self.level_delta > 0:
            self.level_delta -= 1
            player.upgrade_points += 1

    def show(self, window, mouse, player):
        if self.bar_timer + 1 <= FPS:
            self.bar_timer += 1
        else:
            self.bar_timer = 0

        self.show_name_and_level(window)

        if player.upgrade_points == 0 or self.level + self.level_delta == 20:
            self.up_button.disabled = True
        else:
            self.up_button.disabled = False

        if self.level_delta == 0:
            self.down_button.disabled = True
        else:
            self.down_button.disabled = False

        self.up_button.show(window, mouse)
        self.down_button.show(window, mouse)

        for i in range(self.level):
            pygame.draw.rect(window, (180, i * 9, i * 9), [
                             self.x, self.up_button.y - 20 - i * 15, ARROW_BUTTON_WIDTH * 2, 15], border_radius=5)
            pygame.draw.rect(window, COLORS['black'], [
                             self.x, self.up_button.y - 20 - i * 15, ARROW_BUTTON_WIDTH * 2, 15], width=1, border_radius=5)

        for i in range(self.level_delta):
            if self.bar_timer <= FPS * 4 / 5:
                draw_rect_with_alpha(self.x, self.up_button.y - 20 - (self.level + i)
                                     * 15, ARROW_BUTTON_WIDTH * 2, 15, (180, i * 9, i * 9), 128, window,5)
                pygame.draw.rect(window, COLORS['black'], [
                                 self.x, self.up_button.y - 20 - (self.level + i) * 15, ARROW_BUTTON_WIDTH * 2, 15], width=1,border_radius=5)

        if self.is_confirmed:
            self.level += self.level_delta
            self.level_delta = 0

    def show_name_and_level(self, window):
        name = PIXEL_FONT_SMALL.render(str(self.name).replace(
            '_', ' ').capitalize(), True,  COLORS['white'])
        window.blit(name, (self.x, self.y))

        if self.level + self.level_delta == 20:
            level_text = PIXEL_FONT_SMALL.render(
                ('Level: Max'), True,  COLORS['white'])
        else:
            level_text = PIXEL_FONT_SMALL.render(
                ('Level: ' + str(self.level + self.level_delta)), True,  COLORS['white'])
        window.blit(level_text, (self.x, self.y - name.get_rect()
                                 [3] + ARROW_BUTTON_HEIGHT + 10))
