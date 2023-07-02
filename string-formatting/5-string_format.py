#!/usr/bin/python3


name = "Alice"
age = 30
height = 1.65

# Concatenation using the + operator
concatenated = "Name: " + name + ", Age: " + str(age) + ", Height: " + str(height)
print("Concatenated:", concatenated)

# Using the % operator for string interpolation
interpolated = "Name: %s, Age: %d, Height: %.2f" % (name, age, height)
print("Interpolated:", interpolated)

# Using str.format() method for string formatting
formatted = "Name: {}, Age: {}, Height: {:.2f}".format(name, age, height)
print("Formatted:", formatted)

# Utilizing f-strings (formatted string literals)
f_string = f"Name: {name}, Age: {age}, Height: {height:.2f}"
print("F-string:", f_string)
