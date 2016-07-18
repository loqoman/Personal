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
WINDOWWIDTH = 1250
WINDOWHEIGHT = 750
MAZE_TOPLEFT = (50,150)   # Top left corner of the maze area
MAZE_WIDTH = 1000
MAZE_HEIGHT = 600

# Set up the  window itself
windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Some cool sounding name')

ROOMS_V = int(input("How many horizional rooms do you want?"))
ROOMS_H = int(ROOMS_V * (float(MAZE_WIDTH)/float(MAZE_HEIGHT)))


#Used if the program uses keys
pygame.key.set_repeat(WINDOWWIDTH,WINDOWHEIGHT)


# this set the background to so it won't be black
# you can choose the color of your preference
# right now it is commented out
'''
background_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
pygame.draw.rect(windowSurface,BACKGROUND,background_rect,0)
'''
class Maze(object):
#



    def __init__(self):
    # Maze initialization method called when maze is created

        
        return  # return from Maze.__init__

    def build(self,difficulty = 'M'):
    # Maze.build function called at the Maze object level to build a maze.
        if difficulty == 'E':
            temp_rooms = int(ROOMS_V / 2)
        elif difficulty == 'M':
            temp_rooms = int(ROOMS_V)
        elif difficulty == 'H':
            temp_rooms = int(ROOMS_V * 2)
        elif difficulty == 'H+':
            temp_rooms = int(ROOMS_V * 4)

        # Fill in the rooms array with the room objects
        for h in range (0,int(temp_rooms * (float(MAZE_WIDTH)/float(MAZE_HEIGHT)))):
            Room.rooms.append([])  # this creates the second dimension
            for v in range(0,temp_rooms):
                room = Room(size=int(float(MAZE_HEIGHT)/float(temp_rooms)),row=v,col=h)
                Room.rooms[h].append(room)
                Room.unused_rooms.append(room)
        
        # generator doesn't mark the starting room because it is used for branches
        # so mark the starting room as solid white
    def reset(self):
    # Maze method to reset the room array to initial condition
        Room.unused_rooms = []  # empty the unused rooms list
        for col in range (0,ROOMS_H):
            for row in range(0,ROOMS_V):
                room = Room.rooms[col][row]
                Room.unused_rooms.append(room)
                room.room_color = BACKGROUND
                room.state = None;
                room.contents = []  # reset to no contents
                #initialize the state of the walls, True means they are up
                room.n_wall = True
                room.s_wall = True
                room.e_wall = True
                room.w_wall = True
                room.draw()

        return # return from Maze.reset
    #class to hold the rooms
class Room(object):
    
    rooms = []  # holds the doubly indexed list of room objects
    unused_rooms = [] # single indexed list of the unused rooms
    
    def __init__(self,size=20,row=0,col=0):
    #Room initialization method called when room is created.  Column and row
    # give the position in the array
        self.room_color = BACKGROUND  # chose the paint colors
        self.wall_color = BLACK
        self.size = size  # size of the room in pixels
        #print(self.size)
        self.col = col    # column coordinate
        self.row = row   # row coordinate
        self.state = None   # usage state of the room
        self.contents = [] # contents list to empty

        #initialize the state of the walls, True means they are up
        self.n_wall = True
        self.s_wall = True
        self.e_wall = True
        self.w_wall = True

        #define a rectangle for this room and save it
        left = int(float((WINDOWWIDTH-MAZE_WIDTH)/2.)
                   +int(self.col*float(size)))
        top =  int(float((WINDOWHEIGHT-MAZE_HEIGHT)/2)
                   +int(self.row*float(size)))
        self.rect = pygame.Rect(left,top,size,size)

        self.draw()  # draw the room

        return  # return from Room.__init__

    def draw(self):
    # Room method to draw and room and it's walls acording to current wall state

        pygame.draw.rect(windowSurface,self.room_color,self.rect,0) # draw the floor

        #draw the walls based on their state
        if self.n_wall:
            pygame.draw.line(windowSurface,self.wall_color,
                             (self.rect.left,self.rect.top),
                             (self.rect.left+self.size,self.rect.top),1)
        if self.s_wall:
           pygame.draw.line(windowSurface,self.wall_color,
                             (self.rect.left,self.rect.bottom),
                             (self.rect.left+self.size,self.rect.bottom),1)
        if self.w_wall:
           pygame.draw.line(windowSurface,self.wall_color,
                 (self.rect.left,self.rect.top),
                 (self.rect.left,self.rect.top+self.size),1)
        if self.e_wall:
           pygame.draw.line(windowSurface,self.wall_color,
                             (self.rect.right,self.rect.top),
                             (self.rect.right,self.rect.top+self.size),1)
        

        pygame.display.update()

        return  # return from Maze.draw

    def walk(self,direction='N',wall_check=True):
    #Maze method to walk out of a room
    # if walk_check is False, you can walk through walls (used for initial
    # maze setup). Returns false if we can't go that way, also returns updated
    # room object.
    
        moved = False  # establish default
        col = self.col # initial col
        row = self.row
        if ( (direction == 'N') &
             (self.row >0) ):
            if( (not self.n_wall) |  (not wall_check)):
                 row -=1
                 moved = True
        if ( (direction == 'S') &
             (self.row < (ROOMS_V-1) ) ):
            if( (not self.s_wall) |  (not wall_check)):
                 row +=1
                 moved = True
        if ( (direction == 'W') &
             (self.col >0) ):
            if( (not self.w_wall) |  (not wall_check)):
                 col -=1
                 moved = True
        if ( (direction == 'E') &
             (self.col < (ROOMS_H-1) ) ):
            if( (not self.e_wall) |  (not wall_check)):
                 col +=1
                 moved = True
#        print('dir,N,S,E,W= ',direction,self.n_wall,self.s_wall,
#              self.e_wall,self.w_wall)

        return moved,col,row  # returned with indication of success or failure

    def knock_out_walls(direction,room,old_room):
    # General purpose function to clear the walls from which we entered a room.
    # direction is the direction we were going when we entered.
    # room is current room object. old_room is the room we entered from.
 

        if direction == 'N':
            old_room.n_wall = False
            room.s_wall = False
        elif direction == 'S':
            old_room.s_wall = False
            room.n_wall = False
        elif direction == 'E':
            old_room.e_wall = False
            room.w_wall = False
        elif direction == 'W':
            old_room.w_wall = False
            room.e_wall = False
        Room.draw(old_room) # redraw both rooms
        Room.draw(room)

        return # return from knock_out_walls
class Live(object):  # create Rat object

    def __init__(self,direction = 'E',color=DIMGREY ):

        self.direction = direction
        self.color = color
        self.room = Room.rooms[STARTING_COL][STARTING_ROW]
        self.cheeses = []  # empty list of cheeses we carrys

        self.draw()  # draw him in the starting room
        
        return # return from Rat.__init__

    def draw(self):
    # draw the rat in his room

        pygame.draw.circle(windowSurface,self.color,self.room.rect.center,
                           int(self.room.size/3),0)
        pygame.display.update()

        return  # return from Rat.__init__

    def erase(self):
    # erase the rat from this room

        pygame.draw.circle(windowSurface,self.room.room_color,
                           self.room.rect.center,int(self.room.size/3),0)
        pygame.display.update()

        return # return from Rat.erase

    def move(self,direction='E'):
    # move the rat in the indicated direction
        status,col,row = self.room.walk(direction)
        if status: # move was legal
            self.erase()   # erase from the current room
            self.room = Room.rooms[col][row] # get new room he is in
            self.check_for_cheese(self.room)
            self.draw()   # draw rat in new room

        return status   # return whether move occurred or not
        

    def check_for_cheese(self,room):
    # see if there is cheese in room, if so, pick up cheese, change room color
    # to background and return true
        if 'cheese' in room.contents:
            self.cheeses.append('cheese')
            room.contents.remove('cheese')
            room.room_color = BACKGROUND
            self.room.draw() # redraw room with no cheese
            return True
        else:
            return False
                
    def cheese_num(self):
        return len(self.cheeses)
    def reset_cheese(self):
        self.cheeses = []
    def change_color(self,color_n):
        self.color = color_n
#Node class to hold the Nodes for the link-list
##--------------End of classes-------------#
##--------------Begginiing of genral pourpce functions#
def dig_holes(holes):
    #Function to hide holes throught the dungon
    return


dungon = Maze()

dungon.build()


while True:
    foobar = 0
    foobar += 1