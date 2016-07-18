#-----Use this for the start for any new program---------#
import pygame, sys, time , random , math
from pygame.locals import *

# set up pygame
pygame.init()

# Global window definitions


WINDOWWIDTH = 500#Total Width of the Window

WINDOWHEIGHT = 500 # Total Height of the Window


# set up the colors as global constants
BLACK = (0,0,0)
WHITE =  (255,255,255)
YELLOW = (255,255,0)
LIGHTYELLOW = (128,128,0)
RED = (255, 0 ,0)
LIGHTRED = (128,0,0)
BLUE = (0, 0, 255)
SKYBLUE = (135,206,250)
GREEN = (0,255,0)
LIGHTGREEN = (152,251,152)
AQUAMARINE = (123,255,212)
LIGHTBROWN = (210,180,140)
LIGHTGREY = (211,211,211)
DIMGREY = (105,105,105)
VIOLET = (238,130,238)
SALMON = (250,128,114)
GOLD = (255,165,0)
CHOCLATE = (210,105,30)
BACKGROUND = CHOCLATE

# Set up the  window itself
windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Some cool sounding name')

#Used if the program uses keys
pygame.key.set_repeat(200,100)


# this set the background to so it won't be black
# you can choose the color of your preference
# right now it is commented out
'''
background_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
pygame.draw.rect(windowSurface,BACKGROUND,background_rect,0)
'''
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT: 
            sys.exit()
            elif (event.type == KEYDOWN):
                key = pygame.key.name(event.key)
                print(key)
                if ((event.key == K_ESCAPE)
                   or (event.key == K_q)):
                      sys.exit()
				

