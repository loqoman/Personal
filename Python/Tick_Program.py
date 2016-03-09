#-----Use this for the start for any new program---------#
import pygame, sys, time , random , math
from pygame.locals import *

# set up pygame
pygame.init()

# Global window definitions


WINDOWWIDTH = 500#Total Width of the Window

WINDOWHEIGHT = 450 # Total Height of the Window


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

current_t = 0
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
class Widget(object):
# Widget class for all widgets,  its  function is mainly to hold the
# dictionary of all widget objects by name as well as the application
# specific handler function. And support isclicked to
# see if cursor is clicked over widget.

    widgetlist = {} # dictionary of tubles of (button_object,app_handler)
    background_color = BACKGROUND

    def __init__(self):
    # set up default dimensions in case they are not defined in
    # inherited class, this causes isclicked to default to False
        self.left = -1
        self.width = -1
        self.top = -1
        self.height = -1

    def find_widget(widget_name):
    # find the object handle for a widget by name        
        if widget_name in Widget.widgetlist:
            widget_object = Widget.widgetlist[widget_name][0]
            return  widget_object
        else:
            Print ('Error in find_widget, Widget not found ' + widget_name)
            return

    def isclicked (self, curpos):
    # button was clicked, is this the one? curpos is position tuple (x,y)
        

        covered = False

        if (curpos[0] >= self.left and
        curpos[0] <= self.left+self.width and
        curpos[1] >= self.top and
        curpos[1] <= self.top + self.height):
            covered = True

        return covered
    

    def handler(self):
    # prototype for a widget handler to be overridden if desired
        pass     
    
class tick(object):

    global current_t

    def init(name = "ticks"):
        self.name = name
        t_history = []
        global current_t

    def tick_advance(self):
        global current_t
        current_t += 1
        #t_history.append(current_t)
        
    def return_current_tick(self):
        return str(current_t)
        
    def show_ticks(self,Cords):
        cover = pygame.rect
        font = pygame.font.SysFont("comicsansms", 72)
        label = font.render(Ticks.return_current_tick(), 1, (255,255,0))
        windowSurface.blit(label,Cords)
        all_fonts = pygame.font.get_fonts()

Ticks = tick()
#----start of the game loop---------#
while True:
    # check for the QUIT  or mouse event

    Ticks.show_ticks((20,20,20,20))
    time.sleep(2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

