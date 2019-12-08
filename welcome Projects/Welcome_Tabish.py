# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To Welcome


""" Hey Dear this is just to check
 the multi line comment command """
again = "Yes"
while again is "Yes":
    # This is to get the name as Input to use further
    name = input("What is your name?: ")
    gender = input("Are you Male or Female? ")
    # Program 1 Just to welcome Tabish by Print command for this new Project
    if gender == "Female" or gender == "female":
        a = ('You are Welcome Ms.' + name)
        print(" Hello! Ms." + name)
        print(a)
    else:
        a = ('You are Welcome Mr.' + name)
        print(" Hello! Mr." + name)
        print(a)
    # This is to check data types: String, Integer(i-signed/I-unsigned), Float, Long and Boolean(True/False)
    # No need to specify data types, it get automatically detected.
    a = len(name)
    b = 3.5
    c = 'x'
    d = name
    e = (a == c)
    f = 3.0
    g = (a == f)

    print('number of characters in your name=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
    print('e=', e)
    print('g=', g)

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(g))

    again1 = input("If you want to check again!, Press y/Y ")
    if again1 == "y" or again1 == "Y":
        again = "Yes"
    else:
        break
