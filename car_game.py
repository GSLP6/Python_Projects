"""import pygame library, which contains all the functions needed
for creating a game such handing graphics, input and sound"""
import pygame
"""pygame.init() this initializes all the pygame modules 
it must be called before using any pygame functionalities """
# Initialize Pygame
pygame.init()

# Set up display
"""screen_width,screen_height :- both width and height sets the sixe
of the game window"""
screen_width, screen_height = 800, 600
"""creates the game window with specified size"""
screen = pygame.display.set_mode((screen_width, screen_height))
"""pygame.display.set_caption:-Sets the title of the game"""
pygame.display.set_caption("Car Movement")

#pygame.image.load:- Load car image
car_image = pygame.image.load('car.png')  # Use your own image here
#pygame.transform.scale:- resize the car image
car_image = pygame.transform.scale(car_image,(100, 50))  # Resize if needed

# Initial position of the car
car_x, car_y = 0, screen_height // 2  # Start from the left of the screen
car_speed = 5  # Speed of the car

# Run the game loop
"""A variable that controls the main game loop. When running is true
 the game continues to run"""
running = True
while running:
    for event in pygame.event.get():#this part checks for events like mouse clicks, key presses or window closing
        if event.type == pygame.QUIT:#the game ends
            running = False#which exits the loop

    # Move the car automatically to the right
    car_x += car_speed

    # If the car reaches the right edge of the screen, reset its position to the left
    if car_x > screen_width:
        car_x = -100  # Moves car offscreen to the left before reappearing

    # Fill screen with background color
    screen.fill((1, 1, 1))  # Dark green background

    # Draw the car on the screen
    screen.blit(car_image, (car_x, car_y))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
