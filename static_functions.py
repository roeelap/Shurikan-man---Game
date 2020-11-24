from operator import itemgetter
import pygame
import json


def draw_circle_alpha(surface, color, center, width, height):
    target_rect = pygame.Rect(center, (0, 0)).inflate(
        (width * 2, height * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    shape_surf.set_alpha(64)
    pygame.draw.ellipse(shape_surf, color,
                        (width / 2, 4, width, height), width)
    surface.blit(shape_surf, target_rect)


def is_shade_collision(shade1, shade2):
    x1, y1, w1, h1 = itemgetter('x', 'y', 'w', 'h')(shade1)
    x2, y2, w2, h2 = itemgetter('x', 'y', 'w', 'h')(shade2)
    inbound_x = x1 + w1 > x2 and x1 < x2 + w2
    inbound_y = y1 + h1 > y2 and y1 < y2 + h2
    if inbound_x and inbound_y:
        return True
    return False


def save_game(player, player_data):
    player_data['coins'] = player.coins
    player_data['score'] = player.score
    with open('player.json', 'w', encoding='utf-8') as file:
        json.dump(player_data, file, ensure_ascii=False, indent=4)


def load_game(player):
    with open('player.json') as file:
        player_data = json.load(file)
    player.coins = player_data['coins']
    player.score = player_data['score']
    return player_data
