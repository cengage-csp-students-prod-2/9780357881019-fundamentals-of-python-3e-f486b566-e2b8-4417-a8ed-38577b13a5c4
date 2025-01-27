"""
Author: Ashley Francis
Date written: 01/27/2025
Assignment: Module 02 Practice Exercise 3-9
This program continually asks for the user to input until the user
presses Enter without typing anything. Once the user presses Enter
program will display the sum of the numbers and their average.
"""
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "":# Write your program here
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

if numbers:
        total = sum(numbers)
        average = total / len(numbers)
        print(f"Sum: {total}")
        print(f"Average: {average}")
else:
        print("No numbers were entered.")