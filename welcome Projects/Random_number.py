# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To generate a random number


from random import *

condition = "True"

while condition is "True":
    choice = int(input("To get the random number,\n for less than 3 digit Press 1, for 4 - 5 digit Press 2: "))

    if choice == 1:
        print(randint(0, 1000))
    elif choice == 2:
        print(randint(1000, 10000))
    else:
        print("Invalid number")
        break

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
