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


def new_game():
    pygame.init()
    pygame.display.set_caption("Shuriken Man")
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shurikens = []
    background = Background(0, 0, 1650, 610, BACKGROUND_DUNGEON)
    enemies = [Enemy(500, 530, 64, 64, Path(500, 100), -3, 9,
                     GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)]
    player = Player(10, 530)
    return window, background, player, enemies, shurikens


# Pilot for random enemy spawning
def spawn_enemy(spawn_enemy_loop, enemies, countdown):
    spawn_enemy_loop += 1
    if spawn_enemy_loop == int(countdown * FPS):
        start = randint(64, 1650-64)
        end = randint(64, 1650-64)
        while (abs(end - start) < 300):
            start = randint(0, 1650)
            end = randint(0, 1650)
        direction = 1
        if start > end:
            direction = -1
        new_enemy = Enemy(start, 530, 64, 64, Path(start, end), 3 * direction, 9,
                          GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)
        print('enemy_spawned')
        enemies.append(new_enemy)
        spawn_enemy_loop = 0
    return spawn_enemy_loop


def main():

    window, background, player, enemies, shurikens = new_game()

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
        spawn_enemy_loop = spawn_enemy(spawn_enemy_loop, enemies, 5)

        # Exit on quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        check_player_enemy_collision(player, enemies)
        check_shuriken_enemy_collision(shurikens, enemies)

        # Remove shuriken when out of screen
        for shuriken in shurikens:
            if not shuriken.throw():
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

        player_movement(player, enemies, background)
        redraw_window()

        # if the player dies, the game stops (not a real feature, just to check if things are working properly)
        if player.health == 0:
            pygame.time.delay(1000)
            window, background, player, enemies, shurikens = new_game()


if __name__ == "__main__":
    main()
