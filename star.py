import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):

    def __init__(self, screen):
        super(Star, self).__init__()
        self.image = pygame.image.load("images/star.png")
        self.star_rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.star_rect.x = int(random.randint(-10, self.screen_rect.width) + 5)
        self.star_rect.y = int(random.randint(-10, self.screen_rect.height) + 5)

    def draw_star(self):
        self.screen.blit(self.image, self.star_rect)
