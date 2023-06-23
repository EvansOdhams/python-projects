#!/usr/bin/python3


Employee = {"Name": "Dev", "Age": 20, "salary":45000,"Company":"WIPRO"}         
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)        
print("Enter the details of the new employee....");        
Employee["Name"] = input("Name: ");        
Employee["Age"] = int(input("Age: "));        
Employee["salary"] = int(input("Salary: "));        
Employee["Company"] = input("Company:");        
print("printing the new data");        
print(Employee)     
