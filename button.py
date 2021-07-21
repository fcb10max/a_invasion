import pygame.font

class Button():

    def __init__(self, screen, msg, width, height):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.msg = msg

        # Set the dimensions and properties of the button
        self.width, self.height = width, height
        self.button_color = "yellow"
        self.text_color = "black"
        self.font = pygame.font.SysFont(None, 48)

        # Build button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # The button message needs to be prepped only once.
        self.prep_msg()

    def prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
