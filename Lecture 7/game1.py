import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 500))  # Width: 800, Height: 600
pygame.display.set_caption("Python101 Game-1")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 127)

# Define the rectangle's initial position and size
rect_x = 50
rect_y = 50
rect_width = 60
rect_height = 60
speed_x = 3
speed_y = 3

# Game loop
clock = pygame.time.Clock()  # Control the frame rate
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update rectangle position
    rect_x += speed_x
    rect_y += speed_y

    # Boundary checking (bouncing effect)
    if rect_x > 540 or rect_x < 0:
        speed_x = -speed_x
    if rect_y > 440 or rect_y < 0:
        speed_y = -speed_y

    # Fill screen with white
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Set frame rate (60 frames per second)
    clock.tick(60)
