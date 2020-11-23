import pygame
from consts import SOUNDS, SCREEN_WIDTH, SCREEN_MIDDLE


def player_movement(player, enemies, shurikens, background):
    """The main character movement system"""

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.speed - player.width:

        if player.x < SCREEN_MIDDLE and background.x == 0 or player.x > SCREEN_MIDDLE and background.x == SCREEN_WIDTH - background.width:
            player.move_right()

        elif player.x == SCREEN_MIDDLE:
            if background.x == 0 or SCREEN_WIDTH - background.width < background.x < 0:
                background.move_left(player)
                for enemy in enemies:
                    enemy.update_path_limits(player.speed, 1)
                    enemy.move(player.speed, 1)
                for shuriken in shurikens:
                    shuriken.x -= player.speed
            elif background.x == SCREEN_WIDTH - background.width:
                player.move_right()

    elif keys[pygame.K_LEFT] and player.x > player.speed:

        if player.x < SCREEN_MIDDLE and background.x == 0 or player.x > SCREEN_MIDDLE and background.x == SCREEN_WIDTH - background.width:
            player.move_left()

        elif player.x == SCREEN_MIDDLE:
            if background.x == 0:
                player.move_left()
            elif background.x == SCREEN_WIDTH - background.width or SCREEN_WIDTH - background.width < background.x < 0:
                background.move_right(player)
                for enemy in enemies:
                    enemy.update_path_limits(player.speed, -1)
                    enemy.move(player.speed, -1)
                for shuriken in shurikens:
                    shuriken.x += player.speed

    else:
        player.standing = True
        player.walk_count = 3

    if not player.jumping:
        if keys[pygame.K_UP]:
            SOUNDS['player_jump'].play()
            player.jumping = True
    else:
        if player.jump_count >= -PLAYER_JUMP_COUNT:
            player.y -= int((player.jump_count *
                             abs(player.jump_count)) * 0.11)
            player.jump_count -= 1/2
        else:
            player.jump_count = PLAYER_JUMP_COUNT
            player.jumping = False
