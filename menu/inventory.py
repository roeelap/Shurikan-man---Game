from sys import exit
import pygame
from menu.button import Button, ArrowButton, ScrollBar
from menu.inventory_item import InventoryItem
from static_functions import draw_rect_with_alpha
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_FONT_BIG, PIXEL_FONT_MID, PIXEL_FONT_BIG_BUTTON, COLORS, FPS, BACKGROUND_DUNGEON, SHURIKEN_IMAGES, BUTTON_WIDTH_BIG, BUTTON_WIDTH_SMALL, ARROW_BUTTON_WIDTH, SOUNDS


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

backgrounds_up_button = ArrowButton(747, 240, 'up_arrow')
backgrounds_down_button = ArrowButton(747, 570, 'down_arrow')

quit_inventory_button = Button(
    SCREEN_WIDTH // 2 - BUTTON_WIDTH_BIG / 2, SCREEN_HEIGHT * 7 // 8, 'big', 'Back')


def redraw_inventory_menu(mouse, player, shuriken_inventory, shuriken_equipped, shuriken_scroll_bar):
    window.blit(BACKGROUND_DUNGEON, (-200, 0))
    window.blit(inventory_title_text, inventory_title_textRect)

    draw_inventory_bg('Shurikens', SCREEN_WIDTH // 4 - 30, SCREEN_HEIGHT // 6)
    shurikens_up_button.show(window, mouse)
    shurikens_down_button.show(window, mouse)
    shuriken_scroll_bar.show(window, mouse)
    show_shuriken_inventory(shuriken_inventory, mouse, player)
    show_equipped_shuriken(shuriken_inventory, shuriken_equipped)

    draw_inventory_bg('Backgrounds', SCREEN_WIDTH *
                      3 // 4 + 30, SCREEN_HEIGHT // 6)
    backgrounds_up_button.show(window, mouse)
    backgrounds_down_button.show(window, mouse)

    quit_inventory_button.show(window, mouse)

    pygame.display.update()


def inventory_menu(game_objects):
    player = game_objects['player']

    shuriken_inventory_rect = (100, 143, 350, 470)
    shuriken_inventory, shuriken_scroll_bar = get_inventory('shuriken', player.shurikens_owned, SCREEN_WIDTH // 4, SHURIKEN_IMAGES)

    # backgrounds_inventory, backgrounds_scroll_bar = get_inventory('background', player.backgrounds_owned, SCREEN_WIDTH * 3 // 4, BACKGROUND_IMAGES)

    while True:
        mouse = pygame.mouse.get_pos()
        mouse_in_shuriken_inventory = shuriken_inventory_rect[0] < mouse[0] < shuriken_inventory_rect[0] + shuriken_inventory_rect[2]\
            and shuriken_inventory_rect[1] < mouse[1] < shuriken_inventory_rect[1] + shuriken_inventory_rect[3]

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()
                for shuriken in shuriken_inventory:
                    if shuriken.equip_button.is_pressed(mouse, click):
                        equip_shuriken(shuriken, player)

                if shurikens_up_button.is_pressed(mouse, click):
                    move_items_down(shuriken_inventory)
                    shuriken_scroll_bar.y -= 300 * 1 / len(shuriken_inventory)

                elif shurikens_down_button.is_pressed(mouse, click):
                    move_items_up(shuriken_inventory)
                    shuriken_scroll_bar.y += 300 * 1 / len(shuriken_inventory)

                elif shuriken_scroll_bar.is_pressed(mouse, click):
                    shuriken_scroll_bar.is_dragged = True

                if event.button == 4 and mouse_in_shuriken_inventory:
                    shuriken_scroll_bar.is_dragged = True
                    scroll_wheel_movement(
                        shuriken_scroll_bar, shurikens_up_button, shurikens_down_button, shuriken_inventory, 'up')

                elif event.button == 5 and mouse_in_shuriken_inventory:
                    shuriken_scroll_bar.is_dragged = True
                    scroll_wheel_movement(
                        shuriken_scroll_bar, shurikens_up_button, shurikens_down_button, shuriken_inventory, 'down')

                elif quit_inventory_button.is_pressed(mouse, click):
                    return

            elif event.type == pygame.MOUSEBUTTONUP:
                shuriken_scroll_bar.is_dragged = False
                shuriken_scroll_bar.clicked = False

            elif event.type == pygame.MOUSEMOTION:
                scroll_bar_movement(
                    shuriken_scroll_bar, mouse, shurikens_up_button, shurikens_down_button, shuriken_inventory)

        redraw_inventory_menu(
            mouse, player, shuriken_inventory, player.shuriken_equipped, shuriken_scroll_bar)


def get_inventory(item, items_owned, items_x, images_dict):
    inventory = [InventoryItem(items_x, SCREEN_HEIGHT * (items_owned.index(item) + 3) // 8,
                                        item, images_dict[item]) for item in items_owned]
    if len(inventory) > 4:
        scroll_bar = ScrollBar(
            items_x - 180, 270, 30, 300 * 4 / len(inventory), COLORS['white'])
    else:
        scroll_bar = ScrollBar(items_x - 180, 270, 30, 300, COLORS['white'])
    return inventory, scroll_bar


def equip_shuriken(shuriken, player):
    # changing the equipped shuriken
    player.shuriken_equipped = shuriken.name
    shuriken.equip_button.disabled = True
    SOUNDS['item_equip'].play()


def show_equipped_shuriken(shuriken_inventory, shuriken_equipped):
    for shuriken in shuriken_inventory:
        if shuriken.name == shuriken_equipped:
            shuriken.show_without_button(
                SCREEN_WIDTH // 4, SCREEN_HEIGHT * 2 // 9, window)


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


def scroll_bar_movement(scroll_bar, mouse, up_button, down_button, inventory):
    if scroll_bar.is_dragged:
        if mouse[1] > scroll_bar.y + scroll_bar.height * 3 / 4 and scroll_bar.y + scroll_bar.height < down_button.y:
            scroll_bar.y += 300 * 1 / len(inventory)
            move_items_up(inventory)
        elif mouse[1] < scroll_bar.y + scroll_bar.height / 4 and scroll_bar.y > shurikens_up_button.y + up_button.height:
            scroll_bar.y -= 300 * 1 / len(inventory)
            move_items_down(inventory)


def scroll_wheel_movement(scroll_bar, up_button, down_button, inventory, direction):
    if scroll_bar.is_dragged:
        if direction == 'down' and scroll_bar.y + scroll_bar.height < down_button.y:
            scroll_bar.y += 300 * 1 / len(inventory)
            move_items_up(inventory)
        elif direction == 'up' and scroll_bar.y > shurikens_up_button.y + up_button.height:
            scroll_bar.y -= 300 * 1 / len(inventory)
            move_items_down(inventory)


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
