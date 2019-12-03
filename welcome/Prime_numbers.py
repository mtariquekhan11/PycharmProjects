# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To check the prime numbers
condition = "True"
while condition is "True":
    x = int(input("Enter the upper range for which Prime Numbers are required: "))
    y = int(input("Enter the lower range for which Prime Numbers are required: "))
    for num in range(y, x + 1):
        if num <= 1:
            num = str(num)
            print(num + " is not a prime number")
            pass
        else:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    #
    print()
    condition1 = input("Do you want to check more numbers, Press y/Y ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
