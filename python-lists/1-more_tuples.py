#!/usr/bin/python3


# Python program to create a tuple without using parentheses    
# Creating a tuple    
tuple_ = 4, 5.7, "Tuples", ["Python", "Tuples"]    
# Displaying the tuple created    
print(tuple_)    
# Checking the data type of object tuple_    
print(type(tuple_) )    
# Trying to modify tuple_    
try:    
    tuple_[1] = 4.2    
except:    
    print(TypeError )    
