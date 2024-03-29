import pygame
import random

pygame.init()

window = pygame.display.set_mode([600, 450])

snake_x = 100
snake_y = 100

snake_body = []
snake_pixel = pygame.Rect(snake_x, snake_y, 20, 20)
snake_body.append(snake_pixel)

snake_length = 1

apple_x = random.randint(0, 580)
apple_y = random.randint(0, 430)

while True:
    
    # saraksts ar notikumiem
    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                snake_y -= 20

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                snake_x -= 20

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                snake_y += 20

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: 
                snake_x += 20

            new_pixel = pygame.Rect(snake_x, snake_y, 20, 20)
            snake_body.append(new_pixel)

            if len(snake_body) > snake_length:
                snake_body.pop(0)

    apple = pygame.Rect(apple_x, apple_y, 20, 20)
    snake_head = snake_body[len(snake_body) - 1]

    if snake_x < 0 or snake_x > 580 or snake_y < 0 or snake_y > 430:
        pygame.quit()

    if snake_head.collidelist(snake_body[:len(snake_body) - 1]):
        print('a')
        pygame.quit()

    if apple.colliderect(snake_head):
        snake_length += 1

        apple_x = random.randint(0, 580)
        apple_y = random.randint(0, 430)
        apple = pygame.Rect(apple_x, apple_y, 20, 20)

    window.fill([0, 0, 0])

    for pixel in snake_body:
        pygame.draw.rect(window, [13, 55, 13], pixel)

    pygame.draw.rect(window, [255, 192, 203], apple)
    pygame.display.update()
