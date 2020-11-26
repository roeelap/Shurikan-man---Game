import pygame
from consts import SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, FPS, SHURIKEN_LARGE, SOUNDS, COLORS, BUTTON_WIDTH_BIG
import sys
from menu.button import Button
from menu.options_menu import options_menu
from menu.shop_menu import shop_menu
from menu.upgrades import upgrades_shop
from static_functions import save_game, draw_rotated


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Shuriken Man", True,  COLORS['white'])
title_textRect = title_text.get_rect()
title_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8

play_button = Button((SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 2 // 8, 'big', 'Play!')
shop_button = Button((SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 3 // 8, 'big', 'Shop')
upgrades_button = Button((SCREEN_WIDTH // 2) -
                         (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 4 // 8, 'big', 'Upgrades')
save_button = Button((SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 8, 'big', 'Save')
options_button = Button((SCREEN_WIDTH // 2) -
                        (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 6 // 8, 'big', 'Options')
quit_button = Button((SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 7 // 8, 'big', 'Quit Game')


def redraw_start_menu(background, mouse, rotation_angle, pause_screen=False):

    window.blit(background, (0, 0))
    if pause_screen:
        target_rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
        shape_surf = pygame.Surface(window.get_size(), pygame.SRCALPHA)
        shape_surf.set_alpha(128)
        pygame.draw.rect(
            shape_surf, COLORS['black'], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        window.blit(shape_surf, target_rect)

    window.blit(title_text, title_textRect)
    play_button.show(window, mouse)
    upgrades_button.show(window, mouse)
    shop_button.show(window, mouse)
    save_button.show(window, mouse)
    options_button.show(window, mouse)
    quit_button.show(window, mouse)
    draw_rotated(window, SHURIKEN_LARGE, (0.75*SCREEN_WIDTH,
                                          SCREEN_HEIGHT // 20), rotation_angle)
    draw_rotated(window, SHURIKEN_LARGE, (0.17*SCREEN_WIDTH,
                                          SCREEN_HEIGHT // 20), rotation_angle)
    pygame.display.update()


def start_menu(background_image, player, enemies, background, pause_screen=False):
    rotation_angle = 0
    save_button.disabled = False

    while True:
        rotation_angle += 1
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if pause_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        SOUNDS['transition'].play()
                        return
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()

                if play_button.is_pressed(mouse, click):
                    SOUNDS['transition'].play()
                    return

                elif upgrades_button.is_pressed(mouse, click):
                    upgrades_shop(player)

                elif shop_button.is_pressed(mouse, click):
                    save_button.disabled = False
                    shop_menu(player)

                elif save_button.is_pressed(mouse, click):
                    save_game(player, enemies, background)
                    save_button.clicked = True
                    SOUNDS['sword_draw'].play()

                elif options_button.is_pressed(mouse, click):
                    save_button.disabled = False
                    options_menu()

                elif quit_button.is_pressed(mouse, click):
                    pygame.quit()
                    exit()

        redraw_start_menu(background_image, mouse,
                          rotation_angle, pause_screen)
