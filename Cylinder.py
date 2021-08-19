

radius = float(input("Enter the radius of the Cylinder: "))

height = float(input("Enter the height of the cylinder: "))

volume = 3.142 * radius ** 2 * height

total_surface_area = 2 * 3.142 * radius * height + 2 * 3.142 * radius ** 2


print("The volume of the Cylinder is",volume)
print("The total surface area of the cylinder is",total_surface_area)

close = input("Press X to exit")
# The above line of code keeps the program open for the user to see the outcome of the problem.