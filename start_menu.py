import pygame
from consts import *
import sys


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(PLAYER_PORTRAIT)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Shuriken Man", True,  COLORS['white'])


class Button:

    def __init__(self, x, y, width, height, inactive_image, active_image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_image = inactive_image
        self.active_image = active_image
        self.over = False

    def play_hover_sound(self):
        if not self.over:
            BUTTON_HOVER_SOUND.play()
            self.over = True

    def is_mouse_over(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True
        return False

    def show(self, window, mouse):
        if self.is_mouse_over(mouse):
            self.play_hover_sound()
            window.blit(self.active_image, (self.x, self.y))
        else:
            self.over = False
            window.blit(self.inactive_image, (self.x, self.y))

    def is_pressed(self, mouse, click, action=None):
        if self.is_mouse_over(mouse):
            if click[0] == 1:
                BUTTON_CLICK_SOUND.play()
                return True


new_game_button = Button(100, 300, 227, 46, NEW_GAME_INACTIVE_BUTTON,
                         NEW_GAME_ACTIVE_BUTTON)
shop_button = Button(473, 300, 227, 46, SHOP_INACTIVE_BUTTON,
                     SHOP_ACTIVE_BUTTON)
options_button = Button(100, 400, 227, 46, OPTIONS_INACTIVE_BUTTON,
                        OPTIONS_ACTIVE_BUTTON)
quit_button = Button(473, 400, 227, 46, QUIT_INACTIVE_BUTTON,
                     QUIT_ACTIVE_BUTTON)


def redraw_start_menu(mouse):
    window.blit(BACKGROUND_DUNGEON, (0, 0))
    window.blit(title_text, (145, 100))
    new_game_button.show(window, mouse)
    shop_button.show(window, mouse)
    options_button.show(window, mouse)
    quit_button.show(window, mouse)
    pygame.display.update()


def start_menu():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if new_game_button.is_pressed(mouse, click):
            TRANSITION_SOUND.play()
            break

        elif quit_button.is_pressed(mouse, click):
            pygame.quit()
            sys.exit()

        redraw_start_menu(mouse)
