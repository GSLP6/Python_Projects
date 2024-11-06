import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600  # Set the display size to fit the image
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Realistic Spider-Man Image")

# Load the Spider-Man image
spiderman_image = pygame.image.load("spiderman_full.jpg")  # Replace with your file name

# Resize image if needed
spiderman_image = pygame.transform.scale(spiderman_image, (width, height))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display the image
    screen.blit(spiderman_image, (0, 0))
    pygame.display.update()
