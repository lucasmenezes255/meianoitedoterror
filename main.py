import pygame
import sys
from pygame.locals import *
from personagens import *

def tela_inicial():
    """
    Função que exibe a tela inicial. É chamada no loop principal
    """
    tela_inicial = pygame.image.load('imagens\cenarios\meia_noite(dimensão padrao).jpg')
    screen.blit(tela_inicial, (0,0))

def olinda():
    """
    Mostra os sprites do Homem da Meia-Noite no cenário de Olinda. É chamado no loop principal
    """
    screen.blit(hmm_sprites.fundo_olinda, (0,0))
    homem_da_meia_noite.draw(screen)
    homem_da_meia_noite.update()

def igarassu():
    screen.blit(cf_sprites.fundo_igarassu, (0,0))
    comadre_fulozinha.draw(screen)
    comadre_fulozinha.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                prota_sprites.ataque()
                cf_sprites.dano()
        if evento.type == ATAQUE_EVENT:
            cf_sprites.ataque()
            prota_sprites.dano()

def triunfo():
    screen.blit(cdt_sprites.fundo_triunfo, (0,0))
    careta_de_triunfo.draw(screen)
    careta_de_triunfo.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == ATAQUE_EVENT:
            cdt_sprites.ataque()
            prota_sprites.dano()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                cdt_sprites.dano()
                prota_sprites.ataque()

def recife():
    screen.blit(p_sprites.fundo_recife, (0,0))
    papangu.draw(screen)
    papangu.update()

def arena():
    screen.blit(tdf_sprites.fundo_arena, (0,0))
    trio_de_ferro.draw(screen)
    trio_de_ferro.update()

########################################## CRIAÇÃO DA JANELA ###########################################
pygame.init()
clock = pygame.time.Clock() # Método usado para definir a taxa de atualização do jogo enquanto funciona

largura_screen = 1280
altura_screen = 720
screen = pygame.display.set_mode((largura_screen, altura_screen))
pygame.display.set_caption('Meia-Noite do Terror')
ATAQUE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ATAQUE_EVENT, 6000)

prota_sprites = Protagonista()
##################################### CRIANDO O HOMEM DA MEIA-NOITE ####################################
homem_da_meia_noite = pygame.sprite.Group() # Cria um grupo para armazenar as sprites
hmm_sprites = HomemMeiaNoite(-47,237) 
homem_da_meia_noite.add(hmm_sprites) # Adiciona as sprites no grupo

# Criando a Comadre Fulozinha
comadre_fulozinha = pygame.sprite.Group()
cf_sprites = ComadreFulozinha()
comadre_fulozinha.add(cf_sprites, prota_sprites)

# Criando a Careta de Triunfo
careta_de_triunfo = pygame.sprite.Group()
cdt_sprites = CaretadeTriunfo()
careta_de_triunfo.add(cdt_sprites, prota_sprites)

# Criando o Papangu
papangu = pygame.sprite.Group() 
p_sprites = Papangu()
papangu.add(p_sprites)

# Criando o Trio de Ferro
trio_de_ferro = pygame.sprite.Group()
tdf_sprites = TriodeFerro()
trio_de_ferro.add(tdf_sprites)

########################################## EXECUÇÃO DO CÓDIGO ##########################################
estado_tela_inicial = True # Variável de controle pra passagem da tela inicial pra próxima

############################## LOOP PRINCIPAL QUE RODA A JANELA DO JOGO ################################ 
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
    
        if evento.type == pygame.KEYDOWN:  # Verifica se alguma tecla foi pressionada
            estado_tela_inicial = False

    if estado_tela_inicial:
        tela_inicial()
    else:
        triunfo()
                
    pygame.display.update() # Atualiza a janela 
    clock.tick(60) # Define o limite de 60fps para a janela