#####################
#######Jumper########
###Jump to the top###
###And Don't stop####
##(a test of sorts)##
##################MGE

#import the pygame and random modules
import pygame
import random
import time
clock = pygame.time.Clock()       

#THE LEVEL/BG
class Level(pygame.sprite.Sprite):
    def __init__(self,imagename,YPOS=0,XPOS=0):
        #get screen's rect
        self.screen = pygame.display.get_surface().get_rect()
        #load image file to be used for map
        self.image = pygame.image.load(imagename).convert()
        self.image.set_colorkey((255,255,255))
        #define image's rect
        self.rect = self.image.get_rect()
        self.rect.x = XPOS
        self.rect.y = YPOS
        #let me know the map init has been run
        print('Level.__init__')

#THE PLATFORM
class Platform(pygame.sprite.Sprite):
    def __init__(self,imagename,YPOS=0,XPOS=0):
        #get screen's rect
        self.screen = pygame.display.get_surface().get_rect()
        #load image file to be used for map
        self.image = pygame.image.load(imagename).convert()
        self.image.set_colorkey((255,255,255))
        #define image's rect
        self.rect = self.image.get_rect()
        self.rect.x = XPOS
        self.rect.y = YPOS
        #let me know the map init has been run
        print('platform.__init__')

#THE MAIN PLAYER/THE JUMPER
class Player(pygame.sprite.Sprite):
    def __init__(self, coords, SCALE=10):
        #define variables
        self.speed = 1.0
        self.startJumpCoord = 0.0
        self.endJumpCoord = 0.0
        self.maxJumpCoord = 50.0
        self.startJumpTime = 0.0
        self.endJumpTime = 0.0
        self.maxJumpTime = 400.0
        self.falling = True
        #get the screen's rectangle
        self.screen = pygame.display.get_surface().get_rect()
        #set the old coordinates of the player object
        self.oldcoords = (0,0,0,0)
        #load an image, convert it, and define it's colorkey
        self.image = pygame.image.load('jumper.png').convert()
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.image.set_colorkey((255,255,255))
        #define the rectangle from the image's rect size
        self.rect = self.image.get_rect()
        #set x and y coords
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        #let me know the player init has been run
        print('Player.__init__')
        self.gravcheck()
    #moves the rectangle by the amount specified when calling this func
    def move(self,direction):
        self.oldcoords = self.rect
        self.rect =  self.rect.move(direction*self.speed, 0)
    def gravcheck(self):
        for i in platforms:
            if self.rect.colliderect(i):
                print('collision!!!')
                self.falling = False
                self.startJumpCoord = 0
                self.startJumpTime = 0
            if self.falling:
                self.rect = self.rect.move(0,1)
    def jump2(self):
        print('jumpiiiing!')
        if self.falling == False:
            if self.endJumpCoord < self.rect.y:
                self.rect = self.rect.move(0,-5)
                print('rising...')
            else:
                self.falling = True
        if self.startJumpCoord = 0:
            self.oldcoords = self.rect
            self.startJumpCoord = self.rect.y
            print('sJT:' + str(self.startJumpCoord))
            self.endJumpCoord = self.startJumpCoord + self.maxJumpCoord
            print('eJT:' + str(self.endJumpCoord))
                
    def jump(self):
        print('jump initiated')
        if self.startJumpTime == 0:
            self.startJumpTime = pygame.time.get_ticks()
            print('starttime:' + str(self.startJumpTime))
            self.endJumpTime = self.startJumpTime + self.maxJumpTime
            print('endtime:' + str(self.endJumpTime))
        if self.falling == False:
            print('time left:'+ str(pygame.time.get_ticks() - self.endJumpTime))
            if self.endJumpTime >= pygame.time.get_ticks():
                self.rect = self.rect.move(0,-5)
                print('RISING!!!!!!!!!!!!')
            else:
                self.falling = True
                
#<================REST=================>
#set screen and it's size,caption,and color
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('JUMPER')
#define a 'Player' variable and set it's default coordinates
#Player(coordinates,SCALE) //NOTE: change the y coordinate if you change the SCALE
level = Level('crayon.png')
floor = Platform('floor.png',480)
platform = Platform('floor.png',400,100)
platforms = []
platforms.append(floor)
platforms.append(platform)
player = Player((0,420), 30)



#bg color, blank screen to overwrite player's old blit
blank = pygame.Surface((player.rect.width, player.rect.height))
blank.fill((100,100,100))

#looooooooooooooooooooooooooooooop
while pygame.event != pygame.QUIT:
    key = pygame.key.get_pressed()
    events = pygame.event.get()
    player.gravcheck()
    if key[pygame.K_RIGHT]:
        player.move(1)
    if key[pygame.K_LEFT]:
        player.move(-1)
    if key[pygame.K_DOWN]:
        pygame.event = pygame.QUIT
    if key[pygame.K_SPACE]:
        player.jump()
            

    screen.blit(level.image,level.rect)
    for i in platforms:
        screen.blit(i.image,i.rect)
    screen.blit(player.image,player.rect)
    
    pygame.display.update()














        
