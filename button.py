from consts import BUTTON_CLICK_SOUND, BUTTON_HOVER_SOUND, PIXEL_FONT_BUTTON, COLORS, INACTIVE_BUTTON, ACTIVE_BUTTON, CHECKBOX_ACTIVE, CHECKBOX_INACTIVE

class Button:

    def __init__(self, text, x, y):
        self.inactive_text = PIXEL_FONT_BUTTON.render(str(text), True,  COLORS['black'])
        self.active_text = PIXEL_FONT_BUTTON.render(str(text), True,  COLORS['orange'])
        self.x = x
        self.y = y
        self.width = 227
        self.height = 52
        self.center = self.x + self.width // 2, self.y + self.height // 2
        self.inactive_image = INACTIVE_BUTTON
        self.active_image = ACTIVE_BUTTON
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
            textRect = self.active_text.get_rect()
            textRect.center = self.center
            window.blit(self.active_text, textRect)
        else:
            self.over = False
            window.blit(self.inactive_image, (self.x, self.y))
            textRect = self.inactive_text.get_rect()
            textRect.center = self.center
            window.blit(self.inactive_text, textRect)

    def is_pressed(self, mouse, click, action=None):
        if self.is_mouse_over(mouse):
            if click[0] == 1:
                BUTTON_CLICK_SOUND.play()
                return True


class Checkbox:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 52
        self.height = 48
        self.is_on = True
        self.click_counter = 0
        self.inactive_image = CHECKBOX_INACTIVE
        self.active_image = CHECKBOX_ACTIVE

    def play_hover_sound(self):
        if not self.over:
            BUTTON_HOVER_SOUND.play()
            self.over = True

    def is_mouse_over(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True
        return False
    
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
