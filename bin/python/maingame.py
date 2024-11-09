import pygame
import sys
from camera import Camera
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from platforms import Platforms
from player import Player
from orbs import Orbs

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sustainable Hero Sidescroller")

# Setup
player = Player(100, SCREEN_HEIGHT - 150)
camera = Camera(3000, 1200)  # World size
platforms = pygame.sprite.Group(
    # main floor
    Platforms(50, 600, 4000, 20),
    # platforms in air
    Platforms(300, 500, 300, 20),
    # platforms on left wall at start
    Platforms(70, 400, 150, 20),
    Platforms(70, 300, 150, 20),
    Platforms(300, 250, 100, 20),
    Platforms(450, 150, 100, 20)
)
walls = pygame.sprite.Group(
    # left wall
    Platforms(50, 100, 20, 500),
    # right wall
    Platforms(4050, 100, 20, 520), 
    # Air platforms
    Platforms(600, 280, 20, 240),
)
orbs = pygame.sprite.Group(
    # orb
    Orbs(100,200,"green")
)

all_sprites = pygame.sprite.Group(*walls, *orbs, player, *platforms)

# Game loop
running = True
clock = pygame.time.Clock()

bg = pygame.image.load('src/resources/background.jpg')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update player and camera
    player.update(platforms, walls)
    camera.update(player)

    # Draw everything
    screen.fill(WHITE)
    #background
    screen.blit(bg,(0,0))

    #sprites
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))  # Draw with camera offset

    pygame.display.flip()
    clock.tick(30)