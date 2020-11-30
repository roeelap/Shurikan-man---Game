from operator import itemgetter
import pygame
from menu.popup import popup
from menu.button import Button
from menu.settings_menu import settings_menu
from menu.shop_menu import shop_menu
from menu.upgrades import upgrades_shop
from static_functions import draw_rect_with_alpha, reset_game, save_game, draw_rotated
from consts import MENU_SHURIKENS_LARGE, SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, FPS, SOUNDS, COLORS, BUTTON_WIDTH_BIG


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Shuriken Man", True,  COLORS['white'])
title_textRect = title_text.get_rect()
title_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8


def redraw_start_menu(menu_buttons, background, mouse, rotation_angle, player, pause_screen=False):

    window.blit(background, (0, 0))
    if pause_screen:
        draw_rect_with_alpha(0, 0, SCREEN_WIDTH,
                             SCREEN_HEIGHT, COLORS['black'], 128, window)

    window.blit(title_text, title_textRect)
    for button in menu_buttons.values():
        button.show(window, mouse)

    rotating_image = MENU_SHURIKENS_LARGE.get(
        player.shuriken_equipped, 'shuriken')
    draw_rotated(window, rotating_image, (0.75*SCREEN_WIDTH,
                                          SCREEN_HEIGHT // 20), rotation_angle)
    draw_rotated(window, rotating_image, (0.17*SCREEN_WIDTH,
                                          SCREEN_HEIGHT // 20), rotation_angle)
    pygame.display.update()


def check_for_button_press(buttons, mouse, click, game_objects):
    player, enemies, background, settings = itemgetter(
        'player', 'enemies', 'background', 'settings')(game_objects)
    for name, button in buttons.items():
        if button.is_pressed(mouse, click):
            buttons['save'].disabled = False
            if name == 'play':
                SOUNDS['transition'].play()
                return True
            if name == 'new_game':
                SOUNDS['transition'].play()
                reset_game()
                return 'new_game'
            if name == 'upgrades':
                upgrades_shop(game_objects)
            elif name == 'shop':
                shop_menu(game_objects)
            elif name == 'save':
                save_game(player, enemies, background, settings)
                button.clicked = True
                SOUNDS['sword_draw'].play()
            elif name == 'settings':
                settings_menu(game_objects)
            elif name == 'quit':
                popup(window.copy(), game_objects)
            return False


def start_menu(background_image, game_objects, pause_screen=False):
    player = game_objects['player']
    menu_buttons = {'play': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 2 // 9, 'big', 'Play!'),
                    'new_game': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 3 // 9, 'big', 'New Game'),
                    'shop': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 4 // 9, 'big', 'Shop'),
                    'upgrades': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 9, 'big', 'Upgrades'),
                    'save': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 6 // 9, 'big', 'Save'),
                    'settings': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 7 // 9, 'big', 'Settings'),
                    'quit': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 8 // 9, 'big', 'Quit Game')}
    rotation_angle = 0
    menu_buttons['save'].disabled = False

    while True:
        rotation_angle += 1
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)

        for event in pygame.event.get():
            # do other stuff
            if event.type == pygame.QUIT and menu_buttons['save'].disabled:
                exit()
            elif event.type == pygame.QUIT and not menu_buttons['save'].disabled:
                popup(window.copy(), game_objects)

            if pause_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        SOUNDS['transition'].play()
                        return
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()
                state = check_for_button_press(
                    menu_buttons, mouse, click, game_objects)
                if state:
                    return state

        redraw_start_menu(menu_buttons, background_image, mouse,
                          rotation_angle, player, pause_screen)
