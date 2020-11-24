import pygame
import sys
from menu.button import Button
from menu.shop_item import ShopItem
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, COLORS, FPS, BACKGROUND_DUNGEON, BUTTON_WIDTH, SHURIKEN_IMAGE, ORANGE_IMAGE


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

shop_title_text = PIXEL_FONT_BIG.render("Shop", True,  COLORS['white'])
shop_textRect = shop_title_text.get_rect()
shop_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6

shurikens_button = Button('Shurikens', (SCREEN_WIDTH // 2) - (BUTTON_WIDTH // 2), SCREEN_HEIGHT * 2// 6)
weapons_button = Button('Special Weapons', (SCREEN_WIDTH // 2) - (BUTTON_WIDTH // 2), SCREEN_HEIGHT * 3// 6)
backgrounds_button = Button('Backgrounds', (SCREEN_WIDTH // 2) - (BUTTON_WIDTH // 2), SCREEN_HEIGHT * 4// 6)
quit_shop_button = Button('Back', (SCREEN_WIDTH // 2) - (BUTTON_WIDTH // 2), SCREEN_HEIGHT * 5// 6)


def redraw_shop_menu(mouse):
    window.blit(BACKGROUND_DUNGEON, (0, 0))

    window.blit(shop_title_text, shop_textRect)

    shurikens_button.show(window, mouse)
    weapons_button.show(window, mouse)
    backgrounds_button.show(window, mouse)
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
shurikens_shop_items = [ShopItem('Grey shuriken', 0, SCREEN_WIDTH // 8, SCREEN_HEIGHT * 2 // 6, SHURIKEN_IMAGE, True), ShopItem('Orange', 10, SCREEN_WIDTH // 8, SCREEN_HEIGHT * 3 // 6, ORANGE_IMAGE, False) ]
buy_button = Button('Buy', SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT * 6 // 8)
quit_shuriken_shop_button = Button('Back', SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT * 7 // 8)

def redraw_shuriken_shop(mouse):
    window.blit(BACKGROUND_DUNGEON, (0, 0))

    window.blit(shop_title_text, shop_textRect)

    for shop_item in shurikens_shop_items:
        shop_item.show(window, mouse)
    
    buy_button.show(window, mouse)
    quit_shuriken_shop_button.show(window, mouse)

    pygame.display.update()


def shuriken_shop():
    total_price = 0

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        for shop_item in shurikens_shop_items:
            if shop_item.checkbox is not None:
                if shop_item.checkbox.is_pressed(mouse, click):
                    pass

        if buy_button.is_pressed(mouse,click):
            for shop_item in shurikens_shop_items:
                if shop_item.checkbox is not None:
                    if shop_item.checkbox.is_on:
                        shop_item.is_owned = True
                        total_price += shop_item.price
            print(total_price, 'bought')

            total_price = 0
            break

        elif quit_shuriken_shop_button.is_pressed(mouse, click):
            break

        redraw_shuriken_shop(mouse)
