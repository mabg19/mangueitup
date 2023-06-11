# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from ganhou import ganhou_function
from main_menu import main_menu
from jogo import game
from selecao_musica import cardapio


#======= inicialização =======#
pygame.init()
pygame.font.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Mangue It Up')

state = INIT
# try:
while state != QUIT:
    if state == INIT:
        state = main_menu(window) 
    if state == MUSICA:
        state = cardapio(window)
    if state[0] == 2:
        state = game(window)
        dados = state
    if dados[0] == 3:
        state = ganhou_function(window,dados)
# except:
#     print('Jogo finalizado.')

# ===== Finalização ===== 
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados