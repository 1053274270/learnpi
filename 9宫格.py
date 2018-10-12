import pygame,sys
from PIL import Image
import random
import numpy as np
from pygame.locals import *
pygame.init()
pygame.display.set_caption("九宫格")
screen =pygame.display.set_mode([1000,1000])
myfont=pygame.font.SysFont(None,30)     
img=Image.open(r'img\0.png')
size=img.size
i,j=2,2
h=int(size[1]/3)
w=int(size[0]/3)
tuxiang=[1,2,3],[4,5,6],[7,8,9]
tuxiang=np.asarray(tuxiang)
img1=pygame.image.load(r'九宫格\10.png')
img2=pygame.image.load(r'九宫格\11.png')
img3=pygame.image.load(r'九宫格\12.png')
img4=pygame.image.load(r'九宫格\13.png')
img5=pygame.image.load(r'九宫格\14.png')
img6=pygame.image.load(r'九宫格\15.png')
img7=pygame.image.load(r'九宫格\16.png')
img8=pygame.image.load(r'九宫格\17.png')
img9=pygame.image.load(r'九宫格\18.png')
def fenge():
    img=Image.open(r'img\0.png')
    size=img.size
    h=size[1]/3
    w=size[0]/3
    n=3
    k=1
    for i in range(n):
        for j in range(n):       
            a=img.crop((i*w,j*h,(i+1)*w,(j+1)*h))       
            a.save(str(k)+'.png')
            k+=1     
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