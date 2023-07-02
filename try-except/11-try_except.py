#!/usr/bin/python3


def calculate_percentage(score, total):
    if total <= 0:
        raise ValueError("Invalid total score.")
    percentage = (score / total) * 100
    return percentage

try:
    percentage = calculate_percentage(75, 0)
    print("Percentage:", percentage)
except ValueError as error:
    print("Error:", str(error))
