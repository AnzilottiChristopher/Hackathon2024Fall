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
        self.speed = 5
        self.jump_height = -15
        self.gravity = 1

        # Dash attributes
        self.dash_speed = 20  # Speed of the dash
        self.dash_duration = 7  # Frames the dash lasts
        self.dash_cooldown = 15  # Frames before dash can be used again
        self.dash_timer = 0
        self.cooldown_timer = 0
        self.dash_direction = None
        self.dashing = False
        self.invincible = False  # Make player invincible while dashing
        self.key_press = {}

    def update(self, platforms, walls):
        # Horizontal movement
        # Get pressed keys
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.key_press[event.key] = True
            elif event.type == pygame.KEYUP:
                self.key_press[event.key] = False

        # Normal movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Initiate dash if the shift key is pressed and cooldown allows
        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and self.cooldown_timer <= 0:
            if keys[pygame.K_LEFT]:
                self.start_dash("left")
            elif keys[pygame.K_RIGHT]:
                self.start_dash("right")

        # Cooldown management
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

        # Dash movement
        if self.dashing:
            if self.dash_timer > 0:
                if self.dash_direction == "left":
                    self.rect.x -= self.dash_speed
                elif self.dash_direction == "right":
                    self.rect.x += self.dash_speed
                    self.dash_timer -= 1
            else:
                self.dashing = False
                self.invincible = False  # Stop being invincible after the dash


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
                self.rect.left = wall.rect.right
                self.velocity_x = 0

        # Jump if on ground
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_height

    def start_dash(self, direction):
        """Initiate a dash in the specified direction."""
        self.dashing = True
        self.dash_timer = self.dash_duration
        self.dash_direction = direction
        self.invincible = True  # Become invincible during dash