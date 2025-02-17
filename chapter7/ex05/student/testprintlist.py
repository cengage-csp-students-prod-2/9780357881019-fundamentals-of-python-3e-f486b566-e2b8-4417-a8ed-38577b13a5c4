"""
Author: Ashley Francis
Date written: 02/17/2025
Assignment: Module 05 Practice Exercise 7-5
This program is deisgned to define and test a function and to
trace the argument on each call.
"""

def print_sequence(sequence):
    if sequence:
        print(sequence[0])
        print_sequence(sequence[1:])

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6]
    print("Testing with a list:")
    print_sequence(test_list)

    test_string = "Ashley"
    print("\nTesting with a string:")
    print_sequence(test_string)

    test_tuple = (10, 20, 30)
    print("\nTesting with a tuple:")
    print_sequence(test_tuple)