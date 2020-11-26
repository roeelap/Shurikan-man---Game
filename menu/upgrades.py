import pygame
from menu.player_stat import PlayerStat
from menu.button import Button
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, SHURIKEN_IMAGES, BACKGROUND_DUNGEON, FPS, PIXEL_FONT_BIG, COLORS, PIXEL_FONT_BIG_BUTTON

pygame.init()
pygame.display.set_caption("Shuriken Man")
pygame.display.set_icon(SHURIKEN_IMAGES['shuriken'])
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

upgrades_title_text = PIXEL_FONT_BIG.render("Upgrades", True,  COLORS['white'])
upgrades_title_textRect = upgrades_title_text.get_rect()
upgrades_title_textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 7

player_stats = [PlayerStat('max_health', SCREEN_WIDTH * 1 // 7, SCREEN_HEIGHT * 8 // 10),
                PlayerStat('speed', SCREEN_WIDTH * 2 // 7, SCREEN_HEIGHT * 8 // 10),
                PlayerStat('strength', SCREEN_WIDTH * 3 // 7, SCREEN_HEIGHT * 8 // 10),
                PlayerStat('throw_speed', SCREEN_WIDTH * 4 // 7, SCREEN_HEIGHT * 8 // 10)]

confirm_button = Button( SCREEN_WIDTH * 5 // 7, SCREEN_HEIGHT * 7 // 10, 'big', 'Confirm')

back_button = Button(
    SCREEN_WIDTH * 5 // 7, SCREEN_HEIGHT * 8 // 10, 'big', 'Back')


def redraw_upgrades_shop(mouse, player):
    window.blit(BACKGROUND_DUNGEON, (-400, 0))

    window.blit(upgrades_title_text, upgrades_title_textRect)

    for player_stat in player_stats:
        player_stat.show(window, mouse, player)

    upgrade_points = str(player.upgrade_points)
    upgrade_points_text = PIXEL_FONT_BIG_BUTTON.render('Points: ' + upgrade_points, True, COLORS['white'])
    window.blit(upgrade_points_text, (back_button.x, SCREEN_HEIGHT * 6 // 10 + 30))

    confirm_button.show(window, mouse)

    back_button.show(window, mouse)

    pygame.display.update()


def upgrades_shop(player):
    while True:
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()

                for player_stat in player_stats:
                    if player_stat.up_button.is_pressed(mouse, click):
                        player_stat.upgrade_stat(player)
                        player_stat.is_confirmed = False

                for player_stat in player_stats:
                    if player_stat.down_button.is_pressed(mouse, click):
                        player_stat.downgrade_stat(player)
                        player_stat.is_confirmed = False

                if confirm_button.is_pressed(mouse, click):
                    for player_stat in player_stats:
                        player_stat.is_confirmed = True

                if back_button.is_pressed(mouse, click):
                    return

        redraw_upgrades_shop(mouse, player)