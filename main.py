import pygame
from player import player
from enemy import Enemy
from shuriken import Shuriken
from background import background
from moving_function import player_movement
import sys


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 610

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shuriken Man")

clock = pygame.time.Clock()


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
