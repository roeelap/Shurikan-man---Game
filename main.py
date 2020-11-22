import pygame
from player import Player
from path import Path
from enemy import Enemy
from shuriken import Shuriken
from background import Background
from player_movement import player_movement
from collision_checks import *
import sys
from random import randint
from consts import *
from start_menu import start_menu


def new_game():
    pygame.init()
    pygame.display.set_caption("Shuriken Man")
    pygame.display.set_icon(SHURIKEN_IMAGE)
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shurikens = []
    background = Background(0, 0, 1650, 610, BACKGROUND_DUNGEON)
    enemies = []
    player = Player(10, 530)
    return window, background, player, enemies, shurikens


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
    new_enemy = Enemy(start, 530, 64, 64, Path(start, end), 3 * direction, 9,
                      GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)
    ENEMY_SPAWN_SOUND.play()
    enemies.append(new_enemy)


def main():

    start_menu()

    window, background, player, enemies, shurikens = new_game()
    spawn_enemy(enemies, player.x, background)

    clock = pygame.time.Clock()
    shuriken_shootloop = 0
    spawn_enemy_loop = 0

    def redraw_window():
        background.draw(window)
        for shuriken in shurikens:
            shuriken.draw(window)
        for enemy in enemies:
            if enemy.alive:
                enemy.auto_path()
                enemy.draw(window)
            else:
                enemies.remove(enemy)
                player.score += 1
        player.display_player_stats(window)
        player.draw(window)
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
                sys.exit()

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
        if keys[pygame.K_SPACE] and shuriken_shootloop == 0:
            shuriken_shootloop = 1
            facing = 1
            if player.left:
                facing = -1
            if len(shurikens) < MAX_SHURIKENS:
                shurikens.append(Shuriken(
                    round(player.x + player.width // 2), round(player.y + player.height//2), 20*facing))
                SHURIKEN_THROW_SOUND.play()

        # Leave for testing
        # if keys[pygame.K_DOWN]:
        #     spawn_enemy(enemies, player.x, background)

        # if keys[pygame.K_s]:
        #     enemies.clear()

        player_movement(player, enemies, background)
        redraw_window()

        # if the player dies, the game stops (not a real feature, just to check if things are working properly)
        if player.health == 0:
            pygame.time.delay(1000)
            window, background, player, enemies, shurikens = new_game()


if __name__ == "__main__":
    main()
