import pygame
from consts import SHURIKEN_IMAGE, SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, BACKGROUND_DUNGEON, FPS, SOUNDS, COLORS
import sys
from button import Button
from options_menu import options_menu
from shop_menu import shop_menu


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Shuriken Man", True,  COLORS['white'])


new_game_button = Button('New Game', 100, 300)
shop_button = Button('Shop', 473, 300)
options_button = Button('Options', 100, 400)
quit_button = Button('Quit Game', 473, 400)


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
            SOUNDS['transition'].play()
            break

        elif quit_button.is_pressed(mouse, click):
            pygame.quit()
            sys.exit()

        elif options_button.is_pressed(mouse, click):
            options_menu()
        
        elif shop_button.is_pressed(mouse, click):
            shop_menu()

        redraw_start_menu(mouse)
