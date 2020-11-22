import pygame

class Button:
    def __init__(self, x, y, width, height, inactive_image, active_image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_image = inactive_image
        self.active_image = active_image
    
    def show(self, window):
        global mouse
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            window.blit(self.active_image, (self.x, self.y))
        else:
            window.blit(self.inactive_image, (self.x, self.y))
    
    def is_pressed(self, action=None):
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if click[0] == 1:
                return True