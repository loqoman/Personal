
import random
import time
from pygame.locals import *



possibilitiesN = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

foo = open('Code.txt')

finding = foo.readline()
code = []
checking = ''
launch = []
while True:
    chars = random.randrange(0,15)
    for i in range(1,chars):
        letter = random.randrange(0,36)
        charecter = possibilitiesN[letter]
        code.append(charecter)
        print(code)
        checking = checking.join(code)
        #checking = 'M\n'
        print (checking)
        if checking == finding:#Ending the program
            print('I found it!, it is ' + checking)
            exit
    #print('')
    code = []







