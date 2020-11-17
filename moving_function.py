import pygame
from player import player
from background import background
from consts import *


def player_movement():
    """The main character movement system"""

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.speed - player.width:

        if player.x < 350 and background.x == 0 or player.x > 350 and background.x == SCREEN_WIDTH - background.width:
            player.move_right()

        elif player.x == 350:
            if background.x == 0 or SCREEN_WIDTH - background.width < background.x < 0:
                background.move_left()
            elif background.x == SCREEN_WIDTH - background.width:
                player.move_right()

    elif keys[pygame.K_LEFT] and player.x > player.speed:

        if player.x < 350 and background.x == 0 or player.x > 350 and background.x == SCREEN_WIDTH - background.width:
            player.move_left()

        elif player.x == 350:
            if background.x == 0:
                player.move_left()
            elif background.x == SCREEN_WIDTH - background.width:
                background.move_right()
            elif SCREEN_WIDTH - background.width < background.x < 0:
                background.move_right()

    else:
        player.standing = True
        player.walk_count = 3

    if not player.jumping:
        if keys[pygame.K_UP]:
            player.jumping = True
            player.walk_count = 3  # Why this line?
    else:
        if player.jump_count >= -10:
            player.y -= int((player.jump_count *
                             abs(player.jump_count)) * 0.25)
            player.jump_count -= 1
        else:
            player.jump_count = 10
            player.jumping = False
