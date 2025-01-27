"""
Author: Ashley Francis
Date written: 01/27/2025
Assignment: Module 01 Practice Exercise 2-2
This program defines a function to calculate the surface area of a cube
using the formula 6 * side^2; the side is the length of one edge of the cube.
The program will prompt the user to input the length of one edge of the cube,
it will then calculate the surface area. The program will display the surface area.
"""
def cube_surface_area(side_length):
    return 6 * side_length ** 2
    
side_length = float(input("Enter the side length of the cube: "))
surface_area = cube_surface_area(side_length)# Write your program here
print("The surface area of the cube is:", surface_area)