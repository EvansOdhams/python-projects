#!/usr/bin/python3


Employee = {"Name": "David", "Age": 30, "salary":55000,"Company":"WIPRO"}         
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)        
print("Deleting some of the employee data")         
del Employee["Name"]        
del Employee["Company"]        
print("printing the modified information ")        
print(Employee)        
print("Deleting the dictionary: Employee");        
del Employee        
print("Lets try to print it again ");        
print(Employee)       
