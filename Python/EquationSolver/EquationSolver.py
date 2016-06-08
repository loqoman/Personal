import math, decimal
from decimal import *
#Old varibles
target = 'x'
operations = ['+','-','*','/']

print('Hello and welcome to the eqation calcuator!')
print('Made by Darwin Clark')
print('/programming/Personal/Python/EquationSolver.py/')
println('In case you have forgotten, the solutions to a quadric equation are all the x-intercepts')
A = input('What is A?')
B = input('What is B?')
C = input('What is C?')
#Just initing the varibles so that I/we do not get confuzed
tempSquare = 0 
preFork = 0 

#Splitting up the equtation into multiple items, maby a list
#I dont know.
#----#
'''
Important
Froumla for a quadric equation is:

X = ([b*-1]*Math.sqrt[(Math.pow[b,2]) - 4*A*C)/A*2

For words...

X equeals (negitive B plus/equals the squre root of (B Squared minus 4AC)) all divided by 2a

'''
#----#
#equation.split()
print('Calcuating value of X...')
#X = B*-1*math.sqrt(math.pow(B,2) - 4*A*C/A*2)
#That was the old equation, I dont know how Python handles order of opearations, 
#So im just going to do it basically by step
preFork  = int(A)*-1
tempSquare =  Math.sqrt(Math.pow(int(b),2) - 4*int(A)*int(C))


print(X)

#print(equation)

#for i in operations:

#print[equation.index('+')]

#want to take note here that it breaks down the equation by character


