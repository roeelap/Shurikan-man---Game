import pygame
from consts import *
import sys


pygame.init()
pygame.display.set_caption("Shuriken Man")
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
title_text = PIXEL_FONT_BIG.render("Shuriken Man", True,  COLORS['white'])


def button(x, y, width, height, inactive_image, active_image, window, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        window.blit(active_image, (x, y))
        if click[0] == 1:
            action()
    else:
        window.blit(inactive_image, (x, y))


def redraw_main_menu():
    window.blit(BACKGROUND_DUNGEON, (0, 0))
    window.blit(title_text, (145, 100))
    button(100, 400, 227, 46, NEW_GAME_INACTIVE_BUTTON,
           NEW_GAME_ACTIVE_BUTTON, window, sys.exit)
    button(473, 400, 227, 46, OPTIONS_INACTIVE_BUTTON,
           OPTIONS_ACTIVE_BUTTON, window, sys.exit)
    pygame.display.update()


while True:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    redraw_main_menu()
