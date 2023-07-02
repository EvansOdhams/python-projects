#!/usr/bin/python3


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except (ZeroDivisionError, ValueError):
    print("Error: Invalid input or division by zero.")

