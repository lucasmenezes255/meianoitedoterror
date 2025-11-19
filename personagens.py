import pygame

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
        self.fundo_olinda = pygame.image.load('cenarios/olinda.png')

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
