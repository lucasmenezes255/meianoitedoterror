import pygame 

class MagiaComadre(pygame.sprite.Sprite):
    def __init__(self, x_inicial, y_inicial, x_alvo, y_alvo):
        super().__init__()

        # Imagem da magia
        self.image = pygame.Surface((30, 10))
        self.image.fill((0, 120, 255))  # azul brilhante

        self.rect = self.image.get_rect()
        self.rect.center = (x_inicial, y_inicial)

        # Cálculo da direção
        dx = x_alvo - x_inicial
        dy = y_alvo - y_inicial
        distancia = (dx**2 + dy**2) ** 0.5

        # normaliza o vetor (direção)
        self.vel_x = dx / distancia * 10   # velocidade 10 px/frame
        self.vel_y = dy / distancia * 10

    def update(self):
        # move o projetil
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
