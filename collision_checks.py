def check_player_enemy_collision(player, enemies):
    """Check player-enemy collision, the hurt counter is giving the player time to run away."""
    if player.hurt_counter == 0:
        for enemy in enemies:
            if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
                if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                    player.hit()


def check_shuriken_enemy_collision(shurikens, enemies):
    for shuriken in shurikens:
        for enemy in enemies:
            inbound_x_left = shuriken.x + shuriken.radius > enemy.hitbox[0]
            inbound_x_right = shuriken.x - \
                shuriken.radius < enemy.hitbox[0] + enemy.hitbox[2]
            inbound_y_up = shuriken.y - \
                shuriken.radius < enemy.hitbox[1] + enemy.hitbox[3]
            inbound_y_down = shuriken.y + shuriken.radius > enemy.hitbox[1]
            if inbound_x_left and inbound_x_right and inbound_y_up and inbound_y_down:
                enemy.hit(shuriken.speed)
                try:
                    shurikens.pop(shurikens.index(shuriken))
                except:
                    pass
