import pygame
from player import player
from background import background


def player_movement():
    """The main character movement system"""
    SCREEN_WIDTH = 800

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.velocity - player.width:

        if player.x < 350 and background.x == 0 or player.x > 350 and background.x == SCREEN_WIDTH - background.width:
            player.move_right()

        elif player.x == 350:
            if background.x == 0 or SCREEN_WIDTH - background.width < background.x < 0:
                background.move_left()
            elif background.x == SCREEN_WIDTH - background.width:
                player.move_right()

    elif keys[pygame.K_LEFT] and player.x > player.velocity:

        if player.x < 350 and background.x == 0 or player.x > 350 and background.x == SCREEN_WIDTH - background.width:
            player.move_left()

        elif player.x == 350:
            if background.x == 0 or SCREEN_WIDTH - background.width < background.x < 0:
                background.move_right()
            elif background.x == SCREEN_WIDTH - background.width:
                player.move_left()

    else:
        player.standing = True
        player.walk_count = 3

    if not player.is_jump:
        if keys[pygame.K_UP]:
            player.is_jump = True
            player.walk_count = 3  # Why this line?
    else:
        if player.jump_count >= -10:
            player.y -= (player.jump_count * abs(player.jump_count)) * 0.25
            player.jump_count -= 1
        else:
            player.jump_count = 10
            player.is_jump = False
