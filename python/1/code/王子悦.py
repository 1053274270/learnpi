import pygame,sys
import random
import numpy as np
from pygame.locals import *
pygame.init()
pygame.display.set_caption("王子悦小胖子")
screen =pygame.display.set_mode([1000,1000])
myfont=pygame.font.SysFont(None,30)     
size=[2061,2060]
i,j=2,2
h=int(size[1]/3)
w=int(size[0]/3)
tuxiang=[1,2,3],[4,5,6],[7,8,9]
tuxiang=np.asarray(tuxiang)
img1=pygame.image.load(r'wzy\1.png')
img2=pygame.image.load(r'wzy\2.png')
img3=pygame.image.load(r'wzy\3.png')
img4=pygame.image.load(r'wzy\4.png')
img5=pygame.image.load(r'wzy\5.png')
img6=pygame.image.load(r'wzy\6.png')
img7=pygame.image.load(r'wzy\7.png')
img8=pygame.image.load(r'wzy\8.png')
img9=pygame.image.load(r'wzy\9.png')     
while True:         
    screen.fill([0,0,0])  
    for event in pygame.event.get():        
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                if i>0:
                    tuxiang[i][j],tuxiang[i-1][j]=tuxiang[i-1][j],tuxiang[i][j]
                    i-=1
                    print(tuxiang)
            elif event.key==K_RIGHT:
                if i<2:
                    tuxiang[i][j],tuxiang[i+1][j]=tuxiang[i+1][j],tuxiang[i][j]
                    i+=1
                    print(tuxiang)
            elif event.key==K_UP:
                if j>0:
                    tuxiang[i][j],tuxiang[i][j-1]=tuxiang[i][j-1],tuxiang[i][j]
                    j-=1
                    print(tuxiang)
            elif event.key==K_DOWN:
                if j<2:
                    tuxiang[i][j],tuxiang[i][j+1]=tuxiang[i][j+1],tuxiang[i][j]
                    j+=1
                    print(tuxiang)
        if event.type == pygame.QUIT:
            sys.exit()
    for a in range(3):
        for b in range(3):
            if tuxiang[a][b]==1:
                screen.blit(img1,(a*h,b*h))
            elif tuxiang[a][b]==2:
                screen.blit(img2,(a*h,b*h))
            elif tuxiang[a][b]==3:
                screen.blit(img3,(a*h,b*h))
            elif tuxiang[a][b]==4:
                screen.blit(img4,(a*h,b*h))
            elif tuxiang[a][b]==4:
                screen.blit(img4,(a*h,b*h))
            elif tuxiang[a][b]==5:
                screen.blit(img5,(a*h,b*h))
            elif tuxiang[a][b]==6:
                screen.blit(img6,(a*h,b*h))
            elif tuxiang[a][b]==7:
                screen.blit(img7,(a*h,b*h))
            elif tuxiang[a][b]==8:
                screen.blit(img8,(a*h,b*h))
            elif tuxiang[a][b]==9:
                screen.blit(img9,(a*h,b*h))
    pygame.display.update()
