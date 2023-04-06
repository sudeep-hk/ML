import pygame
import random

pygame.init()

# Screen size
WIDTH = 288
HEIGHT = 512

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bg_image = pygame.image.load("background.png").convert()
bird_image = pygame.image.load("bird.png").convert_alpha()
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# Bird position and movement
bird_x = 50
bird_y = 200
bird_y_speed = 0

# Pipe position and movement
pipe_x = WIDTH
pipe_y = random.randint(50, 350)
pipe_speed = 2

# Score
score = 0
font = pygame.font.Font(None, 30)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_speed = -6
    
    # Update bird position and movement
    bird_y_speed += 0.2
    bird_y += bird_y_speed
    
    # Update pipe position
    pipe_x -= pipe_speed
    if pipe_x < -50:
        pipe_x = WIDTH
        pipe_y = random.randint(50, 350)
        score += 1
    
    # Check for collisions
    if bird_y < 0 or bird_y > HEIGHT or (bird_x+40 > pipe_x and bird_x < pipe_x+50 and bird_y-30 < pipe_y or bird_x+40 > pipe_x and bird_x < pipe_x+50 and bird_y+20 > pipe_y+150):
        running = False
    
    # Draw everything
    screen.blit(bg_image, (0, 0))
    screen.blit(bird_image, (bird_x, bird_y))
    screen.blit(pipe_image, (pipe_x, pipe_y))
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

# Quit pygame
pygame.quit()