import pygame

pygame.init()
surface = pygame.image.load('imagens/score.png')

# Set display mode
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update display
    screen.blit(surface, (0, 0))
    pygame.display.update()
