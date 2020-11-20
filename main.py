import pygame
from player import Player
from path import Path
from enemy import Enemy
from shuriken import Shuriken
from background import Background
from player_movement import player_movement
from collision_checks import *
import sys
from consts import *


def new_game():
    pygame.init()
    pygame.display.set_caption("Shuriken player")
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shurikens = []
    background = Background(0, 0, 1650, 610, BACKGROUND_DUNGEON)
    enemies = [Enemy(500, 530, 64, 64, Path(500, 100), -3, 9,
                     GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)]
    player = Player(10, 530)
    return window, background, player, enemies, shurikens


# mainloop
def main():

    window, background, player, enemies, shurikens = new_game()

    clock = pygame.time.Clock()
    shuriken_shootloop = 0

    def redrawGameWindow():
        background.draw(window)
        for shuriken in shurikens:
            shuriken.draw(window)
        for enemy in enemies:
            if enemy.alive:
                enemy.auto_path()
                enemy.draw(window)
            else:
                enemies.remove(enemy)
        player.display_health_status(window)
        player.draw(window)
        pygame.display.update()

    # game loop
    while True:

        clock.tick(FPS)

        # Exit on quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check player-enemy collision, the detector is giving the player time to run away.
        check_player_enemy_collision(player, enemies)

        # Check shuriken - enemy collision
        check_shuriken_enemy_collision(shurikens, enemies)

        # Remove shuriken when out of screen
        for shuriken in shurikens:
            if shuriken.x < SCREEN_WIDTH and shuriken.x > 0 and shuriken.throw_count != -20:
                if shuriken.throw_count >= -20:
                    shuriken.x += shuriken.speed
                    shuriken.y -= int((shuriken.throw_count *
                                       abs(shuriken.throw_count)) * 0.1)
                    shuriken.throw_count -= 1
                else:
                    shuriken.throw_count = 10
            else:
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

        player_movement(player, enemies, background)
        redrawGameWindow()

        # if the player dies, the game stops (not a real feature, just to check if things are working properly)
        if player.health == 0:
            window, background, player, enemies, shurikens = new_game()


if __name__ == "__main__":
    main()
