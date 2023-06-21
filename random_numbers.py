#!/usr/bin/python3
import random

#Generates a random floating point number between 0 and 1
random_number = random.random()
print(random_number)

#Generates a random integer between a given range
random_integer = random.randint(0, 10)
print(random_integer)

#Generates a random number in a specific range with a step value
random_range = random.randrange(0, 20, 2)
print(random_range)
