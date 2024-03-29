import pygame
from menu.popup import popup
from menu.button import Button, Checkbox, ScrollBar
from static_functions import draw_rect_with_alpha
from consts import SHURIKEN_IMAGES, SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, PIXEL_FONT_MID, PIXEL_FONT_BIG, PIXEL_FONT_BIG_BUTTON, BACKGROUND_DUNGEON, FPS, SOUNDS, CHECKBOX_HEIGHT, BUTTON_WIDTH_BIG

pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

settings_title_text = PIXEL_FONT_BIG.render("Settings", True,  COLORS['white'])
settings_textRect = settings_title_text.get_rect()
settings_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8

max_text = PIXEL_FONT_BIG_BUTTON.render("Max", True,  COLORS['white'])
min_text = PIXEL_FONT_BIG_BUTTON.render("Min", True,  COLORS['white'])
toggle_text = PIXEL_FONT_BIG_BUTTON.render("On / Off", True,  COLORS['white'])

music_text = PIXEL_FONT_MID.render("Music", True,  COLORS['white'])
music_textRect = settings_title_text.get_rect()
music_textRect.center = SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 3
music_scroll_bar = ScrollBar(music_textRect[0] + SCREEN_WIDTH // 2 - 48, SCREEN_HEIGHT // 3 - 35, 100, 30, COLORS['orange'])

sound_text = PIXEL_FONT_MID.render("Sound", True,  COLORS['white'])
sound_textRect = settings_title_text.get_rect()
sound_textRect.center = SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2
sound_scroll_bar = ScrollBar(music_textRect[0] + SCREEN_WIDTH // 2 - 48, SCREEN_HEIGHT // 2 - 35, 100, 30, COLORS['cyan'])


def redraw_settings_menu(mouse, music_checkbox, sound_checkbox, back_button, music_scroll_bar, sound_scroll_bar):
    window.blit(BACKGROUND_DUNGEON, (0, 0))
    window.blit(settings_title_text, settings_textRect)

    show_setting(window, mouse, music_text, music_textRect, SCREEN_HEIGHT // 3, music_scroll_bar, music_checkbox)
    show_setting(window, mouse, sound_text, sound_textRect, SCREEN_HEIGHT // 2, sound_scroll_bar, sound_checkbox)

    back_button.show(window, mouse)
    pygame.display.update()


def settings_menu(game_objects):
    settings = game_objects['settings']

    scroll_bar_left_boundary = 393
    scroll_bar_right_boundary = 753
    scroll_bar_range = scroll_bar_right_boundary - scroll_bar_left_boundary

    music_checkbox = Checkbox(SCREEN_WIDTH * 4 // 5,
                              SCREEN_HEIGHT // 3 - CHECKBOX_HEIGHT, settings['music'])
    sound_checkbox = Checkbox(SCREEN_WIDTH * 4 // 5,
                              SCREEN_HEIGHT // 2 - CHECKBOX_HEIGHT, settings['sound'])
    back_button = Button(SCREEN_WIDTH // 2 -
                         (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 6, 'big', 'Back')

    while True:
        mouse = pygame.mouse.get_pos()
        
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                popup(window.copy(), game_objects)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:

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
                
                elif music_scroll_bar.is_pressed(mouse, click):
                    music_scroll_bar.is_dragged = True
                
                elif sound_scroll_bar.is_pressed(mouse, click):
                    sound_scroll_bar.is_dragged = True

                elif back_button.is_pressed(mouse, click):
                    return

            elif event.type == pygame.MOUSEBUTTONUP:
                music_scroll_bar.is_dragged = False
                sound_scroll_bar.is_dragged = False
                music_scroll_bar.clicked = False

            elif event.type == pygame.MOUSEMOTION:
                scroll_bar_movement(music_scroll_bar, mouse, scroll_bar_left_boundary, scroll_bar_right_boundary, scroll_bar_range)

                scroll_bar_movement(sound_scroll_bar, mouse, scroll_bar_left_boundary, scroll_bar_right_boundary, scroll_bar_range)
                if sound_checkbox.is_on:
                    new_volume = float((sound_scroll_bar.x - scroll_bar_left_boundary) / scroll_bar_range)
                    set_all_volumes(SOUNDS.values(), new_volume)

        redraw_settings_menu(mouse, music_checkbox,
                             sound_checkbox, back_button, music_scroll_bar, sound_scroll_bar)


def show_setting(window, mouse, name_text, name_textRect, height, scroll_bar, check_box):
    window.blit(name_text, name_textRect)
    draw_rect_with_alpha(name_textRect[0] + 170, height - 25,
                        SCREEN_WIDTH // 2 - 100, 10, COLORS['white'], 150, window, 5)
    window.blit(max_text, ((name_textRect[0] + SCREEN_WIDTH // 2 + 30, height - 80)))
    window.blit(min_text, (name_textRect[0] + 170, height - 80))
    window.blit(toggle_text, (SCREEN_WIDTH * 4 // 5 - (toggle_text.get_rect()[2] / 4), height - 80))
    scroll_bar.show(window, mouse)
    check_box.show(window, mouse)


def scroll_bar_movement(scroll_bar, mouse, left_boundary, right_boundary, width):
    if scroll_bar.is_dragged:
        if mouse[0] > scroll_bar.x + scroll_bar.width and scroll_bar.x < right_boundary:
            scroll_bar.x += width // 10
        elif mouse[0] < scroll_bar.x and scroll_bar.x > left_boundary:
            scroll_bar.x -= width // 10


def set_all_volumes(all_sounds, new_volume):
    for sound in all_sounds:
        if isinstance(sound, list):
            for inner_sound in sound:
                inner_sound.set_volume(new_volume)
        else:
            sound.set_volume(new_volume)

    