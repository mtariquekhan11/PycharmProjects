# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To check the Armstrong number

"""Armstrong number is a number, whose sum of each digit(raised to the length of power) is equal to the number.
For eg: 153 = 1**3 + 5**3 + 3**3  OR 1634 = 1**4 + 6**4 + 3**4 + 4**4. """
condition = "True"


def armstrong(n):  # function to check Armstrong number
    tot = 0  # variable declared to collect total
    power = len(str(n))  # variable declared to check the length of number and set power

    while n > 0:  # loop to run up to the number
        digit = n % 10  # variable to collect the remainder of number divided by 10
        tot = tot + digit ** power  # Remainder raised to the power of number is added in total
        n = n // 10  # number is divided by 10 and floor value is collected for next loop

    if num == tot:
        print(num, "is armstrong number")
    else:
        print(num, "is not armstrong number")


def armstrong_range(x, y):  # function to check Armstrong number
    # print("x= ", x, "\ny= ", y)

    for i in range(x, y + 1):
        # print("x= ", x, "y= ", y, "i= ", i)
        power = len(str(i))  # variable declared to check the length of number and set power
        tot = 0  # variable declared to collect total
        n = i
        # print("x= ", x, "y= ", y, "\ni= ", i, "power= ", power, "\ntot= ", tot, "n= ", n)
        while n > 0:  # loop to run up to the number
            digit = n % 10  # variable to collect the remainder of number divided by 10
            tot = tot + digit ** power  # Remainder raised to the power of number is added in total
            n = n // 10  # number is divided by 10 and floor value is collected for next loop
            # print("x= ", x, "y= ", y, "\ni= ", i, "power= ", power, "\ntot= ", tot, "n= ", n, "i= ", i)
        if i == tot:
            print(i, "is armstrong number")
        # else:
        #     print(i, "is not armstrong number")
        i = i + 1


while condition is "True":
    print("\nSelect the respective digit for operation: ")
    print("1 To check single number:")
    print("2 To check numbers in a range:")

    choice = int(input("Enter your choice 1/2: "))

    if choice == 1:

        num = int(input("Enter the number to check whether its Armstrong number or not: "))
        armstrong(num)

    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        armstrong_range(a, b)
    else:
        print("Invalid Input")
        break

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
