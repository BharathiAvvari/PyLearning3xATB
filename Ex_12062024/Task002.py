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

# 3.program to find factorial of given number
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial of given number 5 is", factorial)

# 4.program to find fibonacci series of given number
n = 7
a, b = 0, 1
fib_sequence = [a, b]
while len(fib_sequence) <= n:
    next_num = a + b
    fib_sequence.append(next_num)
    a, b = b, next_num
    print("Fibonacci of given number is", fib_sequence)
