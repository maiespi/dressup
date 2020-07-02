import pygame

class Petr():
    def __init__(self,settings,screen):
        self.screen = screen
        self.settings = settings

        # load petr
        self.petr = pygame.image.load('images/Untitled_Artwork.png')

        # get petr rectangle
        self.rect = self.petr.get_rect()
        self.screen_rect = screen.get_rect()

        # start new ship at center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.petr, self.rect)