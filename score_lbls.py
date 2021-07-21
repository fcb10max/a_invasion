import pygame.font

class ScoreLabel():

    def __init__(self, screen, score, date, top):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.score = score
        self.date = date

        # Set the dimensions and properties of the button
        self.width, self.height = int(self.screen_rect.width * 0.66), 50
        self.button_color = "blue"
        self.text_color = "white"
        self.font = pygame.font.SysFont(None, 48)

        # Build button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left = self.screen_rect.width * 0.2
        self.rect.top = (self.screen_rect.height * 0.2 + 70*top)

        # The button message needs to be prepped only once.
        self.prep_msg()

    def prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.score_image = self.font.render(str(self.score), True, self.text_color, self.button_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.left = self.rect.left + 20
        
        self.date_image = self.font.render(str(self.date), True, self.text_color, self.button_color)
        self.date_image_rect = self.date_image.get_rect()
        self.date_image_rect.right = self.rect.right - 20
        self.date_image_rect.top, self.score_image_rect.top = (self.rect.top + 10), (self.rect.top + 10)


    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.date_image, self.date_image_rect)
