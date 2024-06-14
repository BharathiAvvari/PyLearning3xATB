# 1.Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
num = 2
square = num ** 2
cube = num ** 3
print("Square of a given number:", square)
print("Cube of a given number:", cube)

# another way of finding square and cube
import math

num = 2
print("Square of a given number:", math.pow(2, 2))
print("Cube of a given number:", math.pow(2, 3))

# another way of finding square and cube
num = int(input("Enter the number to find its square and cube:\n"))
print("Square of a given number", num ** 2)
print("Cube of a given number:", num ** 3)

# 2. Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
if num1 > num2:
    print("First number is greater than second number")
elif num1 < num2:
    print("First number is lesser than second number")
else:
    print("First number is equal to second number")
