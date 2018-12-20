import pygame,sys
import numpy as np

class Xiangqi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.che=pygame.image.load('车.png') 
        self.rect=self.che.get_rect()
        self.rect.center=[84,84]

pygame.init()
pygame.display.set_caption("象棋")
screen=pygame.display.set_mode([925,520])
clock=pygame.time.Clock()
qipan=pygame.image.load('qipan.jpg')
xiangqi=Xiangqi()
qishi=[33-21,33-21]
h=50#起始位置,50间隔
qizi=([0,0,0,0,0,0,0,0,0],
      [0,1,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],   
      )#棋子位置
while True:     
    clock.tick(60)
    screen.fill([0,0,0]) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()        
    
    screen.blit(qipan,[0,0])
    for a in range(9):
        for b in range(9):
            if   qizi[a][b]==0:
                 pass
            elif qizi[a][b]==1:
                 screen.blit(xiangqi.che,(qishi[0]+a*h,qishi[1]+b*h))
            #elif qizi[a][b]==2:
            #    screen.blit(img2,(a*h,b*h))
            #elif qizi[a][b]==3:
            #    screen.blit(img3,(a*h,b*h))
            #elif qizi[a][b]==4:
            #    screen.blit(img4,(a*h,b*h))
            #elif qizi[a][b]==4:
            #    screen.blit(img4,(a*h,b*h))
            #elif qizi[a][b]==5:
            #    screen.blit(img5,(a*h,b*h))
            #elif qizi[a][b]==6:
            #    screen.blit(img6,(a*h,b*h))
            #elif qizi[a][b]==7:
            #    screen.blit(img7,(a*h,b*h))
            #elif qizi[a][b]==8:
            #    screen.blit(img8,(a*h,b*h))
            #elif qizi[a][b]==9:
            #    screen.blit(img9,(a*h,b*h))
    print(pygame.mouse.get_pos())
    #che[1]=che[1]+1
    pygame.display.update()
