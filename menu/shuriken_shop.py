import pygame
from menu.button import Button
from menu.shop_item import ShopItem
from sys import exit
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, COLORS, FPS, BACKGROUND_DUNGEON, SHURIKEN_IMAGES

pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


shop_title_text = PIXEL_FONT_BIG.render("Shop", True,  COLORS['white'])
shop_textRect = shop_title_text.get_rect()
shop_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6

shurikens_shop = [ShopItem('shuriken', 0, SCREEN_WIDTH // 8, SCREEN_HEIGHT * 2 // 6, SHURIKEN_IMAGES['shuriken']),
                ShopItem('Golden shuriken', 10, SCREEN_WIDTH // 8, SCREEN_HEIGHT * 3 // 6, SHURIKEN_IMAGES['Golden shuriken']),              
                ShopItem('Rainbow shuriken', 50, SCREEN_WIDTH // 8, SCREEN_HEIGHT * 4 // 6, SHURIKEN_IMAGES['Rainbow shuriken']),    
                ShopItem('Orange', 100, SCREEN_WIDTH // 8, SCREEN_HEIGHT * 5 // 6, SHURIKEN_IMAGES['Orange']),
                ShopItem('Tomato', 150, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 6, SHURIKEN_IMAGES['Tomato']),
                ShopItem('Granny', 200, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 6, SHURIKEN_IMAGES['Granny'])]

quit_shuriken_shop_button = Button(
    'Back', SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT * 7 // 8, 'big')


def redraw_shuriken_shop(mouse, player):
    window.blit(BACKGROUND_DUNGEON, (0, 0))

    window.blit(shop_title_text, shop_textRect)

    for shop_item in shurikens_shop:
        shop_item.show(window, mouse, player)

    quit_shuriken_shop_button.show(window, mouse)

    pygame.display.update()


def shuriken_shop(player):
    while True:
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()

                for shuriken in shurikens_shop:
                    if shuriken.name not in player.shurikens_owned:
                        if shuriken.buy_button.is_pressed(mouse, click):
                            player.shurikens_owned.append(shuriken.name)
                            print("bought", shuriken.price)

                for shuriken in shurikens_shop:
                    if shuriken.name != player.shuriken_equipped and shuriken.name in player.shurikens_owned:
                        if shuriken.equip_button.is_pressed(mouse, click):
                            player.shuriken_equipped = shuriken.name

                if quit_shuriken_shop_button.is_pressed(mouse, click):
                    return

        redraw_shuriken_shop(mouse, player)
