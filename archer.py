from random import choice
from operator import itemgetter
import pygame
from enemy import Enemy
from shuriken import Arrow
from consts import COLORS, SOUNDS, ENEMY_SPAWN_IMAGE, ARROW_IMAGES, ARROW_HEIGHT, ARROW_WIDTH


class Archer(Enemy):

    def __init__(self, x, y, width, height, speed, health, damage, walk_right_images, walk_left_images, shoot_right_images, shoot_left_images):
        Enemy.__init__(self, x, y, width, height, speed, health,
                       damage, walk_right_images, walk_left_images)
        self.shoot_right_images = shoot_right_images
        self.shoot_left_images = shoot_left_images

        self.shade = {'x': self.x + self.width / 2,
                      'y': self.hitbox[1] + self.hitbox[3], 'w': 38, 'h': 12}

        self.shoot_timer = 0
        self.is_shooting = False

    def draw(self, window):
        if not self.alive:
            return

        if self.shoot_timer > 12:
            self.shoot_timer = 0

        if self.is_shooting:
            self.shoot_timer += 1
            image_to_blit = self.shoot_right_images[self.walk_count //
                                                    6] if self.speed > 0 else self.shoot_left_images[self.walk_count//6]
        else:
            self.shoot_timer = 0
            image_to_blit = self.walk_right_images[self.walk_count //
                                                   6] if self.speed > 0 else self.walk_left_images[self.walk_count//6]

        timeout_image = None

        if self.hit_timer > 0:
            timeout_image = image_to_blit.copy()
            timeout_image.fill(
                COLORS['red'], special_flags=pygame.BLEND_RGBA_MULT)

        if self.spawn_timer > 0:
            window.blit(ENEMY_SPAWN_IMAGE,
                        (self.x + self.width / 2 - 13, self.y + self.height - 5))
            self.spawn_timer -= 1
        else:
            self.walk_count += 1

        if self.hit_timer > 0:
            image_to_blit = timeout_image
            self.hit_timer -= 1

        if self.walk_count + 1 >= self.walk_count_limit:
            self.walk_count = 0

        image_to_blit = pygame.transform.chop(
            image_to_blit, (0, abs(self.spawn_timer - 77), 0, self.spawn_timer))
        window.blit(image_to_blit, (self.x, self.y + self.spawn_timer))

        self.hitbox = (self.x + 20, self.y + 15, 31, 60)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

        # drawing the health bar
        if self.spawn_timer == 0:
            self.draw_health_bar(window)
            self.draw_shade(window)

    def shoot(self, arrows):
        if self.speed < 0:
            facing = -1
            arrow_start_x = self.hitbox[0] - 20
            arrows.append(Arrow(arrow_start_x, round(self.y + self.height / 2), ARROW_WIDTH, ARROW_HEIGHT, 10 * facing, 1,
                                1, self.hitbox[1] + self.hitbox[3], ARROW_IMAGES['left']))
        if self.speed > 0:
            facing = 1
            arrow_start_x = self.hitbox[0] + self.hitbox[2] + 20
            arrows.append(Arrow(arrow_start_x, round(self.y + self.height / 2), ARROW_WIDTH, ARROW_HEIGHT, 10 * facing, 1,
                                1, self.hitbox[1] + self.hitbox[3], ARROW_IMAGES['right']))
        SOUNDS['shuriken_throw'][0].play()

    def auto_path(self, player_shade, background_width):
        if abs(self.shade['x'] - player_shade['x']) > 400 or abs(self.shade['y'] - player_shade['y']) > 20:
            self.is_shooting = False
            Enemy.auto_path(self, player_shade, background_width)
        else:
            self.is_shooting = True
            return

    def hit(self, shuriken_strength, shuriken_id, coins):
        self.was_hit_by = shuriken_id
        if self.health > shuriken_strength:
            self.hit_timer = 3
            self.health -= shuriken_strength
            self.x += shuriken_strength
        else:
            from coin import Coin
            SOUNDS['archer_death'].play()
            x, y, h = itemgetter('x', 'y', 'h')(self.shade)
            coins.append(
                Coin(x - 20, y - 4 * h, choice(["bronze", "silver", "gold"])))
            self.alive = False
