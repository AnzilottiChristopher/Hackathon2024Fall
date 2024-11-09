import pygame
import sys
from camera import Camera
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from platforms import Platforms
from python.player import Player

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endangered Animal Adventure - Side Scroller")


# Setup
player = Player(100, SCREEN_HEIGHT - 150)
camera = Camera(1600, 1200)  # World size (for example, 1600x1200)
platforms = pygame.sprite.Group(
    Platforms(200, 500, 200, 20),
    Platforms(500, 400, 200, 20),
    Platforms(800, 300, 200, 20),
    Platforms(1200, 200, 200, 20),
    Platforms(50, 1000, 1000, 20),
)

all_sprites = pygame.sprite.Group(player, *platforms)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update player and camera
    player.update(platforms)
    camera.update(player)

    # Draw everything
    screen.fill(WHITE)
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))  # Draw with camera offset

    pygame.display.flip()
    clock.tick(30)