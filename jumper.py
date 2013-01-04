#############12262010
#######Jumper########
###Jump to the top###
###And Don't stop####
##(a test of sorts)##
##################MGE


#<============IMPORTS==============>
#import the pygame and random modules
import pygame
import random
import time
clock = pygame.time.Clock()


#<===========CLASSES===============>
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
        self.oldcoords = (0,0,0,0)
        self.direction = 0
        #let me know the map init has been run
        print('platform.__init__')
    def moveSides(self, move=False):
        if self.direction == 0:
            self.direction = random.randint(-1,1)
        if move:
            self.oldcoords = self.rect
            self.rect = self.rect.move(self.direction,0)
            for i in blocks:
                if self.rect.colliderect(i) and self.rect.right - 1 == i.rect.left:
                    self.direction = -self.direction
                if self.rect.colliderect(i) and self.rect.left + 1 == i.rect.right:
                    self.direction = -self.direction
                    
#THE MAIN PLAYER/THE JUMPER
class Player(pygame.sprite.Sprite):
    def __init__(self, coords, SCALE=10, IMAGENAME='jumper'):
        #define variables
        self.speed = 1.0
        self.startJumpCoord = 0.0
        self.endJumpCoord = 0.0
        self.maxJumpCoord = -75.0
        self.falling = True
        #get the screen's rectangle
        self.screen = pygame.display.get_surface().get_rect()
        #set the old coordinates of the player object
        self.oldcoords = (0,0,0,0)
        #load an image, convert it, and define it's colorkey
        self.image = pygame.image.load(IMAGENAME + '.png').convert()
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.imagename = 'jumper.png'
        self.image.set_colorkey((255,255,255))
        #define the rectangle from the image's rect size
        self.rect = self.image.get_rect()
        #set x and y coords
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        #let me know the player init has been run
        print('Player.__init__')
        self.gravcheck()
    def images(self,IMAGENAME='jumper.png',SCALE=30):
        self.image = pygame.image.load(IMAGENAME).convert()
        self.imagename = IMAGENAME
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.image.set_colorkey((255,255,255))
    #moves the rectangle in the direction specified when calling this func
    def move(self,direction):
        self.oldcoords = self.rect
        #if rect is at far left of screen
        for i in blocks:
            if self.rect.colliderect(i) and self.rect.left + 1 == i.rect.right and (self.rect.bottom - 1) != i.rect.top:
                self.rect.left = i.rect.right
            if self.rect.colliderect(i) and self.rect.right - 1 == i.rect.left and (self.rect.bottom - 1) != i.rect.top:
                self.rect.right = i.rect.left
        #if not at either side of screen, move rect left of right depending of how the func is called
        self.rect =  self.rect.move(direction*self.speed, 0)
        if self.imagename == 'jumper.png':
            self.images('jumper1.png')
##        if self.imagename == 'jumper1.png':
##            self.images('jumper.png')
    #check to see if the rect should fall or stop moving (if touching the floor/a platform
    def gravcheck(self):
        for i in moveplats:
            #if the rectangle collides with any platform and the bottom of the player touches the top of the platform...
            if self.rect.colliderect(i) and (self.rect.bottom - 1) == i.rect.top:
                #set/reset some variables
                self.falling = False
                self.startJumpCoord = 0
                self.oldcoords = self.rect
                self.rect.bottom = i.rect.top + 1
                #change the player image back to the default one
                self.images()
                return
        for i in blocks:
            #if the rectangle collides with any platform and the bottom of the player touches the top of the platform...
            if self.rect.colliderect(i) and (self.rect.bottom - 1) == i.rect.top and self.rect.left + 1 != i.rect.right and self.rect.right - 1 != i.rect.left:
                #set/reset some variables
                self.falling = False
                self.startJumpCoord = 0
                self.oldcoords = self.rect
                self.rect.bottom = i.rect.top + 1
                #change the player image back to the default one
                self.images()
                return
            if self.rect.colliderect(i) and (self.rect.top + 1) <= i.rect.bottom and self.rect.left + 1 != i.rect.right and self.rect.right - 1 != i.rect.left:
                self.falling = True
        else:
            #save old coords in the var and "fall" down
            self.oldcoords = self.rect
            self.rect = self.rect.move(0,1)
    def stopJump(self):
        player.falling = True
    #func to make the player 'jump'
    def jump2(self):
        #if the variables required to jump are correct
        if self.startJumpCoord == 0:
            #find the y coordinate that the jump starts on
            self.startJumpCoord = self.rect.y
            #find the y coordinate the jump will end on
            self.endJumpCoord = self.startJumpCoord + self.maxJumpCoord
        #if the player is not falling
        if self.falling == False:
            #as long as the current y coordinate is less than the highest allowed y coordinate...
            if self.endJumpCoord < self.rect.y:
                #move upwards and change player image
                self.oldcoords = self.rect
                self.rect = self.rect.move(0,-5)
                self.images('jumping.png')
            #once the player goes above the max y coordinate
            else:
                #begin to fall
                self.falling = True

#GAME MANAGEMENT FUNCITONS
class Game:
    def __init__(self):
        #get screen's rect
        self.screen = pygame.display.get_surface().get_rect()
##    def checkPlayerPos(self):
        playerrect = player.rect
        print('got plyer rect!')
        print(str(playerrect))
        print('playerx: ' + str(playerrect[0]))
        print('playery: ' + str(playerrect[1]))
    def areaCheck(self, platforms, moveplats):
        if player.rect[0] >= (0.98 * self.screen.width):
            print('AREA RIGHT')
            return 1
        if player.rect[0] == -20:
            print('AREA LEFT')
            return 2
        else:
            return None


#<=========CLASSLESS_FUNCTIONS=========>
def generateMoveplat(ypos,xpos):
    newmoveplat = 'moveplat' + str(len(moveplats))
    print('MOVEPLATS:' + str(len(moveplats)))
    newmoveplat = Platform('platform.png',ypos,xpos)
    #print the name of the newly created platform and append it to the 'platform' list
    moveplats.append(newmoveplat)
def movePlatforms(platformlist):
    for i in platformlist:
        i.moveSides(True)
def generateBlocks(level=['x','x','x','x','x','x','x','x','x','x'],blockimage='block2.png'):
    xpos = 0
    ypos = 0
    image = pygame.image.load(blockimage)
    scale = image.get_rect().width
    for line in level:
        for char in line:
            if char == 'x':
                block = Platform(blockimage,ypos,xpos)
                blocks.append(block)
            if char == '=':
                generateMoveplat(ypos,xpos)
            if char == '.':
                block = Platform('block1.png',ypos,xpos)
                blocks.append(block)
            xpos += scale
        ypos += scale
        xpos = 0
    print('blocks generated')

    
#<=================REST====================>
#set screen and it's size,caption,and color
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('JUMPER')
#create the background from an image
level = Level('crayon.png')
#create the floor from an image and add it to a list of rectangles
platforms = []
moveplats = []
blocks = []
#define a 'Player' variable and set it's default coordinates
#Player(coordinates,SCALE) //NOTE: change the y coordinate if you change the SCALE
player = Player((100,420), 30)
game = Game()
#bg color, blank screen to overwrite player's old blit
blank = pygame.Surface((player.rect.width, player.rect.height))
screen.blit(level.image,level.rect)
pygame.display.update()

areas={'area1':
        ['xxxxxxxxxx',
        'x________x',
        'x________x',
        'x________x',
        'x________x',
        'x________x',
        'x________x',
        'x________x',
        'x_________',
        'xxxxxxxxxx'],'area2':
        ['xxxxxxxxxx',
        'x________x',
        'x________x',
        'x________x',
        'x_________',
        'x_______xx',
        'x_____..xx',
        'x___x___xx',
        '___xxx__xx',
        'xxxxxxxxxx'],'area3':
       ['xxxxxxxxxx',
        'x________x',
        'x________x',
        'x________x',
        '__________',
        'x_____=_xx',
        'xx_______x',
        'xxx______x',
        'xxxx_____x',
        'xxxxxxxxxx']}

area = 1
generateBlocks(areas['area' + str(area)])
rects = []
rects.append(player)
rects.append(level)


#<=================MAIN_LOOP==================>
while pygame.event != pygame.QUIT:
    key = pygame.key.get_pressed()
    event1 = pygame.event.peek(pygame.KEYUP)
    event2 = pygame.event.get()
    player.gravcheck()
    movePlatforms(moveplats)
    if event1:
        if key[pygame.K_SPACE]:
            player.stopJump()
    if key[pygame.K_RIGHT]:
        player.move(1)
    if key[pygame.K_LEFT]:
        player.move(-1)
    if key[pygame.K_DOWN]:
        pygame.event = pygame.QUIT
    if key[pygame.K_SPACE]:
        player.jump2()
    if game.areaCheck(platforms, moveplats) == 1:
        player.rect.x = 0
        screen.blit(level.image,level.rect)
        area += 1
        blocks = []
        generateBlocks(areas['area' + str(area)])
        print('area' + str(area))
    if game.areaCheck(platforms, moveplats) == 2:
        player.rect.x = 450
        screen.blit(level.image,level.rect)
        area -= 1
        blocks = []
        generateBlocks(areas['area' + str(area)])
        print('area' + str(area))
        
#######################BLITS#######################
    screen.blit(player.image,player.rect)
    screen.blit(level.image,player.oldcoords,player.oldcoords)
    for i in platforms:
        screen.blit(i.image,i.rect)
    for j in moveplats:
        screen.blit(level.image,j.oldcoords,j.oldcoords)
        screen.blit(j.image,j.rect)
    for k in blocks:
        screen.blit(k.image,k.rect)
    screen.blit(player.image,player.rect)
    pygame.display.update(rects)
    clock.tick(100)

#<===================THEND===================>















        
