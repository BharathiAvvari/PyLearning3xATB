# 1. Create a program that determines whether a given year is a leap year.
year = int(input("Enter a year\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")

# 2. Write a program that classifies a triangle based on its side lengths.
side1 = int(input("Enter the length of side 1\n"))
side2 = int(input("Enter the length of side 2\n"))
side3 = int(input("Enter the length of side 3\n"))
if side1 == side2 and side2 == side3:
    print("The triangle is equilateral")
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("The triangle is scalene")
else:
    print("The triangle is isosceles")

