import pygame

pygame.init()

window = pygame.display.set_mode([480, 715])
pygame.display.set_caption('Pew pew Spaceship')

# ielādējam bildi atmiņā
BACKGROUND = pygame.image.load('stars.jpg')
SPACESHIP = pygame.image.load('spaceship.png')

spaceship_x = 100
spaceship_y = 100

while True:

    # saraksts ar visiem notikumiem
    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                spaceship_y -= 15

            elif event.key == pygame.K_a:
                spaceship_x -= 15

            elif event.key == pygame.K_s:
                spaceship_y += 15

            elif event.key == pygame.K_d:
                spaceship_x += 15

    # parādam bildes
    window.blit(BACKGROUND, [0, 0])
    window.blit(SPACESHIP, [spaceship_x, spaceship_y])

    pygame.display.update()
