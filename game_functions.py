import sys
from time import sleep

import pygame

from bullet import Bullets
from star import Star
from alien import Alien
from button import Button


def check_keydown_events(event, ship, bullets, screen, settings, stats):
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    if event.key == pygame.K_UP:
        ship.move_up = True
    if event.key == pygame.K_SPACE and stats.ships_left>=0:
        if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullets(screen, ship, stats)
            bullets.add(new_bullet)
            if settings.sound_active:
                ship_bullet = pygame.mixer.Sound('sounds/ship_bullet.ogg')
                ship_bullet.play()


def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.move_up = False
    if event.key == pygame.K_DOWN:
        ship.move_down = False


def check_events(ship, bullets, screen, settings, stats, play_button, sound_button, scores_button, exit_button, sb, aliens, input_box):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(mouse_x, mouse_y, play_button, sound_button, scores_button, exit_button, stats, sb, screen, settings, aliens)
            if input_box.input_box.collidepoint(mouse_x, mouse_y) and stats.ships_left <= 0:
                input_box.active = True
        elif event.type == pygame.KEYDOWN:
            if input_box.active:
                if event.key == pygame.K_BACKSPACE:
                    input_box.text = input_box.text[:-1]
                else:
                    input_box.text += event.unicode
            if stats.game_active:
                check_keydown_events(event, ship, bullets, screen, settings, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_buttons(mouse_x, mouse_y, play_button, sound_button, scores_button, exit_button, stats, sb, screen, settings, aliens):
    play_button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    sound_button_clicked = sound_button.rect.collidepoint(mouse_x, mouse_y)
    scores_button_clicked = scores_button.rect.collidepoint(mouse_x, mouse_y)
    exit_button_clicked = exit_button.rect.collidepoint(mouse_x, mouse_y)

    if play_button_clicked and not stats.game_active and not stats.scores_active:
        stats.dynamic_stats()
        prepare_scores_and_lvl(sb)
        aliens.empty()
        create_aliens_fleet(screen, settings, aliens, sb, stats)
        stats.game_active = True
    elif exit_button_clicked and not stats.game_active and not stats.scores_active:
        sys.exit()
    elif sound_button_clicked and not stats.game_active and not stats.scores_active:
        if sound_button.msg =='Sound: On':
            settings.sound_active = False
            sound_button.msg = 'Sound: Off'
            sound_button.prep_msg()
            sound_button.draw_button()
            sound_button_clicked = False
        elif sound_button.msg =='Sound: Off':
            settings.sound_active = True
            sound_button.msg = 'Sound: On'
            sound_button.prep_msg()
            sound_button.draw_button()
            sound_button_clicked = False
    return

def prepare_scores_and_lvl(sb):
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_lvl()
    sb.prep_ships()
    sb.prep_background()

def show_bullet(bullets, scoreboard, aliens, stats,screen, settings):
    for bullet in bullets.sprites():
        bullet.update_bullets()
        bullet.draw_bullet()
        check_collisions(scoreboard, stats, bullets, aliens, settings, screen)
        if bullet.rect.x > screen.get_rect().right:
            bullets.remove(bullet)

def check_collisions(scoreboard, stats, bullets, aliens, settings, screen):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        if settings.sound_active:
            alien_explosion = pygame.mixer.Sound('sounds/alien_explosion.ogg')
            alien_explosion.play()
        for aliens in collisions.values():
            stats.score += stats.alien_point * len(aliens)
            check_high_score(stats)
            scoreboard.prep_score()
    if len(aliens)==0:
        bullets.empty()
        level_up(settings,stats)
        create_aliens_fleet(screen, settings, aliens, scoreboard, stats)


def update_screen(bullets, scoreboard, aliens, stats,screen, settings):
    prepare_scores_and_lvl(scoreboard)
    show_bullet(bullets, scoreboard, aliens, stats,screen, settings)
    scoreboard.show_score()


def check_high_score(stats):
    if stats.score > stats.high_score:
        stats.high_score = stats.score

def level_up(settings, stats):
    stats.alien_speed_factor *= settings.level_boost
    stats.bullet_speed_factor *= settings.level_boost
    stats.alien_point += 1
    stats.lvl += 1


def create_stars(settings, stars, screen):
    for a in range(settings.num_stars):
        star = Star(screen)
        stars.add(star)


def draw_stars(stars):
    for star in stars.sprites():
        star.draw_star()


def create_aliens_fleet(screen, settings, aliens, sb, stats):
    screen_rect = screen.get_rect()
    alien = Alien(screen, settings, stats)
    available_space_y = int((settings.screen_height -
                            alien.alien_rect.height) / (2 *
                            alien.alien_rect.height))
    available_space_x = int((settings.screen_width -
                            (8 * alien.alien_rect.width)) /
                            (2 * alien.alien_rect.width))
    for row in range(available_space_y - 1):
        for line in range(available_space_x):
            new_alien = Alien(screen, settings, stats)
            new_alien.alien_rect.x = int(screen_rect.width - (new_alien.alien_rect.width + new_alien.alien_rect.width * line * 2))
            new_alien.alien_rect.y = int(screen_rect.height - (new_alien.alien_rect.height + new_alien.alien_rect.height * row * 2) - 
            (2 * sb.score_rect.height))
            aliens.add(new_alien)


def draw_alien_fleet(aliens):
    for alien in aliens.sprites():
        alien.draw_alien()


def check_fleet_edge(aliens, ai_settings, sb, stats):
    for alien in aliens.sprites():
        if alien.alien_rect.bottom >= (alien.screen_rect.bottom - (2 * sb.score_rect.height)):
            ai_settings.fleet_direction = -1
            for alien in aliens.sprites():
                alien.alien_rect.x -= stats.alien_drop_speed
            break
        elif alien.alien_rect.top <= (2 * sb.score_rect.height):
            ai_settings.fleet_direction = 1
            for alien in aliens.sprites():
                alien.alien_rect.x -= stats.alien_drop_speed
            break


def update_aliens(aliens, ai_settings, ship, bullets, stats, scoreboard, screen, play_button, sound_button, scores_button, exit_button, input_box):
    check_fleet_edge(aliens, ai_settings, scoreboard, stats)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ship, aliens, bullets, stats, screen, ai_settings, scoreboard, play_button, sound_button, scores_button, exit_button, input_box)
    check_aliens_left = check_alien_fleet_left(aliens)
    if check_aliens_left:
        ship_hit(ship, aliens, bullets, stats, screen, ai_settings, scoreboard, play_button, sound_button, scores_button, exit_button, input_box)


    return


def check_alien_fleet_left(aliens):
    for alien in aliens.sprites():
        if alien.rect.left <= 0:
            return True


def ship_hit(ship, aliens, bullets, stats, screen, settings, sb, play_button, sound_button, scores_button, exit_button, input_box):
    if stats.ships_left > 0:
        if settings.sound_active:
            ship_explosion = pygame.mixer.Sound('sounds/ship_explosion.ogg')
            ship_explosion.play()
            sleep(2)
        else:
            sleep(1)
        stats.ships_left -= 1

        ship.center_ship()

        aliens.empty()
        bullets.empty()
        create_aliens_fleet(screen, settings, aliens, sb, stats)
    else:
        if settings.sound_active:
            ship_explosion = pygame.mixer.Sound('sounds/ship_explosion.ogg')
            ship_explosion.play()
            sleep(2)
        else:
            sleep(1)
        aliens.empty()
        bullets.empty()
        score_label = Button(screen, "Your score:{}".format(stats.score), screen.get_rect().width, 150)
        score_label.rect.center = screen.get_rect().center
        score_label.msg_image_rect.centerx = screen.get_rect().centerx
        score_label.msg_image_rect.centery = score_label.rect.centery - 40
        score_label.draw_button()
        input_box.input_box.centerx = screen.get_rect().centerx
        input_box.input_box.centery = screen.get_rect().centery + 20
        input_box.text_surface_rect = input_box.text_surface.get_rect()
        input_box.text_surface_rect.center = input_box.input_box.center
        input_box.blitme()
        print(stats.ships_left)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        stats.game_active = False
                        break
                    else:
                        check_events(ship, bullets, screen, settings, stats, play_button, sound_button, scores_button, exit_button, sb, aliens, input_box)
                        input_box.blitme()
                        pygame.display.flip()
                        continue
                pygame.display.flip()
