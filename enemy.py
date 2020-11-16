import pygame


ENEMY_WALK_RIGHT = [pygame.image.load('./data/goblin-images/R1E.png'), pygame.image.load('./data/goblin-images/R2E.png'), pygame.image.load('./data/goblin-images/R3E.png'),
                    pygame.image.load('./data/goblin-images/R4E.png'), pygame.image.load('./data/goblin-images/R5E.png'), pygame.image.load('./data/goblin-images/R6E.png'),
                    pygame.image.load('./data/goblin-images/R7E.png'), pygame.image.load('./data/goblin-images/R8E.png'), pygame.image.load('./data/goblin-images/R9E.png'),
                    pygame.image.load('./data/goblin-images/R10E.png'), pygame.image.load('./data/goblin-images/R11E.png')]


ENEMY_WALK_LEFT =  [pygame.image.load('./data/goblin-images/L1E.png'), pygame.image.load('./data/goblin-images/L2E.png'), pygame.image.load('./data/goblin-images/L3E.png'),
                    pygame.image.load('./data/goblin-images/L4E.png'), pygame.image.load('./data/goblin-images/L5E.png'), pygame.image.load('./data/goblin-images/L6E.png'),
                    pygame.image.load('./data/goblin-images/L7E.png'), pygame.image.load('./data/goblin-images/L8E.png'), pygame.image.load('./data/goblin-images/L9E.png'),
                    pygame.image.load('./data/goblin-images/L10E.png'), pygame.image.load('./data/goblin-images/L11E.png')]


class Enemy(object):

    def __init__(self, x, y, width, height, x_end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_end = x_end
        self.path = [self.x, self.x_end]
        self.walk_count = 0
        self.velocity = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 9
        self.visible = True

    def draw(self,window):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.velocity < 0:
                window.blit(ENEMY_WALK_RIGHT[self.walk_count //3], (self.x, self.y))
                self.walk_count += 1
            else:
                window.blit(ENEMY_WALK_LEFT[self.walk_count //3], (self.x, self.y))
                self.walk_count += 1

            pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (9 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    def move(self):
        if self.velocity > 0:
            if self.x - self.velocity > self.path[1]:
                self.x -= self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walk_count = 0
        else:
            if self.x + self.velocity < self.path[0]:
                self.x -= self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walk_count = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False