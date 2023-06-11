import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/score.png')

def ganhou_function(tela1, resultado):
    porcentagem_acertos = (resultado[1]['acertos']/(resultado[1]['notas']/2))*100

    valor = '{0:.1f}'.format(porcentagem_acertos)
    valor = str(valor)
    texto_acertos = fontGrande.render(valor + '%',True,verde)

    state = GANHOU
    clock = pygame.time.Clock()
    while state == GANHOU:
        clock.tick(fps)  
        tela1.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = MUSICA
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        tela1.blit(bg, (0,0))

        tela1.blit(texto_acertos,(840,615))

        pygame.display.flip()
        pygame.display.update()

    return state