import pygame
from pygame.locals import *

class HomemMeiaNoite(pygame.sprite.Sprite):
    """
    Classe que reúne as sprites necessárias para a animação do Homem
    da Meia-Noite ainda do bem
    """
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/imagem_1.png'))
        self.sprites.append(pygame.image.load('sprites/imagem_2.png'))
        self.sprites.append(pygame.image.load('sprites/imagem_3.png'))
        self.sprites.append(pygame.image.load('sprites/imagem_4.png'))
        self.sprite_atual = 0
        self.image = self.sprites[self.sprite_atual]
        self.fundo_olinda = pygame.image.load('Imagens/cenarios/olinda(redimensionada).png')

        self.rect = self.image.get_rect()
        self.rect = (pos_x, pos_y)


    def update(self):
        """
        Método para atualizar as imagens e gerar a sensação de movimento
        """
        self.sprite_atual += .029

        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0

        self.image = self.sprites[int(self.sprite_atual)]

class ComadreFulozinha(pygame.sprite.Sprite):
    def __init__(self):
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
        self.rect.bottomright = 1200, 700

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.03
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
        elif self.atacando:
            self.atual = self.atual + 0.10
            if int(self.atual) == 2:
                self.atual = self.atual - 0.07
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
        self.sprites_ataque.append(pygame.image.load('imagens/cf-sprites/fulozinha_ataque1.png'))
        self.sprites_ataque.append(pygame.image.load('imagens/cf-sprites/fulozinha_ataque2.png'))
        self.sprites_ataque.append(pygame.image.load('imagens/cf-sprites/fulozinha_ataque3.png'))
        self.sprites_ataque.append(pygame.image.load('imagens/cf-sprites/fulozinha_ataque1.png'))
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

        self.atacando = False
        self.sofrendo = True

class CaretadeTriunfo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/cdt-sprites/careta_ocio.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_triunfo = pygame.image.load('imagens/cenarios/triunfo(redimensionada).png')
        self.rect = self.image.get_rect()
        self.rect.bottomright = 1200, 730

        self.atacando = False
        self.sofrendo = False

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.03
            if self.atual>= len(self.sprites_dano):
                self.atual = 0
                self.sofrendo = False
            self.image = self.sprites_dano[int(self.atual)]
        elif self.atacando:
            self.atual = self.atual + 0.08
            if int(self.atual) == 2:
                self.atual = self.atual - 0.07
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

        self.atacando = False
        self.sofrendo = True

class Papangu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/p-sprites/Papangu (2)(redimensionada).png'))
        self.sprites.append(pygame.image.load('imagens/p-sprites/papangu2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_recife = pygame.image.load('imagens/cenarios/Recife(redimensionada).png')


        self.rect = self.image.get_rect()
        self.rect.bottomright = 1200, 700

    def update(self):
        self.atual = self.atual + 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (320,320))

class TriodeFerro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/tdf-sprites/Trio de Ferro(redimensionada).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (320,320))
        self.fundo_arena = pygame.image.load('imagens/cenarios/arena(redimensionada).png')


        self.rect = self.image.get_rect()
        self.rect.bottomright = 1200, 700

    def update(self):
        self.atual = self.atual + 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (320,320))

class Protagonista(pygame.sprite.Sprite):
    def __init__(self):
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
        self.rect.bottomright = 400, 700

    def update(self):
        if self.sofrendo:
            self.atual = self.atual + 0.03
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

        self.atacando = False
        self.sofrendo = True