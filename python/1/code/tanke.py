import pygame,sys
import random
from pygame.locals import *
class Tanke(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img=pygame.image.load('tanke\\tanke.png')    
        self.rect=self.img.get_rect()
        self.rect.topleft=500,500
        self.pa=True
        self.speed=1
class Zhuan(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.img=pygame.image.load('tanke\\zhuan.png')    
        self.rect=self.img.get_rect()
        self.rect.topleft=p   
class Q_buttle(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.img=pygame.image.load('tanke\\zidan1.png')
        self.rect=self.img.get_rect()
        self.rect.topleft = pos
        self.speed=10               
    def shoot(self):    
        x1,y1= pygame.mouse.get_pos()
        x2,y2=self.rect.center           
        x,y=x2,y2           
        for i in range(10):                        
            x+=self.speed
            y=(y1-y2)*(x-x2)/(x1-x2)+y2
            print(x,y)
            self.rect.center=x,y
            
pygame.init()
keys=[False,False,False,False,False]
pygame.display.set_caption("Hide Game")
screen =pygame.display.set_mode([1000,1000])
myfont=pygame.font.SysFont(None,30)     
zhuangroup=pygame.sprite.Group()
Qjigroup=pygame.sprite.Group()
tanke=Tanke()
for i in range(10):
    x=random.randint(0,900)
    y=random.randint(0,900)
    zhuangroup.add(Zhuan([x,y]))    
while True:     
    screen.fill([0,0,0])  
    for event in pygame.event.get():        
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True
            elif event.key==K_z:
                tanke.speed=2
            elif event.key==K_q:                
                Qji=Q_buttle(tanke.rect.topleft)
                Qjigroup.add(Qji)
                x1,y1= pygame.mouse.get_pos()
                x2,y2=tanke.rect.center           
                x,y=x2,y2
                for i in range(10):
                    x+=Qji.speed
                    y=(y1-y2)*(x-x2)/(x1-x2)+y2                     
                    screen.blit(Qji.img,Qji.rect.topleft)
        if event.type == KEYUP:
            if event.key==K_LEFT:
                keys[0]=False
            elif event.key==K_RIGHT:
                keys[1]=False
            elif event.key==K_UP:
                keys[2]=False
            elif event.key==K_DOWN:
                keys[3]=False
            elif event.key==K_z:
                tanke.speed=Tanke().speed
        if event.type == pygame.QUIT:
            sys.exit()
    if keys[0]  and tanke.rect.left>0:        
        tanke.rect.left-=tanke.speed
    if keys[1]  and tanke.rect.right<1000:
        tanke.rect.left+=tanke.speed
    if keys[2]  and tanke.rect.top>0:
        tanke.rect.top-=tanke.speed
    if keys[3]  and tanke.rect.bottom<1000:
        tanke.rect.top+=tanke.speed
    screen.blit(tanke.img,tanke.rect.topleft)    
    for zidan in zhuangroup:
        screen.blit(zidan.img,zidan.rect.topleft)   
    pygame.sprite.spritecollide(tanke,zhuangroup,True)
    pygame.display.update()