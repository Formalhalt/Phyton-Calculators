
import math
radius = float(input("Enter the radius of the cone: "))

height = float(input("Enter the height of the cone: "))

volume = 3.142 * radius ** 2 * height/3

total_surface_area = 3.142 * radius * (radius + math.sqrt(height ** 2 + radius ** 2))

print("The total surface area of the cone is", total_surface_area)

print("The volume of the cone is", volume)

close = input("Press X to exit")
# The above line of code keeps the program open for the user to be able to see the outcome of the problem