import pygame
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
pygame.font.init()

# general
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
TOP_BORDER = 500
BOTTOM_BORDER = 630
SCREEN_MIDDLE = int(SCREEN_WIDTH / 2) - 80

FPS = 60

BACKGROUND_DUNGEON = pygame.image.load('./data/images/backgrounds/dungeon.png')
POPUP_IMAGE = pygame.image.load('./data/images/backgrounds/popup-sign.png')

SAVE_TIMEOUT = 5 * FPS
ALLOWED_SAVE_TYPES = (int, float, str, bool, list, dict, tuple)


# colors dict
COLORS = {'black': (0, 0, 0), 'white': (255, 255, 255),
          'red': (255, 51, 51), 'green': (60, 179, 113), 'orange': (255, 201, 14), 'cyan': (1, 185, 224)}


# text fonts
PIXEL_FONT_SMALL = pygame.font.Font('./data/fonts/dpcomic.ttf', 20)
PIXEL_FONT_MID = pygame.font.Font('./data/fonts/dpcomic.ttf', 50)
PIXEL_FONT_BIG = pygame.font.Font('./data/fonts/dpcomic.ttf', 100)
PIXEL_FONT_BIG_BUTTON = pygame.font.Font('./data/fonts/dpcomic.ttf', 30)
PIXEL_FONT_SMALL_BUTTON = pygame.font.Font('./data/fonts/dpcomic.ttf', 24)
BUTTON_PIXEL_FONTS = {'big': PIXEL_FONT_BIG_BUTTON,
                      'small': PIXEL_FONT_SMALL_BUTTON}


# button consts
BUTTON_WIDTH_BIG = 227
BUTTON_HEIGHT_BIG = 52
BUTTON_WIDTH_SMALL = 108
BUTTON_HEIGHT_SMALL = 48
CHECKBOX_WIDTH = 52
CHECKBOX_HEIGHT = 48
ARROW_BUTTON_WIDTH = 30
ARROW_BUTTON_HEIGHT = 30

BUTTON_WIDTHS = {'big': 227, 'small': 108,
                 'checkbox': 52, 'up_arrow': 30, 'down_arrow': 30}

BUTTON_HEIGHTS = {'big': 52, 'small': 48,
                  'checkbox': 48, 'up_arrow': 30, 'down_arrow': 30}

BUTTON_IMAGES = {
    'big': {'inactive': pygame.image.load('./data/images/buttons/button-inactive.png'),
            'active': pygame.image.load('./data/images/buttons/button-active.png'),
            'disabled': pygame.image.load('./data/images/buttons/button-disabled.png')},
    'small': {'inactive': pygame.image.load('./data/images/buttons/button-small-inactive.png'),
              'active': pygame.image.load('./data/images/buttons/button-small-active.png'),
              'disabled': pygame.image.load('./data/images/buttons/button-small-disabled.png')},
    'checkbox': {'inactive': pygame.image.load('./data/images/buttons/checkbox-inactive.png'),
                 'active': pygame.image.load('./data/images/buttons/checkbox-active.png')},
    'up_arrow': {'inactive': pygame.image.load('./data/images/buttons/up-arrow-inactive.png'),
                 'active': pygame.image.load('./data/images/buttons/up-arrow-active.png'),
                 'disabled': pygame.image.load('./data/images/buttons/up-arrow-disabled.png')},
    'down_arrow': {'inactive': pygame.image.load('./data/images/buttons/down-arrow-inactive.png'),
                   'active': pygame.image.load('./data/images/buttons/down-arrow-active.png'),
                   'disabled': pygame.image.load('./data/images/buttons/down-arrow-disabled.png')}
}


MENU_SHURIKENS_LARGE = {'shuriken': pygame.image.load('./data/images/menu-shurikens/large/shuriken.png'), 'orange': pygame.image.load('./data/images/menu-shurikens/large/orange.png'),
                        'golden_shuriken': pygame.image.load('./data/images/menu-shurikens/large/golden-shuriken.png'), 'granny': pygame.image.load('./data/images/menu-shurikens/large/granny.png'),
                        'rainbow_shuriken': pygame.image.load('./data/images/menu-shurikens/large/rainbow-shuriken.png'), 'tomato': pygame.image.load('./data/images/menu-shurikens/large/tomato.png')}
MENU_SHURIKEN_SMALL = pygame.image.load(
    './data/images/menu-shurikens/shuriken-small.png')
MENU_SHURIKENS_MEDIUM = {'shuriken': pygame.image.load('./data/images/menu-shurikens/medium/shuriken.png'), 'orange': pygame.image.load('./data/images/menu-shurikens/medium/orange.png'),
                         'golden_shuriken': pygame.image.load('./data/images/menu-shurikens/medium/golden-shuriken.png'), 'granny': pygame.image.load('./data/images/menu-shurikens/medium/granny.png'),
                         'rainbow_shuriken': pygame.image.load('./data/images/menu-shurikens/medium/rainbow-shuriken.png'), 'tomato': pygame.image.load('./data/images/menu-shurikens/medium/tomato.png')}


# player
PLAYER_STARTING_MAX_HEALTH = 100
PLAYER_STARTING_SPEED = 2.5
PLAYER_STARTING_THROW_SPEED = 12
PLAYER_STARTING_STRENGTH = 1
PLAYER_STARTING_RELOAD_SPEED = 15
PLAYER_STARTING_MAX_SHURIKENS = 3
PLAYER_STARTING_SHURIKEN_DURABILITY = 1
PLAYER_MAX_ENERGY = 200
PLAYER_INVINCIBLE_TIME = 1*FPS

# player images
PLAYER_WALK_RIGHT_IMAGES = [pygame.image.load('./data/images/player/R1.png'), pygame.image.load('./data/images/player/R2.png'), pygame.image.load('./data/images/player/R3.png'),
                            pygame.image.load('./data/images/player/R4.png'), pygame.image.load(
    './data/images/player/R5.png'), pygame.image.load('./data/images/player/R6.png'),
    pygame.image.load('./data/images/player/R7.png'), pygame.image.load('./data/images/player/R8.png'), pygame.image.load('./data/images/player/R9.png')]

PLAYER_WALK_LEFT_IMAGES = [pygame.image.load('./data/images/player/L1.png'), pygame.image.load('./data/images/player/L2.png'), pygame.image.load('./data/images/player/L3.png'),
                           pygame.image.load('./data/images/player/L4.png'), pygame.image.load(
    './data/images/player/L5.png'), pygame.image.load('./data/images/player/L6.png'),
    pygame.image.load('./data/images/player/L7.png'), pygame.image.load('./data/images/player/L8.png'), pygame.image.load('./data/images/player/L9.png')]

PLAYER_STANDING_IMAGE = pygame.image.load('./data/images/player/standing.png')
PLAYER_SHOOT_IMAGES = [pygame.image.load('./data/images/player/S2.png'), pygame.image.load(
    './data/images/player/S1.png')]
PLAYER_PORTRAIT = pygame.image.load(
    './data/images/player/character-portrait.png')


# shuriken
SHURIKEN_RADIUS = 9
SHURIKEN_STARTING_SLOPE = 9.5
SHURIKEN_MIN_SHADE_WIDTH = 20
SHURIKEN_MAX_SHADE_WIDTH = 40
SHURIKEN_ENERGY_REQUIRED = 25

# shuriken images
SHURIKEN_IMAGES = {'shuriken': pygame.image.load('./data/images/shurikens/shuriken.png'), 'golden_shuriken': pygame.image.load('./data/images/shurikens/golden-shuriken.png'),
                   'rainbow_shuriken': pygame.image.load('./data/images/shurikens/rainbow-shuriken.png'), 'orange': pygame.image.load('./data/images/shurikens/orange.png'),
                   'tomato': pygame.image.load('./data/images/shurikens/tomato.png'), 'granny': pygame.image.load('./data/images/shurikens/grandma.png')}
BROKEN_SHURIKENS = {"shuriken": [pygame.image.load('./data/images/shurikens/broken/shuriken/s1.png'), pygame.image.load('./data/images/shurikens/broken/shuriken/s2.png'), pygame.image.load('./data/images/shurikens/broken/shuriken/s3.png'),
                                 pygame.image.load('./data/images/shurikens/broken/shuriken/s4.png')],
                    "granny": [pygame.image.load('./data/images/shurikens/broken/granny/g1.png'), pygame.image.load('./data/images/shurikens/broken/granny/g2.png'), pygame.image.load('./data/images/shurikens/broken/granny/g3.png'),
                               pygame.image.load('./data/images/shurikens/broken/granny/g4.png')],
                    "golden_shuriken": [pygame.image.load('./data/images/shurikens/broken/golden-shuriken/g1.png'), pygame.image.load('./data/images/shurikens/broken/golden-shuriken/g2.png'), pygame.image.load('./data/images/shurikens/broken/golden-shuriken/g3.png'),
                                        pygame.image.load('./data/images/shurikens/broken/golden-shuriken/g4.png')],
                    "rainbow_shuriken": [pygame.image.load('./data/images/shurikens/broken/rainbow-shuriken/r1.png'), pygame.image.load('./data/images/shurikens/broken/rainbow-shuriken/r2.png'), pygame.image.load('./data/images/shurikens/broken/rainbow-shuriken/r3.png'),
                                         pygame.image.load('./data/images/shurikens/broken/rainbow-shuriken/r4.png')],
                    "tomato": [pygame.image.load('./data/images/shurikens/broken/tomato/t1.png'), pygame.image.load('./data/images/shurikens/broken/tomato/t2.png'), pygame.image.load('./data/images/shurikens/broken/tomato/t3.png'),
                               pygame.image.load('./data/images/shurikens/broken/tomato/t4.png')],
                    "orange": [pygame.image.load('./data/images/shurikens/broken/orange/o1.png'), pygame.image.load('./data/images/shurikens/broken/orange/o2.png'), pygame.image.load('./data/images/shurikens/broken/orange/o3.png'),
                               pygame.image.load('./data/images/shurikens/broken/orange/o4.png')]}


# pit image where the enemies appears from
ENEMY_SPAWN_IMAGE = pygame.image.load('./data/images/goblin/spawn.png')

# goblin
GOBLIN_WIDTH = 77
GOBLIN_HEIGHT = 77
GOBLIN_SPAWN_TIMEOUT = 77
GOBLIN_PATH_TIMEOUT = 1*FPS

# goblin images
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


# archer images
ARCHER_WALK_RIGHT_IMAGES = [pygame.image.load('./data/images/archer/walking/R1.png'), pygame.image.load('./data/images/archer/walking/R2.png'), pygame.image.load('./data/images/archer/walking/R3.png'),
                            pygame.image.load('./data/images/archer/walking/R4.png'), pygame.image.load(
                                './data/images/archer/walking/R5.png'), pygame.image.load('./data/images/archer/walking/R6.png'),
                            pygame.image.load('./data/images/archer/walking/R7.png'), pygame.image.load('./data/images/archer/walking/R8.png'), pygame.image.load('./data/images/archer/walking/R9.png')]


ARCHER_WALK_LEFT_IMAGES = [pygame.image.load('./data/images/archer/walking/L1.png'), pygame.image.load('./data/images/archer/walking/L2.png'), pygame.image.load('./data/images/archer/walking/L3.png'),
                           pygame.image.load('./data/images/archer/walking/L4.png'), pygame.image.load(
                               './data/images/archer/walking/L5.png'), pygame.image.load('./data/images/archer/walking/L6.png'),
                           pygame.image.load('./data/images/archer/walking/L7.png'), pygame.image.load('./data/images/archer/walking/L8.png'), pygame.image.load('./data/images/archer/walking/L9.png'), ]


ARCHER_SHOOT_RIGHT_IMAGES = [pygame.image.load('./data/images/archer/shooting/RS1.png'), pygame.image.load('./data/images/archer/shooting/RS2.png'), pygame.image.load('./data/images/archer/shooting/RS3.png'),
                             pygame.image.load('./data/images/archer/shooting/RS4.png'), pygame.image.load(
    './data/images/archer/shooting/RS5.png'), pygame.image.load('./data/images/archer/shooting/RS6.png'),
    pygame.image.load('./data/images/archer/shooting/RS7.png'), pygame.image.load(
    './data/images/archer/shooting/RS8.png'), pygame.image.load('./data/images/archer/shooting/RS9.png'),
    pygame.image.load('./data/images/archer/shooting/RS10.png'), pygame.image.load('./data/images/archer/shooting/RS11.png'), pygame.image.load('./data/images/archer/shooting/RS12.png')]

ARCHER_SHOOT_LEFT_IMAGES = [pygame.image.load('./data/images/archer/shooting/LS1.png'), pygame.image.load('./data/images/archer/shooting/LS2.png'), pygame.image.load('./data/images/archer/shooting/LS3.png'),
                            pygame.image.load('./data/images/archer/shooting/LS4.png'), pygame.image.load(
                            './data/images/archer/shooting/LS5.png'), pygame.image.load('./data/images/archer/shooting/LS6.png'),
                            pygame.image.load('./data/images/archer/shooting/LS7.png'), pygame.image.load(
                            './data/images/archer/shooting/LS8.png'), pygame.image.load('./data/images/archer/shooting/LS9.png'),
                            pygame.image.load('./data/images/archer/shooting/LS10.png'), pygame.image.load('./data/images/archer/shooting/LS11.png'), pygame.image.load('./data/images/archer/shooting/LS12.png')]


# arrow
ARROW_WIDTH = 28
ARROW_HEIGHT = 4
ARROW_MIN_SHADE_WIDTH = 28
ARROW_MAX_SHADE_WIDTH = 45

# arrow images
ARROW_IMAGES = {'right': pygame.image.load('./data/images/archer/arrow/arrow-right.png'),
                    'left': pygame.image.load('./data/images/archer/arrow/arrow-left.png')}
BROKEN_ARROW_IMAGES = {'right': [pygame.image.load('./data/images/archer/arrow/arrow-right-broken1.png'), pygame.image.load(
    './data/images/archer/arrow/arrow-right-broken2.png')], 'left': [pygame.image.load('./data/images/archer/arrow/arrow-left-broken1.png'), pygame.image.load(
    './data/images/archer/arrow/arrow-left-broken2.png')]}


# coins
COIN_VALUE = {'bronze': 1, 'silver': 5, 'gold': 10}
COIN_END_PATH_X = 200
COIN_END_PATH_Y = 200

# coin images
BRONZE_COINS_IMAGES = [pygame.image.load('./data/images/coins/bronze/bronze1.png'), pygame.image.load('./data/images/coins/bronze/bronze2.png'), pygame.image.load('./data/images/coins/bronze/bronze3.png'),
                       pygame.image.load('./data/images/coins/bronze/bronze4.png'), pygame.image.load(
    './data/images/coins/bronze/bronze5.png'), pygame.image.load('./data/images/coins/bronze/bronze6.png'),
    pygame.image.load('./data/images/coins/bronze/bronze7.png'), pygame.image.load('./data/images/coins/bronze/bronze8.png')]
SILVER_COINS_IMAGES = [pygame.image.load('./data/images/coins/silver/silver1.png'), pygame.image.load('./data/images/coins/silver/silver2.png'), pygame.image.load('./data/images/coins/silver/silver3.png'),
                       pygame.image.load('./data/images/coins/silver/silver4.png'), pygame.image.load(
    './data/images/coins/silver/silver5.png'), pygame.image.load('./data/images/coins/silver/silver6.png'),
    pygame.image.load('./data/images/coins/silver/silver7.png'), pygame.image.load('./data/images/coins/silver/silver8.png')]
GOLD_COINS_IMAGES = [pygame.image.load('./data/images/coins/gold/gold1.png'), pygame.image.load('./data/images/coins/gold/gold2.png'), pygame.image.load('./data/images/coins/gold/gold3.png'),
                     pygame.image.load('./data/images/coins/gold/gold4.png'), pygame.image.load(
    './data/images/coins/gold/gold5.png'), pygame.image.load('./data/images/coins/gold/gold6.png'),
    pygame.image.load('./data/images/coins/gold/gold7.png'), pygame.image.load('./data/images/coins/gold/gold8.png')]

SMALL_COINS_IMAGES = {'bronze': pygame.image.load('./data/images/coins/small/bronze.png'), 'silver': pygame.image.load(
    './data/images/coins/small/silver.png'), 'gold': pygame.image.load('./data/images/coins/small/gold.png')}


# health pack info
HEALTH_PACK_IMAGE = pygame.image.load('./data/images/other/health-pack.png')
HEALTH_PACK_WIDTH = 40
HEALTH_PACK_HEIGHT = 33
HEALTH_PACK_HEAL = 30


# Sounds
SPLAT_SOUNDS = [pygame.mixer.Sound('./data/sounds/shuriken/splat-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-2.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-3.wav'),
                pygame.mixer.Sound('./data/sounds/shuriken/splat-4.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-5.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-6.wav')]


SOUNDS = {'player_hit': pygame.mixer.Sound('./data/sounds/combat/player-hit.wav'), 'shuriken_throw': [pygame.mixer.Sound('./data/sounds/shuriken/shuriken-throw-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/shuriken-throw-2.wav')],
          'enemy_spawn': pygame.mixer.Sound('./data/sounds/combat/enemy-spawn.wav'), 'pause': pygame.mixer.Sound('./data/sounds/general/pause.wav'), 'health_pack': pygame.mixer.Sound('./data/sounds/combat/give-health.wav'),
          'transition': pygame.mixer.Sound('./data/sounds/general/transition.wav'), 'button_click': pygame.mixer.Sound('./data/sounds/general/button-click.wav'), 'health_pack_spawn': pygame.mixer.Sound('./data/sounds/combat/pop.wav'),
          'button_hover': pygame.mixer.Sound('./data/sounds/general/button-hover.wav'), 'player_death': pygame.mixer.Sound('./data/sounds/combat/player-death.wav'), 'arrow': pygame.mixer.Sound('./data/sounds/combat/arrow.wav'),
          'bronze_pickup': [pygame.mixer.Sound('./data/sounds/coin/bronze-pickup.wav')], 'gold_pickup': [pygame.mixer.Sound('./data/sounds/coin/gold-pickup.wav')],
          'silver_pickup': [pygame.mixer.Sound('./data/sounds/coin/silver-pickup-1.wav'), pygame.mixer.Sound('./data/sounds/coin/silver-pickup-2.wav')],
          'goblin_deaths': [pygame.mixer.Sound('./data/sounds/combat/goblin-death-1.wav'), pygame.mixer.Sound('./data/sounds/combat/goblin-death-2.wav')], 'archer_death': [pygame.mixer.Sound('./data/sounds/combat/skeleton-death.wav')],
          'shuriken_hits': [pygame.mixer.Sound('./data/sounds/shuriken/shuriken-hit-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/shuriken-hit-2.wav'),
                            pygame.mixer.Sound('./data/sounds/shuriken/shuriken-hit-3.wav')],
          'granny_hits': [pygame.mixer.Sound('./data/sounds/shuriken/granny-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/granny-2.wav'), pygame.mixer.Sound('./data/sounds/shuriken/granny-3.wav')],
          'tomato_hits': SPLAT_SOUNDS, 'orange_hits': SPLAT_SOUNDS,
          'item_equip': pygame.mixer.Sound('./data/sounds/general/item-equip.wav'), 'purchase': pygame.mixer.Sound('./data/sounds/general/purchase.wav'),
          'sword_draw': pygame.mixer.Sound('./data/sounds/general/sword-draw.wav'), 'level_up': pygame.mixer.Sound('./data/sounds/combat/level-up.wav'),
          'level_up_human': pygame.mixer.Sound('./data/sounds/combat/level-up-human.wav'), 'ninja': pygame.mixer.Sound('./data/sounds/general/ninja.wav')}
