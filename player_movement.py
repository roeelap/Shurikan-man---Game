import pygame
from consts import BOTTOM_BORDER, SCREEN_WIDTH, SCREEN_MIDDLE, TOP_BORDER


def player_movement(player, enemies, coins, health_packs, shurikens, background):
    """The main character movement system"""

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.speed:
        if player.x > SCREEN_MIDDLE:
            player.move_left()
        elif background.x > -player.speed:
            background.x = 0
            player.move_left()
        else:
            background.move_right(player)
            for enemy in enemies:
                enemy.move(player.speed, -1)
            for coin in coins:
                coin.move(player.speed, -1)
            for health_pack in health_packs:
                health_pack.move(player.speed, -1)
            for shuriken in shurikens:
                shuriken.x += player.speed

    elif keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.speed - player.width:
        if player.x < SCREEN_MIDDLE:
            player.move_right()
        elif background.x < SCREEN_WIDTH - background.width + player.speed:
            background.x = SCREEN_WIDTH - background.width
            player.move_right()
        else:
            background.move_left(player)
            for enemy in enemies:
                enemy.move(player.speed, 1)
            for coin in coins:
                coin.move(player.speed, 1)
            for health_pack in health_packs:
                health_pack.move(player.speed, 1)
            for shuriken in shurikens:
                shuriken.x -= player.speed

    else:
        player.standing = True

    if keys[pygame.K_UP] and player.y > TOP_BORDER:
        player.move_up()

    elif keys[pygame.K_DOWN] and player.y < BOTTOM_BORDER:
        player.move_down()
