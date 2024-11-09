import pygame
from constants import RED
import time

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)  # Set enemy color (or load an image)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.direction = 1  # 1 for moving right, -1 for moving left
        self.health = 100  # Example health value
        self.last_update_time = time.time()  # Record the initial time
        
    def update(self, platforms):
        # Move the enemy back and forth along a platform
        self.rect.x += self.speed * self.direction

        # Get the current time
        current_time = time.time()

        # Check if 3 seconds have passed
        if current_time - self.last_update_time >= 3:
            self.direction *= -1  # Reverse direction
            self.last_update_time = current_time  # Reset the timer

    def take_damage(self, amount):
        """Reduce health when the enemy is hit."""
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Destroy the enemy sprite when its health reaches 0
