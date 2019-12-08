# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To find the Fibonacci series


"""Fibonacci number is a series of number, which start from the given point and sum of first two numbers is
the next number up to the required number.
For eg: sum of 7 numbers from zero  = 0 + 1 + (0+1) + (1+1) + (2+1) + (3+2) + (3+5) """
condition = "True"


def fibonacci(n1, n2):  # function to check Fibonacci number
    terms = 0
    while terms < num:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        terms = terms + 1


while condition is "True":
    num = int(input("Enter the positive number up to which terms fibonacci number is required: "))

    if num <= 0:
        print("Enter the positive number")
    else:
        print("Fibonacci sequence for the ", num, "terms: ")
        fibonacci(0, 1)

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
