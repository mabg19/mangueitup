from tkinter import RIGHT
import pygame, sys
from config import *

bgmusica = pygame.image.load('imagens/Menu_Musica_fácil.png')


def cardapio(janela):
    clock = pygame.time.Clock()
    state = MUSICA
    musica_escolhida = ''
    velocidade = 0

    while state == MUSICA:
        clock.tick(fps)  
        janela.fill((0,0,0))

        for event in pygame.event.get():
            if event.key == pygame.K_LEFT:
                musica_escolhida = 'assets/musicas/maracatu_atomico.mp3'
                velocidade = 0
                state = GAME
            if event.key == pygame.K_UP:
                musica_escolhida = 'assets/musicas/risoflora.mp3'
                velocidade = -20
                state = GAME
            if event.key == pygame.K_RIGHT:
                musica_escolhida = 'assets/musicas/a_praieira.mp3'
                velocidade = -40
                state = GAME
            if event.key == pygame.K_ESCAPE:
                state = QUIT
                pygame.quit()
                sys.exit()


        janela.blit(bgmusica, (0,0))
        pygame.display.flip()
        pygame.display.update()
        lista_return = [state, musica_escolhida, velocidade]

    return lista_return