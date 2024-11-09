# Orbs class
import pygame

class Orbs(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.image.load(r'../resources/' + color + 'Orb.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))