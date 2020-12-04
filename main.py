from operator import itemgetter
from random import randint, choice
import pygame
from menu.popup import popup
from menu.start_menu import start_menu
from static_functions import load_game
from round_system import RoundSystem
from player import Player
from enemy import Enemy
from archer import Archer
from shuriken import Shuriken
from health_pack import HealthPack
from background import Background
from player_movement import player_movement
from collision_checks import check_collision
from consts import BACKGROUND_DUNGEON, BOTTOM_BORDER, GOBLIN_HEIGHT, SHURIKEN_IMAGES, SCREEN_HEIGHT, SCREEN_WIDTH, GOBLIN_WIDTH, FPS, \
    GOBLIN_WALK_LEFT_IMAGES, GOBLIN_WALK_RIGHT_IMAGES, ARCHER_WALK_LEFT_IMAGES, ARCHER_WALK_RIGHT_IMAGES, ARCHER_SHOOT_LEFT_IMAGES, \
    ARCHER_SHOOT_RIGHT_IMAGES, SHURIKEN_RADIUS, SOUNDS, TOP_BORDER, HEALTH_PACK_WIDTH, HEALTH_PACK_HEIGHT, SHURIKEN_ENERGY_REQUIRED


def new_game():
    pygame.init()
    pygame.display.set_caption("Shuriken Man")
    pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
    game_objects = {'window': pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)),
                    'shurikens': [],
                    'arrows': [],
                    'background': Background(0, 0, 1650, 610, BACKGROUND_DUNGEON),
                    'enemies': [],
                    'coins': [],
                    'health_packs': [],
                    'player': Player(10, 630),
                    'settings': {'sound': True, 'music': True}}
    return game_objects


def can_spawn_health_pack(spawn_health_pack_timer, health_packs, countdown):
    spawn_health_pack_timer += 1
    if spawn_health_pack_timer == int(countdown * FPS):
        spawn_health_pack(health_packs)
        spawn_health_pack_timer = 0
    return spawn_health_pack_timer


def spawn_health_pack(health_packs):
    random_x = randint(HEALTH_PACK_WIDTH, SCREEN_WIDTH - HEALTH_PACK_WIDTH)
    random_y = randint(TOP_BORDER + HEALTH_PACK_HEIGHT, BOTTOM_BORDER)
    new_health_pack = HealthPack(random_x, random_y)
    SOUNDS['health_pack_spawn'].play()
    health_packs.append(new_health_pack)


def set_settings(settings):
    from menu.settings_menu import set_all_volumes
    volume = 0
    if settings['sound']:
        volume = 1
    set_all_volumes(SOUNDS.values(), volume)


def main():

    game_objects = new_game()

    clock = pygame.time.Clock()
    shuriken_shoot_timer = 0
    spawn_health_pack_timer = 0
    # save_timer = 0

    

    window, background, player, enemies, shurikens, arrows, coins, health_packs, settings = itemgetter(
        'window', 'background', 'player', 'enemies', 'shurikens', 'arrows', 'coins', 'health_packs', 'settings')(game_objects)
    load_game(player, enemies, background, settings)
    set_settings(settings)
    if start_menu(BACKGROUND_DUNGEON, game_objects) == 'new_game':
        game_objects = new_game()
    
    game_round = RoundSystem(player.round)

    def redraw_window():
        background.draw(window)
        objects_to_draw = []
        for shuriken in shurikens:
            objects_to_draw.append(shuriken)
            if not shuriken.is_in_screen(background):
                shurikens.remove(shuriken)
        for arrow in arrows:
            objects_to_draw.append(arrow)
            if not arrow.is_in_screen(background):
                arrows.remove(arrow)
        for enemy in enemies:
            objects_to_draw.append(enemy)
            enemy.auto_path(player.shade, background.width)
            if not enemy.alive:
                enemies.remove(enemy)
                player.score += 1
                game_round.enemies_need_to_kill -= 1
                player.earn_xp(1)
        for coin in coins:
            objects_to_draw.append(coin)
            if coin.stored:
                coins.remove(coin)
        for health_pack in health_packs:
            objects_to_draw.append(health_pack)
            if health_pack.taken:
                health_packs.remove(health_pack)
        objects_to_draw.append(player)
        objects_to_draw.sort(
            key=lambda object: object.shade['y'] + object.shade['h'], reverse=False)
        for object in objects_to_draw:
            object.draw(window)

        player.update_stats()
        player.display_player_stats(window)
        game_round.display_game_round(window)

        pygame.display.update()

    # Game loop
    while True:
        window, background, player, enemies, shurikens, arrows, coins, health_packs, settings = itemgetter(
            'window', 'background', 'player', 'enemies', 'shurikens', 'arrows', 'coins', 'health_packs', 'settings')(game_objects)
        clock.tick(FPS)

        # Save game every second (60 fps)
        # if save_timer == SAVE_TIMEOUT:
        #     save_timer = 0
        #     save_game(player, enemies, background, settings)
        # else:
        #     save_timer += 1

        # spawing enemies in rounds
        game_round.spawn_enemy_if_can(enemies, background, player)

        # Randomely spawn an health pack every 30 seconds
        spawn_health_pack_timer = can_spawn_health_pack(
            spawn_health_pack_timer, health_packs, 30)

        for archer in enemies:
            if isinstance(archer, Archer) and archer.is_shooting and archer.shoot_timer == 11:
                archer.shoot(arrows)
                archer.shoot_timer = -49

        # Exit on quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                popup(window.copy(), game_objects)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SOUNDS['pause'].play()
                    state = start_menu(window.copy(), game_objects, True)
                    if state == 'new_game':
                        game_objects = new_game()

        check_collision(player, enemies, shurikens,
                        arrows, coins, health_packs)

        keys = pygame.key.get_pressed()

        # the shurikens won't be thrown together, the shoot loop needs to be reset before every throw
        if shuriken_shoot_timer > 0:
            shuriken_shoot_timer += 1
        if shuriken_shoot_timer > player.reload_speed:
            shuriken_shoot_timer = 0

        # Throwing shurikens with space-bar. Only 3 shurikens allowed
        player_can_shoot = shuriken_shoot_timer == 0 and len(
            shurikens) < player.max_shurikens and player.energy > SHURIKEN_ENERGY_REQUIRED
        if keys[pygame.K_SPACE] and player_can_shoot:
            shuriken_shoot_timer = 1
            facing = 1
            shuriken_start_x = player.hitbox[0] + player.hitbox[2] - 5
            if player.left:
                facing = -1
                shuriken_start_x = player.hitbox[0] + 5
            player.shoot()
            shurikens.append(Shuriken(shuriken_start_x, round(player.y + player.height / 2),
                                      SHURIKEN_RADIUS, player.throw_speed * facing, player.strength, player.shuriken_durability, player.hitbox[1] + player.hitbox[3], SHURIKEN_IMAGES[player.shuriken_equipped], player.shuriken_equipped))
            choice(SOUNDS['shuriken_throw']).play()
            player.energy -= SHURIKEN_ENERGY_REQUIRED

        # Leave for testing
        if keys[pygame.K_d]:
            game_round.spawn_enemy(enemies, background, player.level)

        if keys[pygame.K_s]:
            enemies.clear()

        if keys[pygame.K_h]:
            spawn_health_pack(health_packs)

        player_movement(player, enemies, coins,
                        health_packs, shurikens, arrows, background)
        redraw_window()

        # if the player dies, the game stops (not a real feature, just to check if things are working properly)
        if player.health <= 0:
            player.health = 0
            SOUNDS['player_death'].play()
            pygame.time.delay(1000)
            game_objects = new_game()


if __name__ == "__main__":
    main()
