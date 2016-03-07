#-----Use this for the start for any new program---------#
import pygame, sys, time , random , math
from pygame.locals import *

# set up pygame
pygame.init()

# Global window definitions


WINDOWWIDTH = 1000#Total Width of the Window

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
LIGHTGREY = (128,128,128)
DIMGREY = (105,105,105)
VIOLET = (238,130,238)
SALMON = (250,128,114)
GOLD = (255,165,0)
CHOCLATE = (210,105,30)
BACKGROUND = LIGHTGREY

# Set up the  window itself
windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Apallo 18')

#Used if the program uses keys
pygame.key.set_repeat(200,100)

#pygame.display.toggle_fullscreen()  [does nothing?]

# this set the background to so it won't be black
# you can choose the color of your preference
# right now it is commented out


background_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)

pygame.draw.rect(windowSurface,BACKGROUND,background_rect,0)




#-------------------------Beggining of basic wigit handlers--------------------#
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


#-------------------------------------#
'''
Plan to try to mini the lED and use it on some buildings
'''
#-------------------------------------#




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
            

            

class Button(Widget):

    buttonlist = []
    grouplist = {}
    
    def __init__ (self, window = windowSurface,color = BLACK,
                  topleft = (200,200), size=20,name = '', label='',
                  value = '',app_handler=Widget.handler,
                  group = '',groupaction = 'RADIO'):   

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


class Building(Widget):

    def __init__ (self,img,x=75,y=75,topLeftX = 500, topLeftY = 500,label = 'Text!',phont_size = 20 ):

        self.img = img
        
        self.x = x
        self.y = y
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.phont_size = phont_size

        topLeft = (topLeftX,topLeftY)
        building = pygame.image.load(img).convert()
        scaled_building = pygame.transform.scale(building,(x,y))

        pygame.Surface.blit(windowSurface,scaled_building,topLeft)

        Label = Text(color=BLACK,background_color=GOLD,font_size = self.phont_size, topleft = (self.topLeftX,self.topLeftY - 13), max_chars = 10 ,text = label,justify =
        'LEFT',outline = False)


        

        
    def draw(self):
        while True:
            print("You got this far!")
            time.sleep(.1)
            pos = pygame.mouse.get_pos()
            #pygame.Surface.blit(windowSurface,scaled_building,(pos))
            pygame.draw.rect(windowSurface, GOLD, (pos,20,20), 0)
#---------------
        

        

        
#-----End of class defineing section-------------#
'''

        Make class items section
'''
#------------------------------------------------#

Command_bar_background = Rectangle(window = windowSurface,topleft = (0,550), width = WINDOWWIDTH, height = 5000,color = GOLD,outline_width = 0 )

Solar_Panel = Building(img = 'solarPanel.jpg',
                       x=75,y=75,topLeftX = 45, topLeftY = 600, label = 'solar panel',phont_size = 20)



while True:

    
    
    # check for the QUIT  or mouse event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos() # mouse clicked get (x, y)
            Solar_Panel.draw

            # check through widget dictionary and call handler if clicked
            for widgetname in Widget.widgetlist:
                pos = pygame.mouse.get_pos() # mouse clicked get (x, y)
                widget_object = Widget.find_widget(widgetname)
                
                if widget_object.isclicked(pos):
                    widget_object.handler() 
    Solar_Panel.draw
    print(pygame.mouse.get_pos())
    time.sleep(.1) # just kill a bit of time
    pygame.display.update()



'''
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
'''
'''
        label = Text(self,windowSurface,topleft=(

#    def __init__(self,window=windowSurface,
                 #  color=BLACK,background_color=Widget.background_color,
                 #  topleft=(0,0),name= '',
                 #  font_size=20,max_chars=20,text='',
                 #  outline=True,outline_width=1,
                 #  justify = 'LEFT',
                 #  app_handler=Widget.handler):

'''


