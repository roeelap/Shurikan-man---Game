import pygame
from consts import *
import sys


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Options", True,  COLORS['white'])

