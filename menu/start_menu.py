import pygame
from consts import SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, BACKGROUND_DUNGEON, FPS, SOUNDS, COLORS, BUTTON_WIDTH_BIG
import sys
from menu.button import Button
from menu.options_menu import options_menu
from menu.shop_menu import shop_menu


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['grey_shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Shuriken Man", True,  COLORS['white'])
title_textRect = title_text.get_rect()
title_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4

play_button = Button('Play!', (SCREEN_WIDTH // 3) - (BUTTON_WIDTH_BIG // 2) , SCREEN_HEIGHT // 2, 'big')
shop_button = Button('Shop', (SCREEN_WIDTH * 2 // 3) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT // 2, 'big')
options_button = Button('Options', (SCREEN_WIDTH // 3) - (BUTTON_WIDTH_BIG // 2) , SCREEN_HEIGHT * 3 // 4, 'big')
quit_button = Button('Quit Game', (SCREEN_WIDTH * 2 // 3) - (BUTTON_WIDTH_BIG // 2) , SCREEN_HEIGHT * 3 // 4, 'big')


def redraw_start_menu(background, mouse):
    window.blit(background, (0, 0))
    window.blit(title_text, title_textRect)
    play_button.show(window, mouse)
    shop_button.show(window, mouse)
    options_button.show(window, mouse)
    quit_button.show(window, mouse)
    pygame.display.update()


def start_menu(background):
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if play_button.is_pressed(mouse, click):
            SOUNDS['transition'].play()
            break

        elif quit_button.is_pressed(mouse, click):
            pygame.quit()
            sys.exit()

        elif options_button.is_pressed(mouse, click):
            options_menu()
        
        elif shop_button.is_pressed(mouse, click):
            shop_menu()

        redraw_start_menu(background, mouse)
