
import pygame, sys, time , random , math, serial
from pygame.locals import *
x = 5
int(x)
ser = serial.Serial(timeout = 1, port = 'COM4',baudrate=115200)
# set up pygame
pygame.init()
# Global window definitions


WINDOWWIDTH = 750

WINDOWHEIGHT = 500 # Total Height of the Window
#cant use digital 1 and 2 because they are being used for serial ports
RECT_SIZE = 5

MAX_POT = 1023
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

moving_rect = pygame.Rect(0,0,0,0)
# Set up the  window global object
windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Etch and Schectch')

# this set the background to so it won't be black
# you can choose the color of your preference
"""
background_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
pygame.draw.rect(windowSurface,BACKGROUND,background_rect,0)
"""






pygame.key.set_repeat(200,100)

#------------------Defineing the functions--------------------------#
def square_x():

    ser.write(b'0')
    X = ser.readline()
    X = X.decode("utf-8")
    str(X)
    checkX = X[:1]
    X = X[1:]
    if (checkX == '0'):
        value = int(X)
        return value
    print('X = -1')
    return -1

def square_y():

    ser.write(b'1')
    Y = ser.readline()
    Y = Y.decode("utf-8")
    str(Y)
    checkY = Y[:1]
    Y = Y[1:]
    
    if (checkY == '1'): 
        value2 = int(Y)
        return value2
    print('Y = -1')
    return -1

def if_paint():

    ser.write(b'2')
    P = ser.readline()
    P = P.decode("utf-8")
    str(P)
    checkP = P[:1]
    P = P[1:]
    if (checkP == '2'):
        paint = int(P)
        #print('top paint is ' + paint);
        return paint
    print('paint = -1')
    return -1

def if_erase():

    ser.write(b'3')
    E = ser.readline()
    E = E.decode("utf-8")
    str(E)
    checkE = E[:1]
    E = E[1:]
    if  (checkE == '1'):
        erase = int(E)        
        return erase 
    #print('erase = -1')
    return -1
                
    
    


#---------------------Set-up stuff------------------------#



char = ser.read()
#char = char.decode("utf-8") # decode from byte to string


#print(ser.isOpen())
while True: 
    inByte = ser.read()
    if inByte == b'I':
        ser.write(b'I')
        break
X_pot = 0
Y_pot = 0
paint = 0


#------------------------Main Program loop--------------------#
while True:


    
    

    #---square related stuff-----#
    erase = if_erase()
    print(erase)
    temp_paint = if_paint()
    #print(temp_paint)
    #if (temp_paint  > 0): 
     #   paint = temp_paint
    #print(temp_paint)
    temp_X_pot = square_x()#Start of somthing wierd happening...
    if (temp_X_pot > 0):
        X_pot = temp_X_pot
    X_pot = (X_pot / (MAX_POT / WINDOWWIDTH))# If doing C++ make float
    #print(temp_paint)
    if X_pot > (WINDOWWIDTH - RECT_SIZE):
        X_pot = (WINDOWWIDTH - RECT_SIZE)
    #print('x pot is ' + str(X_pot))
    temp_Y_pot = square_y()
    if (temp_Y_pot > 0):
        Y_pot = temp_Y_pot
    Y_pot = (Y_pot / (MAX_POT / WINDOWHEIGHT))# 2 o'clock in morning synrdrom
    if Y_pot > (WINDOWHEIGHT - RECT_SIZE):
        Y_pot = (WINDOWHEIGHT - RECT_SIZE)#End of somthing wierd happening...
    #print('y pot is ' + str(Y_pot))
    int(paint)
    if temp_paint == 0:
        pygame.draw.rect(windowSurface,BLACK,moving_rect)
        moving_rect = pygame.Rect(X_pot,Y_pot,RECT_SIZE,RECT_SIZE)
        pygame.draw.rect(windowSurface,RED,moving_rect)
    elif temp_paint == 1:
        pygame.draw.rect(windowSurface,YELLOW,moving_rect)
        moving_rect = pygame.Rect(X_pot,Y_pot,RECT_SIZE,RECT_SIZE)
        pygame.draw.rect(windowSurface,RED,moving_rect)
    if erase == 1:
        background_rect = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT )
        pygame.draw.rect(windowSurface,BACKGROUND,background_rect)
    #---end of square related stuff---
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    time.sleep(.01)

#---------------------------End of main program loop-----------#


