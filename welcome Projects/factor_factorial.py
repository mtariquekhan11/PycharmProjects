# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To find the factors and factorials


condition = "True"


def factor(n):
    print("The factors of ", n, "are: ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            i = i + 1


def factorial(n):
    factorial = 1
    if n == 0:
        print("Factorial for", n, "is 1")
    elif n < 0:
        print("Factorial for", n, "does not exist")
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        print("Factorial for", n, "is", factorial)


while condition is "True":
    choice = int(input("Enter the your choice \n '1' for Factor, '2' for Factorial: "))

    if choice == 1:
        num = int(input("Enter the number: "))
        factor(num)
    elif choice == 2:
        num = int(input("Enter the number: "))
        factorial(num)
    else:
        print("Invalid Input")
        break

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
