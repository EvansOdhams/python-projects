#!/usr/bin/python3


with open("image.jpg", "rb") as file:
    binary_data = file.read()

with open("copy.jpg", "wb") as file:
    file.write(binary_data)
