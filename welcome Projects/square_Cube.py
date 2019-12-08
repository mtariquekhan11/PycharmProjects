# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To find the square, square root, cube and cube root of the given number

condition = "True"
while condition is "True":
    import math

    x = float(input("Enter the number : ", ))
    cube = math.pow(x, 3)
    square = (x * x)
    sqroot = math.sqrt(x)
    cbroot = math.pow(x, 1 / 3)
    y = str(x)
    z = str(square)
    cube1 = str(cube)
    sqroot = str(sqroot)
    cbroot = str(cbroot)
    print("Cube of " + y + " is " + cube1)
    print("Square of " + y + " is " + z)
    print("Square root of " + y + " is " + sqroot)
    print("Cube root of " + y + " is " + cbroot)
    condition1 = input("Do you want to check more numbers, Press y/Y ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
