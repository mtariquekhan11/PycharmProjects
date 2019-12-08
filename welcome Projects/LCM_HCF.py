# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To calculate the LCM and HCF/GCD


condition = "True"


def hcf(x, y):
    if x < y:
        smaller = x
    elif x > y:
        smaller = y
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


def lcm(x, y):
    if x > y:
        greater = x
    elif x < y:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater = greater + 1

    return lcm


while condition is "True":
    choice = int(input("Enter the your choice \n '1' for HCF '2' for LCM: "))

    if choice == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("HCF of ", num1, num2, "are: ", hcf(num1, num2))
    elif choice == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("LCM of ", num1, num2, "are: ", lcm(num1, num2))
    else:
        print("Invalid Input")
        break

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
