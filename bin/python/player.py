# Player class
import pygame

from constants import GREEN

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(r'src/resources/char_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 0
        self.velocity_x = 0
        self.on_ground = False
        self.on_wall = False
        self.speed = 5
        self.jump_height = -15
        self.jump_direction_strength = 8  # How strong the jump is when moving diagonally
        self.gravity = 1
        self.slide_speed = 2  # Speed at which the player slides down the wall

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
        # Get pressed keys
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.key_press[event.key] = True
            elif event.type == pygame.KEYUP:
                self.key_press[event.key] = False

        # Normal movement (not dashing)
        if not self.dashing:
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if keys[pygame.K_d]:
                self.rect.x += self.speed

        # Initiate dash if the shift key is pressed and cooldown allows
        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and self.cooldown_timer <= 0:
            if keys[pygame.K_a]:
                self.start_dash("left")
            elif keys[pygame.K_d]:
                self.start_dash("right")

        # Cooldown management
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

        # Dash movement
        if self.dashing:
            if self.dash_timer > 0:
                if self.dash_direction == "left":
                    self.rect.x -= self.dash_speed
                    for wall in walls:
                        if self.rect.colliderect(wall.rect):
                            self.rect.left = wall.rect.right
                            self.on_wall = True
                            break
                elif self.dash_direction == "right":
                    self.rect.x += self.dash_speed
                    for wall in walls:
                        if self.rect.colliderect(wall.rect):
                            self.rect.right = wall.rect.left
                            self.on_wall = True
                            break
                self.dash_timer -= 1
            else:
                self.dashing = False
                self.invincible = False  # Stop being invincible after the dash

        # Apply gravity if not sliding
        if not self.on_wall:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
        else:
            # Apply sliding gravity when touching wall, but only after falling (velocity_y > 0)
            if self.velocity_y > 0:
                self.velocity_y += self.slide_speed
                self.rect.y += self.velocity_y

        # Check for collision with platforms
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.on_ground = True

        # Jump if on ground
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_height

        # Wall jump handling
        if self.on_wall and keys[pygame.K_SPACE]:
            # Apply jump velocity upwards and to the right or left, depending on wall side
            if keys[pygame.K_a]:
                self.velocity_y = self.jump_height
                self.velocity_x = self.jump_direction_strength  # Move to the left
            elif keys[pygame.K_d]:
                self.velocity_y = self.jump_height
                self.velocity_x = -self.jump_direction_strength  # Move to the right
            self.on_wall = False  # Stop wall sliding once you jump

        # Check for collision with walls
        self.on_wall = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # Detect collision with wall and enable sliding if not grounded and falling (velocity_y > 0)
                if not self.on_ground and self.velocity_y > 0:
                    self.on_wall = True
                    self.velocity_y = self.slide_speed  # Begin sliding down

                    # Optional: allow horizontal movement while sliding
                    if keys[pygame.K_LEFT]:
                        self.rect.x -= self.speed
                    if keys[pygame.K_RIGHT]:
                        self.rect.x += self.speed

                # Prevent the player from going through the wall
                if self.rect.left < wall.rect.right:
                    self.rect.left = wall.rect.right
                elif self.rect.right > wall.rect.left:
                    self.rect.right = wall.rect.left

        # Prevent jumping off the wall if on the ground
        self.ability(keys)

        if self.on_ground:
            self.on_wall = False

    def start_dash(self, direction):
        """Initiate a dash in the specified direction."""
        self.dashing = True
        self.dash_timer = self.dash_duration
        self.dash_direction = direction
        self.invincible = True  # Become invincible during dash

    def ability(self, keys):
        if keys[pygame.K_i]:
            print("hi")
        elif keys[pygame.K_o]:
            print("hi")



