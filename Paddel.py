import pygame

noire=(0,0,0)
blan=(255,255,255)
class Paddel(pygame.sprite.Sprite):
    def __init__(self, couleur ,long ,lar):
        super().__init__()

        self.image = pygame.Surface([long,lar])
        self.image.fill(noire)
        self.image.set_colorkey(noire)

        pygame.draw.rect(self.image,couleur,[0,0,long,lar])

        self.rect=self.image.get_rect()

    def paddel_up(self,npixel):
        self.rect.y -= npixel
        if self.rect.y < 0:
            self.rect.y=0
        
    def paddel_down(self,npixel):
        self.rect.y += npixel
        if self.rect.y > 600:
            self.rect.y=600




