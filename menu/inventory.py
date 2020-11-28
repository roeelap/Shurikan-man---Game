from sys import exit
import pygame
from menu.button import Button
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, PIXEL_FONT_MID, COLORS, FPS, BACKGROUND_DUNGEON, SHURIKEN_IMAGES, PIXEL_FONT_BIG_BUTTON, BUTTON_WIDTH_BIG, GOLD_COINS_IMAGES, SOUNDS
from menu.inventory_item import InventoryItem

pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

inventory_title_text = PIXEL_FONT_BIG.render(
    "Inventory", True,  COLORS['white'])
inventory_title_textRect = inventory_title_text.get_rect()
inventory_title_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 7

shurikens_subtitle_text = PIXEL_FONT_MID.render(
    "Shurikens", True,  COLORS['white'])
shurikens_subtitle_textRect = shurikens_subtitle_text.get_rect()
shurikens_subtitle_textRect.center = SCREEN_WIDTH // 4, SCREEN_HEIGHT * 2 // 7

quit_inventory_button = Button(
    SCREEN_WIDTH // 3, SCREEN_HEIGHT * 7 // 8, 'big', 'Back')


def redraw_inventory(mouse, player, shuriken_inventory):
    window.blit(BACKGROUND_DUNGEON, (-200, 0))

    window.blit(inventory_title_text, inventory_title_textRect)
    window.blit(shurikens_subtitle_text, shurikens_subtitle_textRect)

    if len(shuriken_inventory) <= 4:
        for shuriken in shuriken_inventory:
            shuriken.show(window, mouse, player)
    else:
        for shuriken in shuriken_inventory[0:3]:
            shuriken.show(window, mouse, player)

    quit_inventory_button.show(window, mouse)

    pygame.display.update()


def inventory(player):
    shuriken_inventory = [InventoryItem(SCREEN_WIDTH // 4, SCREEN_HEIGHT * (player.shurikens_owned.index(
        shuriken) + 3) // 7, shuriken, SHURIKEN_IMAGES[shuriken]) for shuriken in player.shurikens_owned]

    while True:
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()

                for shuriken in shuriken_inventory:
                    if shuriken.name != player.shuriken_equipped:
                        if shuriken.equip_button.is_pressed(mouse, click):
                            shuriken.equip_button.disabled = True
                            SOUNDS['item_equip'].play()
                            player.shuriken_equipped = shuriken.name

                if quit_inventory_button.is_pressed(mouse, click):
                    return

        redraw_inventory(mouse, player, shuriken_inventory)
