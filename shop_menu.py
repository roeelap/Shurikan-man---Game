import pygame
import sys
from button import Button
from consts import SHURIKEN_IMAGE, SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, COLORS, QUIT_INACTIVE_BUTTON, QUIT_ACTIVE_BUTTON, FPS, BACKGROUND_DUNGEON, SHURIKENS_ACTIVE_BUTTON, SHURIKENS_INACTIVE_BUTTON


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

shurikens_button = Button(280, 250, 227, 46, SHURIKENS_INACTIVE_BUTTON,
                         SHURIKENS_ACTIVE_BUTTON)
quit_shop_button = Button(280, 500, 227, 46, QUIT_INACTIVE_BUTTON,
                         QUIT_ACTIVE_BUTTON)


def redraw_shop_menu(mouse):
    window.blit(BACKGROUND_DUNGEON, (-800, 0))

    shop_title_text = PIXEL_FONT_BIG.render("Shop", True,  COLORS['white'])
    window.blit(shop_title_text, (300, 100))

    shurikens_button.show(window, mouse)

    quit_shop_button.show(window, mouse)

    pygame.display.update()


def shop_menu():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if shurikens_button.is_pressed(mouse, click):
            shuriken_shop()

        elif quit_shop_button.is_pressed(mouse, click):
            break

        redraw_shop_menu(mouse)


# Shuriken shop
quit_shuriken_shop_button = Button(500, 500, 227, 46, QUIT_INACTIVE_BUTTON,
                         QUIT_ACTIVE_BUTTON)

def redraw_shuriken_shop(mouse):
    window.blit(BACKGROUND_DUNGEON, (-800, 0))

    shop_title_text = PIXEL_FONT_BIG.render(
        "Shurikens", True,  COLORS['white'])
    window.blit(shop_title_text, (220, 100))

    quit_shuriken_shop_button.show(window, mouse)

    pygame.display.update()


def shuriken_shop():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if quit_shuriken_shop_button.is_pressed(mouse, click):
            break

        redraw_shuriken_shop(mouse)
