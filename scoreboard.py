import pygame
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():

    def __init__(self, screen, stats):
        self.screen = screen
        self.stats = stats
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = "white"
        self.bg_color = "blue"
    
    def prep_score(self):
        formatted_score = "Score: {:,}".format(self.stats.score)
        self.score_image = self.font.render(formatted_score, True,
            self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x, self.score_rect.y = 10,10

    def show_score(self):
        self.draw_background()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
            """Show how many ships are left."""
            self.ships = Group()
            for ship_number in range(self.stats.ships_left):
                ship = Ship(self.screen, self.stats, self)
                ship.rect.x = (self.screen_rect.width - (ship.rect.width * (2+ship_number)))
                ship.rect.y = 5
                self.ships.add(ship)

    def prep_high_score(self):
        formatted_score = "High score: {:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(formatted_score, True,
            self.text_color, self.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left, self.high_score_rect.y = self.score_rect.left, (self.screen_rect.height - (1.5 * self.score_rect.height))

    def prep_lvl(self):
        formatted_lvl = "Level: {:,}".format(self.stats.lvl)
        self.lvl_image = self.font.render(formatted_lvl, True,
            self.text_color, self.bg_color)
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.x, self.lvl_rect.y = (self.screen_rect.width - (1.5 * self.lvl_rect.width)), self.high_score_rect.y

    def prep_background(self):
        self.top_bg_rect = pygame.Rect(0, 0, self.screen_rect.width, (self.score_rect.height * 2))
        self.bottom_bg_rect = pygame.Rect(0, (self.screen_rect.height - (2 * self.score_rect.height + 5)), self.screen_rect.width, (self.score_rect.height * 2))

    def draw_background(self):
        self.screen.fill("blue", self.top_bg_rect)
        self.screen.fill("blue", self.bottom_bg_rect)