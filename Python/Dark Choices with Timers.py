''' Some useful things for Dark Choices
With addition of the show buttons to show about other windows'''
#--------Things to do that I am writeing down so that I dont froget----
# Change color of scroll                                              |
#                                                                     |
#                                                                     |
#----------------------------------------------------------------------


import pygame, sys, time , random , math
from pygame.locals import *

# set up pygame
pygame.init()

# Global window definitions


WINDOWWIDTH =1000

WINDOWHEIGHT = 700 # Total Height of the Window



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


# Set up the  window global object
windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Dark Choices examples')

# this set the background to so it won't be black
# you can choose the color of your preference
background_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
pygame.draw.rect(windowSurface,BACKGROUND,background_rect,0)








pygame.key.set_repeat(200,100)

#------------------------------------------------------------------
# Define the widget classes
#------------------------------------------------------------------

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
            
class Button(Widget):

    buttonlist = []
    grouplist = {}
    
    def __init__ (self, window = windowSurface,color = BLACK,
                  topleft = (200,200), size=20,name = '', label='',
                  value = '',app_handler=Widget.handler,
                  group = '',groupaction = 'RADIO'):   

        self.hidden = False  # added for Darwin to hide button
        self.old_color = color # hold color during hide
        self.old_label = label # holds label during hide
        self.window = window
        self.color = color
        self.topleft = topleft
        self.left = topleft[0]  # required by isclicked method in Widget
        self.top = topleft[1]   # "
        self.width = size       # "
        self.height = size      # "
        self.right = self.left + size
        self.bottom = self.top + size
        self.size = size
        self.name = name
        self.label = label
        self.labelFont = None # used by the label methods
        self.value = value
        self.app_handler = app_handler # object of applications specific handler
        self.group = group
        
        self.groupaction = groupaction
        # groupaction value of 'RADIO' allows only one in group to be on
        # 'RADIO_WITH_OFF' allows only one but all off also
        # '' means no group action required

        self.state = False    # Initialize button state to 'off'


        # Add widget object keyed by name to widget dictionary.
        # Non-null Widget names must be unique.
        
        if ( (name != '') and (name not in Widget.widgetlist) ):
            Widget.widgetlist[name] = (self,app_handler)
        else:
            print ('Error - duplicate widget name of ' + name)

        Button.buttonlist += [self] # add to button list as a object

        # if button is in a group, add group to dictionary if the group is not
        # already there.  Then add the button to the group.

        if group in Button.grouplist:
            Button.grouplist[group] += (self,)
        else:
            Button.grouplist[group] = (self,)


        
        # get the rectangle for the object
        self.rect = pygame.draw.rect(window,color,
        (topleft[0],topleft[1],size,size),1)

        #write label if any
        if label != '':
           self._label()
            
        self.draw()

    def _label(self): # method to generate label
       labelFont = pygame.font.SysFont(None, int(self.size*1.5) )
       self.labelFont = labelFont  # remember it for erase or relabel
       text = labelFont.render(self.label,True,self.color,
       Widget.background_color)
       
       textRect= text.get_rect()
       textRect.left = self.rect.right + 5
       textRect.bottom = self.rect.bottom
       self.window.blit(text, textRect)
       self.draw()

    def label_erase(self):
    #  method to erase label
       text = self.labelFont.render(self.label,True,Widget.background_color,
       Widget.background_color)
       textRect= text.get_rect()
       textRect.left = self.rect.right + 5
       textRect.bottom = self.rect.bottom
       self.window.blit(text, textRect)
       self.draw()

    def relabel(self,label='',handler=''):
    # method to relabel a button
        self.label_erase()
        self.label = label
        self._label()

    # now change the handler if new one specified
        if handler != '':
            self.app_handler = handler  # set new handler in object
            Widget.widgetlist[self.name] = (self,handler) # also in Widgetlist            
                                                           
    def hide(self):
    # method to hide a button, added for Darwin
        self.hidden = True  # show button as hidden
        self.old_color = self.color # remember color for unhide
        self.old_label = self.label # remember label for unhide
        self.label_erase()
        self.color = BACKGROUND
        self.state = False
        self.draw() # redraw in background color

    def unhide(self):
    # method to unhide a button, added for Darwin
        self.hidden = False
        self.color = self.old_color
        self.label = self.old_label
        self._label() # redraw the label
        self.draw() # redraw in background color
        
    def identify(self):  # print my name
        print ("Button name is:" + self.name)

    def draw (self): # draw button with current state
        

# modified for darwin to draw square buttons only

        if self.state:
            self.rect = pygame.draw.rect(self.window,self.color,
                                        self.rect,0)
        else:
            self.rect = pygame.draw.rect(self.window, self.background_color,
                        self.rect,0)
            self.rect = pygame.draw.rect(self.window, self.color,
                        self.rect,1)
            
        '''
            pygame.draw.circle(self.window,self.color,
            (self.rect.left+int(self.size/2),self.rect.top+int(self.size/2))
            ,int(self.size/2)-2,0)
        else:
            pygame.draw.circle(self.window,WHITE,
            (self.rect.left+int(self.size/2),self.rect.top+int(self.size/2)),
            int(self.size/2)-2,0)
            
            pygame.draw.circle(self.window,self.color,
            (self.rect.left+int(self.size/2),self.rect.top+int(self.size/2)),
            int(self.size/2)-2,1)'''
                               
        pygame.display.update()   # refresh the screen

        
    def toggle (self):  # toggle the button state
        if self.state:
            self.state = False
        else:
            self.state = True
            
        self.draw()




    def group_handler(self):
    # if button in a group, button is now on and is a RADIO button  then
    # turn off all other buttons in the group

        #if groupaction is 'RADIO' or 'RADIO_WITH_OFF'and new state is on,
        # turn off all other buttons in the group. 
        if ( (self.groupaction == 'RADIO') |
             (self.groupaction == 'RADIO_WITH_OFF') ):

            # loop finding other buttons in group and turning them off
            for i in range(len((Button.buttonlist))):

                if (Button.buttonlist[i].group == self.group and
                Button.buttonlist[i] != self):
                    Button.buttonlist[i].state = False
                    Button.draw(Button.buttonlist[i])

        # Now, if 'RADIO' and if new state is off,
        # tun it back on because at least one must be on in the group.
        if self.groupaction == 'RADIO':
            if (self.state == False):
                self.toggle()
                return
#------------------------------------------------------------
# Button handler method,  overriding the Widget
# handler method prototype. Does some general work then calls the
# group handler and application specific handler if any
#------------------------------------------------------------

    def handler(self):

        # don't do anything if the button is hidden
        if self.hidden:
            return

        # toggle the state of the button
        self.toggle()

        # see if button is in a group and if so, call  the group handler
        # in button class to enforce such things as 'RADIO' exclusivity
        if self.group != '':
            self.group_handler()

        # call the application specific handler (if none specified when
        # button is created it defaults to dummy prototype Widget.handler).
        self.app_handler(self)

        return

class Meter_bar(Widget):
# Inherit Widget class to implement a meter bar with moving pointer
# to show value.  Value goes from 0 to 255.

    def __init__ (self, window = windowSurface,color = BLACK,
                  barcolor = RED, topleft = (750,256),
                  width = 10, height = 100,name = '', label='',
                  app_handler=Widget.handler,
                  value = 128):


        self.window = window
        self.color = color
        self.bar_color = barcolor
        self.topleft = topleft
        self.left = topleft[0]  # required by isclicked method in Widget
        self.top = topleft[1]   # "
        self.width = width      # "
        self.height = height    # "
        self.right = self.left + width
        self.bottom = self.top + height
        self.name = name
        self.label = label
        self.app_handler = app_handler
        self.value = value
        

        # Add widget object keyed by name to widget dictionary.
        # Non-null Widget names must be unique.
        
        if ( (name != '') and (name not in Widget.widgetlist) ):
            Widget.widgetlist[name] = (self,app_handler)
        else:
            print ('Error - duplicate widget name of ' + name)

        
        # get the rectangle for the object
        self.rect = pygame.draw.rect(window,color,
        (topleft[0],topleft[1],width,height),0)

        #write label if any
        if label != '':
           self._label()
            
        self.draw()

    def _label(self): # method to generate label for meter
       labelFont = pygame.font.SysFont(None, 15 )
       text = labelFont.render(self.label,True,self.color,
       Controls.background_color)
       
       textRect= text.get_rect()
       textRect.left = self.rect.right + 5
       textRect.bottom = self.rect.bottom
       self.window.blit(text, textRect)
       self.draw()
                                                   

    def identify(self):  # print my name
        print ("Button name is:" + self.name)

    def draw (self): # draw bar_meter with current value
        
        # draw the background rectangle

        self.rect = pygame.draw.rect(self.window, self.color,
        self.rect,0)

        # now overlay the meter bar based on level.
        scaled_height = int (self.value/256. * self.height)
        self.bar_rect = pygame.draw.rect(self.window,self.bar_color,
                        (self.rect.left,self.rect.bottom,self.width,
                        -scaled_height),0)
                               
        pygame.display.update()   # refresh the screen

class Setpoint_bar(Meter_bar):
# Add increment/decrement logic to Meter_bar to allow control of value
# by clicking mouse in upper or lower part of meter bar
    def __init__ (self, window = windowSurface,color = BLACK,
                  barcolor = RED, topleft = (750,256),
                  width = 10, height = 100,name = '', label='',
                  app_handler=Widget.handler,
                  value = 128,perclick = 10): # percent up/down per click


        self.window = window
        self.color = color
        self.bar_color = barcolor
        self.topleft = topleft
        self.left = topleft[0]  # required by isclicked method in Widget
        self.top = topleft[1]   # "
        self.width = width      # "
        self.height = height    # "
        self.right = self.left + width
        self.bottom = self.top + height
        self.name = name
        self.label = label
        self.app_handler = app_handler
        self.value = value
        self.perclick = perclick        

        # Add widget object keyed by name to widget dictionary.
        # Non-null Widget names must be unique.
        
        if ( (name != '') and (name not in Widget.widgetlist) ):
            Widget.widgetlist[name] = (self,app_handler)
        else:
            print ('Error - duplicate widget name of ' + name)

        
        # get the rectangle for the object
        self.rect = pygame.draw.rect(window,color,
        (topleft[0],topleft[1],width,height),0)

        #write label if any
        if label != '':
           self._label()
            
        self.draw()

        # send trigger level to server
        ser.send_trigger_level(self.value)

    def handler(self):
    # handle a click within the setpoint rectangle.

        pos = pygame.mouse.get_pos() # mouse clicked get (x, y)

        # see if in upper or lower part of bar
        if pos[1] < self.top + self.height/2 :
            upper = True
        else:
            upper = False

        # now increment or decrement based on location in bar
        if upper:
            self.value += int(self.perclick/100. * 255)
            if self.value > 255:
                self.value = 255
        else: # in lower part, decrement
            self.value -= int(self.perclick/100. * 255)
            if self.value < 0:
                self.value = 0

        self.draw()

        # send trigger level to the server
        ser.send_trigger_level(self.value)
            

        
        



class Led(Widget):
# Inherit Widget class to implement a LED light. A circle showing
# states of WHITE, GREEN, and RED

    def __init__ (self, window = windowSurface,
                  color = BLACK, # this is outline color for off state
                  topleft = (750,256), size=20,name = '',
                  label='',app_handler=Widget.handler,
                  state = 'GREEN'):
   

        self.window = window
        self.color = color
        self.topleft = topleft
        self.left = topleft[0]
        self.top = topleft[1]
        self.right = self.left + size
        self.bottom = self.top + size
        self.center = ( self.left + int( size/2) , self.top + int (size/2) )
        self.size = size
        self.width = size
        self.height = size
        self.name = name
        self.label = label
        self.app_handler = app_handler
        self.state = state    


        # Add widget object keyed by name to widget dictionary. Widget names
        # must be unique.
        
        if name in Widget.widgetlist:
            print ('Error - duplicate widget name of ' + name)
        else:
            Widget.widgetlist[name] = (self,app_handler)


        #write label if any
        if label != '':
           self._label()
            
        self.draw()

    def _label(self): # private method to generate label, does not do update
       labelFont = pygame.font.SysFont(None, int(self.size) )
       text = labelFont.render(self.label,True,self.color,
       Controls.background_color)
       
       textRect= text.get_rect()
       textRect.left = self.right + 5
       textRect.bottom = self.bottom
       self.window.blit(text, textRect)
                                                   

    def identify(self):  # print my name
        print ("Button name is:" + self.name)

    def draw (self): # draw LED with current state

        if ( (self.state == 'GREEN') or (self.state == 'RED') ):
            if self.state == 'GREEN':
                colortuple = GREEN
            elif self.state == 'RED':
                colortuple = RED

            pygame.draw.circle(self.window,colortuple,
            (self.left+int(self.size/2),self.top+int(self.size/2))
            ,int(self.size/2)-2,0)
        else:
            pygame.draw.circle(self.window,self.color,
            (self.left+int(self.size/2),self.top+int(self.size/2)),
            int(self.size/2)-2,1) # off, draw outline only
                               
        pygame.display.update()   # refresh the screen

class Text(Widget):

    def __init__(self,window=windowSurface,
                 color=BLACK,background_color=Widget.background_color,
                 topleft=(0,0),name= '',
                 font_size=20,max_chars=20,text='',
                 outline=True,outline_width=1,
                 justify = 'LEFT',
                 app_handler=Widget.handler):
        
        # initialize the properties
        self.window=window
        self.color= color
        self.background_color = background_color
        self.name = name
        self.font_size = font_size
        self.max_chars = max_chars
        self.text = text
        self.outline = outline
        self.outline_width = outline_width
        self.justify = justify
        self.app_handler = app_handler
        
        self.topleft=topleft
        self.left=topleft[0]    # reguired by isclicked method in Widget
        self.top=topleft[1]     # "
        
        # render a maximum size string to set size of text rectangle
        max_string = ''
        for i in range(0,max_chars):
            max_string += 'M' # 'M' is one of the biggest letters

        maxFont = pygame.font.SysFont(None,font_size)
        maxtext = maxFont.render(max_string,True,color)
        maxRect= maxtext.get_rect()
        maxRect.left = self.left
        maxRect.top = self.top
        self.maxRect = maxRect  # save for other references
        self.maxFont = maxFont

        # now set the rest required by isclicked method
        self.width = maxRect.right - maxRect.left
        self.height = maxRect.bottom -  maxRect.top
        # plus a couple more for standardization
        self.right = maxRect.right
        self.bottom = maxRect.bottom

        # Add widget object keyed by name to widget dictionary.
        # Non-null Widget names must be unique.
        
        if ( (name != '') and (name not in Widget.widgetlist) ):
            Widget.widgetlist[name] = (self,app_handler)
        elif (name != ''):
            print ('Error - duplicate widget name of ' + name)

        self.draw()  # invoke the method to do the draw

        return   # end of Text initializer

    # Text method to draw the text and any outline on to the screen
    def draw(self):
        # fill the maxRect to background color to wipe any prev text
        pygame.draw.rect(self.window,self.background_color,
                         (self.maxRect.left,self.maxRect.top,
                          self.width, self.height),0)

        # if outline is requested, draw the outline 4 pixels bigger than
        # max text.  Reference topleft stays as specified
        
        if self.outline:
            pygame.draw.rect(self.window,self.color,
                             (self.maxRect.left-self.outline_width-2,
                              self.maxRect.top-self.outline_width-2,
                              self.width+(2*self.outline_width)+2,
                              self.height+(2*self.outline_width)+2),
                              self.outline_width)


        # Now put the requested text within maximum rectangle
        plottext = self.maxFont.render(self.text,True,self.color)
        plotRect = plottext.get_rect()

        plotRect.top = self.top # top doesn't move with justify

        # justify the text
        if self.justify == 'CENTER':
            plotRect.left = self.left + int(plotRect.width/2) 
        elif self.justify == 'LEFT':
            plotRect.left = self.left
        elif self.justify == 'RIGHT':
            plotRect.right = self.maxRect.right
        else:
            print('Illegal justification in Text object ',self.justify, end='\n')

        # blit the text and update screen
        self.window.blit(plottext,plotRect)

        pygame.display.update()

    # Text method to update text and redraw
    def update(self,text):
        self.text = text
        self.draw()

class Number(Text):
# Rectangle for entering numeric values

    def __init__(self,window=windowSurface,
                 color=BLACK,background_color=Widget.background_color,
                 topleft=(750,200),name= '',
                 font_size=20,max_chars=10,value=0,
                 outline=True,outline_width=1,
                 justify = 'RIGHT',
                 app_handler=Widget.handler):
        
        # initialize the properties
        self.window=window
        self.color= color
        self.background_color = background_color
        self.name = name
        self.font_size = font_size
        self.max_chars = max_chars
        self.value = float(value)  # value kept in floating point
        self.text = str(value)
        self.outline = outline
        self.outline_width = outline_width
        self.justify = justify
        self.app_handler = app_handler
        
        self.topleft=topleft
        self.left=topleft[0]    # reguired by isclicked method in Widget
        self.top=topleft[1]     # "
        
        # render a maximum size string to set size of text rectangle
        max_string = ''
        for i in range(0,max_chars):
            max_string += 'D' # 'D' is one of the biggest letters

        maxFont = pygame.font.SysFont(None,font_size)
        maxtext = maxFont.render(max_string,True,color)
        maxRect= maxtext.get_rect()
        maxRect.left = self.left
        maxRect.top = self.top
        self.maxRect = maxRect  # save for other references
        self.maxFont = maxFont

        # now set the rest required by isclicked method
        self.width = maxRect.right - maxRect.left
        self.height = maxRect.bottom -  maxRect.top
        # plus a couple more for standardization
        self.right = maxRect.right
        self.bottom = maxRect.bottom


        # Add widget object keyed by name to widget dictionary.
        # Non-null Widget names must be unique.
        
        if ( (name != '') and (name not in Widget.widgetlist) ):
            Widget.widgetlist[name] = (self,app_handler)
        elif (name != ''):
            print ('Error - duplicate widget name of ' + name)

        self.draw()  # invoke the method to do the draw


        return   # end of Number initializer

    def update_value(self,number_string):
    # number method to update numeric value from text string
        self.value = float(number_string);

        return

    def handler(self):
        # clicked to update number
        old_color = self.color # save values for possible restore
        old_text = self.text
        old_value = self.value

        self.color = BLUE # set up for data entry
        self.text = ''
        self.value = 0
        self.draw()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type is KEYDOWN:
                    key = pygame.key.name(event.key)
                    if ( key == 'return'):
                        if (self.color == RED): # don't allow exit if problem
                            pass
                        else:
                            self.color = old_color
                            self.draw()
                            done = True
                        break
                    
                    if ( key == 'escape'): # restore old values on escape
                        self.color = old_color
                        self.text = old_text
                        self.value = old_value
                        self.draw()
                        done = True
                        break

                    if ( key == 'backspace'): # backspace key
                        if (len(self.text) > 0):
                            self.text = self.text[0:len(self.text)-1]

                    if key.isdigit():
                        self.text += key # digits are OK
                        
                    if ( (len(self.text) == 0) ): # allow '+' '-' as first char
                        char = ''
                        if (key == '='): # unshifted '+'
                            char = '+'
                        if (key == '-'):
                            char = '-'
                        self.text += char 
                        
                    if ( (key == '.') & ( '.' not in self.text) ):
                        self.text += '.' # only one period allowed
                    
                    try:
                        float(self.text)
                        self.update_value(self.text)
                        self.color = BLUE
                    except ValueError:
                          self.color = RED
                    self.draw()
        # exited number entry loop
        self.app_handler(self)  # do applications specific work

class Scroll(Widget):
# Class to implement a scrolling set of lines
    def __init__(self,window=windowSurface,num_lines=4,
                 color=BLACK,background_color=Widget.background_color,
                 topleft=(0,0),name= '',text='line test',
                 font_size=18,max_chars=72,
                 outline=True,outline_width=1,
                 justify = 'LEFT',
                 app_handler=Widget.handler):
        
        # initialize the properties
        self.window=window
        self.num_lines = num_lines
        self.color= color
        self.background_color = background_color
        self.name = name
        self.font_size = font_size
        self.max_chars = max_chars
        self.text = text
        self.outline = outline
        self.outline_width = outline_width
        self.justify = justify
        self.app_handler = app_handler
        
        self.topleft=topleft
        self.left=topleft[0]    # reguired by isclicked method in Widget
        self.top=topleft[1]     # "

        # implement the scoll using the Text class
        # define the sent lines on the display
        self.lines = []
        for i in range (0,self.num_lines):
            if i == 0:
                topleft = self.topleft
            else:
                topleft = (0,self.lines[i-1].bottom)
            line = Text(topleft = topleft,max_chars=max_chars,
                        background_color=background_color,color=color,
                        font_size=self.font_size,
                        text=self.text,
                        outline=outline)
            self.lines.append(line)
            self.bottom = line.bottom  # remember where the bottom is
        # set the current input line index to the first line
        self.line_idx = 0

        return # return from Scroll.__init__()

    def append(self,string):
    # Scroll append method to add a string to the scroll lines

        # check to see if the current line is already full
        if len(self.lines[self.line_idx].text)+len(string) >= self.max_chars:
            #current line is full, see if we can just go down
            if self.line_idx <= self.num_lines-2:
                self.line_idx +=1 # OK just go down a line
            else:  # scroll is full, need to scroll up
                for i in range(1,self.num_lines): # scroll up the lines
                    self.lines[i-1].text = self.lines[i].text
                    self.lines[i-1].draw()
                self.line_idx = self.num_lines-1 # set the index to the last line
                self.lines[self.line_idx].text = ''  # blank the last line
                self.lines[self.line_idx].draw()


        # Now append the string on to the line
        if not string.endswith(' '): # if string doesn't have end space, add one
            string += ' '
        self.lines[self.line_idx].text += string
        self.lines[self.line_idx].draw()

        return # return from Scroll.append()

    def backspace(self):
    # Scroll backspace method to delete the last character in the scroll

        # check if there are still characters in the current line
        if len(self.lines[self.line_idx].text) > 0:
            self.lines[self.line_idx].text = (
            self.lines[self.line_idx].text[:len(self.lines[self.line_idx].text)-1] )
            self.lines[self.line_idx].draw()
        else: # nothing left on the current line
            if self.line_idx > 0: # make sure we were not already on first line
                self.line_idx -= 1 # back up one line
                if len(self.lines[self.line_idx].text) > 0:# do it again              
                    self.lines[self.line_idx].text = (
                    self.lines[self.line_idx].text[:len(self.lines[self.line_idx].text)-1] )
                    self.lines[self.line_idx].draw()

        return # return from Scroll.backspace

    def return_key(self):
    # Scroll method to handle the return key
    # moves to the next line 

        if self.line_idx < self.num_lines-2:
            self.line_idx += 1  # go down to the next line
            self.lines[self.line_idx].text = '' 
            self.lines[self.line_idx].draw()
        else:  # we are on the last line so need to scroll up
            for i in range(1,self.num_lines): # scroll up the lines
                self.lines[i-1].text = self.lines[i].text
                self.lines[i-1].draw()
            self.line_idx = self.num_lines-1 # set the index to the last line
            self.lines[self.line_idx].text = ''
            self.lines[self.line_idx].draw()

        return # return from Scroll.return_key()

    def writeln(self,text=''):
    # Scroll method to write a line followed by a return(new line)

    # Start on a empty line
        if self.lines[self.line_idx].text != '': # check for null current line
            self.return_key() # if not, start on a new line
        self.append(text)
        self.return_key()

        return # return from Scroll.writeln()

    def escape(self):
    # Scroll method to handle the escape key

        # clear all the lines to nulls and reset line index to first line
        for i in range(0,self.num_lines):
            self.lines[i].text = ''
            self.lines[i].draw()
        self.line_idx = 0 # set to first line

        return # return from Scroll.escape
            

class Rectangle(Widget):
# class to wrap the pygame rectangle class to standardize with Widgets 

    def __init__(self, window=windowSurface,color=BLACK,
                 topleft = (200,200), width = 30, height = 20,
                 name = '',outline_width = 1, # width of outline, 0 = fill
                 app_handler=Widget.handler):

        self.window = window
        self.color = color
        self.topleft = topleft
        self.left = topleft[0]      # required by isclicked method in Widget
        self.top = topleft[1]       # "
        self.width = width          # "
        self.height = height        # "
        self.right = self.left + width
        self.bottom = self.top + height
        self.name = name
        self.outline_width = outline_width
        self.app_handler = app_handler

        # Add widget object keyed by name to widget dictionary.
        # Non-null Widget names must be unique.
        
        if ( (name != '') and (name not in Widget.widgetlist) ):
            Widget.widgetlist[name] = (self,app_handler)
        elif (name != ''):
            print ('Error - duplicate widget name of ' + name)

        self.draw()  # invoke the draw method to draw it

        return

    def draw(self):     # Rectangle method to do the draw
        
        # get a rectangle object and draw it
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)
        pygame.draw.rect(self.window,self.color,self.rect,
                         self.outline_width)
        pygame.display.update(self.rect)

        return
    
    def handler(self):  # Rectangle handler
        self.app_handler(self)  # nothing special to do, call app_handler
        return

#----------------- End of Widget Classes -----------------------------------

#------------------- Collection Class  -------------------------------------
# A general class to handle a collection of items including the count of how
# many of a given item we have.  The items and their
# associated counts are  within a dictionary

class Collection(object):

    def __init__(self,name=''):
    # initialization for the collection
        self.name = name
        self.collection = {} # initialize and empty collection


    def add(self,item):
    # add an item to the collection.  If one already exists, just increment
    # the count for that item.
        if item in self.collection:
            self.collection[item] += 1 # in already, just add to count
        else: # not found add it and set the count to 1
            self.collection[item] = 1

    def get(self,item):
    # get an item from the collection. If one or more of them exists, the
    # item is returned and the count is decremented.  If it reaches 0 the
    # item name is deleted from the list. If the item doesn't exist None is
    # returned.

        if item in self.collection: # ensure we have one
            return_item = item  # pass it back in the return
            self.collection[item] -= 1 # decrement the count
            if self.collection[item] <= 0:
                del self.collection[item]
        else:  # none was available
            return_item = None

        return return_item  #

    def get_random(self):
    # get a random item from the collection.  The item is returned.  If none
    # is available, None is returned.

        items = self.collection.items()
        item_list = []
        for item in items:
            item_list.append(item[0])

        if len(item_list) == 0:
            return None  # no items in the collection
        else:
            item = random.choice(item_list)
            item = self.get(item)
            return item

    def number_of(self,item):
    # check to see if an item is in a collection

        if item in self.collection:
            return  self.collection[item] # return the number of items
        else:
            return 0  # item not in there, return 0

    def scroll_contents(self,scroll_object):
    # Collection method to write the contents of a collection to a scroll
        scroll.writeln(self.name + ' contains:')
        items = self.collection.items()
        for item in items:
            scroll_object.append(item[0]+' ('+str(item[1])+') / ')
            
#----------------Timer Class ----------------------------------------
# A class to implement a collection of timer functions

class Timer(object):

    timers = []  # create an empty list of all timers

    def process():
    # Timer processor, called from the main loop at the class
    # level to process timers
        for timer_object in Timer.timers:
            if timer_object.delay > 0.0: # timer is active
                if (time.time() - timer_object.start_time) > timer_object.delay:
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



        
#------------------ End of Timer Class -------------------------------------        
                

#-------------- Applications specific Widget handlers ----------------------
# these are called from the button class, they are functions that get tied to
# specific buttons at the time buttons are made.

def pickup_handler(self):
# handler for pick up button, called at mouse click

    scroll.writeln('Pick up button was pressed')

    # change the option buttons for pickup
    change_button('Option1','Hammer',pickup_option_handler)
    change_button('Option2','Nails',pickup_option_handler)
    change_button('Option3','Wood',pickup_option_handler)

def pickup_option_handler(self):
# handle the option buttons associated with the pickup action

    #From the label, find out what we are to get
    item = self.label

    # logic to put in our pouch or whatever goes here
    scroll.writeln('Pickup up '+item)
    time.sleep(.5)
    self.toggle()


def drop_handler(self):  # handler for drop button, called at mouse click
    scroll.writeln('Drop button was pressed')
    change_button('Option1','Sword',drop_option_handler)
    change_button('Option2','Hat',drop_option_handler)
    change_button('Option3','Hammer',drop_option_handler)

def drop_option_handler(self):
# handle the option buttons associated with the drop action

    # From the label, find out what to drop
    item = self.label

    # logic to take thing out of inventory or whatever
    scroll.writeln('Drop '+item)
    time.sleep(.5)
    self.toggle()


def move_handler(self):  # handler for move button, called at mouse click
    scroll.writeln('Move button was pressed')
    change_button('Option1','to city',move_option_handler)
    change_button('Option2','to woods',move_option_handler)
    change_button('Option3','East',move_option_handler)

def move_option_handler(self):
# handle the option buttons associated with the move action

    # From the label, find where to go
    item = self.label

    # logic to change our location or whatever
    scroll.writeln('Move '+item)
    time.sleep(.5)
    self.toggle()

def show_handler(self):  # handler for show button, called at mouse click
    scroll.writeln('Show button was pressed')
    change_button('Option1','Blue Window',show_option_handler)
    change_button('Option2','Picture',show_option_handler)
    change_button('Option3','Erase',show_option_handler)

def show_option_handler(self):
# handle the option buttons associated with the show action

    # From the label, find where to go
    item = self.label

    # logic to change our location or whatever
    scroll.writeln('Show '+item)

    # display different surface based on the name
    if item == 'Blue Window':
        image = pygame.Surface((400,300))
        image.fill(BLUE)
        pygame.draw.circle(image,RED,(200,200),50,0)
        pygame.Surface.blit(windowSurface,image,(550,300))
        pygame.display.update()
    elif (item == 'Picture'):
        picture = pygame.image.load('somestuff.jpg')
        scaled_picture = pygame.transform.scale(picture,(400,300))
        pygame.Surface.blit(windowSurface,scaled_picture,(550,300))
        pygame.display.update()
    elif (item == 'Erase'):
        image = pygame.Surface((400,300))
        image.fill(BACKGROUND)
        pygame.Surface.blit(windowSurface,image,(550,300))
        pygame.display.update()
    
        
        
    time.sleep(.5)
    self.toggle()
def change_button(name='',label='',handler_function=''):
# change button label and handler by name
    # look up the button object using the name
    button_object = Widget.find_widget(name)
    button_object.relabel(label,handler_function)

def timer4_handler():
    # this is a sample handler connected to a timer to show that
    # a handler can be connected to a timer.
    scroll.writeln('Timer 4 for one minute expired, cancel timer 2')
    tim2.cancel()
    

#------------------ End of Widget handlers --------------------------------
#-------------Initialization routines to set  buttons --------
def game_init():
# main game initialization routine to set up screen and some game variables
    # build the action group buttons in the left column
    but1 = Button(name='but1',color=BLACK,
                  topleft = (500,25),
                  size = 12,label = 'Label for hide test',
                  app_handler = pickup_handler,
                  group='Action')

    but2 = Button(name='but2',color=BLACK,
                  topleft = (but1.left,but1.bottom+5),
                  size = 12,label = '       ',
                  app_handler = drop_handler,
                  group='Action')

    but3 = Button(name='but3',color=BLACK,
                  topleft = (but2.left,but2.bottom+5),
                  size = 12,label = '       ',
                  app_handler = move_handler,
                  group='Action')

    but4 = Button(name='but4',color=BLACK,
                  topleft = (but3.left,but3.bottom+5),
                  size = 12,label = '       ',
                  app_handler = show_handler,
                  group='Action')

    #build the option group buttons in the right column
    #they are left blank for now
    opt1 = Button(name='Option1',color=BLACK,
                  topleft = (700,25),
                  size = 12, label ='       ',
                  group = 'Option')

    opt2 = Button(name='Option2',color=BLACK,
                  topleft = (opt1.left,opt1.bottom+5),
                  size = 12, label = '      ',
                  group = 'Option')    

    opt3 = Button(name='Option3',color=BLACK,
                  topleft = (opt2.left,opt2.bottom+5),
                  size = 12, label = '      ',
                  group = 'Option')


    opt4 = Button(name='Option4',color=BLACK,
                  topleft = (opt3.left,opt3.bottom+5),
                  size = 12, label = '      ',
                  group = 'Option')
    
    
    

#****************** Main program **************************************

# call the game initialization routine to set up buttons  and attach
# them to their handlers

game_init()

scroll = Scroll(num_lines=30,topleft=(0,20),text = '',
        background_color=WHITE,color = BLACK,
        font_size=18,max_chars = 50,
        outline=False)
  
Inventory = Collection(name='Knapsack')

# this is some code to show how to use the collection Class
# you can have as many collections as you want in order to keep
# up with various things
#---------------------look at the green text to look at for more collection stuff---
'''
# write the contents of the knapsack to the scroll
knapsack.scroll_contents(scroll)

# use the .number_of method to find out how many hammers in knapsack
num_hammers = knapsack.number_of('Hammer')

# use the .get method to get a hammer out of the sack
item = knapsack.get('Hammer')
scroll.writeln('Retrieved '+item+' using .get')

# use the .get_random method to get a random item out of the sack
item = knapsack.get_random()
scroll.writeln('Retrieved '+item+' randomly')

# scroll the contents again to see what is left
knapsack.scroll_contents(scroll)

# output some text to show how it is done. scroll is a global
# object so you can write from anywhere in the program by invoking
# the scroll.append() method. If you want a new line, invoke
# scroll.return_key().  Otherwise it will auto wrap at the end of
# the line.
'''
#----------End of green text----------------------------------------------------
# you can also use the new scroll.writeln method to make sure you are
# on a new line each time. No need for a .return_key call
time.sleep(3)
scroll.writeln('You wake up under a large, spreading tree at the edge of a field.')
time.sleep(2)
scroll.writeln('A large forest is visible in the distance.')
time.sleep(2)
scroll.writeln('Even farther still is a mountain range with snow capped peaks.')
time.sleep(2)
scroll.writeln('What do you wish to do?')

# this is code to test the hide logic
scroll.writeln('hide the first two buttons for 5 seconds')
button = Widget.find_widget('but1')
button.hide()
button = Widget.find_widget('but2')
button.hide()
time.sleep(5)
scroll.writeln('Now unhide the first two buttons')
button = Widget.find_widget('but1')
button.unhide()
button = Widget.find_widget('but2')
button.unhide()

# Test timers
scroll.writeln('Set some timers to test timer logic')
tim1 = Timer()
tim1.set (5,repeat=True) # Timer 1 for 5 seconds with repeats
tim2 = Timer()
tim2.set (10,repeat=True) # Timer 2 for 10 seconds with repeats
tim3 = Timer()
tim3.set(30,repeat=False)  # Timer3 for 30 seconds with no repeats
tim4 = Timer()
tim4.set(60,repeat=False,handler=timer4_handler) # set timer 3 with handler

              

#--------------------------------------------------------------
# Top of main program loop 
#--------------------------------------------------------------

while True:

    # some logic to test the timers
    if tim1.check_state():
        scroll.writeln('tim1 for 5 seconds expired')
        tim1.reset_state()
    if tim2.check_state():
        scroll.writeln('tim2 for 10 seconds expired')
        tim2.reset_state()
    if tim3.check_state():
        scroll.writeln('tim3 for 30 seconds expired, no repeat')
        tim3.reset_state()
        scroll.writeln('Cancel timer 1')
        tim1.cancel()

    # check for the QUIT  or mouse event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() # mouse clicked get (x, y)

            # check through widget dictionary and call handler if clicked
            for widgetname in Widget.widgetlist:
                widget_object = Widget.find_widget(widgetname)

                if widget_object.isclicked(pos):
                    widget_object.handler()
    
    Timer.process()
    time.sleep(.1) # just kill a bit of time

