import pygame
from random import randint 

noire=(0,0,0)
blan=(255,255,255)

class Ball(pygame.sprite.Sprite):
    def __init__(self, couleur ,long ,lar):
        super().__init__()

        self.image = pygame.Surface([long,lar])
        self.image.fill(noire)
        self.image.set_colorkey(noire)

        pygame.draw.rect(self.image,couleur,[0,0,long,lar])

        self.velocity =[randint(4,8), randint(-8,8)]

        self.rect=self.image.get_rect()


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bouncing(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = self.velocity[1]

