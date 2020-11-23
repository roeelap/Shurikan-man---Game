from consts import BRONZE_COINS, SILVER_COINS, GOLD_COINS

class Coin:

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.radius = 20
        self.kind = kind
        self.spin_count = 0

    def draw(self, window):
        if self.spin_count + 1 >= 16:
            self.spin_count = 0
        if self.kind == "bronze":
            window.blit(BRONZE_COINS[self.spin_count // 2], (self.x, self.y))
        elif self.kind == "silver":
            window.blit(SILVER_COINS[self.spin_count // 2], (self.x, self.y))
        elif self.kind == "gold":
            window.blit(GOLD_COINS[self.spin_count // 2], (self.x, self.y))
        
        self.spin_count += 1

    def move(self, player_speed, direction):
        self.x -= player_speed * direction


