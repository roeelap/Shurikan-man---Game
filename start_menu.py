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
    
    def show(self, window):
        global mouse
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            window.blit(self.active_image, (self.x, self.y))
        else:
            window.blit(self.inactive_image, (self.x, self.y))
    
    def is_pressed(self, action=None):
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if click[0] == 1:
                return True


new_game_button = Button(100, 300, 227, 46, NEW_GAME_INACTIVE_BUTTON,
           NEW_GAME_ACTIVE_BUTTON)
shop_button = Button(473, 300, 227, 46, SHOP_INACTIVE_BUTTON,
           SHOP_ACTIVE_BUTTON)
options_button = Button(100, 400, 227, 46, OPTIONS_INACTIVE_BUTTON,
           OPTIONS_ACTIVE_BUTTON)
quit_button = Button(473, 400, 227, 46, QUIT_INACTIVE_BUTTON,
           QUIT_ACTIVE_BUTTON) 


def redraw_start_menu():
    window.blit(BACKGROUND_DUNGEON, (0, 0))
    window.blit(title_text, (145, 100))
    new_game_button.show(window)
    shop_button.show(window)
    options_button.show(window)
    quit_button.show(window)
    pygame.display.update()


def start_menu():
    while True:

        clock.tick(FPS)

        redraw_start_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if new_game_button.is_pressed():
            break
        
        elif quit_button.is_pressed():
            pygame.quit()
            sys.exit() 