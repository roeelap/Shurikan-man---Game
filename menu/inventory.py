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
shurikens_subtitle_textRect.center = SCREEN_WIDTH // 4 - 30, SCREEN_HEIGHT * 2 // 7

shurikens_up_button = ArrowButton(120, 342, 'up_arrow')
shurikens_down_button = ArrowButton(120, 569, 'down_arrow')


quit_inventory_button = Button(
    SCREEN_WIDTH // 2 - BUTTON_WIDTH_BIG / 2, SCREEN_HEIGHT * 7 // 8, 'big', 'Back')


def redraw_inventory(mouse, player, shuriken_inventory, shuriken_equipped):
    window.blit(BACKGROUND_DUNGEON, (-200, 0))

    window.blit(inventory_title_text, inventory_title_textRect)
    window.blit(shurikens_subtitle_text, shurikens_subtitle_textRect)
    draw_rect_with_alpha(100, 250, 350, 350, COLORS['white'], 50, window,15)
    pygame.draw.rect(window, COLORS['white'],(100, 250, 350, 350), width=2, border_radius=15)
    pygame.draw.line(window, COLORS['white'], (100, 340), (449, 340), width=2)

    show_shuriken_inventory(shuriken_inventory, shuriken_equipped, window, mouse, player)

    shurikens_up_button.show(window, mouse)
    shurikens_down_button.show(window, mouse)

    quit_inventory_button.show(window, mouse)

    pygame.display.update()


def inventory(player):

    shuriken_inventory = [InventoryItem(0, 0, shuriken, SHURIKEN_IMAGES[shuriken]) for shuriken in player.shurikens_owned if shuriken != player.shuriken_equipped]
    update_inventory_item_locations(shuriken_inventory, SCREEN_WIDTH // 4)

    shuriken_equipped = InventoryItem(SCREEN_WIDTH // 4, SCREEN_HEIGHT * 3 // 8, player.shuriken_equipped, SHURIKEN_IMAGES[player.shuriken_equipped])

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
                        shuriken_equipped = equip_shuriken(shuriken, shuriken_inventory, shuriken_equipped, player)
                            
                if shurikens_up_button.is_pressed(mouse, click):
                    move_items_up(shuriken_inventory)

                elif shurikens_down_button.is_pressed(mouse, click):
                    move_items_down(shuriken_inventory)

                elif quit_inventory_button.is_pressed(mouse, click):
                    return

        redraw_inventory(mouse, player, shuriken_inventory, shuriken_equipped)


def equip_shuriken(shuriken, shuriken_inventory, previous_shuriken, player):
    #returning the previous shuriken to the inventory
    shuriken_inventory.append(previous_shuriken)
    update_inventory_item_locations(shuriken_inventory, SCREEN_WIDTH // 4)
    
    # changing the equipped shuriken
    shuriken_equipped = shuriken_inventory.pop(shuriken_inventory.index(shuriken))
    update_inventory_item_locations(shuriken_inventory, SCREEN_WIDTH // 4)
    shuriken_equipped.update_location(SCREEN_WIDTH // 4, SCREEN_HEIGHT * 3 // 8)
    player.shuriken_equipped = shuriken.name
    
    shuriken.equip_button.disabled = True
    SOUNDS['item_equip'].play()

    return shuriken_equipped


def show_shuriken_inventory(shuriken_inventory, shuriken_equipped, window, mouse, player):
    shuriken_equipped.show(window, mouse, player)

    if len(shuriken_inventory) <= 3:
        shurikens_up_button.disabled = True
        shurikens_down_button.disabled = True
        for shuriken in shuriken_inventory:
            shuriken.show(window, mouse, player)
            
    else:
        shurikens_up_button.disabled = False
        shurikens_down_button.disabled = False
        for shuriken in shuriken_inventory[0:3]:
            shuriken.show(window, mouse, player)
            

def move_items_up(inventory):
    inventory.insert(0, inventory.pop(-1))
    update_inventory_item_locations(inventory, SCREEN_WIDTH // 4)
    

def move_items_down(inventory):
    inventory.append(inventory.pop(0))
    update_inventory_item_locations(inventory, SCREEN_WIDTH // 4)


def update_inventory_item_locations(inventory, x):
    for item in inventory:
        item.update_location(x, SCREEN_HEIGHT * (inventory.index(item) + 4) // 8)

