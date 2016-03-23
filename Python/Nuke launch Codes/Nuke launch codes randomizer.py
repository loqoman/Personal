#-------V. 1.0----------#
'''
This Nuke code finder reads from a file named 'Code.txt'
and finds that code by making a ton of random strings
'''
# Please leave me a comment on Github(https://github.com/loqoman/Personal-Python)
# If you want to see anything new done
'''
As a side note this program is pretty useless,
I just found it a good exersise in learning text manipulation,
which I havent really had a strong knowlage of. 
'''
#-----------------------#
import random, sys
import time
from pygame.locals import *



possibilitiesN = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#All of the letters that we might use, only caps because in all the movies the codes are caps.

foo = open('Code.txt')#Opening the file

finding = foo.readline() # Reading the code that we need 
code = []#Initing some varibles that we might need
checking = ''
launch = []
while True:
    chars = random.randrange(0,15)#Getting how many Chars in the string, 15 just seemed like a good ending to me.
    checking = ''#We need to reset this at the begginning of each cycle, otherwise we get a very long string
    for i in range(1,chars):#This is just ment to repeat for every character that it randomises
        letter = random.randrange(0,36)#Getting a random letter
        charecter = possibilitiesN[letter]#Fiinding that letter in the list
        code.append(charecter)#Adding the letter to a list
    
    checking = checking.join(str(e) for e in code)#Turning the list into a string
    print(checking)#Printing the code,IT LOOKS COOL!
    if checking == finding:#Ending the program
        print('\n@#%BEEP BOOP CODE FOUND#!@\n %&@#PRINTING CODE%#@\n         ' + checking)#yay! We found it!
        sys.exit()#You dont really need to exit the program, however for demonstration it makes it easy to see if it has found the right letter.
    code = []#need to reset this or we end up with a long string









