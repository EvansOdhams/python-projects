#!/usr/bin/python3


while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

result = num ** 2
print("Square of", num, "is", result)
