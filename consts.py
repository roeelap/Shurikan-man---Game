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
SAVE_TIMEOUT = 5 * FPS
ALLOWED_SAVE_TYPES = (int,float,str,bool,list,dict,tuple)

# player
PLAYER_STARTING_MAX_HEALTH = 100
PLAYER_STARTING_SPEED = 3.5
PLAYER_STARTING_THROW_SPEED = 12
PLAYER_STARTING_STRENGTH = 1
PLAYER_INVINCIBLE_TIME = 1*FPS
STARTING_SHURIKEN_TIMEOUT = 15
STARTING_MAX_SHURIKENS = 3

# coins
COIN_VALUE = {'bronze': 1, 'silver': 5, 'gold': 10}
COIN_END_PATH_X = 200
COIN_END_PATH_Y = 200

# goblin
GOBLIN_WIDTH = 77
GOBLIN_HEIGHT = 77
GOBLIN_SPAWN_TIMEOUT = 1*FPS
GOBLIN_PATH_TIMEOUT = 1*FPS

# text fonts
PIXEL_FONT_SMALL = pygame.font.Font('./data/fonts/dpcomic.ttf', 20)
PIXEL_FONT_MID = pygame.font.Font('./data/fonts/dpcomic.ttf', 50)
PIXEL_FONT_BIG = pygame.font.Font('./data/fonts/dpcomic.ttf', 100)
PIXEL_FONT_BIG_BUTTON = pygame.font.Font('./data/fonts/dpcomic.ttf', 30)
PIXEL_FONT_SMALL_BUTTON = pygame.font.Font('./data/fonts/dpcomic.ttf', 24)

BUTTON_PIXEL_FONTS = {'big': pygame.font.Font('./data/fonts/dpcomic.ttf', 30),
                      'small': pygame.font.Font('./data/fonts/dpcomic.ttf', 24)}

# shuriken
SHURIKEN_RADIUS = 9
SHURIKEN_STARTING_SLOPE = 9.5
SHURIKEN_MIN_SHADE_WIDTH = 20
SHURIKEN_MAX_SHADE_WIDTH = 40

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

# colors dict
COLORS = {'black': (0, 0, 0), 'white': (255, 255, 255),
          'red': (255, 51, 51), 'green': (60, 179, 113), 'orange': (255, 201, 14), 'cyan': (1, 185, 224)}

# characters images
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
ENEMY_SPAWN_IMAGE = pygame.image.load('./data/images/goblin/spawn.png')

PLAYER_PORTRAIT = pygame.image.load(
    './data/images/player/character-portrait.png')

SPLAT_SOUNDS = [pygame.mixer.Sound('./data/sounds/shuriken/splat-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-2.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-3.wav'),
                pygame.mixer.Sound('./data/sounds/shuriken/splat-4.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-5.wav'), pygame.mixer.Sound('./data/sounds/shuriken/splat-6.wav')]

# Sounds
SOUNDS = {'player_hit': pygame.mixer.Sound('./data/sounds/combat/player-hit.wav'), 'shuriken_throw': [pygame.mixer.Sound('./data/sounds/shuriken/shuriken-throw-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/shuriken-throw-2.wav')],
          'enemy_spawn': pygame.mixer.Sound('./data/sounds/combat/enemy-spawn.wav'), 'pause': pygame.mixer.Sound('./data/sounds/general/pause.wav'),
          'transition': pygame.mixer.Sound('./data/sounds/general/transition.wav'), 'button_click': pygame.mixer.Sound('./data/sounds/general/button-click.wav'),
          'button_hover': pygame.mixer.Sound('./data/sounds/general/button-hover.wav'), 'player_death': pygame.mixer.Sound('./data/sounds/combat/player-death.wav'),
          'bronze_pickup': [pygame.mixer.Sound('./data/sounds/coin/bronze-pickup.wav')], 'gold_pickup': [pygame.mixer.Sound('./data/sounds/coin/gold-pickup.wav')],
          'silver_pickup': [pygame.mixer.Sound('./data/sounds/coin/silver-pickup-1.wav'), pygame.mixer.Sound('./data/sounds/coin/silver-pickup-2.wav')],
          'goblin_deaths': [pygame.mixer.Sound('./data/sounds/combat/goblin-death-1.wav'), pygame.mixer.Sound('./data/sounds/combat/goblin-death-2.wav')],
          'shuriken_hits': [pygame.mixer.Sound('./data/sounds/shuriken/shuriken-hit-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/shuriken-hit-2.wav'),
                            pygame.mixer.Sound('./data/sounds/shuriken/shuriken-hit-3.wav')],
          'granny_hits': [pygame.mixer.Sound('./data/sounds/shuriken/granny-1.wav'), pygame.mixer.Sound('./data/sounds/shuriken/granny-2.wav'), pygame.mixer.Sound('./data/sounds/shuriken/granny-3.wav')],
          'tomato_hits': SPLAT_SOUNDS, 'orange_hits': SPLAT_SOUNDS,
          'item_equip': pygame.mixer.Sound('./data/sounds/general/item-equip.wav'), 'purchase': pygame.mixer.Sound('./data/sounds/general/purchase.wav'),
          'sword_draw': pygame.mixer.Sound('./data/sounds/general/sword-draw.wav'), 'level_up': pygame.mixer.Sound('./data/sounds/combat/level-up.wav'),
          'level_up_human': pygame.mixer.Sound('./data/sounds/combat/level-up-human.wav')}

# button consts
BUTTON_WIDTH_BIG = 227
BUTTON_HEIGHT_BIG = 52
BUTTON_WIDTH_SMALL = 108
BUTTON_HEIGHT_SMALL = 48
CHECKBOX_WIDTH = 52
CHECKBOX_HEIGHT = 48
ARROW_BUTTON_WIDTH = 30
ARROW_BUTTON_HEIGHT = 30

BUTTON_WIDTHS = {'big': 227, 'small': 108, 'checkbox': 52, 'up_arrow': 30, 'down_arrow': 30}

BUTTON_HEIGHTS = {'big': 52, 'small': 48, 'checkbox': 48, 'up_arrow': 30, 'down_arrow': 30}

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
