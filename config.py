import pygame

#============= Estados para a troca de telas =============#
INIT = 0
MUSICA = 1
GAME = 2
GANHOU = 3
QUIT = 4
PERDEU = 5

#======= variáveis e dimensões =======#
width = 1920
height = 1080

fps = 30

branco = (255,255,255)
verde = (152,215,51,255)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
laranja = (255,122,0)
transparente = (0,0,0,0)

terco = int(width/3)
sexto = int(terco/6)

linha_e_i = (terco, 0)
linha_e_f = (terco, height)

linha_d_i = (2*terco, 0)
linha_d_f = (2*terco, height)

y_teclas = 225

pygame.init()
fontMedia = pygame.font.Font('assets/font/RetroMario-Regular.otf', 50)
fontGrande = pygame.font.Font('assets/font/RetroMario-Regular.otf', 80)
fontPequena = pygame.font.Font('assets/font/RetroMario-Regular.otf', 25)

#========== Dicionário com o tempo de parada para as musicas ==========#
dicio = {'assets/musicas/maracatu_atomico.mp3':30, 'assets/musicas/risoflora.mp3':30, 'assets/musicas/a_praieira.mp3':30}

