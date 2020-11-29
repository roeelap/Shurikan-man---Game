import sys
import pygame
from consts import MENU_SHURIKEN_SMALL, SOUNDS, BUTTON_PIXEL_FONTS, COLORS, BUTTON_IMAGES, BUTTON_HEIGHTS, BUTTON_WIDTHS
from static_functions import draw_rotated, draw_rect_with_alpha


class Button:

    def __init__(self, x, y, kind, text):
        self.x = x
        self.y = y
        self.kind = kind

        self.width = BUTTON_WIDTHS[kind]
        self.height = BUTTON_HEIGHTS[kind]
        self.center = self.x + self.width // 2, self.y + self.height // 2

        self.inactive_image = BUTTON_IMAGES[kind]['inactive']
        self.active_image = BUTTON_IMAGES[kind]['active']
        self.disabled_image = BUTTON_IMAGES[kind]['disabled']

        self.inactive_text = BUTTON_PIXEL_FONTS[kind].render(
            str(text), True,  COLORS['black'])
        self.active_text = BUTTON_PIXEL_FONTS[kind].render(
            str(text), True,  COLORS['orange'])

        self.over = False
        self.clicked = False
        self.disabled = False
        self.exit = False

        self.shuriken_rotation_angle = 0
        self.shuriken_x = [self.x-30, self.x+self.width+5]
        self.display_shurikens = self.kind == 'big'

    def show(self, window, mouse):
        if self.disabled and not self.clicked:
            window.blit(self.disabled_image, (self.x, self.y))
            self.display_button_text(window, 'disabled')
            if self.exit:
                pygame.time.wait(300)
                pygame.quit()
                sys.exit()

        else:
            if self.is_mouse_over(mouse) or self.clicked:
                self.play_hover_sound()
                window.blit(self.active_image, (self.x, self.y))
                self.display_button_text(window, 'active')

                if self.display_shurikens:
                    self.shuriken_rotate_animation(
                        window, (self.shuriken_x[0], self.y+12))
                    self.shuriken_rotate_animation(
                        window, (self.shuriken_x[1], self.y+12))
            else:
                self.over = False
                window.blit(self.inactive_image, (self.x, self.y))
                self.display_button_text(window, 'inactive')

            if self.clicked:
                self.update_shuriken_x()

    def display_button_text(self, window, state):
        if state == 'disabled' or state == 'inactive':
            text_rect = self.inactive_text.get_rect()
            text_rect.center = self.center
            window.blit(self.inactive_text, text_rect)
        elif state == 'active':
            text_rect = self.active_text.get_rect()
            text_rect.center = self.center
            window.blit(self.active_text, text_rect)

    def play_hover_sound(self):
        if not self.over:
            SOUNDS['button_hover'].play()
            self.over = True

    def is_mouse_over(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True
        return False

    def is_pressed(self, mouse, click):
        if not self.disabled:
            if self.is_mouse_over(mouse):
                if click[0] == 1:
                    SOUNDS['button_click'].play()
                    return True

    def shuriken_rotate_animation(self, window, center):
        draw_rotated(window, MENU_SHURIKEN_SMALL, center,
                     self.shuriken_rotation_angle)
        self.shuriken_rotation_angle += 3

    def update_shuriken_x(self):
        self.disabled = True
        if self.shuriken_x[1] >= self.x-30 and self.shuriken_x[0] <= self.x+self.width+5:
            self.shuriken_x[0] += 10
            self.shuriken_x[1] -= 10
        else:
            self.shuriken_x = [self.x-30, self.x+self.width+5]
            self.clicked = False

    def update_location(self, x, y):
        self.x = x
        self.y = y
        self.center = self.x + self.width // 2, self.y + self.height // 2


class ArrowButton(Button):
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind

        self.width = BUTTON_WIDTHS[kind]
        self.height = BUTTON_HEIGHTS[kind]
        self.center = self.x + self.width // 2, self.y + self.height // 2

        self.inactive_image = BUTTON_IMAGES[kind]['inactive']
        self.active_image = BUTTON_IMAGES[kind]['active']
        self.disabled_image = BUTTON_IMAGES[kind]['disabled']

        self.over = False
        self.clicked = False
        self.disabled = False

    def show(self, window, mouse):
        if self.disabled:
            window.blit(self.disabled_image, (self.x, self.y))

        else:
            if self.is_mouse_over(mouse) or self.clicked:
                self.play_hover_sound()
                window.blit(self.active_image, (self.x, self.y))

            else:
                self.over = False
                window.blit(self.inactive_image, (self.x, self.y))


class Checkbox(Button):
    def __init__(self, x, y, is_on):
        self.x = x
        self.y = y
        self.width = BUTTON_WIDTHS['checkbox']
        self.height = BUTTON_HEIGHTS['checkbox']
        self.is_on = is_on
        self.click_counter = 0
        self.inactive_image = BUTTON_IMAGES['checkbox']['inactive']
        self.active_image = BUTTON_IMAGES['checkbox']['active']

    def show(self, window, mouse):
        if self.click_counter > 0:
            self.click_counter -= 1

        if self.is_on:
            window.blit(self.active_image, (self.x, self.y))
        else:
            window.blit(self.inactive_image, (self.x, self.y))

        if not self.is_mouse_over(mouse):
            self.over = False

    def is_pressed(self, mouse, click):
        if self.is_mouse_over(mouse):
            if click[0] == 1 and self.click_counter == 0:
                if self.is_on:
                    self.is_on = False
                else:
                    self.is_on = True
                self.click_counter = 7
                SOUNDS['button_click'].play()
                return True


class ScrollBar:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (self.x, self.y, self.width, self.height)
        self.color = color
        self.is_full_length = False
        self.is_dragged = False
        self.clicked = False

    def show(self, window, mouse):
        if self.is_mouse_over(mouse) or self.clicked:
            draw_rect_with_alpha(self.x, self.y, self.width,
                                 self.height, self.color, 255, window, 15)
        else:
            draw_rect_with_alpha(self.x, self.y, self.width,
                                 self.height, self.color, 128, window, 15)

    def is_mouse_over(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True
        return False

    def is_pressed(self, mouse, click):
        if not self.is_full_length:
            if self.is_mouse_over(mouse):
                if click[0] == 1:
                    self.clicked = True
                    return True
            else:
                self.clicked = False
