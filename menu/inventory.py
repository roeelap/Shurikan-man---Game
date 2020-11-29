from sys import exit
import pygame
from menu.button import Button, ArrowButton
from menu.inventory_item import InventoryItem
from static_functions import draw_rect_with_alpha
from consts import SCREEN_WIDTH, SCREEN_HEIGHT,PIXEL_FONT_SMALL, PIXEL_FONT_BIG, PIXEL_FONT_MID, PIXEL_FONT_BIG_BUTTON, COLORS, FPS, BACKGROUND_DUNGEON, SHURIKEN_IMAGES, BUTTON_WIDTH_BIG, BUTTON_WIDTH_SMALL, ARROW_BUTTON_WIDTH, SOUNDS


pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

inventory_title_text = PIXEL_FONT_BIG.render(
    "Inventory", True,  COLORS['white'])
inventory_title_textRect = inventory_title_text.get_rect()
inventory_title_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 12

shurikens_up_button = ArrowButton(120, 240, 'up_arrow')
shurikens_down_button = ArrowButton(120, 570, 'down_arrow')

quit_inventory_button = Button(
    SCREEN_WIDTH // 2 - BUTTON_WIDTH_BIG / 2, SCREEN_HEIGHT * 7 // 8, 'big', 'Back')


def redraw_inventory_menu(mouse, player, shuriken_inventory, shuriken_equipped):
    window.blit(BACKGROUND_DUNGEON, (-200, 0))

    window.blit(inventory_title_text, inventory_title_textRect)

    draw_inventory_bg('Shurikens', SCREEN_WIDTH // 4 - 30, SCREEN_HEIGHT // 6)
    shurikens_up_button.show(window, mouse)
    shurikens_down_button.show(window, mouse)
    show_shuriken_inventory(
        shuriken_inventory, mouse, player)
    for shuriken in shuriken_inventory:
        if shuriken.name == shuriken_equipped:
            shuriken.show_without_button(SCREEN_WIDTH // 4, SCREEN_HEIGHT * 2 // 9, window)
    
    draw_inventory_bg('Backgrounds', SCREEN_WIDTH * 3 // 4 + 30, SCREEN_HEIGHT // 6)

    quit_inventory_button.show(window, mouse)

    pygame.display.update()


def inventory_menu(player):

    shuriken_inventory = [InventoryItem(0, 0, shuriken, SHURIKEN_IMAGES[shuriken])
                          for shuriken in player.shurikens_owned]
    update_inventory_item_locations(shuriken_inventory, SCREEN_WIDTH // 4)

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
                    if shuriken.equip_button.is_pressed(mouse, click):
                        equip_shuriken(shuriken, player)

                if shurikens_up_button.is_pressed(mouse, click):
                    move_items_down(shuriken_inventory)

                elif shurikens_down_button.is_pressed(mouse, click):
                    move_items_up(shuriken_inventory)

                elif quit_inventory_button.is_pressed(mouse, click):
                    return

        redraw_inventory_menu(
            mouse, player, shuriken_inventory, player.shuriken_equipped)


def equip_shuriken(shuriken, player):
    # changing the equipped shuriken
    player.shuriken_equipped = shuriken.name
    shuriken.equip_button.disabled = True
    SOUNDS['item_equip'].play()


def show_shuriken_inventory(shuriken_inventory, mouse, player):
    if len(shuriken_inventory) <= 3:
        shurikens_up_button.disabled = True
        shurikens_down_button.disabled = True
        for shuriken in shuriken_inventory:
            shuriken.show(window, mouse, player)
            shuriken.is_shown = True

    else:
        shurikens_up_button.disabled = False
        shurikens_down_button.disabled = False
        for shuriken in shuriken_inventory:
            if 227 < shuriken.y < 570:
                shuriken.show(window, mouse, player)
                shuriken.is_shown = True
            else:
                shuriken.is_shown = False

        if shuriken_inventory[0].is_shown:
            shurikens_up_button.disabled = True

        elif shuriken_inventory[-1].is_shown:
            shurikens_down_button.disabled = True


def move_items_up(inventory):
    for item in inventory:
        item.y -= 90
        item.equip_button.update_location(
            item.x - BUTTON_WIDTH_SMALL - 10, item.y)


def move_items_down(inventory):
    for item in inventory:
        item.y += 90
        item.equip_button.update_location(
            item.x - BUTTON_WIDTH_SMALL - 10, item.y)


def update_inventory_item_locations(inventory, x):
    for item in inventory:
        item.update_location(x, SCREEN_HEIGHT *
                             (inventory.index(item) + 3) // 8)


def draw_inventory_bg(subtitle, subtitle_center_x, subtitle_center_y):
    subtitle_text = PIXEL_FONT_MID.render(subtitle, True,  COLORS['white'])
    subtitle_textRect = subtitle_text.get_rect()
    subtitle_textRect.center = subtitle_center_x, subtitle_center_y
    window.blit(subtitle_text, subtitle_textRect)

    draw_rect_with_alpha(subtitle_textRect[0] - 82, subtitle_textRect[1] +
                         subtitle_textRect[3], subtitle_textRect[2] + 173, 470, COLORS['white'], 50, window, 15)
    pygame.draw.rect(window, COLORS['white'], (subtitle_textRect[0] - 82,
                                               subtitle_textRect[1] + subtitle_textRect[3], subtitle_textRect[2] + 173, 470), width=2, border_radius=15)

    equipped_text = PIXEL_FONT_BIG_BUTTON.render(
        'Equipped:', True,  COLORS['white'])
    window.blit(
        equipped_text, (subtitle_textRect[0] - 40, subtitle_textRect[1] + subtitle_textRect[3] + 25))

    pygame.draw.line(window, COLORS['white'], (
        subtitle_textRect[0] - 82, subtitle_textRect[1] + 130), (subtitle_textRect[0] - 82 + subtitle_textRect[2] + 173, subtitle_textRect[1] + 130), width=2)

    pygame.draw.rect(window, COLORS['white'], (subtitle_textRect[0] - 64,
                                               subtitle_textRect[1] + 141, ARROW_BUTTON_WIDTH + 4, 365), width=2)
