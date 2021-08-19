

length = float(input("Enter the length of the cuboid: "))

height = float(input("Enter the height of the cuboid: "))

breadth = float(input("Enter the breadth of the cuboid: "))


total_surface_area = 2 * (length * breadth + breadth * height + length * height)

volume = length * breadth * height

print("The volume of the cuboid is", volume)
print("The surface area of the cuboid is", total_surface_area)

close = input("Press X to exit")
# The above line of code keeps the program open for the user to see the outcome of the problem.