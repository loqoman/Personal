
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
#windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT),0,32)
#pygame.display.set_caption('Some cool sounding name')   #--I dont really need pygame for this. --#

#Used if the program uses keys
pygame.key.set_repeat(200,100)


# this set the background to so it won't be black
# you can choose the color of your preference
# right now it is commented out
'''
background_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
pygame.draw.rect(windowSurface,BACKGROUND,background_rect,0)
'''
#--Start of program --#
class Player(object):
	def __init__ (self, name, gender):
		self.name = name
		self.gender = gender
	def say(self, words):
		print(words)
class NPC(object):   # the idea is to have the NPC something like:  <townie1 = NPC(Bob, man)>
	def __init__(self, name = 'NPC' ,layerN1 = 'NPC,trait):
		self.name = name
		self.trait = trait
		self.Layer_Name_1 = layerN1
	def say(self, words):
		print(name + ": " + words)
class Item(object):
	def __init__ (self, title = 0, weapon = 'gun' ,DMG_min = 0, DMG_max = 10):
		self.name = name
		self.weapon = weapon
		self.DMG_min = DMG_min
		self.DMG_max = DMG_max


plasma = Item(title = 'hevenly', weapon = 'gun', DMG_min = 3, DMG_max = 10)

IntroGuide = NCP(name = 'Sylva-sylver-spring' , layerN1 = 'Space-worker')# still not shure what the difference between ' and " is#

IntroGuide.say ("Hello?")
	

		

