from static_functions import is_shade_collision
from consts import SOUNDS


def check_player_enemy_collision(player, enemies):
    """Check player-enemy collision, the hurt counter is giving the player time to run away."""
    if player.hurt_counter == 0:
        for enemy in enemies:
            if is_shade_collision(enemy.shade, player.shade):
                player.hit()


def check_shuriken_enemy_collision(shurikens, enemies):
    for shuriken in shurikens:
        for enemy in enemies:
            if is_shade_collision(enemy.shade, shuriken.shade):
                enemy.hit(shuriken.speed)
                try:
                    shurikens.pop(shurikens.index(shuriken))
                except:
                    pass


def check_player_coin_collision(player, coins):
    for coin in coins:
        if is_shade_collision(player.shade, coin.shade):
            try:
                player.coins += 1
                coins.pop(coins.index(coin))
                SOUNDS['coin_pickup'].play()
            except:
                pass
