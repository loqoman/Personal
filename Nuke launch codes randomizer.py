
import random
import time
from pygame.locals import *



possibilitiesN = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
finding = 'YH53GXMHQQTZ'

foo = open(code2Find)

 
launch = []
while True:
    chars = random.randrange(0,15)
    for i in range(0,chars):
        code = []
        letter = random.randrange(0,36)
        charecter = possibilitiesN[letter]
        code.append(charecter)

        for i in code:
            launch.append(i)
            print(i, end = "")
            checking = ''.join(str(e) for e in launch)
            if checking == finding:#Ending the program
                print('I found it!, it is' + checking)
                exit
    print('') 








