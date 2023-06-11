import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/mangue_inicial.png')

def main_menu(tela):
    state = INIT
    clock = pygame.time.Clock()
    while state == INIT:
        clock.tick(fps)  
        tela.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                state = MUSICA
                if event.key == pygame.K_ESCAPE:
                    state = QUIT

        tela.blit(bg, (0,0))
        pygame.display.flip()
        pygame.display.update()

    return state

