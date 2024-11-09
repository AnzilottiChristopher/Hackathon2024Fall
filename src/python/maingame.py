import pygame
import sys
from camera import Camera
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from platforms import Platforms
from player import Player
from orbs import Orbs
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sustainable Hero Sidescroller")

# Setup
player = Player(100, SCREEN_HEIGHT - 150)
camera = Camera(2650, 1200)  # World size
enemies = pygame.sprite.Group(
    Enemy(700, 230, 50, 50, 1),  # x, y, width, height, speed
    Enemy(900, 230, 50, 50, 1),
    Enemy(1330, 550, 50, 50, 3),
    Enemy(2100, 550, 50, 50, 1)
)
platforms = pygame.sprite.Group(
    # main floor
    Platforms(50, 600, 3470, 20),
    # platforms in air
    Platforms(300, 500, 300, 20),
    # platforms on left wall at start
    Platforms(70, 400, 150, 20),
    Platforms(70, 300, 150, 20),
    Platforms(300, 250, 100, 20),
    Platforms(450, 150, 100, 20),
    # Air platforms
    Platforms(600, 280, 400, 20),
    Platforms(1050, 430, 200, 20),

    # Room with enemy
    Platforms(2000, 250, 500, 20)
)
walls = pygame.sprite.Group(
    # left wall
    Platforms(50, 100, 20, 500),
    # right wall
    Platforms(3500, 100, 20, 520), 
    # Air platforms
    Platforms(600, 280, 20, 240),
     # Blocking wall
    Platforms(900, 400, 20, 200),
    # Blocking wall in middle that needs to be jumped over
    Platforms(1400, 100, 20, 500),

    # Room with enemy
    Platforms(2000, 250, 20, 240),
    Platforms(2500, 250, 20, 360)
)
orbs = pygame.sprite.Group(
    # orb
    Orbs(100,200,"green"),
    Orbs(400,480,"magenta"),
    Orbs(700,200,"red"),
    Orbs(800,500,"purple"),
    Orbs(1500,500,"lightblue"),
    Orbs(2300,450,"pink")
)

all_sprites = pygame.sprite.Group(*walls, *orbs, player, *platforms, *enemies)

# Game loop
running = True
clock = pygame.time.Clock()

bg = pygame.image.load('src/resources/background.jpg')

# Font for story text
font = pygame.font.Font(None, 36)

# Story text
story_text = [
    "Welcome.",
    "Due to global industrialization and climate change,",
    "the world has lost its light.",
    "You are here on a mission to collect the light orbs,",
    "and restore the world to what it once was.",
    "",
    "",
    "It all depends on you and your mission."
]

# Timer for the splash screen (in milliseconds)
splash_duration = 3000  # 3 seconds
start_ticks = pygame.time.get_ticks()  # Start time for splash screen

# Splash screen loop
while running:

    # Check if the splash screen duration has passed
    if pygame.time.get_ticks() - start_ticks >= splash_duration:
        # Proceed to the main game loop after the splash screen
        running = False
        continue

    # Draw splash screen (story text)
    screen.fill(WHITE)  # Clear the screen
    screen.blit(bg, (0, 0))  # Background image

    # Render and display the story text
    y_offset = SCREEN_HEIGHT // 4  # Start drawing text from a quarter of the screen height
    for line in story_text:
        text = font.render(line, True, (0, 0, 0))  # Black text
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y_offset))
        y_offset += 40  # Move the next line down

    pygame.display.flip()
    clock.tick(30)  # Limit the framerate to 30 FPS



# Main game loop (this will run after the splash screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw splash screen (story text)
    screen.fill(WHITE)  # Clear the screen
    screen.blit(bg, (0, 0))  # Background image

    # Render and display the story text
    y_offset = SCREEN_HEIGHT // 4  # Start drawing text from a quarter of the screen height

    # Update player and camera
    player.update(platforms, walls, orbs)
    camera.update(player)

    # Draw everything
    screen.fill(WHITE)
    #background
    screen.blit(bg,(0,0))

    #sprites
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))  # Draw with camera offset
    for enemy in enemies:
        enemy.update(platforms)

    text_surface = font.render("Score: "+str(player.score), False, (0, 0, 0))
    screen.blit(text_surface, (0,0))

    pygame.display.flip()
    clock.tick(30)
    # win event
    if (player.score >= 6):
        running = False
        continue


# Win screen
win_text = [
    "You have collected all of the light orbs.",
    "You have saved the earth for future generations to come.",
    "Congratulations!"
]

splash_duration = 3000  # 3 seconds
start_ticks = pygame.time.get_ticks()  # Start time for splash screen

running = True
while running:

    # Check if the splash screen duration has passed
    if pygame.time.get_ticks() - start_ticks >= splash_duration:
        # Proceed to the main game loop after the splash screen
        running = False
        continue

    # Draw splash screen (story text)
    screen.fill(WHITE)  # Clear the screen
    screen.blit(bg, (0, 0))  # Background image

    # Render and display the story text
    y_offset = SCREEN_HEIGHT // 4  # Start drawing text from a quarter of the screen height
    for line in win_text:
        text = font.render(line, True, (0, 0, 0))  # Black text
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y_offset))
        y_offset += 40  # Move the next line down

    pygame.display.flip()
    clock.tick(30)  # Limit the framerate to 30 FPS
