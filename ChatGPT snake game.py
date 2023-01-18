import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
win_size = (500, 500)

# Create the window
screen = pygame.display.set_mode(win_size)

# Set the title of the window
pygame.display.set_caption("Kill me")

# Set the size of the snake
block_size = 10

# Set the snake's starting position
snake_pos = [250, 250]

# Set the snake's starting speed
snake_speed = 10

# Set the snake's initial direction
snake_dir = "right"

# Set the food's starting position
food_pos = [random.randint(0, win_size[0] / block_size) * block_size,
            random.randint(0, win_size[1] / block_size) * block_size]

# Set the initial length of the snake
snake_length = 1

# Run the game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the snake
    if snake_dir == "right":
        snake_pos[0] += snake_speed
    elif snake_dir == "left":
        snake_pos[0] -= snake_speed
    elif snake_dir == "up":
        snake_pos[1] -= snake_speed
    elif snake_dir == "down":
        snake_pos[1] += snake_speed

    # Check if the snake has hit the edge of the screen
    if snake_pos[0] >= win_size[0] or snake_pos[0] < 0 or snake_pos[1] >= win_size[1] or snake_pos[1] < 0:
        game_over = True

    # Check if the snake has hit the food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        # Increase the length of the snake
        snake_length += 1

        # Move the food to a new location
        food_pos = [random.randint(0, win_size[0] / block_size) * block_size,
                    random.randint(0, win_size[1] / block_size) * block_size]

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the snake
    for i in range(snake_length):
        pygame.draw.rect(screen, (0, 0, 0), (snake_pos[0], snake_pos[1] + (i * block_size), block_size, block_size))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), (food_pos[0], food_pos[1], block_size, block_size))

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
