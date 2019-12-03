# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: want to continue syntax for programs


def want_to_continue():
    condition = "True"

    while condition is "True":
        # num = int(input("Enter the number to check whether its positive/ negative / Zero"))

        # check(num)

        condition1 = input("Do you want to check more, Press Y or y: ")
        if condition1 == "y" or condition1 == "Y":
            condition = "True"
        else:
            break
