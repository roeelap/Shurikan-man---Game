import os
import json
import pygame
from consts import ALLOWED_SAVE_TYPES, GOBLIN_WALK_LEFT_IMAGES, GOBLIN_WALK_RIGHT_IMAGES


def draw_circle_alpha(surface, color, center, width, height):
    target_rect = pygame.Rect(center, (0, 0)).inflate(
        (width * 2, height * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    shape_surf.set_alpha(64)
    pygame.draw.ellipse(shape_surf, color,
                        (width / 2, 4, width, height), width)
    surface.blit(shape_surf, target_rect)


def draw_rect_with_alpha(x, y, width, height, color, alpha, window, border_radius=0):
    target_rect = pygame.Rect((x, y), (width, height))
    shape_surf = pygame.Surface((width, height), pygame.SRCALPHA)
    shape_surf.set_alpha(alpha)
    pygame.draw.rect(
        shape_surf, color, (0, 0, width, height), border_radius=border_radius)
    window.blit(shape_surf, target_rect)


def draw_rotated(window, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=topleft).center)
    window.blit(rotated_image, new_rect.topleft)


def reset_game():
    files = os.listdir('./saves')
    for file in files:
        with open(f'./saves/{file}', 'w', encoding='utf-8') as file:
            if file == 'enemies.json':
                file.write('[]')
            else:
                file.write('{}')


def save_game(player, enemies, background, settings):
    save_object_status(player, 'player')
    save_object_status(background, 'background')
    save_objects_status(enemies, 'enemies')
    save_dict(settings, 'settings')


def load_game(player, enemies, background, settings):
    from enemy import Enemy
    load_object_status(player, 'player')
    load_object_status(background, 'background')
    load_objects_status(enemies, 'enemies', Enemy)
    load_dict(settings, 'settings')


def save_objects_status(objects, name):
    objects_data = []
    for object in objects:
        object_data = object.__dict__
        object_dict = {}
        for attr, value in object_data.items():
            if is_valid_type(value, object):
                object_dict[attr] = value
        objects_data.append(object_dict)
    with open(f'./saves/{name}.json', 'w', encoding='utf-8') as file:
        json.dump(objects_data, file, ensure_ascii=False, indent=4)


def save_object_status(object, name):
    object_data = object.__dict__
    object_dict = {}
    for attr, value in object_data.items():
        if is_valid_type(value, object):
            object_dict[attr] = value
    with open(f'./saves/{name}.json', 'w', encoding='utf-8') as file:
        json.dump(object_dict, file, ensure_ascii=False, indent=4)


def save_dict(dict, dict_name):
    with open(f'./saves/{dict_name}.json', 'w', encoding='utf-8') as file:
        json.dump(dict, file, ensure_ascii=False, indent=4)


def load_object_status(object, name):
    with open(f'./saves/{name}.json') as file:
        object_data = json.load(file)
    for attr, value in object_data.items():
        if is_valid_type(value, object):
            setattr(object, attr, value)


def load_objects_status(objects, name, type):
    with open(f'./saves/{name}.json') as file:
        objects_data = json.load(file)
    for object in objects_data:
        new_object = type(0, 0, 0, 0, 0, 0, 0,
                          GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)
        for attr, value in object.items():
            if is_valid_type(value, object):
                setattr(new_object, attr, value)
        objects.append(new_object)


def load_dict(dict, dict_name):
    with open(f'./saves/{dict_name}.json') as file:
        data = json.load(file)
    for key, value in data.items():
        dict[key] = value


def is_valid_type(value, instance):
    from enemy import Enemy
    if isinstance(value, ALLOWED_SAVE_TYPES):
        if isinstance(instance, Enemy) and isinstance(value, list):
            return False
        return True
    return False
