#!/usr/bin/python3


# Simple Python program to understand elif statement  
marks = int(input("Enter the marks? "))    
# Here, we are taking an integer marks and taking input dynamically  
if marks > 85 and marks <= 100:  
# Here, we are checking the condition. If the condition is true, we will enter the block    
   print("Congrats ! you scored grade A ...")    
elif marks > 60 and marks <= 85:    
# Here, we are checking the condition. If the condition is true, we will enter the block  
   print("You scored grade B + ...")    
elif marks > 40 and marks <= 60:  
# Here, we are checking the condition. If the condition is true, we will enter the block    
   print("You scored grade B ...")    
elif (marks > 30 and marks <= 40):    
# Here, we are checking the condition. If the condition is true, we will enter the block  
   print("You scored grade C ...")    
else:    
   print("Sorry you are fail ?") 
