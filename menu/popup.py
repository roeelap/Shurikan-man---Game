from operator import itemgetter
import sys
import pygame
from consts import POPUP_IMAGE, SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SOUNDS, COLORS, BUTTON_WIDTH_BIG
from menu.button import Button
from static_functions import save_game, draw_rect_with_alpha


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def redraw_popup(menu_buttons, background, mouse):

    window.blit(background, (0, 0))
    draw_rect_with_alpha(0, 0, SCREEN_WIDTH,
                         SCREEN_HEIGHT, COLORS['black'], 128, window)
    window.blit(POPUP_IMAGE, (350, 200))
    for button in menu_buttons.values():
        button.show(window, mouse)
    pygame.display.update()


def check_for_button_press(buttons, mouse, click, game_objects):
    player, enemies, background, settings = itemgetter(
        'player', 'enemies', 'background', 'settings')(game_objects)
    for name, button in buttons.items():
        if button.is_pressed(mouse, click):
            if name == 'save_and_exit':
                save_game(player, enemies, background, settings)
                button.clicked = True
                button.exit = True
                SOUNDS['sword_draw'].play()
            if name == 'exit_without_save':
                pygame.quit()
                sys.exit()
            if name == 'cancel':
                return False
    return True

def popup(background_image, game_objects):
    menu_buttons = {'save_and_exit': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 3 // 9, 'big', 'Save And Exit'),
                    'exit_without_save': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 4 // 9, 'big', 'Exit Without Save'),
                    'cancel': Button((SCREEN_WIDTH // 2) - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 9, 'big', 'Cancel')}

    while True:
        mouse = pygame.mouse.get_pos()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SOUNDS['button_click'].play()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()
                state = check_for_button_press(
                    menu_buttons, mouse, click, game_objects)
                if not state:
                    return

        redraw_popup(menu_buttons, background_image, mouse)
