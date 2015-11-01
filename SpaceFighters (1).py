"""                 _______
                   |_TO_DO_|
   Be sure to do powerups for guns and stuff
   Be shure to start work on a light bike game
       SPACE FIGHTERS! Verson 0.1 BETA!



"""
import pygame, sys, time, random
from pygame.locals import *

pygame.init()

disappear = 0
WHITE =  (255,255,255)
S1speed = 3
S2speed = 3
STARTTIME = time.time()
YELLOW = (255,255,0)
RED = (255, 0 ,0)
BLUE = (0, 0, 255)
ASTROIDCOLOR = (169, 169, 169)
BACKGROUND = (0,0,0)
WINDOWWIDTH = 1350
WINDOWHEIGHT = 400
ASTNUM = 25
windowSurface = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
pygame.display.set_caption('CHAGE THIS LATER')

#==================================================================#
astspeed = []
powerPill = []
PPnum = 9
astroid = []
power = []
speedKeep = []
for i in range(0,ASTNUM):
    Ay = random.randrange(0,WINDOWHEIGHT-100)
    Ax = random.randrange(60,WINDOWWIDTH-100)#where the astroid is
    astroid.append(pygame.Rect(Ax,Ay,70,60))
    astspeed.append(random.randrange(1,5))
    AstS = random.randrange(20,80)
    astroid[i].size = (AstS,AstS)#speaks for itself
for i in range (0,PPnum):#power pill stuff
    Px = random.randrange(100,WINDOWWIDTH-100)
    Py = random.randrange(0, WINDOWHEIGHT)
    powerPill.append(pygame.Rect(Px,Py,5,5))
   # pygame.draw.rect(windowSurface,WHITE, powerPill[i])  
    power.append
for i in range (3,PPnum):
    power.append(i)
    
#==================================================================#


Ship1 = pygame.Rect(20, 200,10, 10)
Ship2 = pygame.Rect(WINDOWWIDTH - 30,200,10,10)


pygame.key.set_repeat(50,50)
#================================================================#
while True:#Game loop. everything after this has to be indented
    currenttime = time.time()
    elapsedtime = currenttime -STARTTIME
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type is KEYDOWN:
            pygame.draw.rect(windowSurface, BACKGROUND, Ship2)
            pygame.draw.rect(windowSurface, BACKGROUND, Ship1)
            key = pygame.key.name(event.key)
            if(key == 'd'):
                Ship1.left += S1speed
              
            elif(key == 's'):
                Ship1.bottom += S1speed
                if Ship1.bottom >= WINDOWHEIGHT:
                    Ship1.bottom = WINDOWHEIGHT-2
            elif(key == 'a'):
                Ship1.left -= S1speed
                if Ship1.left <= 0:
                    Ship1.left = 0 
            elif(key == 'w'):
                Ship1.bottom -= S1speed
                if Ship1.top <= 0:
                    Ship1.top = 0
            if(key == 'right'):
                Ship2.left += S2speed
                if Ship2.right >= WINDOWWIDTH:
                    Ship2.right = WINDOWWIDTH - 2
            elif(key == 'down'):
                Ship2.bottom += S2speed
                if Ship2.bottom >= WINDOWHEIGHT:
                    Ship2.bottom = WINDOWHEIGHT-2
            elif(key == 'left'):
                Ship2.left -= S2speed
            elif(key == 'up'):
                Ship2.bottom -= S2speed
                if Ship2.top <= 0:
                    Ship2.top = WINDOWHEIGHT - 400
    print(S1speed)                

            

    if Ship1.right >= WINDOWWIDTH:
            # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont(0,90)#setting for the font it self
        
        # render text
        label = myfont.render("RED SHIP WINS!!!", 1,RED)#("text",size, color
        textrec = label.get_rect()
        textrec.top=WINDOWHEIGHT/2#puttting the textrec on the screen
        textrec.left=200#above
        windowSurface.blit(label,textrec)#putting the text rec onto the surface
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    if Ship2.left <= 0:
            # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont2 = pygame.font.SysFont(0,90)#setting for the font it self
        
        # render text
        label = myfont2.render("YELLOW SHIP WINS!!!", 1,YELLOW)#("text",size, color
        textrec = label.get_rect()
        textrec.top=200#puttting the textrec on the screen
        textrec.left=200#above
        windowSurface.blit(label,textrec)#putting the text rec onto the surface
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    



    pygame.draw.rect(windowSurface, YELLOW, Ship2)
    pygame.draw.rect(windowSurface, RED, Ship1)
   
    
 
    #print(astroid.left)
    pygame.display.update()


    #============================================================#
    
    

#============================================================================#
    powerloc = Ship1.collidelist(powerPill)
    if powerloc >= 0:
        if power[powerloc] == 1:
            S1speed += 1
            power[powerloc] = 0
            pygame.draw.rect(windowSurface,BACKGROUND,powerPill[powerloc])

    
    '''for i in range(0,len(powerPill)):
        if power[i] > 0:
            pygame.draw.rect(windowSurface,WHITE, powerPill[i])   
'''



    
    for i in range(0,ASTNUM):
        pygame.draw.rect(windowSurface, BACKGROUND, astroid[i])
        if astroid[i].top >= WINDOWHEIGHT:
            astroid[i].bottom = 0
        astroid[i].bottom += astspeed[i]
        pygame.draw.rect(windowSurface, ASTROIDCOLOR,astroid[i])
    if Ship1.collidelist(astroid) > -1:
        pygame.draw.rect(windowSurface, BACKGROUND, Ship1)
        Ship1.left = 0
    if Ship2.collidelist(astroid) > -1:
        pygame.draw.rect(windowSurface, BACKGROUND, Ship2)
        Ship2.right = WINDOWWIDTH
    powerloc = Ship1.collidelist(powerPill)
 #   for i in range(0,PPnum):
  #      pygame.draw.rect(windowSurface, WHITE, powerPill[i])
  
    powerloc = Ship1.collidelist(powerPill)
    if powerloc >= 0:
        S1speed += 1
        power[powerloc] = 0



    time.sleep(.05)
#==============+==+====================================================#
  
    
    

    
#Everything before this i can work in
    
    
    



