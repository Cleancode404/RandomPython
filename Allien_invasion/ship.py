import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """
        initialize the ship and set its starting position
        """
        self.ai_settings = ai_settings
        self.screen = screen

        #load the ship image and get its rect
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #movemnt flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        "update ship location base on the movement flag"
        #update the ship's center value, not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_soeed_factor

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_soeed_factor
        
        #update rect object from self.center
        self.rect.centerx = self.center 

    def blitme(self):
        "Draw the ship at its current location"
        self.screen.blit(self.image, self.rect)