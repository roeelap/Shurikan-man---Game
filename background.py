class Background:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move_right(self, player):
        self.x += player.speed
        player.left = True
        player.right = False
        player.standing = False

    def move_left(self, player):
        self.x -= player.speed
        player.left = False
        player.right = True
        player.standing = False
