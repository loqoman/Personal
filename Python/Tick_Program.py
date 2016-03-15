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
test = 'you made it this far'
BACKGROUND = BLACK

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

#--------------YAY TIMERS!------------------#    
class Timer(object):

    timers = []  # create an empty list of all timers

    print(timers)
    

    def process():
    # Timer processor, called from the main loop at the class
    # level to process timers
        for timer_object in Timer.timers:
            if timer_object.delay > 0.0: # timer is active
                if (time.time() - timer_object.start_time) >= timer_object.delay:
                    # timer has timed out
                    timer_object.state = True
                    timer_object.start_time = time.time()
                    if not (timer_object.handler == ''): # see if handler exists
                        timer_object.handler() # call the handler
                    if not timer_object.repeat:
                        timer_object.delay = 0.0
                    # else leave the delay in place so it will repeat

    def __init__(self,name='',handler='',repeat=False):
    # constructor for timer, must set with .set() method
        self.name = name
        self.start_time = time.time()
        self.delay = 0.0
        self.handler = ''
        self.repeat = repeat
        self.state = False  # show time not timed out
        Timer.timers += [self] # add timer object to the list of timers
        

    def set(self,delay,handler='',repeat=False):
    # set a timer, optionally associate a handler with it
        self.delay = delay   # time period in seconds WHY IS THIS CALLED DELAY?!?!?! I need to fuckign change that
        self.handler = handler
        self.repeat = repeat
        self.start_time = time.time()

    def check_state(self):
    # check the state of the timer, return true if timed out
        return self.state

    def reset_state(self):
    # reset the state of the counter to false
        self.state = False
        
    def cancel(self):
    # cancel a timer
        self.delay = 0.0
        self.state = False
        timer_object.state = True
        timer_object.start_time = time.time()
        if not (timer_object.handler == ''): # see if handler exists
            timer_object.handler() # call the handler
            if not timer_object.repeat:
                timer_object.delay = 0.0
                    # else leave the delay in place so it will repeat

    def __init__(self,name='',handler='',repeat=False):
    # constructor for timer, must set with .set() method
        self.name = name
        self.start_time = time.time()
        self.delay = 0.0
        self.handler = ''
        self.repeat = repeat
        self.state = False  # show time not timed out
        Timer.timers += [self] # add timer object to the list of timers
        

    def set(self,delay,handler='',repeat=False):
    # set a timer, optionally associate a handler with it
        self.delay = delay   # time period in seconds
        self.handler = handler
        self.repeat = repeat
        self.start_time = time.time()

    def check_state(self):
    # check the state of the timer, return true if timed out
        return self.state

    def reset_state(self):
    # reset the state of the counter to false
        self.state = False
        
    def cancel(self):
    # cancel a timer
        self.delay = 0.0
        self.state = False
#---------------------END OF TIMERS------------------------------#
        
#---------Everything byond this point is being prototyped-----------#

ticksPerSec = Timer()# I only ever want 20 TPS so using this calss im able to do so.


class tick(object):

    global current_t # Need the global stuff because otherwise it cant read outside of this varible
    #print('foo')

    def init(name = "ticks"):
        self.name = name
        t_history = []
        global current_t
        ticksPerSec.set( .05,repeat=True)

    def tick_advance(self): # ONLY ever adds to the current tick and appends to the tick list.
        global current_t    # I think in the future I want the tick list to come back, be able to read back into histroy and find out what happened during that time.
        #t_history.append(current_t)
        if ticksPerSec.check_state():
            current_t += 1
            

    def return_current_tick(self):
        return str(current_t)
        
    def show_ticks(self,Cords, font_size):
        pygame.draw.rect(windowSurface, BACKGROUND, (Cords[0], Cords[1],font_size + 50,font_size + 10 ), 0) # Drawing over the last number
        font = pygame.font.SysFont("comicsansms", font_size )




        label = font.render(Ticks.return_current_tick(), 1, (255,255,0))
        windowSurface.blit(label,Cords)
        all_fonts = pygame.font.get_fonts()

Ticks = tick()
#----start of the game loop---------#
while True:
    # check for the QUIT  or mouse event
    #print(ticksPerSec.check_state())
    Timer.process()
    
    Ticks.show_ticks((20,20,20,20), 15)
    
    Ticks.tick_advance()
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

