# Player class
import pygame

from constants import GREEN

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.invincibility_timer = 0
        self.image = pygame.image.load(r'../resources/char_idle.png').convert_alpha()
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
        # Inside your Player class
        self.initial_y = y
        self.direction = "right"
        self.initial_x = x

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

        # Slash attributes
        self.is_slashing = False  # Track if player is slashing
        self.slash_duration = 10  # How long the slash lasts
        self.slash_timer = 0  # Timer to track slash duration

        self.score = 0

        self.health = 5

    def update(self, platforms, walls, orbs, enemies):
        # Get pressed keys
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.key_press[event.key] = True
            elif event.type == pygame.KEYUP:
                self.key_press[event.key] = False

        # Handle horizontal movement: left/right
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = "left"
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = "right"

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

        # Check for collision with orbs
        for orb in orbs:
            if self.rect.colliderect(orb.rect):
                # remove orb
                orb.kill()
                self.score += 1

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
                    if keys[pygame.K_a]:
                        self.rect.x -= self.speed
                    if keys[pygame.K_d]:
                        self.rect.x += self.speed

               # Prevent the player from going through the wall
                if self.rect.right > wall.rect.left and self.rect.left < wall.rect.left:  # Moving right
                    self.rect.right = wall.rect.left
                elif self.rect.left < wall.rect.right and self.rect.right > wall.rect.right:  # Moving left
                    self.rect.left = wall.rect.right
                

        # Prevent jumping off the wall if on the ground
        # self.ability(keys)

        if self.on_ground:
            self.on_wall = False

        if keys[pygame.K_i] and not self.is_slashing:
            self.start_slash()

        if self.is_slashing:
            self.slash_timer -= 1
            if self.slash_timer <= 0:
                self.is_slashing = False
                self.invincible = False

        if self.is_slashing:
            for enemy in enemies:
                if self.rect.colliderect(enemy.rect):
                    enemy.take_damage(1)  # Call the kill method of the enemy

        # if not self.is_slashing and not self.dashing:
        #     for enemy in enemies:
        #         if self.rect.colliderect(enemy.rect):
        #             # Handle player getting hurt by enemy when not slashing
        #             self.take_damage(1)
        #             self.invincible = True
        #
        # if self.invincible:
        #     self.invincibility_timer += 1
        #     if self.invincibility_timer >= 360:  # 180 frames = 3 seconds at 60 FPS
        #         self.invincible = False
        #         self.invincibility_timer = 0  # Reset the timer






    def start_dash(self, direction):
        """Initiate a dash in the specified direction."""
        self.dashing = True
        self.dash_timer = self.dash_duration
        self.dash_direction = direction
        self.invincible = True  # Become invincible during dash

    def start_slash(self):
        """Start the slash action."""
        self.is_slashing = True
        self.slash_timer = self.slash_duration  # Set the slash duration
        print("Slash")

    def take_damage(self, amount):
        self.health -= amount

        if(self.health <= 0):
            self.kill()
