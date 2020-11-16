import pygame


# PLAYER_STANDING = pygame.image.load('./data/player images/standing.png')


PLAYER_WALK_RIGHT = [pygame.image.load('./data/player-images/R1.png'), pygame.image.load('./data/player-images/R2.png'), pygame.image.load('./data/player-images/R3.png'),
                     pygame.image.load('./data/player-images/R4.png'), pygame.image.load(
                         './data/player-images/R5.png'), pygame.image.load('./data/player-images/R6.png'),
                     pygame.image.load('./data/player-images/R7.png'), pygame.image.load('./data/player-images/R8.png'), pygame.image.load('./data/player-images/R9.png')]


PLAYER_WALK_LEFT = [pygame.image.load('./data/player-images/L1.png'), pygame.image.load('./data/player-images/L2.png'), pygame.image.load('./data/player-images/L3.png'),
                    pygame.image.load('./data/player-images/L4.png'), pygame.image.load(
                        './data/player-images/L5.png'), pygame.image.load('./data/player-images/L6.png'),
                    pygame.image.load('./data/player-images/L7.png'), pygame.image.load('./data/player-images/L8.png'), pygame.image.load('./data/player-images/L9.png')]


class Player:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 28, 53)

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                window.blit(
                    PLAYER_WALK_LEFT[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                window.blit(
                    PLAYER_WALK_RIGHT[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.left:
                window.blit(PLAYER_WALK_LEFT[0], (self.x, self.y))
            else:
                window.blit(PLAYER_WALK_RIGHT[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 28, 53)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)


player = Player(10, 530, 64, 64)
