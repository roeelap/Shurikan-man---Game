from consts import SHURIKEN_SMALL, SOUNDS, PIXEL_FONT_BIG_BUTTON, PIXEL_FONT_SMALL_BUTTON, COLORS, INACTIVE_BUTTON_BIG, ACTIVE_BUTTON_BIG, DISABLED_BUTTON_BIG, INACTIVE_BUTTON_SMALL, ACTIVE_BUTTON_SMALL, CHECKBOX_ACTIVE, CHECKBOX_INACTIVE,\
    BUTTON_HEIGHT_BIG, BUTTON_WIDTH_BIG, BUTTON_WIDTH_SMALL, CHECKBOX_WIDTH, CHECKBOX_HEIGHT
from static_functions import draw_rotated


class Button:

    def __init__(self, text, x, y, big_or_small):
        self.x = x
        self.y = y
        if big_or_small == 'big':
            self.width = BUTTON_WIDTH_BIG
            self.height = BUTTON_HEIGHT_BIG
            self.inactive_image = INACTIVE_BUTTON_BIG
            self.active_image = ACTIVE_BUTTON_BIG
            self.disabled_image = DISABLED_BUTTON_BIG
            self.inactive_text = PIXEL_FONT_BIG_BUTTON.render(
                str(text), True,  COLORS['black'])
            self.active_text = PIXEL_FONT_BIG_BUTTON.render(
                str(text), True,  COLORS['orange'])
        elif big_or_small == 'small':
            self.width = BUTTON_WIDTH_SMALL
            self.height = BUTTON_HEIGHT_BIG
            self.inactive_image = INACTIVE_BUTTON_SMALL
            self.active_image = ACTIVE_BUTTON_SMALL
            self.inactive_text = PIXEL_FONT_SMALL_BUTTON.render(
                str(text), True,  COLORS['black'])
            self.active_text = PIXEL_FONT_SMALL_BUTTON.render(
                str(text), True,  COLORS['orange'])
        self.center = self.x + self.width // 2, self.y + self.height // 2
        self.over = False
        self.shuriken_rotation_angle = 0
        self.disabled = False
        self.clicked = False
        self.shuriken_x = [self.x-30, self.x+self.width+5]

    def play_hover_sound(self):
        if not self.over:
            SOUNDS['button_hover'].play()
            self.over = True

    def is_mouse_over(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True
        return False

    def show(self, window, mouse):
        if self.disabled:
            window.blit(self.disabled_image, (self.x, self.y))
            textRect = self.inactive_text.get_rect()
            textRect.center = self.center
            window.blit(self.inactive_text, textRect)

        else:
            if self.is_mouse_over(mouse) or self.clicked:
                self.play_hover_sound()
                window.blit(self.active_image, (self.x, self.y))
                textRect = self.active_text.get_rect()
                textRect.center = self.center
                window.blit(self.active_text, textRect)
                self.shuriken_rotate_animation(
                    window, (self.shuriken_x[0], self.y+12))
                self.shuriken_rotate_animation(
                    window, (self.shuriken_x[1], self.y+12))
            else:
                self.over = False
                window.blit(self.inactive_image, (self.x, self.y))
                textRect = self.inactive_text.get_rect()
                textRect.center = self.center
                window.blit(self.inactive_text, textRect)
            if self.clicked:
                self.update_shuriken_x()

    def shuriken_rotate_animation(self, window, center):
        draw_rotated(window, SHURIKEN_SMALL, center,
                     self.shuriken_rotation_angle)
        self.shuriken_rotation_angle += 3

    def update_shuriken_x(self):
        if self.shuriken_x[1] >= self.x-30 and self.shuriken_x[0] <= self.x+self.width+5:
            self.shuriken_x[0] += 10
            self.shuriken_x[1] -= 10
        else:
            self.disabled = True

    def is_pressed(self, mouse, click, action=None):
        if not self.disabled:
            if self.is_mouse_over(mouse):
                if click[0] == 1:
                    SOUNDS['button_click'].play()
                    return True


class Checkbox(Button):
    def __init__(self, x, y, is_on):
        self.x = x
        self.y = y
        self.width = CHECKBOX_WIDTH
        self.height = CHECKBOX_HEIGHT
        self.is_on = is_on
        self.click_counter = 0
        self.inactive_image = CHECKBOX_INACTIVE
        self.active_image = CHECKBOX_ACTIVE

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
                SOUNDS['button_click'].play()
                return True
