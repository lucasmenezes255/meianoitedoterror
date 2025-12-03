import pygame 
from random import randint

class Magia(pygame.sprite.Sprite):
    def __init__(self, x_inicial, y_inicial, x_alvo, y_alvo, alvo_sprite):
        super().__init__()
        self.ativa = False
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.x_alvo = x_alvo
        self.y_alvo = y_alvo
        self.alvo_sprite = alvo_sprite
        self.callback_fim = None

        # Imagem da magia
        self.image = pygame.image.load('imagens/magia.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))# azul brilhante

        self.rect = self.image.get_rect(center=(-9999,-9999))
        self.mask = pygame.mask.from_surface(self.image)

        self.setar_direcao(x_alvo,y_alvo)

        # Cálculo da direção
    def setar_direcao(self, x_alvo, y_alvo):
        dx = x_alvo - self.x_inicial
        dy = y_alvo - self.y_inicial
        distancia = (dx**2 + dy**2) ** 0.5

        # normaliza o vetor (direção)
        self.vel_x = dx / distancia * 10   # velocidade 10 px/frame
        self.vel_y = dy / distancia * 10

    def ativar(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_inicial, self.y_inicial)
        self.ativa = True

    def update(self):
        if not self.ativa:
            return

        # move o projetil
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.colisao():
            self.alvo_sprite.dano()
            self.desativar()

    def colisao(self):
        return pygame.sprite.collide_mask(self, self.alvo_sprite) is not None
    
    def desativar(self):
        self.ativa=False
        self.rect.center = (-9999, -9999)
        if self.callback_fim:
            self.callback_fim()

class D20(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        w, h= 185, 190
        escala= 0.5
        dado_d20 = pygame.image.load("imagens/d20.png").convert_alpha()
        frame = dado_d20.subsurface((0, 0, w, h))
        novo_w = int(w*escala)
        novo_h = int(h*escala)
        frame_atualizado = pygame.transform.scale(frame, (novo_w, novo_h))
        self.image = frame_atualizado
        self.rect = self.image.get_rect(topright = (x , y))
        self.sprites = [self.image]
        self.sprites_giro = []
        self.girando = False
        self.selecionado = False

    def update(self):
        if self.girando:
            self.atual = self.atual + 0.3
            if self.atual>= len(self.sprites_giro):
                self.atual = 0
            self.image = self.sprites_giro[int(self.atual)]
        elif self.selecionado:
            self.image =  self.sprites_selecionado[int(self.atual)]
        else:
            self.atual = 0
            self.image = self.sprites[0]

    def rodando(self):
        escala = 0.5
        y, w, h = 800, 185, 190
        dado_d20 = pygame.image.load("imagens/d20.png").convert_alpha()
        frame1 = dado_d20.subsurface((0, y, w, h))
        frame2 = dado_d20.subsurface((190, y, w, h))
        frame3 = dado_d20.subsurface((380, y, w, h))
        frame4 = dado_d20.subsurface((570, y, w, h))
        frame5 = dado_d20.subsurface((750, y, w, h))
        frame_atualizado1 = pygame.transform.scale(frame1, (int(w*escala), int(h*escala)))
        frame_atualizado2 = pygame.transform.scale(frame2, (int(w*escala), int(h*escala)))
        frame_atualizado3 = pygame.transform.scale(frame3, (int(w*escala), int(h*escala)))
        frame_atualizado4 = pygame.transform.scale(frame4, (int(w*escala), int(h*escala)))
        frame_atualizado5 = pygame.transform.scale(frame5, (int(w*escala), int(h*escala)))
        self.sprites_giro = [frame_atualizado1, frame_atualizado2, frame_atualizado3, frame_atualizado4, frame_atualizado5]
        self.atual = 0
        self.image = self.sprites_giro[self.atual]

        self.girando = True
        self.selecionado = False

    def selecionar(self):
        escala = 0.5
        w, h = 180, 190
        y1, y2, y3, y4 = 0, 200, 400, 600
        x = 185
        dado_d20 = pygame.image.load("imagens/d20.png").convert_alpha()
        self.sprites_selecionado = []
        for i in range(5):
            frame = dado_d20.subsurface((i*x, y1, w, h))
            frame_atualizado = pygame.transform.scale(frame, (int(w*escala), int(h*escala)))
            self.sprites_selecionado.append(frame_atualizado)
        for i in range(5):
            frame = dado_d20.subsurface((i*x, y2, w, h))
            frame_atualizado = pygame.transform.scale(frame, (int(w*escala), int(h*escala)))
            self.sprites_selecionado.append(frame_atualizado)
        for i in range(5):
            frame = dado_d20.subsurface((i*x, y3, w, h))
            frame_atualizado = pygame.transform.scale(frame, (int(w*escala), int(h*escala)))
            self.sprites_selecionado.append(frame_atualizado)
        for i in range(5):
            frame = dado_d20.subsurface((i*x, y4, w, h))
            frame_atualizado = pygame.transform.scale(frame, (int(w*escala), int(h*escala)))
            self.sprites_selecionado.append(frame_atualizado)
        self.atual = randint(0, 19)
        self.image = self.sprites_selecionado[self.atual]
        self.valor = self.atual +1
        self.girando = False
        self.selecionado = True
