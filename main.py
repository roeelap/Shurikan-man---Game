from sys import exit
from random import randint, choice
import pygame
from static_functions import load_game, save_game
from player import Player
from enemy import Enemy
from shuriken import Shuriken
from background import Background
from player_movement import player_movement
from collision_checks import check_collision
from consts import BACKGROUND_DUNGEON, BOTTOM_BORDER, GOBLIN_HEIGHT, SAVE_TIMEOUT, SHURIKEN_IMAGES, SCREEN_HEIGHT, SCREEN_WIDTH, GOBLIN_WIDTH, FPS, \
    GOBLIN_WALK_LEFT_IMAGES, GOBLIN_WALK_RIGHT_IMAGES, SHURIKEN_RADIUS, SOUNDS, TOP_BORDER
from menu.start_menu import start_menu


def new_game():
    pygame.init()
    pygame.display.set_caption("Shuriken Man")
    pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shurikens = []
    background = Background(0, 0, 1650, 610, BACKGROUND_DUNGEON)
    enemies = []
    coins = []
    player = Player(10, 630)
    return window, background, player, enemies, shurikens, coins


# Pilot for random enemy spawning
def can_spawn_enemy(spawn_enemy_timer, enemies, countdown, background):
    spawn_enemy_timer += 1
    if spawn_enemy_timer == int(countdown * FPS):
        spawn_enemy(enemies, background)
        spawn_enemy_timer = 0
    return spawn_enemy_timer


def spawn_enemy(enemies, background):
    start_x = background.x + \
        randint(background.width-300, background.width - GOBLIN_WIDTH)
    start_y = randint(TOP_BORDER, BOTTOM_BORDER)
    direction = -1
    new_enemy = Enemy(start_x, start_y, GOBLIN_WIDTH, GOBLIN_HEIGHT, 1.4 * direction, 9, 10,
                      GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)
    SOUNDS['enemy_spawn'].play()
    enemies.append(new_enemy)


def main():

    window, background, player, enemies, shurikens, coins = new_game()
    # enemies.append(Enemy(500, 600, GOBLIN_WIDTH, GOBLIN_HEIGHT, -1.4, 9,
    #                      GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES))

    clock = pygame.time.Clock()
    shuriken_shoot_timer = 0
    spawn_enemy_timer = 0
    save_timer = 0

    load_game(player, enemies, background)
    start_menu(BACKGROUND_DUNGEON, player, enemies, background)

    def redraw_window():
        background.draw(window)
        objects_to_draw = []
        for shuriken in shurikens:
            objects_to_draw.append(shuriken)
            if not shuriken.is_in_screen(background):
                shurikens.remove(shuriken)
        for enemy in enemies:
            objects_to_draw.append(enemy)
            enemy.auto_path(player.shade, background.width)
            if not enemy.alive:
                enemies.remove(enemy)
                player.score += 1
                player.earn_xp(1)
        for coin in coins:
            objects_to_draw.append(coin)
            if coin.stored:
                coins.remove(coin)
        objects_to_draw.append(player)
        objects_to_draw.sort(
            key=lambda object: object.shade['y'] + object.shade['h'], reverse=False)
        for object in objects_to_draw:
            object.draw(window)

        player.update_stats()
        player.display_player_stats(window)

        pygame.display.update()

    # Game loop
    while True:
        clock.tick(FPS)

        # Save game every second (60 fps)
        if save_timer == SAVE_TIMEOUT:
            save_timer = 0
            save_game(player, enemies, background)
        else:
            save_timer += 1

        # Randomely spawn enemies every 5 seconds
        spawn_enemy_timer = can_spawn_enemy(
            spawn_enemy_timer, enemies, 5, background)

        # Exit on quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SOUNDS['pause'].play()
                    win_at_the_moment = window.copy()
                    start_menu(win_at_the_moment, player,
                               enemies, background, True)

        check_collision(player, enemies, shurikens, coins)

        keys = pygame.key.get_pressed()

        # the shurikens won't be thrown together, the shoot loop needs to be reset before every throw
        if shuriken_shoot_timer > 0:
            shuriken_shoot_timer += 1
        if shuriken_shoot_timer > player.reload_speed:
            shuriken_shoot_timer = 0

        # Throwing shurikens with space-bar. Only 3 shurikens allowed
        if keys[pygame.K_SPACE] and shuriken_shoot_timer == 0 and len(shurikens) < player.max_shurikens:
            shuriken_shoot_timer = 1
            facing = 1
            shuriken_start_x = player.hitbox[0] + player.hitbox[2] - 5
            if player.left:
                facing = -1
                shuriken_start_x = player.hitbox[0] + 5
            shurikens.append(Shuriken(shuriken_start_x, round(player.y + player.height / 2),
                                      SHURIKEN_RADIUS, player.throw_speed * facing, player.strength, player.shuriken_durability, player.hitbox[1] + player.hitbox[3], SHURIKEN_IMAGES[player.shuriken_equipped], player.shuriken_equipped))
            choice(SOUNDS['shuriken_throw']).play()

        # Leave for testing
        if keys[pygame.K_d]:
            spawn_enemy(enemies, background)

        if keys[pygame.K_s]:
            enemies.clear()

        player_movement(player, enemies, coins, shurikens, background)
        redraw_window()

        # if the player dies, the game stops (not a real feature, just to check if things are working properly)
        if player.health == 0:
            SOUNDS['player_death'].play()
            pygame.time.delay(1000)
            window, background, player, enemies, shurikens, coins = new_game()


if __name__ == "__main__":
    main()
