import pygame
import sys
from pygame.locals import *
from personagens import *
from elementos import *
from telas import tela_inicial, tela_menu1, tela_menu2, tela_menu3, tela_menu4, tela_menufinal, tela_derrota1, tela_derrota2, tela_derrota3, tela_derrota4, tela_derrota5, tela_vitoria1, tela_vitoria2, tela_vitoria3, tela_vitoria4, tela_vitoria5

def olinda():
    global screen
    global fullscreen
    global animacao_rolando
    screen.blit(hmn_sprites.fundo_olinda, (0,0))
    homem_da_meia_noite.draw(screen)
    homem_da_meia_noite.update()
    hmn_sprites.desenhar_barra_vida(screen)
    prota_sprites1.desenhar_barra_vida(screen)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return "tela_derrota5"
            if evento.key == pygame.K_SPACE:
                if animacao_rolando:
                    continue
                if not dado9.girando and not dado10.girando:
                    dado9.rodando()
                    dado10.rodando()
                    continue
                if  dado10.girando and dado10.girando:    
                    dado9.selecionar()
                    dado10.selecionar()
                    animacao_rolando = True
                    if dado9.valor > dado10.valor:
                        if dado9.valor - dado10.valor <= 5:
                            prota_sprites1.damage = 5
                        elif dado9.valor - dado10.valor <= 10:
                            prota_sprites1.damage = 10
                        elif dado9.valor - dado10.valor <= 18:
                            prota_sprites1.damage = 15
                        else:
                            prota_sprites1.damage = 20
                        magia_hmn.ativar()
                        hmn_sprites.ataque()
                    elif dado10.valor> dado9.valor:
                        if dado10.valor - dado9.valor <= 5:
                            hmn_sprites.damage = 5
                        elif dado10.valor - dado9.valor <= 10:
                            hmn_sprites.damage = 10
                        elif dado10.valor - dado9.valor <= 18:
                            hmn_sprites.damage = 15
                        else:
                            hmn_sprites.damage = 20
                        magia_prota1.ativar()
                        prota_sprites1.ataque()
                    else:
                        animacao_rolando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((largura_screen,altura_screen), pygame.FULLSCREEN | pygame.SCALED)
                else:
                    screen = pygame.display.set_mode((largura_screen, altura_screen), pygame.SCALED)

    def liberar_rodada():
        global animacao_rolando
        animacao_rolando = False
    if hmn_sprites.vida <= 0:
        return "tela_vitoria5"
    if prota_sprites1.vida <=0:
        return "tela_derrota5"
    else:
        magia_hmn.callback_fim = lambda: liberar_rodada()
        magia_prota1.callback_fim = lambda: liberar_rodada()
        print(prota_sprites1.vida, hmn_sprites.vida)
        return "olinda"

def igarassu():
    global screen
    global fullscreen
    global animacao_rolando, estado
    screen.blit(cf_sprites.fundo_igarassu, (0,0))
    comadre_fulozinha.draw(screen)
    comadre_fulozinha.update()
    prota_sprites2.desenhar_barra_vida(screen)
    cf_sprites.desenhar_barra_vida(screen)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return "tela_derrota1"
            if evento.key == pygame.K_SPACE:
                if animacao_rolando:
                    continue
                if not dado1.girando and not dado2.girando:
                    dado1.rodando()
                    dado2.rodando()
                    continue
                if  dado1.girando and dado2.girando:    
                    dado1.selecionar()
                    dado2.selecionar()
                    animacao_rolando = True
                    if dado1.valor > dado2.valor:
                        if dado1.valor - dado2.valor <= 5:
                            prota_sprites2.damage = 5
                        elif dado1.valor - dado2.valor <= 10:
                            prota_sprites2.damage = 10
                        elif dado1.valor - dado2.valor <= 18:
                            prota_sprites2.damage = 15
                        else:
                            prota_sprites2.damage = 20
                        magia_cf.ativar()
                        cf_sprites.ataque()
                    elif dado2.valor> dado1.valor:
                        if dado2.valor - dado1.valor <= 5:
                            cf_sprites.damage = 5
                        elif dado2.valor - dado1.valor <= 10:
                            cf_sprites.damage = 10
                        elif dado2.valor - dado1.valor <= 18:
                            cf_sprites.damage = 15
                        else:
                            cf_sprites.damage = 20
                        magia_prota2.ativar()
                        prota_sprites2.ataque()
                    else:
                        animacao_rolando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((largura_screen,altura_screen), pygame.FULLSCREEN | pygame.SCALED)
                else:
                    screen = pygame.display.set_mode((largura_screen, altura_screen), pygame.SCALED)
                        
    def liberar_rodada():
        global animacao_rolando
        animacao_rolando = False

    if cf_sprites.vida <= 0:
        global passou1
        passou1 = True
        return "tela_vitoria1"
    if prota_sprites2.vida <=0:
        return "tela_derrota1"
    else:
        magia_cf.callback_fim = lambda: liberar_rodada()
        magia_prota2.callback_fim = lambda: liberar_rodada()
        print(prota_sprites2.vida, cf_sprites.vida)
        return "igarassu"

def triunfo():
    global screen
    global fullscreen
    global animacao_rolando
    screen.blit(cdt_sprites.fundo_triunfo, (0,0))
    careta_de_triunfo.draw(screen)
    careta_de_triunfo.update()
    cdt_sprites.desenhar_barra_vida(screen)
    prota_sprites3.desenhar_barra_vida(screen)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return "tela_derrota4"
            if evento.key == pygame.K_SPACE:
                if animacao_rolando:
                    continue
                if not dado3.girando and not dado4.girando:
                    dado3.rodando()
                    dado4.rodando()
                    continue
                if  dado3.girando and dado4.girando:    
                    dado3.selecionar()
                    dado4.selecionar()
                    animacao_rolando = True
                    if dado3.valor > dado4.valor:
                        if dado3.valor - dado4.valor <= 5:
                            prota_sprites3.damage = 5
                        elif dado3.valor - dado4.valor <= 10:
                            prota_sprites3.damage = 10
                        elif dado3.valor - dado4.valor <= 18:
                            prota_sprites3.damage = 15
                        else:
                            prota_sprites3.damage = 20
                        magia_cdt.ativar()
                        cdt_sprites.ataque()
                    if dado4.valor> dado3.valor:
                        if dado4.valor - dado3.valor <= 5:
                            cdt_sprites.damage = 5
                        elif dado4.valor - dado3.valor <= 10:
                            cdt_sprites.damage = 10
                        elif dado4.valor - dado3.valor <= 18:
                            cdt_sprites.damage = 15
                        else:
                            cdt_sprites.damage = 20
                        magia_prota3.ativar()
                        prota_sprites3.ataque()
                    else:
                        animacao_rolando = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((largura_screen,altura_screen), pygame.FULLSCREEN | pygame.SCALED)
                else:
                    screen = pygame.display.set_mode((largura_screen, altura_screen), pygame.SCALED)

    def liberar_rodada():
        global animacao_rolando
        animacao_rolando = False
    if cdt_sprites.vida <= 0:
        global passou4 
        passou4 = True
        return "tela_vitoria4"
    if prota_sprites3.vida <=0:
        return "tela_derrota4"
    else:
        magia_cdt.callback_fim = lambda: liberar_rodada()
        magia_prota3.callback_fim = lambda: liberar_rodada()
        print(prota_sprites3.vida, cdt_sprites.vida)
        return "triunfo"

def recife():
    global screen
    global fullscreen
    global animacao_rolando
    screen.blit(p_sprites.fundo_recife, (0,0))
    papangu.draw(screen)
    papangu.update()
    p_sprites.desenhar_barra_vida(screen)
    prota_sprites5.desenhar_barra_vida(screen)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                    return "tela_derrota3"
            if evento.key == pygame.K_SPACE:
                if animacao_rolando:
                    continue
                if not dado7.girando and not dado8.girando:
                    dado7.rodando()
                    dado8.rodando()
                    continue
                if  dado7.girando and dado8.girando:    
                    dado7.selecionar()
                    dado8.selecionar()
                    animacao_rolando = True
                    if dado7.valor > dado8.valor:
                        if dado7.valor - dado8.valor <= 5:
                            prota_sprites5.damage = 5
                        elif dado7.valor - dado8.valor <= 10:
                            prota_sprites5.damage = 10
                        elif dado7.valor - dado8.valor <= 18:
                            prota_sprites5.damage = 15
                        else:
                            prota_sprites5.damage = 20
                        magia_p.ativar()
                        p_sprites.ataque()
                    elif dado8.valor> dado7.valor:
                        if dado8.valor - dado7.valor <= 5:
                            p_sprites.damage = 5
                        elif dado8.valor - dado7.valor <= 10:
                            p_sprites.damage = 10
                        elif dado8.valor - dado7.valor <= 18:
                            p_sprites.damage = 15
                        else:
                            p_sprites.damage = 20
                        magia_prota5.ativar()
                        prota_sprites5.ataque()
                    else:
                        animacao_rolando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((largura_screen,altura_screen), pygame.FULLSCREEN | pygame.SCALED)
                else:
                    screen = pygame.display.set_mode((largura_screen, altura_screen), pygame.SCALED)

    def liberar_rodada():
        global animacao_rolando
        animacao_rolando = False
    if p_sprites.vida <= 0:
        global passou3
        passou3 = True
        return "tela_vitoria3"
    if prota_sprites5.vida <=0:
        return "tela_derrota3"
    else:
        magia_p.callback_fim = lambda: liberar_rodada()
        magia_prota5.callback_fim = lambda: liberar_rodada()
        print(prota_sprites5.vida, p_sprites.vida)
        return "recife"

def arena():
    global screen
    global fullscreen
    global animacao_rolando
    screen.blit(tdf_sprites.fundo_arena, (0,0))
    trio_de_ferro.draw(screen)
    trio_de_ferro.update()
    tdf_sprites.desenhar_barra_vida(screen)
    prota_sprites4.desenhar_barra_vida(screen)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return "tela_derrota2"
            if evento.key == pygame.K_SPACE:
                if animacao_rolando:
                    continue
                if not dado5.girando and not dado6.girando:
                    dado5.rodando()
                    dado6.rodando()
                    continue
                if  dado5.girando and dado6.girando:    
                    dado5.selecionar()
                    dado6.selecionar()
                    animacao_rolando = True
                    if dado5.valor > dado6.valor:
                        if dado5.valor - dado6.valor <= 5:
                            prota_sprites4.damage = 5
                        elif dado5.valor - dado6.valor <= 10:
                            prota_sprites4.damage = 10
                        elif dado5.valor - dado6.valor <= 18:
                            prota_sprites4.damage = 15
                        else:
                            prota_sprites4.damage = 20
                        magia_tdf.ativar()
                        tdf_sprites.ataque()
                    elif dado6.valor> dado5.valor:
                        if dado6.valor - dado5.valor <= 5:
                            tdf_sprites.damage = 5
                        elif dado6.valor - dado5.valor <= 10:
                            tdf_sprites.damage = 10
                        elif dado6.valor - dado5.valor <= 18:
                            tdf_sprites.damage = 15
                        else:
                            tdf_sprites.damage = 20
                        magia_prota4.ativar()
                        prota_sprites4.ataque()
                    else:
                        animacao_rolando = False
                
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((largura_screen,altura_screen), pygame.FULLSCREEN | pygame.SCALED)
                else:
                    screen = pygame.display.set_mode((largura_screen, altura_screen), pygame.SCALED)

    def liberar_rodada():
        global animacao_rolando
        animacao_rolando = False

    if tdf_sprites.vida <= 0:
        global passou2 
        passou2 = True
        return "tela_vitoria2"
    if prota_sprites4.vida <=0:
        return "tela_derrota2"
    else:
        magia_tdf.callback_fim = lambda: liberar_rodada()
        magia_prota4.callback_fim = lambda: liberar_rodada()
        print(prota_sprites4.vida, tdf_sprites.vida)
        return "arena"

########################################## CRIAÇÃO DA JANELA ###########################################
pygame.init()
clock = pygame.time.Clock() # Método usado para definir a taxa de atualização do jogo enquanto funciona
animacao_rolando = False
largura_screen = 1280
altura_screen = 720
screen = pygame.display.set_mode((largura_screen, altura_screen))
fullscreen = False
pygame.display.set_caption('Meia-Noite do Terror')
ATAQUE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ATAQUE_EVENT, 6000)

grupo_dado = pygame.sprite.Group()
grupo_magia = pygame.sprite.Group()
##################################### CRIANDO O HOMEM DA MEIA-NOITE ####################################
homem_da_meia_noite = pygame.sprite.Group() # Cria um grupo para armazenar as sprites
hmn_sprites = HomemMeiaNoite(1200, 700)
prota_sprites1 = Protagonista(400, 700)
dado9 = D20 (1100, 200)
dado10 = D20 (300, 200) 
grupo_dado.add(dado9,dado10)
magia_hmn = Magia((hmn_sprites.x_hmn - 300), (hmn_sprites.y_hmn - 200), (prota_sprites1.x_prota-170), (prota_sprites1.y_prota - 200), prota_sprites1)
magia_prota1 = Magia(prota_sprites1.x_prota, (prota_sprites1.y_prota - 150),(hmn_sprites.x_hmn - 150), (hmn_sprites.y_hmn - 150), hmn_sprites)
grupo_magia.add(magia_hmn, magia_prota1)
homem_da_meia_noite.add(hmn_sprites, prota_sprites1, grupo_dado, grupo_magia) # Adiciona as sprites no grupo

# Criando a Comadre Fulozinha
comadre_fulozinha = pygame.sprite.Group()
cf_sprites = ComadreFulozinha(1200, 700)
prota_sprites2 = Protagonista(400, 700)
dado1 = D20(1100, 200)
dado2 = D20(300, 250)
grupo_dado.remove(dado9, dado10)
grupo_dado.add(dado1, dado2)
magia_cf = Magia((cf_sprites.x_cf - 300), (cf_sprites.y_cf - 200), (prota_sprites2.x_prota-170), (prota_sprites2.y_prota - 200), prota_sprites2)
magia_prota2 = Magia(prota_sprites2.x_prota, (prota_sprites2.y_prota - 150),(cf_sprites.x_cf - 150), (cf_sprites.y_cf - 150), cf_sprites)
grupo_magia.remove(magia_hmn, magia_prota1)
grupo_magia.add(magia_cf, magia_prota2)
comadre_fulozinha.add(cf_sprites, prota_sprites2, grupo_dado, grupo_magia)

# Criando a Careta de Triunfo
careta_de_triunfo = pygame.sprite.Group()
cdt_sprites = CaretadeTriunfo(1200, 730)
prota_sprites3 = Protagonista(400, 700)
dado3 = D20(1100, 275)
dado4 = D20(300, 250)
grupo_dado.remove(dado1, dado2)
grupo_dado.add(dado3, dado4)
magia_cdt = Magia((cdt_sprites.x_cdt - 300), (cdt_sprites.y_cdt - 200), (prota_sprites3.x_prota-170), (prota_sprites3.y_prota - 200), prota_sprites3)
magia_prota3 = Magia(prota_sprites3.x_prota, (prota_sprites3.y_prota - 150),(cdt_sprites.x_cdt - 150), (cdt_sprites.y_cdt - 150), cdt_sprites)
grupo_magia.remove(magia_cf, magia_prota2)
grupo_magia.add(magia_cdt, magia_prota3)
careta_de_triunfo.add(cdt_sprites, prota_sprites3, grupo_dado, grupo_magia)

# Criando o Trio de Ferro
trio_de_ferro = pygame.sprite.Group()
tdf_sprites = TriodeFerro(1200, 700)
prota_sprites4 = Protagonista(400, 640) 
dado5 = D20(1100, 200)
dado6 = D20(300, 200)
grupo_dado.remove(dado3, dado4)
grupo_dado.add(dado5, dado6)
magia_tdf = Magia((tdf_sprites.x_tdf - 300), (tdf_sprites.y_tdf - 200), (prota_sprites4.x_prota-170), (prota_sprites4.y_prota - 140), prota_sprites4)
magia_prota4 = Magia(prota_sprites4.x_prota, (prota_sprites4.y_prota - 150),(tdf_sprites.x_tdf - 150), (tdf_sprites.y_tdf - 150),tdf_sprites)
grupo_magia.remove(magia_cdt, magia_prota3)
grupo_magia.add(magia_tdf, magia_prota4)
trio_de_ferro.add(tdf_sprites, prota_sprites4, grupo_dado, grupo_magia)

# Criando o Papangu
papangu = pygame.sprite.Group() 
p_sprites = Papangu(1200, 700)
prota_sprites5 = Protagonista(400, 680) 
dado7 = D20(1100, 200)
dado8 = D20(300, 220)
grupo_dado.remove(dado5, dado6)
grupo_dado.add(dado7, dado8)
magia_p = Magia((p_sprites.x_p - 300), (p_sprites.y_p - 200), (prota_sprites5.x_prota-170), (prota_sprites5.y_prota - 200), prota_sprites5)
magia_prota5 = Magia(prota_sprites5.x_prota, (prota_sprites5.y_prota - 150),(p_sprites.x_p - 150), (p_sprites.y_p - 150),p_sprites)
grupo_magia.remove(magia_tdf, magia_prota4)
grupo_magia.add(magia_p, magia_prota5)
papangu.add(p_sprites, prota_sprites5, grupo_dado, grupo_magia)

########################################## EXECUÇÃO DO CÓDIGO ##########################################
estado = "telainicial"
passou1 = False
passou2 = False
passou3 = False
passou4 = False
############################## LOOP PRINCIPAL QUE RODA A JANELA DO JOGO ################################ 
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a janela quando clica no X
            sys.exit()

    if estado == "telainicial":
        estado = tela_inicial()
    elif estado == "menu1":
        estado = tela_menu1()
    elif estado == "menu2":
        estado = tela_menu2()
    elif estado == "menu3":
        estado = tela_menu3()
    elif estado == "menu4":
        estado = tela_menu4()
    elif estado == "menufinal":
        estado = tela_menufinal()
    elif estado == "tela_derrota1":
        estado = tela_derrota1(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_derrota2":
        estado = tela_derrota2(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_derrota3":
        estado = tela_derrota3(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_derrota4":
        estado = tela_derrota4(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_derrota5":
        estado = tela_derrota5(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_vitoria1":
        estado = tela_vitoria1(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_vitoria2":
        estado = tela_vitoria2(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_vitoria3":
        estado = tela_vitoria3(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_vitoria4":
        estado = tela_vitoria4(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "tela_vitoria5":
        estado = tela_vitoria5(cf_sprites, tdf_sprites, p_sprites, cdt_sprites, hmn_sprites, prota_sprites1, prota_sprites2, prota_sprites3, prota_sprites4, prota_sprites5, passou1, passou2, passou3, passou4)
    elif estado == "igarassu":
        estado = igarassu()
    elif estado == "arena":
        estado = arena()
    elif estado == "recife":
        estado = recife()
    elif estado == "triunfo":
        estado = triunfo()
    elif estado == "olinda":
        estado = olinda()
    pygame.display.update() # Atualiza a janela 
    clock.tick(40) # Define o limite de 60fps para a janela