#!/usr/bin/python3


try:
    file = open("data.txt", "r")
    # Perform some file operations
except FileNotFoundError:
    print("Error: File not found.")
finally:
    file.close()

