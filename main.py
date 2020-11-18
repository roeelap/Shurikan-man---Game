import pygame
from player import player
from enemy import Enemy
from shuriken import Shuriken
from background import background
from player_movement import player_movement
import sys
from consts import *


pygame.init()
pygame.display.set_caption("Shuriken player")
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

shurikens = []
enemies = [Enemy(500, 530, 64, 64, 100, 3, 9)]


def redrawGameWindow():
    background.draw(window)
    player.draw(window)
    for shuriken in shurikens:
        shuriken.draw(window)
    for enemy in enemies:
        if enemy.alive:
            enemy.draw(window)
        else:
            enemies.remove(enemy)
    pygame.display.update()


# mainloop
def main():

    shuriken_shootloop = 0

    # game loop
    while True:
        clock.tick(FPS)

        # Only 3 shurikens allowed
        if shuriken_shootloop > 0:
            shuriken_shootloop += 1
        if shuriken_shootloop > MAX_SHURIKENS:
            shuriken_shootloop = 0

        # Exit on quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check player - enemy collision
        for enemy in enemies:
            if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
                if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                    player.hit()

        # Check shuriken collision
        for shuriken in shurikens:
            for enemy in enemies:
                inbound_x_left = shuriken.x + shuriken.radius > enemy.hitbox[0]
                inbound_x_right = shuriken.x - \
                    shuriken.radius < enemy.hitbox[0] + enemy.hitbox[2]
                inbound_y_up = shuriken.y - \
                    shuriken.radius < enemy.hitbox[1] + enemy.hitbox[3]
                inbound_y_down = shuriken.y + shuriken.radius > enemy.hitbox[1]
                if inbound_x_left and inbound_x_right and inbound_y_up and inbound_y_down:
                    enemy.hit()
                    shurikens.pop(shurikens.index(shuriken))

            # Remove shuriken when out of screen
            if shuriken.x < SCREEN_WIDTH and shuriken.x > 0 and shuriken.throw_count != -20:
                if shuriken.throw_count >= -20:
                    shuriken.x += shuriken.speed
                    shuriken.y -= int((shuriken.throw_count *
                                       abs(shuriken.throw_count)) * 0.1)
                    shuriken.throw_count -= 1
                else:
                    shuriken.throw_count = 10
            else:
                shurikens.pop(shurikens.index(shuriken))

        keys = pygame.key.get_pressed()

        # Jumping on space
        if keys[pygame.K_SPACE] and shuriken_shootloop == 0:
            if player.left:
                facing = -1
            elif player.right:
                facing = 1
            else:
                facing = 1
            if len(shurikens) < 3:
                shurikens.append(Shuriken(
                    round(player.x + player.width // 2), round(player.y + player.height//2), facing))

        player_movement(enemies)
        redrawGameWindow()


if __name__ == "__main__":
    main()
