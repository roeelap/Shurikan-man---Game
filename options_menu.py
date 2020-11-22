import pygame
from consts import *


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

title_text = PIXEL_FONT_BIG.render("Options", True,  COLORS['white'])

music_text = PIXEL_FONT_MID.render("Music", True,  COLORS['white'])

sound_text = PIXEL_FONT_MID.render("Sound", True,  COLORS['white'])

music_button = Button(100, 300, 227, 46, CHECKBOX_INACTIVE,
                         CHECKBOX_ACTIVE)
sound_button = Button(473, 300, 227, 46, CHECKBOX_INACTIVE,
                         CHECKBOX_ACTIVE)
