import pygame
pygame.mixer.init()
pygame.font.init()

# screen consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 610
SCREEN_MIDDLE = 350
FPS = 27
BACKGROUND_DUNGEON = pygame.image.load('./data/background-images/dungeon.png')

# text fonts
PIXEL_FONT = pygame.font.Font('./data/dpcomic.ttf', 20)

# shuriken consts
MAX_SHURIKENS = 3
SHURIKEN_IMAGE = pygame.image.load('./data/player-images/shuriken.png')

# colors dict
COLORS = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 128, 0)}

# character images
GOBLIN_WALK_RIGHT_IMAGES = [pygame.image.load('./data/goblin-images/R1E.png'), pygame.image.load('./data/goblin-images/R2E.png'), pygame.image.load('./data/goblin-images/R3E.png'),
                    pygame.image.load('./data/goblin-images/R4E.png'), pygame.image.load(
                        './data/goblin-images/R5E.png'), pygame.image.load('./data/goblin-images/R6E.png'),
                    pygame.image.load('./data/goblin-images/R7E.png'), pygame.image.load(
                        './data/goblin-images/R8E.png'), pygame.image.load('./data/goblin-images/R9E.png'),
                    pygame.image.load('./data/goblin-images/R10E.png'), pygame.image.load('./data/goblin-images/R11E.png')]

GOBLIN_WALK_LEFT_IMAGES = [pygame.image.load('./data/goblin-images/L1E.png'), pygame.image.load('./data/goblin-images/L2E.png'), pygame.image.load('./data/goblin-images/L3E.png'),
                   pygame.image.load('./data/goblin-images/L4E.png'), pygame.image.load(
    './data/goblin-images/L5E.png'), pygame.image.load('./data/goblin-images/L6E.png'),
    pygame.image.load('./data/goblin-images/L7E.png'), pygame.image.load(
    './data/goblin-images/L8E.png'), pygame.image.load('./data/goblin-images/L9E.png'),
    pygame.image.load('./data/goblin-images/L10E.png'), pygame.image.load('./data/goblin-images/L11E.png')]

PLAYER_WALK_RIGHT_IMAGES = [pygame.image.load('./data/player-images/R1.png'), pygame.image.load('./data/player-images/R2.png'), pygame.image.load('./data/player-images/R3.png'),
                     pygame.image.load('./data/player-images/R4.png'), pygame.image.load(
                         './data/player-images/R5.png'), pygame.image.load('./data/player-images/R6.png'),
                     pygame.image.load('./data/player-images/R7.png'), pygame.image.load('./data/player-images/R8.png'), pygame.image.load('./data/player-images/R9.png')]

PLAYER_WALK_LEFT_IMAGES = [pygame.image.load('./data/player-images/L1.png'), pygame.image.load('./data/player-images/L2.png'), pygame.image.load('./data/player-images/L3.png'),
                    pygame.image.load('./data/player-images/L4.png'), pygame.image.load(
                        './data/player-images/L5.png'), pygame.image.load('./data/player-images/L6.png'),
                    pygame.image.load('./data/player-images/L7.png'), pygame.image.load('./data/player-images/L8.png'), pygame.image.load('./data/player-images/L9.png')]

PLAYER_STANDING_IMAGE = pygame.image.load('./data/player-images/standing.png')

PLAYER_PORTRAIT = pygame.image.load('./data/player-images/character-portrait.png')