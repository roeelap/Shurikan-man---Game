import pygame
from menu.popup import popup
from menu.button import Button, Checkbox
from consts import SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, PIXEL_FONT_MID, PIXEL_FONT_BIG, BACKGROUND_DUNGEON, FPS, SOUNDS, CHECKBOX_HEIGHT, BUTTON_WIDTH_BIG

pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

settings_title_text = PIXEL_FONT_BIG.render("Settings", True,  COLORS['white'])
settings_textRect = settings_title_text.get_rect()
settings_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8

music_text = PIXEL_FONT_MID.render("Music", True,  COLORS['white'])
music_textRect = settings_title_text.get_rect()
music_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3


sound_text = PIXEL_FONT_MID.render("Sound", True,  COLORS['white'])
sound_textRect = settings_title_text.get_rect()
sound_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 7


def set_all_volumes(all_sounds, new_volume):
    for sound in all_sounds:
        if isinstance(sound, list):
            for inner_sound in sound:
                inner_sound.set_volume(new_volume)
        else:
            sound.set_volume(new_volume)


def redraw_settings_menu(mouse, music_checkbox, sound_checkbox, back_button):
    window.blit(BACKGROUND_DUNGEON, (0, 0))
    window.blit(settings_title_text, settings_textRect)
    window.blit(music_text, music_textRect)
    window.blit(sound_text, sound_textRect)
    music_checkbox.show(window, mouse)
    sound_checkbox.show(window, mouse)
    back_button.show(window, mouse)
    pygame.display.update()


def settings_menu(game_objects):
    settings = game_objects['settings']
    music_checkbox = Checkbox(SCREEN_WIDTH * 4 // 7,
                              SCREEN_HEIGHT // 3 - CHECKBOX_HEIGHT, settings['music'])
    sound_checkbox = Checkbox(SCREEN_WIDTH * 4 // 7,
                              SCREEN_HEIGHT * 3 // 7 - CHECKBOX_HEIGHT, settings['sound'])
    back_button = Button(SCREEN_WIDTH // 2 -
                         (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 6, 'big', 'Back')
    while True:
        mouse = pygame.mouse.get_pos()
        
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                popup(window.copy(), game_objects)
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                click = pygame.mouse.get_pressed()

                # modify this when we add real music into the game
                if music_checkbox.is_pressed(mouse, click):
                    if music_checkbox.is_on:
                        settings['music'] = True
                    else:
                        settings['music'] = False

                elif sound_checkbox.is_pressed(mouse, click):
                    if sound_checkbox.is_on:
                        set_all_volumes(SOUNDS.values(), 1.0)
                        settings['sound'] = True
                    else:
                        set_all_volumes(SOUNDS.values(), 0.0)
                        settings['sound'] = False

                elif back_button.is_pressed(mouse, click):
                    return

        redraw_settings_menu(mouse, music_checkbox,
                             sound_checkbox, back_button)
