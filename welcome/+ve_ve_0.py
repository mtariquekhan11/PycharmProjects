# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To check the number is positive or negative


condition = "True"


def check(n):
    if n == 0:
        print(n, "is ZERO")

    elif n < 0:
        print(n, "is NEGATIVE")
    else:
        print(n, "is POSITIVE")


while condition is "True":
    num = int(input("Enter the number to check whether its positive/ negative / Zero"))

    check(num)

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
