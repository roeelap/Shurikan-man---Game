import pygame
from consts import SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, FPS, SHURIKEN_LARGE, SOUNDS, COLORS, BUTTON_WIDTH_BIG
import sys
from menu.button import Button
from menu.options_menu import options_menu
from menu.shop_menu import shop_menu
from static_functions import save_game, draw_rotated


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Shuriken Man", True,  COLORS['white'])
title_textRect = title_text.get_rect()
title_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 7

play_button = Button('Play!', (SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 2 // 7, 'big')
save_button = Button('Save', (SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 3 // 7, 'big')
shop_button = Button('Shop', (SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 4 // 7, 'big')
options_button = Button('Options', (SCREEN_WIDTH // 2) -
                        (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 7, 'big')
quit_button = Button('Quit Game', (SCREEN_WIDTH // 2) -
                     (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 6 // 7, 'big')


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
    save_button.show(window, mouse)
    shop_button.show(window, mouse)
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

                elif save_button.is_pressed(mouse, click):
                    save_button.clicked = True
                    SOUNDS['sword_draw'].play()
                    save_game(player, enemies, background)

                elif quit_button.is_pressed(mouse, click):
                    pygame.quit()
                    sys.exit()

                elif options_button.is_pressed(mouse, click):
                    options_menu()

                elif shop_button.is_pressed(mouse, click):
                    shop_menu(player)

        redraw_start_menu(background_image, mouse,
                          rotation_angle, pause_screen)
