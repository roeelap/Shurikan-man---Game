from sys import exit
import pygame
from menu.button import Button, ArrowButton
from menu.inventory_item import InventoryItem
from static_functions import draw_rect_with_alpha
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, PIXEL_FONT_MID, COLORS, FPS, BACKGROUND_DUNGEON, SHURIKEN_IMAGES, BUTTON_WIDTH_BIG, SOUNDS


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

shurikens_up_button = ArrowButton(
    shurikens_subtitle_textRect[0] - 80, SCREEN_HEIGHT // 2, 'up_arrow')
shurikens_down_button = ArrowButton(
    shurikens_subtitle_textRect[0] - 80, SCREEN_HEIGHT // 2 + 60, 'down_arrow')


quit_inventory_button = Button(
    SCREEN_WIDTH // 2 - BUTTON_WIDTH_BIG / 2, SCREEN_HEIGHT * 7 // 8, 'big', 'Back')


def redraw_inventory(mouse, player, shuriken_inventory):
    window.blit(BACKGROUND_DUNGEON, (-200, 0))
    draw_rect_with_alpha(100, 250, 350, 350, COLORS['white'], 50, window,15)
    pygame.draw.rect(window, COLORS['white'],
                         (100, 250, 350, 350), width=1, border_radius=15)

    window.blit(inventory_title_text, inventory_title_textRect)
    window.blit(shurikens_subtitle_text, shurikens_subtitle_textRect)

    if len(shuriken_inventory) <= 4:
        for shuriken in shuriken_inventory:
            shuriken.show(window, mouse, player)
            shurikens_up_button.disabled = True
            shurikens_down_button.disabled = True
    else:
        for shuriken in shuriken_inventory[0:4]:
            shuriken.show(window, mouse, player)
            shurikens_up_button.disabled = False
            shurikens_down_button.disabled = False

    shurikens_up_button.show(window, mouse)
    shurikens_down_button.show(window, mouse)

    quit_inventory_button.show(window, mouse)

    pygame.display.update()


def inventory(player):
    shuriken_inventory = [InventoryItem(SCREEN_WIDTH // 4, SCREEN_HEIGHT * (player.shurikens_owned.index(
        shuriken) + 3) // 8, shuriken, SHURIKEN_IMAGES[shuriken]) for shuriken in player.shurikens_owned]

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

                if shurikens_up_button.is_pressed(mouse, click):
                    move_items_up(shuriken_inventory)

                elif shurikens_down_button.is_pressed(mouse, click):
                    move_items_down(shuriken_inventory)

                elif quit_inventory_button.is_pressed(mouse, click):
                    return

        redraw_inventory(mouse, player, shuriken_inventory)


def move_items_up(item_list):
    item_list.insert(0, item_list.pop(-1))
    for item in item_list:
        item.update_y_value(SCREEN_HEIGHT * (item_list.index(item) + 3) // 8)


def move_items_down(item_list):
    item_list.append(item_list.pop(0))
    for item in item_list:
        item.update_y_value(SCREEN_HEIGHT * (item_list.index(item) + 3) // 8)
