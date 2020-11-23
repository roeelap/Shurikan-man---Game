import pygame
from consts import SHURIKEN_IMAGE, SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, PIXEL_FONT_MID, PIXEL_FONT_BIG, BACKGROUND_DUNGEON, FPS
from button import Button, Checkbox
import sys


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

options_title_text = PIXEL_FONT_BIG.render("Options", True,  COLORS['white'])

music_text = PIXEL_FONT_MID.render("Music", True,  COLORS['white'])

sound_text = PIXEL_FONT_MID.render("Sound", True,  COLORS['white'])

music_checkbox = Checkbox(530, 300)
sound_checkbox = Checkbox(530, 400)
quit_button = Button('Back', 280, 500)


def redraw_options_menu(mouse):
    window.blit(BACKGROUND_DUNGEON, (-300, 0))
    window.blit(options_title_text, (260, 100))
    window.blit(music_text, (200, 300))
    window.blit(sound_text, (200, 400))
    music_checkbox.show(window, mouse)
    sound_checkbox.show(window, mouse)
    quit_button.show(window, mouse)
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
            pass

        elif quit_button.is_pressed(mouse, click):
            break

        redraw_options_menu(mouse)
