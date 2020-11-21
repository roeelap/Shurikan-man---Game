import pygame
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
pygame.font.init()

# screen consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 610
SCREEN_MIDDLE = 350
FPS = 27
BACKGROUND_DUNGEON = pygame.image.load('./data/images/backgrounds/dungeon.png')
PLAYER_INVINCIBLE_TIME = 27

# goblin
GOBLIN_WIDTH = 64
GOBLIN_HEIGHT = 64

# text fonts
PIXEL_FONT = pygame.font.Font('./data/fonts/dpcomic.ttf', 20)

# shuriken consts
MAX_SHURIKENS = 3
SHURIKEN_TIMEOUT = 6
SHURIKEN_IMAGE = pygame.image.load('./data/images/player/shuriken.png')
SHURIKEN_RADIUS = 12

# colors dict
COLORS = {'black': (0, 0, 0), 'white': (255, 255, 255),
          'red': (255, 0, 0), 'green': (0, 128, 0)}

# character images
GOBLIN_WALK_RIGHT_IMAGES = [pygame.image.load('./data/images/goblin/R1E.png'), pygame.image.load('./data/images/goblin/R2E.png'), pygame.image.load('./data/images/goblin/R3E.png'),
                            pygame.image.load('./data/images/goblin/R4E.png'), pygame.image.load(
    './data/images/goblin/R5E.png'), pygame.image.load('./data/images/goblin/R6E.png'),
    pygame.image.load('./data/images/goblin/R7E.png'), pygame.image.load(
    './data/images/goblin/R8E.png'), pygame.image.load('./data/images/goblin/R9E.png'),
    pygame.image.load('./data/images/goblin/R10E.png'), pygame.image.load('./data/images/goblin/R11E.png')]

GOBLIN_WALK_LEFT_IMAGES = [pygame.image.load('./data/images/goblin/L1E.png'), pygame.image.load('./data/images/goblin/L2E.png'), pygame.image.load('./data/images/goblin/L3E.png'),
                           pygame.image.load('./data/images/goblin/L4E.png'), pygame.image.load(
    './data/images/goblin/L5E.png'), pygame.image.load('./data/images/goblin/L6E.png'),
    pygame.image.load('./data/images/goblin/L7E.png'), pygame.image.load(
    './data/images/goblin/L8E.png'), pygame.image.load('./data/images/goblin/L9E.png'),
    pygame.image.load('./data/images/goblin/L10E.png'), pygame.image.load('./data/images/goblin/L11E.png')]

PLAYER_WALK_RIGHT_IMAGES = [pygame.image.load('./data/images/player/R1.png'), pygame.image.load('./data/images/player/R2.png'), pygame.image.load('./data/images/player/R3.png'),
                            pygame.image.load('./data/images/player/R4.png'), pygame.image.load(
    './data/images/player/R5.png'), pygame.image.load('./data/images/player/R6.png'),
    pygame.image.load('./data/images/player/R7.png'), pygame.image.load('./data/images/player/R8.png'), pygame.image.load('./data/images/player/R9.png')]

PLAYER_WALK_LEFT_IMAGES = [pygame.image.load('./data/images/player/L1.png'), pygame.image.load('./data/images/player/L2.png'), pygame.image.load('./data/images/player/L3.png'),
                           pygame.image.load('./data/images/player/L4.png'), pygame.image.load(
    './data/images/player/L5.png'), pygame.image.load('./data/images/player/L6.png'),
    pygame.image.load('./data/images/player/L7.png'), pygame.image.load('./data/images/player/L8.png'), pygame.image.load('./data/images/player/L9.png')]

PLAYER_STANDING_IMAGE = pygame.image.load('./data/images/player/standing.png')

PLAYER_PORTRAIT = pygame.image.load(
    './data/images/player/character-portrait.png')

# Sounds
PLAYER_HIT_SOUND = pygame.mixer.Sound('./data/sounds/player-hit.wav')
SHURIKEN_THROW_SOUND = pygame.mixer.Sound('./data/sounds/shuriken-throw.wav')
PLAYER_JUMP_SOUND = pygame.mixer.Sound('./data/sounds/player-jump.wav')
ENEMY_SPAWN_SOUND = pygame.mixer.Sound('./data/sounds/enemy-spawn.wav')
