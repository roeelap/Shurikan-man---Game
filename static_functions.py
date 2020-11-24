import pygame


def draw_circle_alpha(surface, color, center, width, height):
    target_rect = pygame.Rect(center, (0, 0)).inflate(
        (width * 2, height * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    shape_surf.set_alpha(64)
    pygame.draw.ellipse(shape_surf, color,
                        (width / 2, 4, width, height), width)
    surface.blit(shape_surf, target_rect)
