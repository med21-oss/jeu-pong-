import pygame
from pygame import*
import sys
from Paddel import Paddel
from Ball import Ball



pygame.init()

taille_lon =800
taille_lar =600
taille_jeu = pygame.display.set_mode((taille_lon,taille_lar))
pygame.display.set_caption("projet multi men 3and el boss")
noire=(0,0,0)
blan=(255,255,255)



joueur1= Paddel(blan,10,100)
joueur1.rect.x=25
joueur1.rect.y=250


joueur2= Paddel(blan,10,100)
joueur2.rect.x=765
joueur2.rect.y=250


ball=Ball(blan,20,20)
ball.rect.x=400
ball.rect.y=200

score_j1=0
score_j2=0




temp= pygame.time.Clock()
jeu_fct=True


sprites_list = pygame.sprite.Group()
sprites_list.add(joueur1)
sprites_list.add(joueur2)
sprites_list.add(ball)

      
            
while jeu_fct:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_fct=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                jeu_fct=False

    
    
   
    movment = pygame.key.get_pressed()
    if movment[pygame.K_z]:
        joueur1.paddel_up(6)
    if movment[pygame.K_s]:
        joueur1.paddel_down(6)
    if movment[pygame.K_UP]:
        joueur2.paddel_up(6)
    if movment[pygame.K_DOWN]:
        joueur2.paddel_down(6)
    
    sprites_list.update()

    if ball.rect.x >=780:
        score_j1 += 1
        ball.velocity[0]= -ball.velocity[0]
        ball.rect.x= 400
        ball.rect.y= 200

    if ball.rect.x < 2:
        score_j2 += 1

        ball.velocity[0]= -ball.velocity[0]
        ball.rect.x= 400
        ball.rect.y= 200

    if ball.rect.y >=580:
        ball.velocity[1]= -ball.velocity[1]
        

    if ball.rect.y <0:
        ball.velocity[1]= -ball.velocity[1]
        
    
    if pygame.sprite.collide_mask(ball,joueur1) or pygame.sprite.collide_mask(ball,joueur2):
        ball.bouncing()


    taille_jeu.fill(noire)
    pygame.draw.line(taille_jeu,blan,[400,0],[400,600],10)
    sprites_list.draw(taille_jeu)

    font = pygame.font.Font(None,100)
    text=font.render(str(score_j1),1,blan)
    taille_jeu.blit(text,(320,10))

    text=font.render(str(score_j2),1,blan)
    taille_jeu.blit(text,(450,10))


    pygame.display.update()
    temp.tick(60)
pygame.quit()
    

    

    