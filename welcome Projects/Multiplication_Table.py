# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To prepare the multiplication table

from math import *

condition = "True"
while condition is "True":
    num = int(input("Enter the number for multiplication table: "))
    max = int(input("Enter the last number up to which table is required: "))

    for i in range(1, max + 1, 1):
        table = num * i

        table = str(table)
        num = str(num)
        i = str(i)
        print(num + " * " + i + " = ", table)
        i = int(i)
        table = int(table)

        num = int(num)

        i = i + 1

    print()
    condition1 = input("Do you want to check more numbers, Press y/Y ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
