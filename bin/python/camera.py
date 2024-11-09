# Camera class
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Offset an entity's position by the camera's position
        return entity.rect.move(self.camera_rect.topleft)

    def update(self, target):
        # Center the camera on the player
        x = -target.rect.centerx + SCREEN_WIDTH // 2
        y = -target.rect.centery + SCREEN_HEIGHT // 2

        # Limit scrolling to the edges of the world (e.g., right and bottom bounds)
        x = min(0, x)  # Don't scroll past the left edge
        y = min(0, y)  # Don't scroll past the top edge
        x = max(-(self.width - SCREEN_WIDTH), x)  # Right edge
        y = max(-(self.height - SCREEN_HEIGHT), y)  # Bottom edge

        self.camera_rect = pygame.Rect(x, y, self.width, self.height)