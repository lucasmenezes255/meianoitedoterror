import pygame
import sprites
import sys

class HomemMeiaNoite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/imagem_1.png'))
        self.sprites.append(pygame.image.load('sprites/imagem_2.png'))
        self.sprites.append(pygame.image.load('sprites/imagem_3.png'))
        self.sprites.append(pygame.image.load('sprites/imagem_4.png'))
        self.sprite_atual = 0
        self.image = self.sprites[self.sprite_atual]

        self.rect = self.image.get_rect()
        self.rect = (pos_x, pos_y)


    def update(self):
        self.sprite_atual += .029

        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0

        self.image = self.sprites[int(self.sprite_atual)]

pygame.init()
clock = pygame.time.Clock()

largura_screen = 700
altura_screen = 900
screen = pygame.display.set_mode((largura_screen, altura_screen))
fundo_cenario = pygame.image.load('cenarios/olinda.png')
homem_da_meia_noite = pygame.sprite.Group()
hmm_sprites = HomemMeiaNoite(-47,237)
homem_da_meia_noite.add(hmm_sprites)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    screen.blit(fundo_cenario, (0,0))
    homem_da_meia_noite.draw(screen)
    homem_da_meia_noite.update()

    pygame.display.update()
    clock.tick(60)