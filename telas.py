import pygame
import sys
from pygame.locals import *

largura_screen = 1280
altura_screen = 720
screen = pygame.display.set_mode((largura_screen, altura_screen))

def tela_inicial():
    """
    Função que exibe a tela inicial. É chamada no loop principal
    """
    tela_inicial = pygame.image.load('imagens/telas/meia_noite(dimensão padrao).jpg')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:  # Verifica se alguma tecla foi pressionada
            if evento.key == pygame.K_RETURN:
                return "menu1"
            
    pygame.display.update()
    return "telainicial"

def tela_menu1():
    """
    Função que exibe a tela inicial. É chamada no loop principal
    """
    centro = (170,370)
    circulo = pygame.draw.circle(screen, (0, 0, 255), centro, 100)
    tela_inicial = pygame.image.load('imagens/telas/menu_1.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                pos = pygame.mouse.get_pos()
                mx, my = pos
                cx, cy =centro
                distancia = ((mx - cx)**2 + (my - cy)**2)**0.5

                if distancia <= 100:
                    return "igarassu"

    pygame.display.update()
    return "menu1"

def tela_derrota():
    tela_inicial = pygame.image.load('imagens/telas/teladerrota.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                return "igarassu"

            if evento.key == pygame.K_q:
                return "menu1"

    pygame.display.update()