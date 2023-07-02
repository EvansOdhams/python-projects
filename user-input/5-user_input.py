#!/usr/bin/python3


def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print("Result:", result)
elif choice == 2:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = subtract_numbers(num1, num2)
    print("Result:", result)
elif choice == 3:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = multiply_numbers(num1, num2)
    print("Result:", result)
else:
    print("Invalid choice. Please select a valid option.")
