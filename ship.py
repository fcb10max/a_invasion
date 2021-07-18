import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen, sb, stats):
        super(Ship, self).__init__()

        self.sb = sb
        self.screen = screen
        self.stats = stats
        self.image = pygame.image.load("images/ship.xcf")
        self.rotated_image = pygame.transform.rotate(self.image, -90)
        self.rect = self.rotated_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_up and (self.rect.top > (2 * self.sb.score_rect.height)):
            self.y -= self.stats.ship_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom - (2 * self.sb.score_rect.height):
            self.y += self.stats.ship_speed_factor
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.rotated_image, self.rect)

    def center_ship(self):
        self.rect.left = self.screen_rect.left
        self.rect.y = self.screen_rect.centery
