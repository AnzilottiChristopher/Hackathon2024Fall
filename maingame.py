import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endangered Animal Adventure")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 5

# Obstacle settings
obstacle_size = 50
obstacle_pos = [100, 100]

# Resource settings
resource_size = 30
resource_pos = [300, 300]

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < SCREEN_HEIGHT - player_size:
        player_pos[1] += player_speed

    # Collision with obstacles
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    obstacle_rect = pygame.Rect(obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size)
    resource_rect = pygame.Rect(resource_pos[0], resource_pos[1], resource_size, resource_size)

    if player_rect.colliderect(obstacle_rect):
        print("Collision with obstacle!")  # This could reduce health or restart the level

    # Collecting resources
    if player_rect.colliderect(resource_rect):
        score += 1
        print("Resource collected! Score:", score)
        resource_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]  # Move the resource or reset position

    # Draw player, obstacles, resources
    pygame.draw.rect(screen, GREEN, player_rect)
    pygame.draw.rect(screen, RED, obstacle_rect)
    pygame.draw.rect(screen, (0, 0, 255), resource_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
