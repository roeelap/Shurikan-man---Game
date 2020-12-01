from enemy import Enemy
from shuriken import Arrow
from random import choice
from operator import itemgetter
import pygame
from consts import COLORS, ENEMY_SPAWN_IMAGE, SOUNDS, GOBLIN_PATH_TIMEOUT, TOP_BORDER, BOTTOM_BORDER, ARROW_IMAGES, ARROW_HEIGHT, ARROW_WIDTH


class Archer(Enemy):

    def __init__(self, x, y, width, height, speed, health, damage, walk_right_images, walk_left_images, shoot_right_images, shoot_left_images):
        Enemy.__init__(self, x, y, width, height, speed, health,
                       damage, walk_right_images, walk_left_images)

        self.walking_speed = speed

        self.shoot_right_images = shoot_right_images
        self.shoot_left_images = shoot_left_images

        self.shade = {'x': self.x + self.width / 2,
                      'y': self.hitbox[1] + self.hitbox[3], 'w': 38, 'h': 12}

        self.shoot_timer = 0
        self.is_shooting = False

    def draw(self, window, player_shade):
        if not self.alive:
            return

        if self.shoot_timer > 12:
            self.shoot_timer = 0

        timeout_image = None

        if abs(self.shade['x'] - player_shade['x']) > 400 or abs(self.shade['y'] - player_shade['y']) > 20:
            self.shoot_timer = 0
            self.is_shooting = False
            image_to_blit = self.walk_right_images[self.walk_count //
                                                   6] if self.speed > 0 else self.walk_left_images[self.walk_count//6]
        else:
            self.shoot_timer += 1
            self.is_shooting = True
            image_to_blit = self.shoot_right_images[self.walk_count //
                                                    6] if self.speed > 0 else self.shoot_left_images[self.walk_count//6]

        if self.hit_timer > 0:
            timeout_image = image_to_blit.copy()
            timeout_image.fill(
                COLORS['red'], special_flags=pygame.BLEND_RGBA_MULT)
        if self.spawn_timer > 0:
            window.blit(ENEMY_SPAWN_IMAGE,
                        (self.x+self.width/2-13, self.y+self.height-5))
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
