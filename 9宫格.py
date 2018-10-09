import pygame,sys
from PIL import Image
import random
import numpy as np
from pygame.locals import *
pygame.init()
keys=[False,False,False,False,False]
pygame.display.set_caption("九宫格")
screen =pygame.display.set_mode([1000,1000])
myfont=pygame.font.SysFont(None,30)     
img=Image.open(r'img\1.png')
size=img.size
h=size[1]/3
w=size[0]/3
tuxiang=[1,2,3],[4,5,6],[7,8,9]
tuxiang=np.asarray(tuxiang)
i,j=2,2
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
    img=Image.open(r'img\1.png')
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
                keys[0]=True
                if j>0:
                    tuxiang[i][j],tuxiang[i][j-1]=tuxiang[i][j-1],tuxiang[i][j]
                    j-=1
                    print(tuxiang)
            elif event.key==K_RIGHT:
                keys[1]=True
                if j<2:
                    tuxiang[i][j],tuxiang[i][j+1]=tuxiang[i][j+1],tuxiang[i][j]
                    j+=1
                    print(tuxiang)
            elif event.key==K_UP:
                keys[2]=True
                if i>0:
                    tuxiang[i][j],tuxiang[i-1][j]=tuxiang[i-1][j],tuxiang[i][j]
                    i-=1
                    print(tuxiang)
            elif event.key==K_DOWN:
                keys[3]=True
                if i<2:
                    tuxiang[i][j],tuxiang[i+1][j]=tuxiang[i+1][j],tuxiang[i][j]
                    i+=1
                    print(tuxiang)
        if event.type == KEYUP:
            if event.key==K_LEFT:
                keys[0]=False
            elif event.key==K_RIGHT:
                keys[1]=False
            elif event.key==K_UP:
                keys[2]=False
            elif event.key==K_DOWN:
                keys[3]=False
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(img1,[0,0])
    pygame.display.update()