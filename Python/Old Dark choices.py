#---------------Inination code ver 0.1-------------

import pygame,sys, time, random
from pygame.locals import *

pygame.init()
# Rec = recources
TREEHOUSEREC = "12 bords,14 nails"
BUTTONCOLOR = (184, 134, 11)
WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
BACKGROUND = (128, 0 , 0)
windowSurface = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
pygame.display.set_caption('CHAGE THIS LATER')
Inventory = []
#--------------------Button Inination ver 0.1-----------

def collect(item,num):
    inventory.append('x' + num + item)
    
def build_start(tree,hut,cave):
    if tree == 1:
        write_text(text='You build a small wooden platform from wood and nails',
            topleft =(250,250),font_size=45,color=YELLOW)
        treeHouse = true
    elif hut == 1:
        hut = true
        write_text(text='You build a wodden shack near a rather tall tree',
            topleft=(250,250),font_size=45,color=YELLOW)
    elif cave == 1:
        caveHouse = true
        write_text(text='You dig a ditch under a fallen tree with a plank and reenforce it with wooden platforms',
            topleft=(250,250),font_size=45,color=YELLOW)


def search(item1,item2,rare,chance1,chance2,chance3):
    Chance = random.randrange(0,100)
    if Chance <= chance1:
         item1N = random.randrange(1,3)
         add_inventory(item1,item1N)
    if chance > chance1 and chance > chance2:
         item1N = random.randrange(1,2)
         item2N = random.randrange(1,3)
         add_inventory(item1,itemN)
         add_inventory(item2,itemN)
    if chance > chance2 and chance > chance3:
         rareN = 1
         add_inventory(rare,rareN)
# OK, im hopeing for this to be a button that just stays there the whole game

    

        






#50 40 10










































    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()









        
