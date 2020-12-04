from enemy import Enemy
from archer import Archer
from random import choice, randint
from consts import TOP_BORDER, BOTTOM_BORDER, GOBLIN_WIDTH, GOBLIN_HEIGHT, GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES, ARCHER_WALK_RIGHT_IMAGES, \
    ARCHER_WALK_LEFT_IMAGES, ARCHER_SHOOT_RIGHT_IMAGES, ARCHER_SHOOT_LEFT_IMAGES, PIXEL_FONT_BIG_BUTTON, COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SOUNDS


class RoundSystem:
    def __init__(self, round_number):
        self.round_number = round_number
        self.spawn_enemy_timer = 0
        self.enemies_need_to_kill = self.round_number * 2

    def spawn_enemy_if_can(self, enemies, background, player_level):
        self.spawn_enemy_timer += 1
        if self.spawn_enemy_timer == int(3 * FPS) and len(enemies) < self.enemies_need_to_kill:
            self.spawn_enemy(enemies, background, player_level)
            self.spawn_enemy_timer = 0
        elif self.enemies_need_to_kill == 0:
            self.round_number += 1
            self.enemies_need_to_kill = self.round_number * 2
            self.spawn_enemy_timer = 0

    def spawn_enemy(self, enemies, background, player_level):
        start_x = background.x + \
            randint(background.width-300, background.width - GOBLIN_WIDTH)
        start_y = randint(TOP_BORDER, BOTTOM_BORDER)
        direction = -1

        new_goblin = Enemy(start_x, start_y, GOBLIN_WIDTH, GOBLIN_HEIGHT, 1.4 * direction, player_level + 8, player_level + 9,
                           GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)
        new_archer = Archer(start_x, start_y, GOBLIN_WIDTH, GOBLIN_HEIGHT, 1.1 * direction, player_level + 6, player_level + 9, ARCHER_WALK_RIGHT_IMAGES, ARCHER_WALK_LEFT_IMAGES,
                            ARCHER_SHOOT_RIGHT_IMAGES, ARCHER_SHOOT_LEFT_IMAGES)

        if self.round_number < 3:
            new_enemy = new_goblin
        elif self.round_number >= 3:
            new_enemy = choice([new_goblin, new_archer])

        enemies.append(new_enemy)
        SOUNDS['enemy_spawn'].play()

    def display_game_round(self, window):
        round_text = 'Round: ' + str(self.round_number)
        round_text = PIXEL_FONT_BIG_BUTTON.render(
            round_text, True, COLORS['white'])
        round_textRect = round_text.get_rect()
        round_textRect.center = (SCREEN_WIDTH * 9 / 10, SCREEN_HEIGHT / 7)
        window.blit(round_text, round_textRect)
