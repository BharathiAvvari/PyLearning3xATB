# Program - Calculate the area of circle.
# input -> radius
# output -> area
import math

# data types
# input -> int or float -> float
# output -> float

# Core Logic -> pi*r*r = 3.14

radius = float(input("Enter the radius\n"))
print("pi value is", math.pi)
area = math.pi*(radius**2)
area2 = math.pi*(math.pow(radius,2))
print("area of circle is", area)
print("area of circle is", area2)
