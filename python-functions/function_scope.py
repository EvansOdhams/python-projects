#!/usr/bin/python3


# Python code to demonstrate scope and lifetime of variables  
#defining a function to print a number.    
def number( ):    
    num = 50    
    print( "Value of num inside the function: ", num)    
    
num = 10    
number()    
print( "Value of num outside the function:", num)    
