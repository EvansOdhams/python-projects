#!/usr/bin/python3


# Python program to show how to use else statement with for loop  
  
# Creating a sequence  
tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)  
  
# Initiating the loop  
for value in tuple_:  
    if value % 2 != 0:  
        print(value)  
# giving an else statement  
else:  
    print("These are the odd numbers present in the tuple")  
