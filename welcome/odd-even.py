# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To check the numbers as odd or even numbers

condition = "True"
while condition is "True":
    odd_even = input("You want to check Even or Odd Numbers: ")
    x = int(input("Enter the number up to which odd/even is required: "))
    y = 1
    if x < y:
        x = str(x)
        print(x + " is a natural number")
        pass
    elif odd_even == "Even" or odd_even == "even":
        print('Even Numbers: ', end=" ")
        for i in range(y, x + 1):
            if odd_even == "Even" or "even" and i % 2 == 0:
                print(i, end=" ")
    elif odd_even == "Odd" or odd_even == "odd":
        print('Odd Numbers: ', end=" ")
        for i in range(y, x + 1):
            if odd_even == "Odd" or "odd" and i % 2 != 0:
                print(i, end=" ")

    print()
    condition1 = input("Do you want to check more numbers, Press y/Y ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
