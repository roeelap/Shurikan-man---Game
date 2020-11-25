import pygame
import sys
from menu.button import Button
from menu.shop_item import ShopItem
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, COLORS, FPS, BACKGROUND_DUNGEON, BUTTON_WIDTH_BIG, SHURIKEN_IMAGES


def equip_item(shop_item_name, shop_item_list):
    for item in shop_item_list:
        if item.is_equipped and item.name != shop_item_name:
            item.is_equipped = False


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['grey_shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

shop_title_text = PIXEL_FONT_BIG.render("Shop", True,  COLORS['white'])
shop_textRect = shop_title_text.get_rect()
shop_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6

shurikens_button = Button('Shurikens', (SCREEN_WIDTH // 2) -
                          (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 2 // 6, 'big')
weapons_button = Button('Special Weapons', (SCREEN_WIDTH // 2) -
                        (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 3 // 6, 'big')
backgrounds_button = Button('Backgrounds', (SCREEN_WIDTH // 2) -
                            (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 4 // 6, 'big')
quit_shop_button = Button('Back', (SCREEN_WIDTH // 2) -
                          (BUTTON_WIDTH_BIG // 2), SCREEN_HEIGHT * 5 // 6, 'big')


def redraw_shop_menu(mouse):
    window.blit(BACKGROUND_DUNGEON, (0, 0))

    window.blit(shop_title_text, shop_textRect)

    shurikens_button.show(window, mouse)
    weapons_button.show(window, mouse)
    backgrounds_button.show(window, mouse)
    quit_shop_button.show(window, mouse)

    pygame.display.update()


def shop_menu():
    shurikens_owned = []
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if shurikens_button.is_pressed(mouse, click):
            shurikens_owned = shuriken_shop()

        elif quit_shop_button.is_pressed(mouse, click):
            return shurikens_owned

        redraw_shop_menu(mouse)


# Shuriken shop
shurikens_shop_items = [ShopItem('Grey shuriken', 0, SCREEN_WIDTH // 8, SCREEN_HEIGHT * 2 // 6, SHURIKEN_IMAGES['grey_shuriken'], True, True),
                        ShopItem('Golden shuriken', 10, SCREEN_WIDTH // 8, SCREEN_HEIGHT *
                                 3 // 6, SHURIKEN_IMAGES['golden_shuriken'], False, False),
                        ShopItem('Rainbow shuriken', 50, SCREEN_WIDTH // 8, SCREEN_HEIGHT *
                                 4 // 6, SHURIKEN_IMAGES['rainbow_shuriken'], False, False),
                        ShopItem('Orange', 100, SCREEN_WIDTH // 8, SCREEN_HEIGHT *
                                 5 // 6, SHURIKEN_IMAGES['orange'], False, False),
                        ShopItem('Tomato', 150, SCREEN_WIDTH // 2, SCREEN_HEIGHT *
                                 2 // 6, SHURIKEN_IMAGES['tomato'], False, False),
                        ShopItem('Granny', 200, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 6, SHURIKEN_IMAGES['grandma'], False, False)]

quit_shuriken_shop_button = Button(
    'Back', SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT * 7 // 8, 'big')


def redraw_shuriken_shop(mouse):
    window.blit(BACKGROUND_DUNGEON, (0, 0))

    window.blit(shop_title_text, shop_textRect)

    for shop_item in shurikens_shop_items:
        shop_item.show(window, mouse)

    quit_shuriken_shop_button.show(window, mouse)

    pygame.display.update()


def shuriken_shop():
    shurikens_owned = []
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for shop_item in shurikens_shop_items:
            if not shop_item.is_owned:
                if shop_item.buy_button.is_pressed(mouse, click):
                    shop_item.is_owned = True
                    shurikens_owned.append(shop_item.name)
                    print("bought", shop_item.price)

        for shop_item in shurikens_shop_items:
            if not shop_item.is_equipped and shop_item.is_owned:
                if shop_item.equip_button.is_pressed(mouse, click):
                    shop_item.is_equipped = True
                    equip_item(shop_item.name, shurikens_shop_items)

        if quit_shuriken_shop_button.is_pressed(mouse, click):
            return shurikens_owned

        redraw_shuriken_shop(mouse)
