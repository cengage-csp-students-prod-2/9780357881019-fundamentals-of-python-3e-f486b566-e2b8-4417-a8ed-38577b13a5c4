def cube_surface_area(side_length):
  """Calculates the surface area of a cube.

  Args:
    side_length: The length of a side of the cube.

  Returns:
    The surface area of the cube.
  """

  return 6 * side_length ** 2

# Get the side length from the user
side_length = float(input("Enter the side length of the cube: "))

# Calculate and print the surface area
surface_area = cube_surface_area(side_length)
print("The surface area of the cube is:", surface_area)# Write your program here
