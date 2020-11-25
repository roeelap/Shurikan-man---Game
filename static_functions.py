from consts import GOBLIN_WALK_LEFT_IMAGES, GOBLIN_WALK_RIGHT_IMAGES
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


def save_game(player, enemies, background):
    save_object_status(player, 'player')
    save_object_status(background, 'background')
    save_objects_status(enemies, 'enemies')


def load_game(player, enemies, background):
    from enemy import Enemy
    load_object_status(player, 'player')
    load_object_status(background, 'background')
    load_objects_status(enemies, 'enemies', Enemy)


def save_objects_status(objects, name):
    objects_data = []
    for object in objects:
        object_data = object.__dict__
        object_dict = {}
        for attr, value in object_data.items():
            if is_valid_type(value, object):
                object_dict[attr] = value
        objects_data.append(object_dict)
    with open(f'./status/{name}.json', 'w', encoding='utf-8') as file:
        json.dump(objects_data, file, ensure_ascii=False, indent=4)


def save_object_status(object, name):
    object_data = object.__dict__
    object_dict = {}
    for attr, value in object_data.items():
        if is_valid_type(value, object):
            object_dict[attr] = value
    with open(f'./status/{name}.json', 'w', encoding='utf-8') as file:
        json.dump(object_dict, file, ensure_ascii=False, indent=4)


def load_object_status(object, name):
    with open(f'./status/{name}.json') as file:
        object_data = json.load(file)
    for attr, value in object_data.items():
        if is_valid_type(value, object):
            setattr(object, attr, value)


def load_objects_status(objects, name, type):
    with open(f'./status/{name}.json') as file:
        objects_data = json.load(file)
    for object in objects_data:
        new_object = type(0, 0, 0, 0, 0, 0,
                          GOBLIN_WALK_RIGHT_IMAGES, GOBLIN_WALK_LEFT_IMAGES)
        for attr, value in object.items():
            if is_valid_type(value, object):
                setattr(new_object, attr, value)
        objects.append(new_object)


def is_valid_type(value, instance):
    from enemy import Enemy
    if type(value) is int or type(value) is float or type(value) is dict or type(value) is tuple or type(value) is bool:
        return True
    if type(instance) != Enemy and type(value) is list:
        return True
    return False
