import pygame
from hero import player
from enemy import Enemy
from projectile import Shuriken
from background import background
import sys


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 610

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shuriken Man")

clock = pygame.time.Clock()


def player_movement():
    """The main character movement system"""
    keys = pygame.key.get_pressed()

    if player.x < 350 and background.x == 0:
        if keys[pygame.K_LEFT] and player.x > player.velocity:
            player.x -= player.velocity
            player.left = True
            player.right = False
            player.standing = False

        elif keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.velocity - player.width:
            player.x += player.velocity
            player.left = False
            player.right = True
            player.standing = False

        else:
            player.standing = True
            player.walk_count = 0

    elif player.x == 350:
        if background.x == 0:
            if keys[pygame.K_LEFT]:
                player.x -= player.velocity
                player.left = True
                player.right = False
                player.standing = False

            elif keys[pygame.K_RIGHT] and background.x > SCREEN_WIDTH - background.width:
                background.x -= background.velocity
                player.left = False
                player.right = True
                player.standing = False

            else:
                player.standing = True
                player.walk_count = 0

        elif SCREEN_WIDTH - background.width < background.x < 0:
            if keys[pygame.K_LEFT] and background.x < 0:
                background.x += background.velocity
                player.left = True
                player.right = False
                player.standing = False

            elif keys[pygame.K_RIGHT] and background.x > SCREEN_WIDTH - background.width:
                background.x -= background.velocity
                player.left = False
                player.right = True
                player.standing = False

            else:
                player.standing = True
                player.walk_count = 0

        elif background.x == SCREEN_WIDTH - background.width:
            if keys[pygame.K_LEFT] and background.x < 0:
                background.x += background.velocity
                player.left = True
                player.right = False
                player.standing = False

            elif keys[pygame.K_RIGHT] and background.x == SCREEN_WIDTH - background.width:
                player.x += player.velocity
                player.left = False
                player.right = True
                player.standing = False

            else:
                player.standing = True
                player.walk_count = 0

    if player.x > 350 and SCREEN_WIDTH - background.width:
        if keys[pygame.K_LEFT] and player.x > player.velocity:
            player.x -= player.velocity
            player.left = True
            player.right = False
            player.standing = False

        elif keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.velocity - player.width:
            player.x += player.velocity
            player.left = False
            player.right = True
            player.standing = False

        else:
            player.standing = True
            player.walk_count = 0

    if not player.is_jump:
        if keys[pygame.K_UP]:
            player.is_jump = True
            player.walk_count = 0
    else:
        if player.jump_count >= -10:
            player.y -= (player.jump_count * abs(player.jump_count)) * 0.25
            player.jump_count -= 1
        else:
            player.jump_count = 10
            player.is_jump = False


# mainloop
def main():

    def redrawGameWindow():
        background.draw(window)
        player.draw(window)
        goblin.draw(window)
        for shuriken in shurikens:
            shuriken.draw(window)
        pygame.display.update()

    goblin = Enemy(500, 530, 64, 64, 100)
    shurikens = []
    shuriken_shootloop = 0

    # game loop
    while True:
        clock.tick(27)

        if shuriken_shootloop > 0:
            shuriken_shootloop += 1
        if shuriken_shootloop > 3:
            shuriken_shootloop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for shuriken in shurikens:
            if goblin.visible:
                if shuriken.y - shuriken.radius < goblin.hitbox[1] + goblin.hitbox[3] and shuriken.y + shuriken.radius > goblin.hitbox[1]:
                    if shuriken.x + shuriken.radius > goblin.hitbox[0] and shuriken.x - shuriken.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                        goblin.hit()
                        shurikens.pop(shurikens.index(shuriken))

            if shuriken.x < SCREEN_WIDTH and shuriken.x > 0 and shuriken.throw_count != -20:
                if shuriken.throw_count >= -20:
                    shuriken.x += shuriken.velocity
                    shuriken.y -= (shuriken.throw_count *
                                   abs(shuriken.throw_count)) * 0.1
                    shuriken.throw_count -= 1
                else:
                    shuriken.throw_count = 10
            else:
                shurikens.pop(shurikens.index(shuriken))

        keys = pygame.key.get_pressed()

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

        player_movement()

        redrawGameWindow()


if __name__ == "__main__":
    main()
