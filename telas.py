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
    tela_inicial = pygame.image.load('imagens/telas/meia_noite.png')
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
    centro = (170,370)
    pygame.draw.circle(screen, (0, 0, 255), centro, 100)
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

def tela_menu2():
    centro = (170, 370)
    pygame.draw.circle(screen, (0, 0, 255), centro, 100)
    centro2 = (415, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro2, 100)
    tela_inicial = pygame.image.load('imagens/telas/menu_2.png')
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
                c2x, c2y =centro2
                distancia2 = ((mx - c2x)**2 + (my - c2y)**2)**0.5

                if distancia <= 100:
                    return "igarassu"
                if distancia2 <= 100:
                    return "arena"

    pygame.display.update()
    return "menu2"

def tela_menu3():
    centro = (170, 370)
    pygame.draw.circle(screen, (0, 0, 255), centro, 100)
    centro2 = (415, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro2, 100)
    centro3 = (660, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro3, 100)
    tela_inicial = pygame.image.load('imagens/telas/menu_3.png')
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
                c2x, c2y =centro2
                distancia2 = ((mx - c2x)**2 + (my - c2y)**2)**0.5
                c3x, c3y =centro3
                distancia3 = ((mx - c3x)**2 + (my - c3y)**2)**0.5

                if distancia <= 100:
                    return "igarassu"
                if distancia2 <= 100:
                    return "arena"
                if distancia3 <= 100:
                    return "recife"

    pygame.display.update()
    return "menu3"

def tela_menu4():
    centro = (170, 370)
    pygame.draw.circle(screen, (0, 0, 255), centro, 100)
    centro2 = (415, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro2, 100)
    centro3 = (660, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro3, 100)
    centro4 = (895, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro4, 100)
    tela_inicial = pygame.image.load('imagens/telas/menu_4.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                pos = pygame.mouse.get_pos()
                mx, my = pos
                cx, cy = centro
                distancia = ((mx - cx)**2 + (my - cy)**2)**0.5
                c2x, c2y = centro2
                distancia2 = ((mx - c2x)**2 + (my - c2y)**2)**0.5
                c3x, c3y = centro3
                distancia3 = ((mx - c3x)**2 + (my - c3y)**2)**0.5
                c4x, c4y = centro4
                distancia4 = ((mx - c4x)**2 + (my - c4y)**2)**0.5

                if distancia <= 100:
                    return "igarassu"
                if distancia2 <= 100:
                    return "arena"
                if distancia3 <= 100:
                    return "recife"
                if distancia4 <= 100:
                    return "triunfo"

    pygame.display.update()
    return "menu4"

def tela_menufinal():
    centro = (170, 370)
    pygame.draw.circle(screen, (0, 0, 255), centro, 100)
    centro2 = (415, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro2, 100)
    centro3 = (660, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro3, 100)
    centro4 = (895, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro4, 100)
    centro5 = (1145, 370)
    pygame.draw.circle(screen, (0, 0, 0), centro5, 100)
    tela_inicial = pygame.image.load('imagens/telas/menu_final.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                pos = pygame.mouse.get_pos()
                mx, my = pos
                cx, cy = centro
                distancia = ((mx - cx)**2 + (my - cy)**2)**0.5
                c2x, c2y = centro2
                distancia2 = ((mx - c2x)**2 + (my - c2y)**2)**0.5
                c3x, c3y = centro3
                distancia3 = ((mx - c3x)**2 + (my - c3y)**2)**0.5
                c4x, c4y = centro4
                distancia4 = ((mx - c4x)**2 + (my - c4y)**2)**0.5
                c5x, c5y = centro5
                distancia5 = ((mx - c5x)**2 + (my - c5y)**2)**0.5

                if distancia <= 100:
                    return "igarassu"
                if distancia2 <= 100:
                    return "arena"
                if distancia3 <= 100:
                    return "recife"
                if distancia4 <= 100:
                    return "triunfo"
                if distancia5 <= 100:
                    return "olinda"

    pygame.display.update()
    return "menufinal"

def tela_derrota1(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/teladerrota.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "igarassu"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"
                else:
                    return "menu1"

    pygame.display.update()
    return "tela_derrota1"

def tela_derrota2(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/teladerrota.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "arena"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"
                else:
                    return "menu1"
    pygame.display.update()
    return "tela_derrota2"

def tela_derrota3(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/teladerrota.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "recife"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"
                else:
                    return "menu1"
    pygame.display.update()
    return "tela_derrota3"

def tela_derrota4(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/teladerrota.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "triunfo"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"
                else:
                    return "menu1"
    pygame.display.update()
    return "tela_derrota4"

def tela_derrota5(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/teladerrota.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "olinda"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"
                else:
                    return "menu1"
    pygame.display.update()
    return "tela_derrota5"

def tela_vitoria1(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/telavitoria.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "igarassu"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"

    pygame.display.update()
    return "tela_vitoria1"

def tela_vitoria2(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/telavitoria.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "arena"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"

    pygame.display.update()
    return "tela_vitoria2"

def tela_vitoria3(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/telavitoria.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "recife"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"

    pygame.display.update()
    return "tela_vitoria3"

def tela_vitoria4(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/telavitoria.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "triunfo"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"

    pygame.display.update()
    return "tela_vitoria4"

def tela_vitoria5(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4):
    tela_inicial = pygame.image.load('imagens/telas/telavitoria.png')
    screen.blit(tela_inicial, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                cf_sprites.vida = 100
                prota_sprites2.vida = 100
                return "olinda"

            if evento.key == pygame.K_q:
                cf_sprites.vida = 100
                tdf_sprites.vida = 100
                p_sprites.vida = 100
                cdt_sprites.vida = 100
                hmn_sprites.vida = 100
                prota_sprites1.vida = 100
                prota_sprites2.vida = 100
                prota_sprites3.vida = 100
                prota_sprites4.vida = 100
                prota_sprites5.vida = 100
                if passou4:
                    return "menufinal"
                elif passou3:
                    return "menu4"
                elif passou2:
                    return "menu3"
                elif passou1:
                    return "menu2"

    pygame.display.update()
    return "tela_vitoria5"