from consts import COIN_VALUE, SOUNDS
from operator import itemgetter


def check_player_enemy_collision(player, enemies):
    """Check player-enemy collision, the hurt counter is giving the player time to run away."""
    if player.hurt_counter == 0:
        for enemy in enemies:
            if is_shade_collision(enemy.shade, player.shade):
                player.hit()


def check_shuriken_enemy_collision(shurikens, enemies, coins):
    for shuriken in shurikens:
        for enemy in enemies:
            if is_shade_collision(enemy.shade, shuriken.shade) and not shuriken.has_hit:
                enemy.hit(shuriken.speed, coins)
                shuriken.hit()
                # try:
                #     shurikens.remove(shuriken)
                # except:
                #     pass


def check_player_coin_collision(player, coins):
    for coin in coins:
        if is_shade_collision(player.shade, coin.shade) and not coin.taken:
            SOUNDS['bronze_pickup'].play()
            player.coins += COIN_VALUE[coin.kind]
            coin.taken = True
            coin.set_pickup_delta()


def check_collision(player, enemies, shurikens, coins):
    check_player_enemy_collision(player, enemies)
    check_shuriken_enemy_collision(shurikens, enemies, coins)
    check_player_coin_collision(player, coins)


def is_shade_collision(shade1, shade2):
    x1, y1, w1, h1 = itemgetter('x', 'y', 'w', 'h')(shade1)
    x2, y2, w2, h2 = itemgetter('x', 'y', 'w', 'h')(shade2)
    inbound_x = x1 + w1 > x2 and x1 < x2 + w2
    inbound_y = y1 + h1 > y2 and y1 < y2 + h2
    if inbound_x and inbound_y:
        return True
    return False
