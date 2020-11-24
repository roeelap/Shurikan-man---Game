import pygame
from consts import SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, PIXEL_FONT_MID, PIXEL_FONT_BIG, BACKGROUND_DUNGEON, FPS, SOUNDS, CHECKBOX_HEIGHT, BUTTON_WIDTH_BIG
from menu.button import Button, Checkbox
import sys


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['grey_shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

options_title_text = PIXEL_FONT_BIG.render("Options", True,  COLORS['white'])
options_textRect = options_title_text.get_rect()
options_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4

music_text = PIXEL_FONT_MID.render("Music", True,  COLORS['white'])
music_textRect = options_title_text.get_rect()
music_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2


sound_text = PIXEL_FONT_MID.render("Sound", True,  COLORS['white'])
sound_textRect = options_title_text.get_rect()
sound_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4

music_checkbox = Checkbox(SCREEN_WIDTH * 4 // 7 , SCREEN_HEIGHT // 2 - CHECKBOX_HEIGHT, True)
sound_checkbox = Checkbox(SCREEN_WIDTH * 4 // 7 , SCREEN_HEIGHT * 3 // 4 - CHECKBOX_HEIGHT, True)
back_button = Button('Back', SCREEN_WIDTH // 2 - (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 6, 'big')

def set_all_volumes(all_sounds, new_volume):
    for sound in all_sounds:
        if isinstance(sound, list):
            for sound in sound:
                sound.set_volume(new_volume)
        else:
            sound.set_volume(new_volume)

def redraw_options_menu(mouse):
    window.blit(BACKGROUND_DUNGEON, (0, 0))
    window.blit(options_title_text, options_textRect)
    window.blit(music_text, music_textRect)
    window.blit(sound_text, sound_textRect)
    music_checkbox.show(window, mouse)
    sound_checkbox.show(window, mouse)
    back_button.show(window, mouse)
    pygame.display.update()


def options_menu():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # modify this when we add real music into the game
        if music_checkbox.is_pressed(mouse, click):
            pass

        elif sound_checkbox.is_pressed(mouse, click):
            if sound_checkbox.is_on:
                set_all_volumes(SOUNDS.values(), 1.0)
            else:
                set_all_volumes(SOUNDS.values(), 0.0)

        elif back_button.is_pressed(mouse, click):
            break

        redraw_options_menu(mouse)
