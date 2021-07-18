import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):

    def __init__(self, screen, ship, stats):
        super(Bullets, self).__init__()
        self.stats = stats
        self.screen = screen
        self.ship_rect = ship.rect
        self.bullet_width = 15
        self.bullet_height = 10
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.x = self.ship_rect.x + 30
        self.rect.y = self.ship_rect.y + 5
        self.x = float(self.rect.x)
        self.color = 184, 22, 22
        self.rect1 = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect1.x = self.ship_rect.x + 30
        self.rect1.y = self.ship_rect.y + 45
        self.x1 = float(self.rect1.x)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect1)

    def update_bullets(self):
        self.x += self.stats.bullet_speed_factor
        self.rect.x = self.x
        self.x1 += self.stats.bullet_speed_factor
        self.rect1.x = self.x
