# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To find the Leap year in the given range

condition = "True"


def leap(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                print(yr, "is a leap year.")
            else:
                print(yr, "is not a leap year.")
        else:
            print(yr, "is a leap year.")
    else:
        print(yr, "is not a leap year.")


def leap_range(yr_s, yr_e):
    for i in range(yr_s, yr_e + 1):
        if yr_s % 4 == 0:
            if yr_s % 100 == 0:
                if yr_s % 400 == 0:
                    print(yr_s, "is a leap year.")
                else:
                    print(yr_s, "is not a leap year.")
            else:
                print(yr_s, "is a leap year.")
        else:
            print(yr_s, "is not a leap year.")
        yr_s = yr_s + 1


while condition is "True":
    choice = int(input("Enter the choice to check: \n 1- for single year, 2- for range: "))

    if choice == 1:
        year = int(input("Enter the year to check for leap year: "))
        leap(year)
    elif choice == 2:
        year_s = int(input("Enter the starting year to check for leap year: "))
        year_e = int(input("Enter the ending year to check for leap year: "))
        leap_range(year_s, year_e)

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
