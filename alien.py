import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, settings, stats):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.image = pygame.image.load("images/giphy.xcf")
        self.alien_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect = self.alien_rect

    def draw_alien(self):
        self.screen.blit(self.image, self.alien_rect)

    def update(self):
        self.alien_rect.y += (self.stats.alien_speed_factor *
        self.settings.fleet_direction)

