import pygame
from pygame.locals import *

class HomemMeiaNoite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/hmn-sprites/hmn_ocio.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.fundo_olinda = pygame.image.load('imagens/cenarios/olinda(redimensionada).png')
        self.fundo_olinda = pygame.transform.scale(self.fundo_olinda, (1286,724))
        self.atacando = False
        self.sofrendo = False
        self.rect = self.image.get_rect()
        self.x_hmn = x
        self.y_hmn = y
        self.rect.bottomright = (self.x_hmn, self.y_hmn)
        self.vida = 100
        self.damage = 10

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.06
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
        elif self.atacando:
            self.atual = self.atual + 0.07
            if self.atual>= len(self.sprites_ataque):
                self.atual = 0
                self.atacando = False
            self.image = self.sprites_ataque[int(self.atual)]
        else:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_olinda = pygame.transform.scale(self.fundo_olinda, (1286,724))
    
    def ataque(self):
        self.sprites_ataque = []
        self.sprites_ataque.append(pygame.image.load('imagens/hmn-sprites/hmn_ataque.png'))
        self.atual = 0
        self.image = self.sprites_ataque[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_olinda = pygame.image.load('imagens/cenarios/olinda(redimensionada).png')
        self.fundo_olinda = pygame.transform.scale(self.fundo_olinda, (1286,724))

        self.atacando = True

    def dano(self):
        self.sprites_dano = []
        self.sprites_dano.append(pygame.image.load('imagens/hmn-sprites/hmn_dano.png'))
        self.atual = 0
        self.image = self.sprites_dano[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_olinda = pygame.image.load('imagens/cenarios/olinda(redimensionada).png')
        self.fundo_olinda = pygame.transform.scale(self.fundo_olinda, (1286,724))
        self.vida = self.vida - self.damage
        self.atacando = False
        self.sofrendo = True

    def desenhar_barra_vida(self, screen, x = 810, y = 20, vida_maxima = 100, largura=400, altura=20, cor=(0,255,0)):
        if self.vida < 0:
            self.vida = 0
        if self.vida > vida_maxima:
            self.vida = vida_maxima

        proporcao = self.vida / vida_maxima
        barra_cheia = int(largura * proporcao)

        pygame.draw.rect(screen, (255, 0, 0), (x, y, largura, altura))
        pygame.draw.rect(screen, cor, (x, y, barra_cheia, altura))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, largura, altura), 2)

class ComadreFulozinha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/cf-sprites/fulozinha_ocio1.png'))
        self.sprites.append(pygame.image.load('imagens/cf-sprites/fulozinha_ocio2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_igarassu = pygame.image.load('imagens/cenarios/igarassu(redimensionada).png')
        self.atacando = False
        self.sofrendo = False
        self.rect = self.image.get_rect()
        self.x_cf = x
        self.y_cf = y
        self.rect.bottomright = self.x_cf, self.y_cf
        self.vida = 100
        self.damage = 10

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.06
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
        elif self.atacando:
            self.atual = self.atual + 0.07
            if self.atual>= len(self.sprites_ataque):
                self.atual = 0
                self.atacando = False
            self.image = self.sprites_ataque[int(self.atual)]
        else:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (320,320))

    def ataque(self):
        self.sprites_ataque = []
        self.sprites_ataque.append(pygame.image.load('imagens/cf-sprites/fulozinha_ataque3.png'))
        self.atual = 0
        self.image = self.sprites_ataque[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_igarassu = pygame.image.load('imagens/cenarios/igarassu(redimensionada).png')
    
        self.atacando = True

    def dano(self):
        self.sprites_dano = []
        self.sprites_dano.append(pygame.image.load('imagens/cf-sprites/fulozinha_dano.png'))
        self.atual = 0
        self.image = self.sprites_dano[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_igarassu = pygame.image.load('imagens/cenarios/igarassu(redimensionada).png')
        self.vida = self.vida - self.damage
        self.atacando = False
        self.sofrendo = True

    def desenhar_barra_vida(self, screen, x = 810, y = 20, vida_maxima = 100, largura=400, altura=20, cor=(0,255,0)):
        if self.vida < 0:
            self.vida = 0
        if self.vida > vida_maxima:
            self.vida = vida_maxima

        proporcao = self.vida / vida_maxima
        barra_cheia = int(largura * proporcao)

        pygame.draw.rect(screen, (255, 0, 0), (x, y, largura, altura))
        pygame.draw.rect(screen, cor, (x, y, barra_cheia, altura))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, largura, altura), 2)

class CaretadeTriunfo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/cdt-sprites/careta_ocio.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_triunfo = pygame.image.load('imagens/cenarios/triunfo(redimensionada).png')
        self.atacando = False
        self.sofrendo = False
        self.rect = self.image.get_rect()
        self.x_cdt = x
        self.y_cdt = y
        self.rect.bottomright = self.x_cdt, self.y_cdt
        self.vida = 100
        self.damage = 10


    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.06
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
        elif self.atacando:
            self.atual = self.atual + 0.07
            if self.atual>= len(self.sprites_ataque):
                self.atual = 0
                self.atacando = False
            self.image = self.sprites_ataque[int(self.atual)]
        else:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (320,320))

    def ataque(self):
        self.sprites_ataque = []
        self.sprites_ataque.append(pygame.image.load('imagens/cdt-sprites/careta_ataque1.png'))
        self.sprites_ataque.append(pygame.image.load('imagens/cdt-sprites/careta_ataque2.png'))
        self.atual = 0
        self.image = self.sprites_ataque[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_triunfo = pygame.image.load('imagens/cenarios/triunfo(redimensionada).png')
    
        self.atacando = True

    def dano(self):
        self.sprites_dano = []
        self.sprites_dano.append(pygame.image.load('imagens/cdt-sprites/careta_dano.png'))
        self.atual = 0
        self.image = self.sprites_dano[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_triunfo = pygame.image.load('imagens/cenarios/triunfo(redimensionada).png')
        self.vida = self.vida - self.damage
        self.atacando = False
        self.sofrendo = True

    def desenhar_barra_vida(self, screen, x = 810, y = 20, vida_maxima = 100, largura=400, altura=20, cor=(0,255,0)):
        if self.vida < 0:
            self.vida = 0
        if self.vida > vida_maxima:
            self.vida = vida_maxima

        proporcao = self.vida / vida_maxima
        barra_cheia = int(largura * proporcao)

        pygame.draw.rect(screen, (255, 0, 0), (x, y, largura, altura))
        pygame.draw.rect(screen, cor, (x, y, barra_cheia, altura))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, largura, altura), 2)

class Papangu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/p-sprites/Papangu (2)(redimensionada).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_recife = pygame.image.load('imagens/cenarios/Recife(redimensionada).png')
        self.atacando = False
        self.sofrendo = False
        self.rect = self.image.get_rect()
        self.x_p = x
        self.y_p = y
        self.rect.bottomright = self.x_p, self.y_p
        self.vida = 100
        self.damage = 10

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.06
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
        elif self.atacando:
            self.atual = self.atual + 0.07
            if self.atual>= len(self.sprites_ataque):
                self.atual = 0
                self.atacando = False
            self.image = self.sprites_ataque[int(self.atual)]
        else:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (320,320))

    def ataque(self):
        self.sprites_ataque = []
        self.sprites_ataque.append(pygame.image.load('imagens/p-sprites/papangu2.png'))
        self.atual = 0
        self.image = self.sprites_ataque[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_recife = pygame.image.load('imagens/cenarios/Recife(redimensionada).png')
    
        self.atacando = True

    def dano(self):
        self.sprites_dano = []
        self.sprites_dano.append(pygame.image.load('imagens/p-sprites/papangu_dano.png'))
        self.atual = 0
        self.image = self.sprites_dano[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_recife = pygame.image.load('imagens/cenarios/Recife(redimensionada).png')
        self.vida = self.vida - self.damage
        self.atacando = False
        self.sofrendo = True

    def desenhar_barra_vida(self, screen, x = 810, y = 20, vida_maxima = 100, largura=400, altura=20, cor=(0,255,0)):
        if self.vida < 0:
            self.vida = 0
        if self.vida > vida_maxima:
            self.vida = vida_maxima

        proporcao = self.vida / vida_maxima
        barra_cheia = int(largura * proporcao)

        pygame.draw.rect(screen, (255, 0, 0), (x, y, largura, altura))
        pygame.draw.rect(screen, cor, (x, y, barra_cheia, altura))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, largura, altura), 2)

class TriodeFerro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/tdf-sprites/mascotes_ocio.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_arena = pygame.image.load('imagens/cenarios/arena(redimensionada).png')
        self.atacando = False
        self.sofrendo = False
        self.rect = self.image.get_rect()
        self.x_tdf = x
        self.y_tdf = y
        self.rect.bottomright = self.x_tdf, self.y_tdf
        self.vida = 100
        self.damage = 10

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.06
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
        elif self.atacando:
            self.atual = self.atual + 0.07
            if self.atual>= len(self.sprites_ataque):
                self.atual = 0
                self.atacando = False
            self.image = self.sprites_ataque[int(self.atual)]
        else:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (320,320))

    def ataque(self):
        self.sprites_ataque = []
        self.sprites_ataque.append(pygame.image.load('imagens/tdf-sprites/mascotes_ataque1.png'))
        self.sprites_ataque.append(pygame.image.load('imagens/tdf-sprites/mascotes_ataque2.png'))
        self.atual = 0
        self.image = self.sprites_ataque[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_arena = pygame.image.load('imagens/cenarios/arena(redimensionada).png')
    
        self.atacando = True

    def dano(self):
        self.sprites_dano = []
        self.sprites_dano.append(pygame.image.load('imagens/tdf-sprites/mascotes_dano.png'))
        self.atual = 0
        self.image = self.sprites_dano[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_arena = pygame.image.load('imagens/cenarios/arena(redimensionada).png')
        self.vida = self.vida - self.damage
        self.atacando = False
        self.sofrendo = True

    def desenhar_barra_vida(self, screen, x = 810, y = 20, vida_maxima = 100, largura=400, altura=20, cor=(0,255,0)):
        if self.vida < 0:
            self.vida = 0
        if self.vida > vida_maxima:
            self.vida = vida_maxima

        proporcao = self.vida / vida_maxima
        barra_cheia = int(largura * proporcao)

        pygame.draw.rect(screen, (255, 0, 0), (x, y, largura, altura))
        pygame.draw.rect(screen, cor, (x, y, barra_cheia, altura))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, largura, altura), 2)

class Protagonista(pygame.sprite.Sprite):
    def __init__(self, x_prota, y_prota):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/protagonista-sprites/prota_ocio1.png'))
        self.sprites.append(pygame.image.load('imagens/protagonista-sprites/prota_ocio2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.atacando = False
        self.sofrendo = False
        self.rect = self.image.get_rect()
        self.x_prota = x_prota
        self.y_prota = y_prota
        self.rect.bottomright = self.x_prota, self.y_prota
        self.vida = 100
        self.damage = 10

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.06
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
            
        elif self.atacando:
            self.atual = self.atual + 0.08
            if self.atual>= len(self.sprites_ataque):
                self.atual = 0
                self.atacando = False
            self.image = self.sprites_ataque[int(self.atual)]
        else:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (320,320))

    def ataque(self):
        self.sprites_ataque = []
        self.sprites_ataque.append(pygame.image.load('imagens/protagonista-sprites/prota_ataque.png'))
        self.atual = 0
        self.image = self.sprites_ataque[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
    
        self.atacando = True
    
    def dano(self):
        self.sprites_dano = []
        self.sprites_dano.append(pygame.image.load('imagens/protagonista-sprites/prota_dano.png'))
        self.atual = 0
        self.image = self.sprites_dano[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.vida = self.vida - self.damage
        self.atacando = False
        self.sofrendo = True

    def desenhar_barra_vida(self, screen, x = 70, y = 20, vida_maxima = 100, largura=400, altura=20, cor=(0,255,0)):
        if self.vida < 0:
            self.vida = 0
        if self.vida > vida_maxima:
            self.vida = vida_maxima

        proporcao = self.vida / vida_maxima
        barra_cheia = int(largura * proporcao)

        pygame.draw.rect(screen, (255, 0, 0), (x, y, largura, altura))
        pygame.draw.rect(screen, cor, (x, y, barra_cheia, altura))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, largura, altura), 2)