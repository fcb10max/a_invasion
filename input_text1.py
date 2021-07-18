import pygame
from pygame import color

class Input_text():

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.input_box = pygame.Rect(0, 0, 140, 48)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.active = False
        self.color = self.color_inactive if self.active else self.color_active
        self.text = ''
        self.text_surface = self.font.render(self.text, True, self.color)

    def blitme(self):
        width = max(200, self.text_surface.get_width()+10)
        self.input_box.w = width
        self.screen.blit(self.text_surface, (self.input_box.x+5, self.input_box.y+5))
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)