#####################
#######Jumper########
###Jump to the top###
###And Don't stop####
#########(a test)####
##################MGE

#import the pygame and random modules
import pygame
import random

#THE MAIN PLAYER/THE JUMPER
class Player(pygame.sprite.Sprite):
    def __init__(self, coords, SCALE=10):
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
    #moves the rectangle by the amount specified when calling this func
    def update(self, amount, walls='NO'):
        self.oldcoords = self.rect
        self.rect = self.rect.move(amount)
        #only runs if walls is not set to 'NO'
        #if it runs it makes the window 'wall' in the player
        if walls != 'NO':
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > (self.screen.width - self.rect.width):
                self.rect.x = self.screen.width - self.rect.width
            if self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.y > (self.screen.height - self.rect.height):
                self.rect.y = self.screen.height - self.rect.height

#THE LEVEL/BG
class Level(pygame.sprite.Sprite):
    def __init__(self,imagename):
        #get screen's rect
        self.screen = pygame.display.get_surface().get_rect()
        #load image file to be used for map
        self.image = pygame.image.load(imagename).convert()
        self.image.set_colorkey((255,255,255))
        #define image's rect
        self.rect = self.image.get_rect()
        #let me know the map init has been run
        print('Level.__init__')

#<================REST=================>
#set screen and it's size,caption,and color
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('JUMPER')
#define a 'Player' variable and set it's default coordinates
#Player(coordinates,SCALE) //NOTE: change the y coordinate if you change the SCALE
player = Player((0,470), 30)
level = Level('crayon.png')
#bg color, blank screen to overwrite player's old blit
blank = pygame.Surface((player.rect.width, player.rect.height))
blank.fill((100,100,100))

#looooooooooooooooooooooooooooooop
while pygame.event != pygame.QUIT:
    key = pygame.key.get_pressed()
    events = pygame.event.get()
    if key[pygame.K_RIGHT]:
        player.update([1,0])
    if key[pygame.K_LEFT]:
        player.update([-1,0])
    if key[pygame.K_SPACE]:
        player.update([0,-1])
    if key[pygame.K_DOWN]:
        pygame.event = pygame.QUIT

    screen.blit(level.image,level.rect)
    screen.blit(player.image,player.rect)
    pygame.display.update()














        
