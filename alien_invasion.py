from game_stats import Game_stats
import sys

import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from ship import Ship
from scoreboard import Scoreboard
from button import Button
from input_text1 import Input_text


def run_game():

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_rect = screen.get_rect()
    input_box = Input_text(screen)
    settings = Settings()
    game_stats = Game_stats(settings)
    play_button = Button(screen, "Play", 200, 50) 
    sound_button = Button(screen, "Sound: On", 200, 50) 
    scores_button = Button(screen, "Scores", 200, 50) 
    exit_button = Button(screen, "Exit", 200, 50)
    bullets = Group()
    sb = Scoreboard(screen, game_stats)
    game_stats.dynamic_stats()
    gf.prepare_scores_and_lvl(sb)
    ship = Ship(screen, sb, game_stats)
    stars = Group()
    aliens = Group()
    gf.create_stars(settings, stars, screen)
    gf.create_aliens_fleet(screen, settings, aliens, sb, game_stats)



    while True:

        if game_stats.game_active:
            screen.fill(settings.bg_color)

            sb.show_score()

            gf.draw_stars(stars)
            gf.check_events(ship, bullets, screen, settings, game_stats, play_button, sound_button, scores_button, exit_button, sb, aliens, input_box)
            gf.update_screen(bullets, sb, aliens, game_stats, screen, settings)
            ship.update()
            gf.update_aliens(aliens, settings, ship, bullets, game_stats, sb, screen, play_button, sound_button, scores_button, exit_button, input_box)
            aliens.update()
            ship.blitme()
            gf.draw_alien_fleet(aliens)

            pygame.display.flip()
        else:
            image = pygame.image.load("images/bg.gif")
            image = pygame.transform.scale(image, (int(screen_rect.width*0.33), int(screen_rect.height*0.33)))
            image_rect = image.get_rect()
            image_rect = image_rect.move(screen_rect.width * 0.33, screen_rect.height * 0.05)

            sound_button.rect.center = screen_rect.center
            sound_button.rect.y -= (sound_button.rect.height + 10)
            play_button.rect.bottom = sound_button.rect.top - 10
            play_button.rect.left = sound_button.rect.left
            scores_button.rect.top = sound_button.rect.bottom + 10 
            scores_button.rect.left = sound_button.rect.left
            exit_button.rect.top = scores_button.rect.bottom + 10
            exit_button.rect.left = scores_button.rect.left
            
            play_button.msg_image_rect.center = play_button.rect.center
            sound_button.msg_image_rect.center = sound_button.rect.center
            scores_button.msg_image_rect.center = scores_button.rect.center
            exit_button.msg_image_rect.center = exit_button.rect.center

            screen.fill(settings.bg_color)
            screen.blit(image, image_rect)
            play_button.draw_button()
            sound_button.draw_button()
            scores_button.draw_button()
            exit_button.draw_button()
            gf.check_events(ship, bullets, screen, settings, game_stats, play_button, sound_button, scores_button, exit_button, sb, aliens, input_box)
            pygame.display.flip()


run_game()
