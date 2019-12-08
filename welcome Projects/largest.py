# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To find the largest number


condition = "True"


def check(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(n1, "is largest ")
    elif n2 >= n1 and n2 >= n3:
        print(n2, "is largest ")
    elif n3 >= n1 and n3 >= n2:
        print(n3, "is largest ")


while condition is "True":
    num1 = int(input("Enter the number 1 to check largest: "))
    num2 = int(input("Enter the number 2 to check largest: "))
    num3 = int(input("Enter the number 3 to check largest: "))

    check(num1, num2, num3)

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
