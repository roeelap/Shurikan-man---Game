import pygame
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
pygame.font.init()

# screen consts
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SCREEN_MIDDLE = int(SCREEN_WIDTH / 2) - 80
FPS = 60
BACKGROUND_DUNGEON = pygame.image.load('./data/images/backgrounds/dungeon.png')
PLAYER_INVINCIBLE_TIME = 1
PLAYER_JUMP_COUNT = 11

# goblin
GOBLIN_WIDTH = 77
GOBLIN_HEIGHT = 77

# text fonts
PIXEL_FONT_SMALL = pygame.font.Font('./data/fonts/dpcomic.ttf', 20)
PIXEL_FONT_MID = pygame.font.Font('./data/fonts/dpcomic.ttf', 50)
PIXEL_FONT_BIG = pygame.font.Font('./data/fonts/dpcomic.ttf', 100)
PIXEL_FONT_BUTTON = pygame.font.Font('./data/fonts/dpcomic.ttf', 30)

# shuriken consts
SHURIKEN_TIMEOUT = 15
MAX_SHURIKENS = 3
SHURIKEN_RADIUS = 9
SHURIKEN_STARTING_SLOPE = 9

# shuriken images
SHURIKEN_IMAGE = pygame.image.load('./data/images/shurikens/shuriken.png')
ORANGE_IMAGE = pygame.image.load('./data/images/shurikens/orange.png')

# colors dict
COLORS = {'black': (0, 0, 0), 'white': (255, 255, 255),
          'red': (255, 0, 0), 'green': (0, 128, 0), 'orange': (255, 201, 14)}

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
SOUNDS = {'player_hit': pygame.mixer.Sound('./data/sounds/player-hit.wav'), 'shuriken_throw': pygame.mixer.Sound('./data/sounds/shuriken-throw.wav'),
          'player_jump': pygame.mixer.Sound('./data/sounds/player-jump.wav'), 'enemy_spawn': pygame.mixer.Sound('./data/sounds/enemy-spawn.wav'),
          'transition': pygame.mixer.Sound('./data/sounds/transition.wav'), 'button_click': pygame.mixer.Sound('./data/sounds/button-click.wav'),
          'button_hover': pygame.mixer.Sound('./data/sounds/button-hover.wav'),
          'goblin_deaths': [pygame.mixer.Sound('./data/sounds/goblin-death-1.wav'), pygame.mixer.Sound('./data/sounds/goblin-death-2.wav')],
          'shuriken_hits': [pygame.mixer.Sound('./data/sounds/shuriken-hit-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken-hit-2.wav'), pygame.mixer.Sound('./data/sounds/shuriken-hit-3.wav')]}

# button consts
BUTTON_WIDTH = 227
BUTTON_HEIGHT = 52
INACTIVE_BUTTON = pygame.image.load(
    './data/images/buttons/button-inactive.png')
ACTIVE_BUTTON = pygame.image.load(
    './data/images/buttons/button-active.png')
CHECKBOX_INACTIVE = pygame.image.load(
    './data/images/buttons/checkbox-inactive.png')
CHECKBOX_ACTIVE = pygame.image.load(
    './data/images/buttons/checkbox-active.png')

# coin images
BRONZE_COINS = [pygame.image.load('./data/images/coins/bronze/bronze1.png'), pygame.image.load('./data/images/coins/bronze/bronze2.png'), pygame.image.load('./data/images/coins/bronze/bronze3.png'),
                pygame.image.load('./data/images/coins/bronze/bronze4.png'), pygame.image.load(
                    './data/images/coins/bronze/bronze5.png'), pygame.image.load('./data/images/coins/bronze/bronze6.png'),
                pygame.image.load('./data/images/coins/bronze/bronze7.png'), pygame.image.load('./data/images/coins/bronze/bronze8.png')]
SILVER_COINS = [pygame.image.load('./data/images/coins/silver/silver1.png'), pygame.image.load('./data/images/coins/silver/silver2.png'), pygame.image.load('./data/images/coins/silver/silver3.png'),
                pygame.image.load('./data/images/coins/silver/silver4.png'), pygame.image.load(
                    './data/images/coins/silver/silver5.png'), pygame.image.load('./data/images/coins/silver/silver6.png'),
                pygame.image.load('./data/images/coins/silver/silver7.png'), pygame.image.load('./data/images/coins/silver/silver8.png')]
GOLD_COINS = [pygame.image.load('./data/images/coins/gold/gold1.png'), pygame.image.load('./data/images/coins/gold/gold2.png'), pygame.image.load('./data/images/coins/gold/gold3.png'),
              pygame.image.load('./data/images/coins/gold/gold4.png'), pygame.image.load(
                  './data/images/coins/gold/gold5.png'), pygame.image.load('./data/images/coins/gold/gold6.png'),
              pygame.image.load('./data/images/coins/gold/gold7.png'), pygame.image.load('./data/images/coins/gold/gold8.png')]
