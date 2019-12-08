# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To swap the given variable

a = input("Enter the variable 1: ")
b = input("Enter the variable 2: ")
print("a= ", a, "\nb= ", b)
a, b = b, a
print("After Swapping variables, variables are: a= {0}, b= {1}", a, b)
