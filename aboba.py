from pygame import*


game=True
clock= time.Clock()

okno = display.set_mode((700,600))

fon = transform.scale(image.load('city1.png'), (700, 900))

class GameSprite(sprite.Sprite):
    def __init__(self, pikt, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(pikt), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direct="verh"

    def ris(self):

        if self.direct == "pravo":
            self.image = transform.scale(image.load('right.png'),(50,50))
        elif self.direct == "levo":
            self.image = transform.scale(image.load('left.png'),(50,50))
        okno.blit(self.image, (self.rect.x,self.rect.y))

gravity = 0
class igrok(GameSprite):
    def  control(self):
        global gravity
        self.ris()
        self.lastx = self.rect.x
        self.lasty = self.rect.y
        kn = key.get_pressed()
        if self.rect.y<500:
            self.rect.y =self.rect.y + 2 + gravity
        if self.rect.y>498:
            gravity=1

        if kn[K_LEFT]:
            #igrok.image = transform.scale(image.load('left.png'),(100,100))    
            self.rect.x -= 3
            self.direct="levo"
        if kn[K_RIGHT]:
            #igrok.image =   transform.scale(image.load('right.png'),(100,100))  
            self.rect.x += 3
            self.direct="pravo"
        if kn[K_UP]:
            self.rect.y -=8
            gravity+=0.1

class Wall(sprite.Sprite):
    def __init__(self, x,y,shir,vis):
        super().__init__()
        self.image = Surface((shir,vis))
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x,self.rect.y))

Wallgroup = [
Wall(335, 340, 75, 50),
Wall(170, 340, 75, 50),
Wall(20, 370, 80, 50),
Wall(495, 295, 75, 50),
Wall(620, 360, 75, 50)
]

class Wall1(sprite.Sprite):
    def __init__(self, x,y,shir,vis):
        super().__init__()
        self.image = Surface((shir,vis))
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x,self.rect.y))
    
Wallgroup1 = [
Wall1(0, 500, 700, 50),
]

from random import randint
class cemka(GameSprite):
    def padat(self):
        self.ris()
        self.rect.y+=10
        if self.rect.y>600:
            self.rect.y = -2
            self.rect.x=randint(30,680)
   
Cema = cemka('CEMKA.png', 350, 10, 20, 20)
    
player = igrok('right.png',335, 320, 50,50)     

Cemagroup = [
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),
cemka('CEMKA.png', randint(30,680), randint(30,680), 20, 20),


]

CEMA = 0

while game:
    for i in event.get():
        if i .type == QUIT:
            game  = False
    okno.blit(fon, (0,0))
    player.control()
    for i in Wallgroup:
       # i.ris()
        if sprite.collide_rect(i, player):
            player.rect.y-=15
        CEMA=+1
            
    for s in Cemagroup:
        s.padat()
        if sprite.collide_rect(s, player):
            CEMA+=1
            Cemagroup.remove(s)
        if CEMA >= 10:
            game=False
        #Cema.rect.y=-300
        #Cema.rect.x=randint(30,680)
    #Cema.padat()
    for i in Wallgroup1:
        #i.ris()
        if sprite.collide_rect(i, player):
            game=False
    if CEMA >= 10:
        game=False
    clock.tick(60)
    display.update()
    









