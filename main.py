import pygame
import sys
from personagens import HomemMeiaNoite

def tela_inicial():
    """
    Função que exibe a tela inicial. É chamada no loop principal
    """
    tela_inicial = pygame.image.load('cenarios/meia_noite.png')
    screen.blit(tela_inicial, (0,0))

def olinda():
    """
    Mostra os sprites do Homem da Meia-Noite no cenário de Olinda. É chamado no loop principal
    """
    screen.blit(hmm_sprites.fundo_olinda, (0,0))
    homem_da_meia_noite.draw(screen)
    homem_da_meia_noite.update()

########################################## CRIAÇÃO DA JANELA ###########################################
pygame.init()
clock = pygame.time.Clock() # Método usado para definir a taxa de atualização do jogo enquanto funciona

largura_screen = 700
altura_screen = 900
screen = pygame.display.set_mode((largura_screen, altura_screen))
pygame.display.set_caption('Meia-Noite do Terror')

##################################### CRIANDO O HOMEM DA MEIA-NOITE ####################################
homem_da_meia_noite = pygame.sprite.Group() # Cria um grupo para armazenar as sprites
hmm_sprites = HomemMeiaNoite(-47,237) 
homem_da_meia_noite.add(hmm_sprites) # Adiciona as sprites no grupo

########################################## EXECUÇÃO DO CÓDIGO ##########################################
estado_tela_inicial = True # Variável de controle pra passagem da tela inicial pra próxima

############################## LOOP PRINCIPAL QUE RODA A JANELA DO JOGO ################################ 
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
    
        if evento.type == pygame.KEYDOWN:  # Verifica se alguma tecla foi pressionada
            if evento.key == pygame.K_RETURN and estado_tela_inicial:
                estado_tela_inicial = False

    if estado_tela_inicial:
        tela_inicial()
    else:
        olinda()
                
    pygame.display.update() # Atualiza a janela 
    clock.tick(60) # Define o limite de 60fps para a janela