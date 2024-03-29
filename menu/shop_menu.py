import pygame
from menu.popup import popup
from menu.button import Button
from menu.shuriken_shop import shuriken_shop
from menu.inventory import inventory_menu
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, COLORS, FPS, BACKGROUND_DUNGEON, BUTTON_WIDTH_BIG, SHURIKEN_IMAGES

pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

shop_title_text = PIXEL_FONT_BIG.render("Shop", True,  COLORS['white'])
shop_textRect = shop_title_text.get_rect()
shop_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 7

shurikens_button = Button((SCREEN_WIDTH // 2) -
                          (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 2 // 6, 'big', 'Shurikens')
backgrounds_button = Button((SCREEN_WIDTH // 2) -
                            (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 3 // 6, 'big', 'Backgrounds')
inventory_button = Button((SCREEN_WIDTH // 2) -
                          (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 4 // 6, 'big', 'Inventory')
quit_shop_button = Button((SCREEN_WIDTH // 2) -
                          (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 6, 'big', 'Back')


def redraw_shop_menu(mouse):
    window.blit(BACKGROUND_DUNGEON, (0, 0))

    window.blit(shop_title_text, shop_textRect)

    shurikens_button.show(window, mouse)
    backgrounds_button.show(window, mouse)
    inventory_button.show(window, mouse)
    quit_shop_button.show(window, mouse)

    pygame.display.update()


def shop_menu(game_objects):
    while True:
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                popup(window.copy(), game_objects)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()

                if shurikens_button.is_pressed(mouse, click):
                    shuriken_shop(game_objects)

                elif inventory_button.is_pressed(mouse, click):
                    inventory_menu(game_objects)

                elif quit_shop_button.is_pressed(mouse, click):
                    return

        redraw_shop_menu(mouse)
