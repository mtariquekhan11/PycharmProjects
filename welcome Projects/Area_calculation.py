# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To find the area of Triangle/square/rectangle/rhombus/parallelogram/circle

condition = "True"

while condition is "True":
    import math

    area = input("Enter the shape you want to calculate area (Triangle/square/rectangle/rhombus/trapezium/circle): ")

    if area == "Triangle" or area == "triangle":
        b = float(input("Enter the base: "))
        h = float(input("Enter the height: "))
        area_tri = 1 / 2 * b * h
        area_tri = str(area_tri)
        print("Area of triangle is " + area_tri)

    elif area == "Square" or area == "square":
        s = float(input("Enter the side: "))
        area_sqr = (s * s)
        area_sqr = str(area_sqr)
        print("Area of square is " + area_sqr)

    elif area == "Rectangle" or area == "rectangle":
        s1 = float(input("Enter the side 1: "))
        s2 = float(input("Enter the side 2: "))
        area_rect = (s1 * s2)
        area_rect = str(area_rect)
        print("Area of rectangle is " + area_rect)

    elif area == "Rhombus" or area == "rhombus":
        b = float(input("Enter the base: "))
        h = float(input("Enter the perpendicular height: "))
        area_rhom = (b * h)
        area_rhom = str(area_rhom)
        print("Area of rhombus is " + area_rhom)

    elif area == "Trapezium" or area == "trapezium":
        p1 = float(input("Enter the parallel side 1: "))
        p2 = float(input("Enter the parallel side 2: "))
        h = float(input("Enter the perpendicular height: "))
        area_trap = (1 / 2 * h * (p1 + p2))
        area_trap = str(area_trap)
        print("Area of trapezium is " + area_trap)

    elif area == "Circle" or area == "circle":
        r = float(input("Enter the radius: "))
        area_cir = (math.pi * r * r)
        area_cir = str(area_cir)
        print("Area of square is " + area_cir)
    condition1 = input("Do you want to check more numbers, Press y/Y ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
