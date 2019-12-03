# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To find out the value of quadratic equation

condition = "True"
# to find the solution for quadratic equation ax^2+bx+c=0
while condition is "True":
    import cmath
    import math

    a = float(input("Enter the number a): "))
    b = float(input("Enter the number b): "))
    c = float(input("Enter the number c): "))
    #    a1, b1, c1 = float(input("Enter the number a,b, c): "))
    # to find the solution x= (-b +- (b^2-4ac)^1/2) / 2a, we have to take discriminant

    d = b ** 2 - 4 * a * c

    expr1 = (-b + cmath.sqrt(d)) / (2 * a)
    expr2 = (-b - cmath.sqrt(d)) / (2 * a)

    expr1 = str(expr1)
    expr2 = str(expr2)

    print("value for x= " + expr1)
    print("value for x= " + expr2)
    print('The solution are {0} and {1}'.format(expr1, expr2))

    condition1 = input("Do you want to check more equation, Press y/Y ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
