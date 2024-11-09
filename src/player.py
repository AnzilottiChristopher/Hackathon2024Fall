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
        self.dash_duration = 10  # Frames the dash lasts
        self.dash_cooldown = 30  # Frames before dash can be used again
        self.dash_timer = 0
        self.cooldown_timer = 0
        self.dashing = False
        self.invincible = False  # Make player invincible while dashing

        # Wall jump attributes
        self.wall_jump_height = -12  # Height for wall jump
        self.wall_jump_cooldown = 20  # Cooldown for wall jumping
        self.wall_jump_timer = 0
        self.on_wall = False  # Check if the player is touching a wall
        self.wall_side = None  # Which side of the wall (left or right)

    def update(self, platforms):
        # Get pressed keys
        keys = pygame.key.get_pressed()

        # Wall jump logic
        if self.wall_jump_timer > 0:
            self.wall_jump_timer -= 1

        if self.on_wall and keys[pygame.K_SPACE] and self.wall_jump_timer <= 0:
            # Perform the wall jump
            if self.wall_side == "left":
                self.velocity_y = self.wall_jump_height
                self.rect.x += 10  # Move slightly away from the wall (right)
            elif self.wall_side == "right":
                self.velocity_y = self.wall_jump_height
                self.rect.x -= 10  # Move slightly away from the wall (left)
            self.wall_jump_timer = self.wall_jump_cooldown  # Start cooldown

        # Horizontal movement and dash logic
        if self.dashing:
            if self.dash_direction == "left":
                self.rect.x -= self.dash_speed
            elif self.dash_direction == "right":
                self.rect.x += self.dash_speed

            # Decrease the dash timer and end dash if timer runs out
            self.dash_timer -= 1
            if self.dash_timer <= 0:
                self.dashing = False
                self.invincible = False
                self.cooldown_timer = self.dash_cooldown
        else:
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

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Check for collision with platforms and walls
        self.on_ground = False
        self.on_wall = False  # Reset wall check each frame
        self.wall_side = None  # Reset wall side

        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.on_ground = True

            # Wall detection (left and right side of player)
            if self.rect.colliderect(platform.rect) and not self.on_ground:
                if self.rect.left < platform.rect.right and self.rect.right > platform.rect.left:
                    if self.rect.top < platform.rect.bottom and self.rect.bottom > platform.rect.top:
                        if self.rect.right <= platform.rect.left:  # Wall on the left
                            self.on_wall = True
                            self.wall_side = "left"
                        elif self.rect.left >= platform.rect.right:  # Wall on the right
                            self.on_wall = True
                            self.wall_side = "right"

        # Wall jump only when not on ground
        if self.on_ground:
            self.wall_jump_timer = 0  # Reset wall jump cooldown if on the ground

        # Jump if on ground
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_height

    def start_dash(self, direction):
        """Initiate a dash in the specified direction."""
        self.dashing = True
        self.dash_timer = self.dash_duration
        self.dash_direction = direction
        self.invincible = True  # Become invincible during dash
