# Platform class
import pygame

from constants import BLUE

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r'src/resources/tile.png').convert_alpha(), (width, height))#pygame.Surface((width, height))
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

    def create_with_argument(self, x, y, param):
        super().__init__()
        self.image = pygame.Surface((param[0], param[1]))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))