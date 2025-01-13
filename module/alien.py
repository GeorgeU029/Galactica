import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ This class will represent a single alien we will create mutiple but this will be how each is created"""
    def __init__(self,ai_settings,screen):
        """Initialize the alien"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the images of the setting and set there hit box
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Spawn the alien at the top left of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Keep track of the aliens exact pos in the screen
        self.x = float(self.rect.x)
    def blitme(self):
        """Draw the laien at its current locaiton."""
        self.screen.blit(self.image,self.rect)