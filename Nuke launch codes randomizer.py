
import random
from pygame.locals import *

chars = 9#random.randrange(0,9)


possibilitiesN = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    for i in range(0,chars):
        code = []
        letter = random.randrange(0,50)
        charecter = possibilitiesN[letter]
        code.append(charecter)

        for i in code:
            print(i,end = "")

    print('')






