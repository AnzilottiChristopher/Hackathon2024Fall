# Player class
import pygame

from constants import GREEN


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 0
        self.on_ground = False
        self.on_wall = False
        self.speed = 5
        self.jump_height = -15
        self.gravity = 1

    def update(self, platforms, walls):
        # set on ground and on wall to false to begin
        self.on_ground = False
        self.on_wall = False
        # Horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Check for collision with platforms
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.on_ground = True
        # check for collision with walls and disallow it
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.on_wall = True
                self.rect.left = wall.rect.right
                self.velocity_x = 0

        # Jump if on ground
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_height