from consts import BUTTON_CLICK_SOUND, BUTTON_HOVER_SOUND, PIXEL_FONT_BUTTON, COLORS, INACTIVE_BUTTON, ACTIVE_BUTTON

class Button:

    def __init__(self, text, x, y, width, height, inactive_image, active_image):
        self.inactive_text = PIXEL_FONT_BUTTON.render(text, True,  COLORS['black'])
        self.active_text = PIXEL_FONT_BUTTON.render(text, True,  COLORS['orange'])
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center = (self.width // 2, self.height // 2)
        self.inactive_image = inactive_image
        self.active_image = active_image
        self.over = False

    def play_hover_sound(self):
        if not self.over:
            BUTTON_HOVER_SOUND.play()
            self.over = True

    def is_mouse_over(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True
        return False

    def show(self, window, mouse):
        if self.is_mouse_over(mouse):
            self.play_hover_sound()
            window.blit(self.active_image, (self.x, self.y))
        else:
            self.over = False
            window.blit(self.inactive_image, (self.x, self.y))

    def is_pressed(self, mouse, click, action=None):
        if self.is_mouse_over(mouse):
            if click[0] == 1:
                BUTTON_CLICK_SOUND.play()
                return True


class Checkbox(Button):
    def __init__(self, x, y, width, height, inactive_image, active_image):
        Button.__init__(self, x, y, width, height, inactive_image, active_image)
        self.is_on = True
        self.click_counter = 0
    
    def show(self, window, mouse):
        if self.click_counter > 0:
            self.click_counter -= 1

        if self.is_on:
            window.blit(self.active_image, (self.x, self.y))
        else:
            window.blit(self.inactive_image, (self.x, self.y))            

        if not self.is_mouse_over(mouse):
            self.over = False

    def is_pressed(self, mouse, click, action=None):
        if self.is_mouse_over(mouse):
            if click[0] == 1 and self.click_counter == 0:
                if self.is_on:
                    self.is_on = False
                else:
                    self.is_on = True
                self.click_counter = 7
                BUTTON_CLICK_SOUND.play()
                return True
