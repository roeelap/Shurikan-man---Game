import pygame
from player import Player
from path import Path
from enemy import Enemy
from shuriken import Shuriken
from background import Background
from player_movement import player_movement
from collision_checks import *
from sys import exit
from random import randint
from consts import BACKGROUND_DUNGEON, GOBLIN_HEIGHT, MAX_SHURIKENS, SHURIKEN_IMAGE, SCREEN_HEIGHT, SCREEN_WIDTH, BACKGROUND_DUNGEON, GOBLIN_WIDTH, FPS, \
    GOBLIN_WALK_LEFT_IMAGES, GOBLIN_WALK_RIGHT_IMAGES, SHURIKEN_RADIUS, SHURIKEN_TIMEOUT, SOUNDS
from start_menu import start_menu
from coin import Coin


def new_game():
    pygame.init()
    pygame.display.set_caption("Shuriken Man")
    pygame.display.set_icon(SHURIKEN_IMAGE)
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shurikens = []
    background = Background(0, 0, 1650, 610, BACKGROUND_DUNGEON)
    enemies = []
    coins = []
    player = Player(10, 630)
    return window, background, player, enemies, shurikens, coins


# Pilot for random enemy spawning
def can_spawn_enemy(spawn_enemy_loop, enemies, player_x_pos, countdown, background):
    spawn_enemy_loop += 1
    if spawn_enemy_loop == int(countdown * FPS):
        spawn_enemy(enemies, player_x_pos, background)
        spawn_enemy_loop = 0
    return spawn_enemy_loop


def spawn_enemy(enemies, player_x_pos, background):
    start = background.x + \
        randint(GOBLIN_WIDTH, background.width - GOBLIN_WIDTH)
    end = background.x + randint(GOBLIN_WIDTH, background.width - GOBLIN_WIDTH)
    while (abs(end - start) < 300 or abs(start - player_x_pos) < 100):
        start = background.x + \
            randint(GOBLIN_WIDTH, background.width - GOBLIN_WIDTH)
        end = background.x + \
            randint(GOBLIN_WIDTH, background.width - GOBLIN_WIDTH)
    direction = 1
    if start > end:
        direction = -1
    new_enemy = Enemy(start, 600, GOBLIN_WIDTH, GOBLIN_HEIGHT, Path(start, end), 1.4 * direction, 9,
                      GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)
    SOUNDS['enemy_spawn'].play()
    enemies.append(new_enemy)


def main():

    start_menu()

    window, background, player, enemies, shurikens, coins = new_game()
    spawn_enemy(enemies, player.x, background)

    clock = pygame.time.Clock()
    shuriken_shootloop = 0
    spawn_enemy_loop = 0

    def redraw_window():
        background.draw(window)
        objects_to_draw = []
        for shuriken in shurikens:
            objects_to_draw.append(shuriken)
        for enemy in enemies:
            objects_to_draw.append(enemy)
        for coin in coins:
            objects_to_draw.append(coin)
        objects_to_draw.append(player)
        objects_to_draw.sort(key=lambda object: object.y +
                             object.height, reverse=False)
        for object in objects_to_draw:
            object.draw(window)
            if(type(object) == Enemy):
                if object.alive:
                    object.can_hit = True if player.y - 15 <= object.y <= player.y + 15 else False
                else:
                    enemies.remove(object)
                    coins.append(Coin(object.x, object.y, "bronze"))
                    player.score += 1

        player.display_player_stats(window)
        pygame.display.update()

    # Game loop
    while True:

        clock.tick(FPS)

        # Randomely spawn enemies every 5 seconds
        spawn_enemy_loop = can_spawn_enemy(
            spawn_enemy_loop, enemies,  player.x, 5, background)

        # Exit on quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        check_player_enemy_collision(player, enemies)
        check_shuriken_enemy_collision(shurikens, enemies)

        # Remove shuriken when out of screen
        for shuriken in shurikens:
            if not shuriken.is_in_screen(background):
                try:
                    shurikens.pop(shurikens.index(shuriken))
                except:
                    pass

        keys = pygame.key.get_pressed()

        # the shurikens won't be thrown together, the shoot loop needs to be reset before every throw
        if shuriken_shootloop > 0:
            shuriken_shootloop += 1
        if shuriken_shootloop > SHURIKEN_TIMEOUT:
            shuriken_shootloop = 0

        # Throwing shurikens with space-bar. Only 3 shurikens allowed
        if keys[pygame.K_SPACE] and shuriken_shootloop == 0 and len(shurikens) < MAX_SHURIKENS:
            shuriken_shootloop = 1
            facing = 1
            shuriken_start_x = player.hitbox[0] + player.hitbox[2] - 5
            if player.left:
                facing = -1
                shuriken_start_x = player.hitbox[0] + 5
            shurikens.append(Shuriken(
                shuriken_start_x, round(player.y + player.height / 2), SHURIKEN_RADIUS, player.throw_speed * facing, player.hitbox[1] + player.hitbox[3]))
            SOUNDS['shuriken_throw'].play()

        # Leave for testing
        # if keys[pygame.K_DOWN]:
        #     spawn_enemy(enemies, player.x, background)

        # if keys[pygame.K_s]:
        #     enemies.clear()

        player_movement(player, enemies, coins, shurikens, background)
        redraw_window()

        # if the player dies, the game stops (not a real feature, just to check if things are working properly)
        if player.health == 0:
            pygame.time.delay(1000)
            window, background, player, enemies, shurikens, coins = new_game()


if __name__ == "__main__":
    main()
