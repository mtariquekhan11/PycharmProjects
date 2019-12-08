# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To calculate the numbers


import math

condition = "True"
while condition is "True":

    def su(a, b):
        return a + b


    def subt(a, b):
        return a - b


    def mult(a, b):
        return a * b


    def div(a, b):
        return a / b


    def perc(a, b):
        return (a / 100) * b


    print("\nSelect the respective digit for operation: ")
    print("1 for Addition:")
    print("2 for Subtraction:")
    print("3 for Multiplication:")
    print("4 for Division:")
    print("5 for Percentage:")

    choice = int(input("Enter your choice 1/2/3/4/5: "))
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if choice == 1:
        # print (a "+" b "=", su(a,b))
        print("a+b=", su(a, b))

    elif choice == 2:
        # print (a "-" b "=", subt(a,b))
        print("a-b=", subt(a, b))

    elif choice == 3:
        # print (a "*" b "=", mult(a,b))
        print("a*b=", mult(a, b))

    elif choice == 4:
        # print (a "/" b "=", div(a,b))
        print("a/b=", div(a, b))

    elif choice == 5:
        # print (a "%" b "=", perc(a,b))
        print("a%b=", perc(a, b))

    elif choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5:
        print("Invalid Input")

    condition1 = input("\nDo you want to check more numbers, Press y/Y ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        print()
        print()
        condition = "False"
