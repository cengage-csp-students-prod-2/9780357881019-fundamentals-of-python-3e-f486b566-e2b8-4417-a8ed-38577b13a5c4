"""
Author: Ashley Francis
Date written: 01/27/2025
Assignment: Module 01 Practice Exercise 2-2
This program defines a function to calculate the surface area of a cube
using the formula 6 * side^2; the side is the length of one edge of the cube.
The program will prompt the user to input the length of one edge of the cube,
it will then calculate the surface area. The program will display the surface area.
"""

try:
    edge_length = int(input("Enter the length of an edge of the cube: "))
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative.")
    
    surface_area = 6 * (edge_length ** 2)
    print(f"The surface area of the cube is: {surface_area}")
except ValueError as e:
    print(f"Invalid input: {e}. Please enter a valid integer.")