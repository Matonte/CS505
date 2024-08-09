# Michael Matonte
# 8.9.24
# Module 6- Example Program

#Declare needed libraries For business logic and Formulas to define functions

#Import numpy for trig functions
import numpy as np
#Import root solver from scipy.optimize
from scipy.optimize import root

#Define the functions that will declare the list 
#of functions from which the root will be found		 
def your_funcs(X):
   
    #declare variables 
    x, y, a, b = X

    #declare list of one or more functions
    f = [np.cos(x) / x - 0.21 * a - 0.41,
         np.cos(y) / y - 0.43 * b - 0.48,
         a + b - 1,
         0.93 * np.sinc(x) - 0.72 * np.sinc(y)]
    
    #return function list
    return f
    
#Declare a solution variable that will call the solver on the list of functions, with a list of constants
# Declare solution variable
# create a list of constants
#call root solver with function list and list of constants
sol2 = root(your_funcs, [0.13, 0.11, 0.29, 0.11])

#print solution
print(sol2.x)
