# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: To convert different units

condition = "True"

while condition is "True":
    print("************UNIT CONVERTER************")
    print("--------------------------------------")

    choice = int(input("Enter the your choice \n '1' for Temperature \n'2' for Length \n '3' for Mass "
                       "\n '4' for Volume \n '5' for Area \n '6' for Time "
                       "\n '7' for Digital Storage \n '8' for Speed : "))

    if choice == 1:
        choice1 = int(input("Enter the your choice for Temperature \n '1' Celsius to Fahrenheit "
                            "\n'2' Celsius to Kelvin \n '3' Fahrenheit to Celsius "
                            "\n '4' Fahrenheit to Kelvin \n '5' Kelvin to Celsius \n '6' Kelvin to Fahrenheit: "))

        num1 = int(input("Enter the number: "))
        if choice1 == 1:
            print(num1, " Celsius = ", (num1 * (9 / 5) + 32), " Fahrenheit")
        elif choice1 == 2:
            print(num1, " Celsius = ", (num1 + 273.15), " Kelvin")
        elif choice1 == 3:
            print(num1, " Fahrenheit = ", (num1 - 32) * (5 / 9), " Celsius")
        elif choice1 == 4:
            print(num1, " Fahrenheit = ", ((num1 - 32) * (5 / 9) + 273.15)), " Kelvin"
        elif choice1 == 5:
            print(num1, " Kelvin = ", (num1 - 273.15), " Celsius")
        elif choice1 == 6:
            print(num1, " Kelvin = ", (num1 - 273.15) * (9 / 5) + 32), " Fahrenheit"
        else:
            print("Invalid Input")
            break

    elif choice == 2:
        choice2 = int(input("Enter the your choice for Length: "
                            "\n'1' Kilometer to Meter \n'2' Kilometer to Centimeter \n'3' Kilometer to Millimeter"
                            "\n'4' Kilometer to Mile \n'5' Kilometer to Yard \n'6' Kilometer to Foot"
                            "\n'7' Kilometer to Inch \n'8' Kilometer to Nautical Mile \n'9' Meter to Kilometer "
                            "\n'10' Meter to Centimeter \n'11' Meter to Millimeter \n'12' Meter to Mile "
                            "\n'13' Meter to Yard \n'14' Meter to Foot \n'15' Meter to Inch "
                            "\n'16 Meter to nautical Mile \n'17' Centimeter to Kilometer "
                            "\n'18' Centimeter to Meter \n'19' Centimeter to Millimeter \n'20' Centimeter to Mile "
                            "\n'21' Centimeter to Yard \n'22' Centimeter to Foot \n'23' Centimeter to Inch "
                            "\n'24' Centimeter to nautical Mile \n'25' Millimeter to Kilometer "
                            "\n'26' Millimeter to Meter \n'27' Millimeter to Centimeter \n'28' Millimeter to Mile "
                            "\n'29' Millimeter to Yard \n'30' Millimeter to Foot \n'31' Millimeter to Inch "
                            "\n'32' Millimeter to nautical Mile \n'33' Mile to Kilometer "
                            "\n'34' Mile to Meter \n'35' Mile to Centimeter \n'36' Mile to Millimeter "
                            "\n'37' Mile to Yard \n'38' Mile to Foot \n'39' Mile to Inch "
                            "\n'40' Mile to nautical Mile \n'41' Yard to Kilometer "
                            "\n'42' Yard to Meter \n'43' Yard to Centimeter \n'44' Yard to Millimeter "
                            "\n'45' Yard to Mile \n'46' Yard to Foot \n'47' Yard to Inch "
                            "\n'48' Yard to nautical Mile \n'49' Foot to Kilometer "
                            "\n'50' Foot to Meter \n'51' Foot to Centimeter \n'52' Foot to Millimeter "
                            "\n'53' Foot to Mile \n'54' Foot to Yard \n'55' Foot to Inch "
                            "\n'56' Foot to nautical Mile \n'57' Inch to Kilometer "
                            "\n'58' Inch to Meter \n'59' Inch to Centimeter \n'60' Inch to Millimeter "
                            "\n'61' Inch to Mile \n'62' Inch to Yard \n'63' Inch to Foot "
                            "\n'64' Inch to nautical Mile \n'65' Nautical Mile to Kilometer "
                            "\n'66' Nautical Mile to Meter \n'67' Nautical Mile to Centimeter "
                            "\n'68' Nautical Mile to Millimeter \n'69' Nautical Mile to Mile "
                            "\n'70' Nautical Mile to Yard \n'71' Nautical Mile to Foot "
                            "\n'72' Nautical Mile to Inch : "))

        num1 = int(input("Enter the number: "))
        if choice2 == 1:
            print(num1, " Kilometer = ", num1 * 1000, " Meter")
        elif choice2 == 2:
            print(num1, " Kilometer = ", num1 * 1000 * 100, " Centimeter")
        elif choice2 == 3:
            print(num1, " Kilometer = ", num1 * 1000 * 1000, " Millimeter")
        elif choice2 == 4:
            print(num1, " Kilometer = ", num1 / 1.609, " Mile")
        elif choice2 == 5:
            print(num1, " Kilometer = ", num1 * 1093.613, " Yard")
        elif choice2 == 6:
            print(num1, " Kilometer = ", num1 * 3280.84, " Foot")
        elif choice2 == 7:
            print(num1, " Kilometer = ", num1 * 39370.079, " Inch")
        elif choice2 == 8:
            print(num1, " Kilometer = ", num1 / 1.852, " Nautical Mile")
        elif choice2 == 9:
            print(num1, " Meter = ", num1 / 1000, " Kilometer")
        elif choice2 == 10:
            print(num1, " Meter = ", num1 / 100, " Centimeter")
        elif choice2 == 11:
            print(num1, " Meter = ", num1 * 1000, " Millimeter")
        elif choice2 == 12:
            print(num1, " Meter = ", num1 / 1609.344, " Mile")
        elif choice2 == 13:
            print(num1, " Meter = ", num1 * 1.094, " Yard")
        elif choice2 == 14:
            print(num1, " Meter = ", num1 * 3.281, " Foot")
        elif choice2 == 15:
            print(num1, " Meter = ", num1 * 39.37, " Inch")
        elif choice2 == 16:
            print(num1, " Meter = ", num1 / 1852, " Nautical Mile")
        elif choice2 == 17:
            print(num1, " Centimeter = ", num1 / 100000, " Kilometer")
        elif choice2 == 18:
            print(num1, " Centimeter = ", num1 / 100, " Meter")
        elif choice2 == 19:
            print(num1, " Centimeter = ", num1 * 10, " Millimeter")
        elif choice2 == 20:
            print(num1, " Centimeter = ", num1 / 160934.4, " Mile")
        elif choice2 == 21:
            print(num1, " Centimeter = ", num1 / 91.44, " Yard")
        elif choice2 == 22:
            print(num1, " Centimeter = ", num1 / 30.48, " Foot")
        elif choice2 == 23:
            print(num1, " Centimeter = ", num1 / 2.54, " Inch")
        elif choice2 == 24:
            print(num1, " Centimeter = ", num1 / 185200, " Nautical Mile")
        elif choice2 == 25:
            print(num1, " Millimeter = ", num1 / 1000000, " Kilometer")
        elif choice2 == 26:
            print(num1, " Millimeter = ", num1 / 1000, " Meter")
        elif choice2 == 27:
            print(num1, " Millimeter = ", num1 / 10, " Centimeter")
        elif choice2 == 28:
            print(num1, " Millimeter = ", num1 / (1.609 * 10 ** 6), " Mile")
        elif choice2 == 29:
            print(num1, " Millimeter = ", num1 / 914.4, " Yard")
        elif choice2 == 30:
            print(num1, " Millimeter = ", num1 / 304.8, " Foot")
        elif choice2 == 31:
            print(num1, " Millimeter = ", num1 / 25.4, " Inch")
        elif choice2 == 32:
            print(num1, " Millimeter = ", num1 / (1.852 * 10 ** 6), " Nautical Mile")
        elif choice2 == 33:
            print(num1, " Mile = ", num1 * 1.60934, " Kilometer")
        elif choice2 == 34:
            print(num1, " Mile = ", num1 * 1609.344, " Meter")
        elif choice2 == 35:
            print(num1, " Mile = ", num1 * 160934.4, " Centimeter")
        elif choice2 == 36:
            print(num1, " Mile = ", num1 * 1609344, " Millimeter")
        elif choice2 == 37:
            print(num1, " Mile = ", num1 * 1760, " Yard")
        elif choice2 == 38:
            print(num1, " Mile = ", num1 * 5280, " Foot")
        elif choice2 == 39:
            print(num1, " Mile = ", num1 * 63360, " Inch")
        elif choice2 == 40:
            print(num1, " Mile = ", num1 / 1.151, " Nautical Mile")
        elif choice2 == 41:
            print(num1, " Yard = ", num1 / 1093.613, " Kilometer")
        elif choice2 == 42:
            print(num1, " Yard = ", num1 / 1.09613, " Meter")
        elif choice2 == 43:
            print(num1, " Yard = ", num1 * 91.44, " Centimeter")
        elif choice2 == 44:
            print(num1, " Yard = ", num1 * 914.4, " Millimeter")
        elif choice2 == 45:
            print(num1, " Yard = ", num1 / 1760, " Mile")
        elif choice2 == 46:
            print(num1, " Yard = ", num1 * 3, " Foot")
        elif choice2 == 47:
            print(num1, " Yard = ", num1 * 36, " Inch")
        elif choice2 == 48:
            print(num1, " Yard = ", num1 / 2025.372, " Nautical Mile")
        elif choice2 == 49:
            print(num1, " Foot = ", num1 / 3280.84, " Kilometer")
        elif choice2 == 50:
            print(num1, " Foot = ", num1 / 3.281, " Meter")
        elif choice2 == 51:
            print(num1, " Foot = ", num1 * 30.48, " Centimeter")
        elif choice2 == 52:
            print(num1, " Foot = ", num1 * 304.8, " Millimeter")
        elif choice2 == 53:
            print(num1, " Foot = ", num1 / 5280, " Mile")
        elif choice2 == 54:
            print(num1, " Foot = ", num1 / 3, " Yard")
        elif choice2 == 55:
            print(num1, " Foot = ", num1 * 12, " Inch")
        elif choice2 == 56:
            print(num1, " Foot = ", num1 / 6076.115, " Nautical Mile")
        elif choice2 == 57:
            print(num1, " Inch = ", num1 / 39370.079, " Kilometer")
        elif choice2 == 58:
            print(num1, " Inch = ", num1 / 39.370079, " Meter")
        elif choice2 == 59:
            print(num1, " Inch = ", num1 * 2.54, " Centimeter")
        elif choice2 == 60:
            print(num1, " Inch = ", num1 * 25.4, " Millimeter")
        elif choice2 == 61:
            print(num1, " Inch = ", num1 / 63360, " Mile")
        elif choice2 == 62:
            print(num1, " Inch = ", num1 / 36, " Yard")
        elif choice2 == 63:
            print(num1, " Inch = ", num1 / 12, " Foot")
        elif choice2 == 64:
            print(num1, " Inch = ", num1 / 72913.386, " Nautical Mile")
        elif choice2 == 65:
            print(num1, " Nautical Mile = ", num1 * 1.852, " Kilometer")
        elif choice2 == 66:
            print(num1, " Nautical Mile = ", num1 * 1852, " Meter")
        elif choice2 == 67:
            print(num1, " Nautical Mile = ", num1 * 185200, " Centimeter")
        elif choice2 == 68:
            print(num1, " Nautical Mile = ", num1 * (1.852 * 10 ** 6), " Millimeter")
        elif choice2 == 69:
            print(num1, " Nautical Mile = ", num1 * 1.151, " Mile")
        elif choice2 == 70:
            print(num1, " Nautical Mile = ", num1 * 2025.372, " Yard")
        elif choice2 == 71:
            print(num1, " Nautical Mile = ", num1 * 676.115, " Foot")
        elif choice2 == 72:
            print(num1, " Nautical Mile = ", num1 * 72913.4, " Inch")
        else:
            print("Invalid Input")
            break

    elif choice == 3:
        choice3 = int(input(
            "Enter the your choice for Mass \n'1' Kilogram to Gram \n'2' Kilogram to Milligram \n'3' Kilogram to Micro gram"
            "\n'4' Kilogram to Metric Ton \n'5' Kilogram to Pound \n'6' Kilogram to Ounce"
            "\n'7' Gram to Kilogram \n'8' Gram to Milligram \n'9' Gram to Micro gram "
            "\n'10' Gram to Metric Ton \n'11' Gram to Pound \n'12' Gram to Ounce "
            "\n'13' Milligram to Kilogram \n'14' Milligram to Gram \n'15' Milligram to Micro Gram "
            "\n'16 Milligram to Metric Ton \n'17' Milligram to Pound \n'18' Milligram to Ounce "
            "\n'19' Micro gram to Kilogram \n'20' Micro gram to Gram \n'21' Micro gram to Milligram "
            "\n'22' Micro gram to Metric Ton \n'23' Micro gram to Pound \n'24' Micro gram to Ounce "
            "\n'25' Metric Ton to Kilogram \n'26' Metric Ton to gram \n'27' Metric Ton to Milligram "
            "\n'28' Metric Ton to Micro gram \n'29' Metric Ton to Pound \n'30' Metric Ton to Ounce "
            "\n'31' Pound to Kilogram \n'32' Pound to Gram \n'33' Pound to Milligram "
            "\n'34' Pound to Micro gram \n'35' Pound to Metric Ton \n'36' Pound to Ounce "
            "\n'37' Ounce to Kilogram \n'38' Ounce to Gram \n'39' Ounce to Milligram "
            "\n'40' Ounce to Micro gram \n'41' Ounce to Metric Ton \n'42' Ounce to Pound : "))

        num1 = int(input("Enter the number: "))
        if choice3 == 1:
            print(num1, " Kilogram = ", num1 * 1000, " Gram")
        elif choice3 == 2:
            print(num1, " Kilogram = ", num1 * 10 ** 6, " Milligram")
        elif choice3 == 3:
            print(num1, " Kilogram = ", num1 * 10 ** 9, " Micro gram")
        elif choice3 == 4:
            print(num1, " Kilogram = ", num1 * .001, " Metric Ton")
        elif choice3 == 5:
            print(num1, " Kilogram = ", num1 * 2.205, " Pound")
        elif choice3 == 6:
            print(num1, " Kilogram = ", num1 * 35.274, " Ounce")
        elif choice3 == 7:
            print(num1, " Gram = ", num1 / 1000, " Kilogram")
        elif choice3 == 8:
            print(num1, " Gram = ", num1 * 1000, " Milligram")
        elif choice3 == 9:
            print(num1, " Gram = ", num1 * 10 ** 6, " Micro gram")
        elif choice3 == 10:
            print(num1, " Gram = ", num1 * 10 ** -6, " Metric Ton")
        elif choice3 == 11:
            print(num1, " Gram = ", num1 / 453.592, " Pound")
        elif choice3 == 12:
            print(num1, " Gram = ", num1 / 0.035274, " Ounce")
        elif choice3 == 13:
            print(num1, " Milligram = ", num1 * 10 ** 6, " Kilogram")
        elif choice3 == 14:
            print(num1, " Milligram = ", num1 / 1000, " Gram")
        elif choice3 == 15:
            print(num1, " Milligram = ", num1 * 1000, " Micro gram")
        elif choice3 == 16:
            print(num1, " Milligram = ", num1 * 10 ** -9, " Metric Ton ")
        elif choice3 == 17:
            print(num1, " Milligram = ", num1 / 453592.37, " Pound")
        elif choice3 == 18:
            print(num1, " Milligram = ", num1 / 28349.523, " Ounce")
        elif choice3 == 19:
            print(num1, " Micro gram = ", num1 / 10 ** 9, " Kilogram")
        elif choice3 == 20:
            print(num1, " Micro gram = ", num1 / 10 ** 6, " Gram")
        elif choice3 == 21:
            print(num1, " Micro gram = ", num1 / 1000, " Milligram")
        elif choice3 == 22:
            print(num1, " Micro gram = ", num1 * 10 ** -12, " Metric Ton")
        elif choice3 == 23:
            print(num1, " Micro gram = ", num1 / 4.53 * 10 ** 8, " pound")
        elif choice3 == 24:
            print(num1, " Micro gram = ", num1 / 2.83 * 10 ** 7, " Ounce")
        elif choice3 == 25:
            print(num1, " Metric Ton = ", num1 * 1000, " Kilogram")
        elif choice3 == 26:
            print(num1, " Metric Ton = ", num1 * 10 ** 6, " Gram")
        elif choice3 == 27:
            print(num1, " Metric Ton = ", num1 * 10 ** 9, " Milligram")
        elif choice3 == 28:
            print(num1, " Metric Ton = ", num1 * 10 ** 12, " Micro gram")
        elif choice3 == 29:
            print(num1, " Metric Ton = ", num1 * 2204.62, " Pound")
        elif choice3 == 30:
            print(num1, " Metric Ton = ", num1 * 35274.0, " Ounce")
        elif choice3 == 31:
            print(num1, " Pound = ", num1 / 2.205, " Kilogram")
        elif choice3 == 32:
            print(num1, " Pound = ", num1 * 453.592, " Gram")
        elif choice3 == 33:
            print(num1, " Pound = ", num1 * 453592.37, " Milligram")
        elif choice3 == 34:
            print(num1, " Pound = ", num1 * 4.53592 * 10 ** 8, " Micro gram")
        elif choice3 == 35:
            print(num1, " Pound = ", num1 * 4.53592 * 10 ** -4, " Metric Ton")
        elif choice3 == 36:
            print(num1, " Pound = ", num1 * 16, " Ounce")
        elif choice3 == 37:
            print(num1, " Ounce = ", num1 / 35.274, " Kilogram")
        elif choice3 == 38:
            print(num1, " Ounce = ", num1 * 28.34953, " Gram")
        elif choice3 == 39:
            print(num1, " Ounce = ", num1 * 28349.523, " Milligram")
        elif choice3 == 40:
            print(num1, " Ounce = ", num1 * 2.835 * 10 ** 7, " Micro gram")
        elif choice3 == 41:
            print(num1, " Ounce = ", num1 * 2.835 * 10 ** -5, " Metric Ton")
        elif choice3 == 42:
            print(num1, " Ounce = ", num1 / 16, " Pound")
        else:
            print("Invalid Input")
            break

    elif choice == 4:
        choice4 = int(input("Enter the your choice for Volume "
                            "\n'1' US Gallon to US Quart \n'2' US Gallon to US Oz \n'3' US Gallon to Cubic meter"
                            "\n'4' US Gallon to Liter \n'5' US Gallon to Milliliter \n'6' US Gallon to Cubic Foot"
                            "\n'7' US Gallon to Cubic Inch \n'8' US Quart to US Gallon \n'9' US Quart to US Oz "
                            "\n'10' US Quart to Cubic meter \n'11' US Quart to Liter \n'12' US Quart to Milliliter "
                            "\n'13' US Quart to Cubic Foot \n'14' US Quart to Cubic Inch \n'15' US Oz to US Gallon "
                            "\n'16' US Oz to US Quartz \n'17' US Oz to Cubic Mater \n'18' US Oz to Liter "
                            "\n'19' US Oz to Milliliter \n'20' US Oz to Cubic Foot \n'21' US Oz to Cubic Inch "
                            "\n'22' Cubic meter to US Gallon \n'23' Cubic meter to US Quartz "
                            "\n'24' Cubic meter to US Oz \n'25' Cubic meter to Liter "
                            "\n'26' Cubic meter to Milliliter \n'27' Cubic meter to Cubic Foot "
                            "\n'28' Cubic meter to Cubic Inch \n'29' Liter to US Gallon \n'30' Liter to US Quartz "
                            "\n'31' Liter to US Oz \n'32' Liter to Cubic meter "
                            "\n'33' Liter to Milliliter \n'34' Liter to Cubic Foot \n'35' Liter to Cubic Inch "
                            "\n'36' Milliliter to US Gallon \n'37' Milliliter to US Quartz "
                            "\n'38' Milliliter to US Oz \n'39' Milliliter to Cubic meter "
                            "\n'40' Milliliter to Liter \n'41' Milliliter to Cubic Foot "
                            "\n'42' Milliliter to Cubic Inch "
                            "\n'43' Cubic Foot to US Gallon \n'44' Cubic Foot to US Quartz "
                            "\n'45' Cubic Foot to US Oz \n'46' Cubic Foot to Cubic meter "
                            "\n'47' Cubic Foot to Liter \n'48' Cubic Foot to Milliliter "
                            "\n'49' Cubic Foot to Cubic Inch "
                            "\n'50' Cubic Inch to US Gallon \n'51' Cubic Inch to US Quartz "
                            "\n'52' Cubic Inch to US Oz \n'53' Cubic Inch to Cubic meter "
                            "\n'54' Cubic Inch to Liter \n'55' Cubic Inch to Milliliter "
                            "\n'56' Cubic Inch to Cubic Foot : "))

        num1 = int(input("Enter the number: "))
        if choice4 == 1:
            print(num1, " US Gallon = ", num1 * 4, " Us Quart")
        elif choice4 == 2:
            print(num1, " US Gallon = ", num1 * 128, " Us Oz")
        elif choice4 == 3:
            print(num1, " US Gallon = ", num1 / 264.172, " Cubic Meter")
        elif choice4 == 4:
            print(num1, " US Gallon = ", num1 * 3.785, " Liter")
        elif choice4 == 5:
            print(num1, " US Gallon = ", num1 * 3785.412, " Milliliter")
        elif choice4 == 6:
            print(num1, " US Gallon = ", num1 / 7.481, " Cubic Foot")
        elif choice4 == 7:
            print(num1, " US Gallon = ", num1 * 231, " Cubic Inch")
        elif choice4 == 8:
            print(num1, " Us Quart = ", num1 / 4, " US Gallon")
        elif choice4 == 9:
            print(num1, " Us Quart = ", num1 * 32, " Us Oz")
        elif choice4 == 10:
            print(num1, " Us Quart = ", num1 / 1056.688, " Cubic Meter")
        elif choice4 == 11:
            print(num1, " Us Quart = ", num1 / 1.057, " Liter")
        elif choice4 == 12:
            print(num1, " Us Quart = ", num1 * 946.353, " Milliliter")
        elif choice4 == 13:
            print(num1, " Us Quart = ", num1 / 29.922, " Cubic Foot")
        elif choice4 == 14:
            print(num1, " Us Quart = ", num1 * 57.75, " Cubic Inch")
        elif choice4 == 15:
            print(num1, " Us Oz = ", num1 / 128, " US Gallon")
        elif choice4 == 16:
            print(num1, " Us Oz = ", num1 / 32, " Us Quart")
        elif choice4 == 17:
            print(num1, " Us Oz = ", num1 / 33814.023, " Cubic Meter")
        elif choice4 == 18:
            print(num1, " Us Oz = ", num1 / 33.814, " Liter")
        elif choice4 == 19:
            print(num1, " Us Oz = ", num1 * 29.574, " Milliliter")
        elif choice4 == 20:
            print(num1, " Us Oz = ", num1 / 957.506, " Cubic Foot")
        elif choice4 == 21:
            print(num1, " Us Oz = ", num1 * 1.805, " Cubic Inch")
        elif choice4 == 22:
            print(num1, " Cubic Meter = ", num1 * 264.172, " US Gallon")
        elif choice4 == 23:
            print(num1, " Cubic Meter = ", num1 * 1056.688, " Us Quart")
        elif choice4 == 24:
            print(num1, " Cubic Meter = ", num1 * 33814.02, " Us Oz")
        elif choice4 == 25:
            print(num1, " Cubic Meter = ", num1 * 1000, " Liter")
        elif choice4 == 26:
            print(num1, " Cubic Meter = ", num1 * 10 ** 6, " Milliliter")
        elif choice4 == 27:
            print(num1, " Cubic Meter = ", num1 * 35.315, " Cubic Foot")
        elif choice4 == 28:
            print(num1, " Cubic Meter = ", num1 * 61023.744, " Cubic Inch")
        elif choice4 == 29:
            print(num1, " Liter = ", num1 / 3.785, " US Gallon")
        elif choice4 == 30:
            print(num1, " Liter = ", num1 * 1.057, " Us Quart")
        elif choice4 == 31:
            print(num1, " Liter = ", num1 * 33.814, " Us Oz")
        elif choice4 == 32:
            print(num1, " Liter = ", num1 / 1000, " Cubic Meter")
        elif choice4 == 33:
            print(num1, " Liter = ", num1 * 1000, " Milliliter")
        elif choice4 == 34:
            print(num1, " Liter = ", num1 / 28.317, " Cubic Foot")
        elif choice4 == 35:
            print(num1, " Liter = ", num1 * 61.024, " Cubic Inch")
        elif choice4 == 36:
            print(num1, " Milliliter = ", num1 * 2.64172 * 10 ** -4, " US Gallon")
        elif choice4 == 37:
            print(num1, " Milliliter = ", num1 * 0.00105669, " Us Quart")
        elif choice4 == 38:
            print(num1, " Milliliter = ", num1 * 0.033814, " Us Oz")
        elif choice4 == 39:
            print(num1, " Milliliter = ", num1 * 10 ** -6, " Cubic Meter")
        elif choice4 == 40:
            print(num1, " Milliliter = ", num1 * 0.001, " Liter")
        elif choice4 == 41:
            print(num1, " Milliliter = ", num1 * 3.5315 * 10 ** -5, " Cubic Foot")
        elif choice4 == 42:
            print(num1, " Milliliter = ", num1 * 0.0610237, " Cubic Inch")
        elif choice4 == 43:
            print(num1, " Cubic Foot = ", num1 * 7.48052, " US Gallon")
        elif choice4 == 44:
            print(num1, " Cubic Foot = ", num1 * 29.9221, " Us Quart")
        elif choice4 == 45:
            print(num1, " Cubic Foot = ", num1 * 957.506, " Us Oz")
        elif choice4 == 46:
            print(num1, " Cubic Foot = ", num1 * 0.0283168, " Cubic Meter")
        elif choice4 == 47:
            print(num1, " Cubic Foot = ", num1 * 28.3168, " Liter")
        elif choice4 == 48:
            print(num1, " Cubic Foot = ", num1 * 28316.8, " Milliliter")
        elif choice4 == 49:
            print(num1, " Cubic Foot = ", num1 * 1728.0, " Cubic Inch")
        elif choice4 == 50:
            print(num1, " Cubic Inch = ", num1 * 0.004329, " US Gallon")
        elif choice4 == 51:
            print(num1, " Cubic Inch = ", num1 * 0.017316, " Us Quart")
        elif choice4 == 52:
            print(num1, " Cubic Inch = ", num1 * 0.554113, " Us Oz")
        elif choice4 == 53:
            print(num1, " Cubic Inch = ", num1 * 1.6387 * 10 ** -5, " Cubic Meter")
        elif choice4 == 54:
            print(num1, " Cubic Inch = ", num1 * 0.0163871, " Liter")
        elif choice4 == 55:
            print(num1, " Cubic Inch = ", num1 * 16.3871, " Milliliter")
        elif choice4 == 56:
            print(num1, " Cubic Inch = ", num1 * 5.78704 * 10 ** -4, " Cubic Foot")
        else:
            print("Invalid Input")
            break

    elif choice == 5:
        choice5 = int(input("Enter the your choice for Area \n '1' Square Km to Square Meter "
                            "\n'2' Square Km to Square Mile \n '3' Square Km to Square Yard "
                            "\n '4' Square Km to Square Foot "
                            "\n '5' Square Km to Square Inch \n '6' Square Km to Hectare "
                            "\n '7' Square Km to Acre "
                            "\n '8' Square Meter to Square Km \n '9' Square Meter to Square Mile "
                            "\n '10' Square Meter to Square Yard \n '11' Square Meter to Square Foot "
                            "\n '12' Square Meter to Square Inch \n '13' Square Meter to Hectare "
                            "\n '14' Square Meter to Acre "
                            "\n '15' Square Mile to Square Km \n '16' Square Mile to Square Meter "
                            "\n '17' Square Mile to Square Yard \n '18' Square Mile to Square Foot "
                            "\n '19' Square Mile to Square Inch \n '20' Square Mile to Hectare "
                            "\n '21' Square Mile to Acre "
                            "\n '22' Square Yard to Square Km \n '23' Square Yard to Square Meter "
                            "\n '24' Square Yard to Square Mile \n '25' Square Yard to Square Foot "
                            "\n '26' Square Yard to Square Inch \n '27' Square Yard to Hectare "
                            "\n '28' Square Yard to Acre "
                            "\n '29' Square Foot to Square Km \n '30' Square Foot to Square Meter "
                            "\n '31' Square Foot to Square Yard \n '32' Square Foot to Square Mile "
                            "\n '33' Square Foot to Square Inch \n '34' Square Foot to Hectare "
                            "\n '35' Square Foot to Acre "
                            "\n '36' Square Inch to Square Km \n '37' Square Inch to Square Meter "
                            "\n '38' Square Inch to Square Mile \n '39' Square Inch to Square Yard "
                            "\n '40' Square Inch to Square Foot \n '41' Square Inch to Hectare "
                            "\n '42' Square Inch to Acre "
                            "\n '43' Hectare to Square Km \n '44' Hectare to Square Meter "
                            "\n '45' Hectare to Square Yard \n '46' Hectare to Square Foot "
                            "\n '47' Hectare to Square Inch \n '48' Hectare to Square Mile "
                            "\n '49' Hectare to Acre "
                            "\n '50' Acre to Square Km \n '51' Acre to Square Meter "
                            "\n '52' Acre to Square Yard \n '53' Acre to Square Foot "
                            "\n '54' Acre to Square Inch \n '55' Acre to Hectare "
                            "\n '56' Acre to Square Mile : "))

        num1 = int(input("Enter the number: "))
        if choice5 == 1:
            print(num1, " Square Km = ", (num1 * 1000 ** 2), " Square Meter")
        elif choice5 == 2:
            print(num1, " Square Km = ", (num1 / 259), " Square Mile")
        elif choice5 == 3:
            print(num1, " Square Km = ", (num1 * 1.196 * 10 ** 6), " Square Yard")
        elif choice5 == 4:
            print(num1, " Square Km = ", (num1 * 1.076 * 10 ** 7), " Square Foot")
        elif choice5 == 5:
            print(num1, " Square Km = ", (num1 * 1.55 * 10 ** 9), " Square Inch")
        elif choice5 == 6:
            print(num1, " Square Km = ", (num1 * 100), " Hectare")
        elif choice5 == 7:
            print(num1, " Square Km = ", (num1 * 247.105), " Acre")
        elif choice5 == 8:
            print(num1, " Square Meter = ", (num1 / 1000 ** 2), " Square Km")
        elif choice5 == 9:
            print(num1, " Square Meter = ", (num1 / 2.59 * 10 ** 6), " Square Mile")
        elif choice5 == 10:
            print(num1, " Square Meter = ", (num1 * 1.196), " Square Yard")
        elif choice5 == 11:
            print(num1, " Square Meter = ", (num1 * 10.7639), " Square Foot")
        elif choice5 == 12:
            print(num1, " Square Meter = ", (num1 * 1550.003), " Square Inch")
        elif choice5 == 13:
            print(num1, " Square Meter = ", (num1 / 10000), " Hectare")
        elif choice5 == 14:
            print(num1, " Square Meter = ", (num1 / 4046.856), " Acre")
        elif choice5 == 15:
            print(num1, " Square Mile = ", (num1 * 2.59), " Square Km")
        elif choice5 == 16:
            print(num1, " Square Mile = ", (num1 * 2.59 * 10 ** 6), " Square Meter")
        elif choice5 == 17:
            print(num1, " Square Mile = ", (num1 * 3.098 * 10 ** 6), " Square Yard")
        elif choice5 == 18:
            print(num1, " Square Mile = ", (num1 * 2.788 * 10 ** 7), " Square Foot")
        elif choice5 == 19:
            print(num1, " Square Mile = ", (num1 * 4.014 * 10 ** 9), " Square Inch")
        elif choice5 == 20:
            print(num1, " Square Mile = ", (num1 * 258.999), " Hectare")
        elif choice5 == 21:
            print(num1, " Square Mile = ", (num1 * 640), " Acre")
        elif choice5 == 22:
            print(num1, " Square Yard = ", (num1 / 1.196 * 10 ** 6), " Square Km")
        elif choice5 == 23:
            print(num1, " Square Yard = ", (num1 / 1.196), " Square Meter")
        elif choice5 == 24:
            print(num1, " Square Yard = ", (num1 / 3.098 * 10 ** 6), " Square Mile")
        elif choice5 == 25:
            print(num1, " Square Yard = ", (num1 * 9), " Square Foot")
        elif choice5 == 26:
            print(num1, " Square Yard = ", (num1 * 1296), " Square Inch")
        elif choice5 == 27:
            print(num1, " Square Yard = ", (num1 / 11959.9), " Hectare")
        elif choice5 == 28:
            print(num1, " Square Yard = ", (num1 / 4840), " Acre")
        elif choice5 == 29:
            print(num1, " Square Foot = ", (num1 * 1.076 * 10 ** 7), " Square Km")
        elif choice5 == 30:
            print(num1, " Square Foot = ", (num1 / 10.764), " Square Meter")
        elif choice5 == 31:
            print(num1, " Square Foot = ", (num1 / 9), " Square Yard")
        elif choice5 == 32:
            print(num1, " Square Foot = ", (num1 / 2.788 * 10 ** 7), " Square Mile")
        elif choice5 == 33:
            print(num1, " Square Foot = ", (num1 * 144), " Square Inch")
        elif choice5 == 34:
            print(num1, " Square Foot = ", (num1 / 107639.104), " Hectare")
        elif choice5 == 35:
            print(num1, " Square Foot = ", (num1 / 43560), " Acre")
        elif choice5 == 36:
            print(num1, " Square Inch = ", (num1 / 1.55 * 10 ** 9), " Square Km")
        elif choice5 == 37:
            print(num1, " Square Inch = ", (num1 / 1550.003), " Square Meter")
        elif choice5 == 38:
            print(num1, " Square Inch = ", (num1 / 4.014 * 10 ** 9), " Square Mile")
        elif choice5 == 39:
            print(num1, " Square Inch = ", (num1 / 1296), " Square Yard")
        elif choice5 == 40:
            print(num1, " Square Inch = ", (num1 / 144), " Square Foot")
        elif choice5 == 41:
            print(num1, " Square Inch = ", (num1 / 1.55 * 10 ** 7), " Hectare")
        elif choice5 == 42:
            print(num1, " Square Inch = ", (num1 / 6.273 * 10 ** 6), " Acre")
        elif choice5 == 43:
            print(num1, " Hectare = ", (num1 / 100), " Square Km")
        elif choice5 == 44:
            print(num1, " Hectare = ", (num1 * 10000), " Square Meter")
        elif choice5 == 45:
            print(num1, " Hectare = ", (num1 * 11959.9), " Square Yard")
        elif choice5 == 46:
            print(num1, " Hectare = ", (num1 * 107639.104), " Square Foot")
        elif choice5 == 47:
            print(num1, " Hectare = ", (num1 * 1.55 * 10 ** 7), " Square Inch")
        elif choice5 == 48:
            print(num1, " Hectare = ", (num1 / 258.999), " Square Mile")
        elif choice5 == 49:
            print(num1, " Hectare = ", (num1 * 2.47105), " Acre")
        elif choice5 == 50:
            print(num1, " Acre = ", (num1 / 247.105), " Square Km")
        elif choice5 == 51:
            print(num1, " Acre = ", (num1 * 4046.856), " Square Meter")
        elif choice5 == 52:
            print(num1, " Acre = ", (num1 * 4840), " Square Yard")
        elif choice5 == 53:
            print(num1, " Acre = ", (num1 * 43560), " Square Foot")
        elif choice5 == 54:
            print(num1, " Acre = ", (num1 * 6.273 * 10 ** 6), " Square Inch")
        elif choice5 == 55:
            print(num1, " Acre = ", (num1 / 640), " Square Mile")
        elif choice5 == 56:
            print(num1, " Acre = ", (num1 / 2.471), " Hectare")
        else:
            print("Invalid Input")
            break

    elif choice == 6:
        choice6 = int(input("Enter the your choice for Time \n'1' Nanosecond to Microsecond "
                            "\n'2' Nanosecond to Millisecond "
                            "\n '3' Nanosecond to Second \n'4' Nanosecond to Minute \n'5' Nanosecond to Hour "
                            "\n '6' Nanosecond to Day \n'7' Nanosecond to Week \n'8' Nanosecond to Month "
                            "\n '9' Nanosecond to Year \n'10' Nanosecond to Decade \n'11' Nanosecond to Century "
                            "\n '12' Microsecond to Nanosecond \n'13' Microsecond to Millisecond "
                            "\n '14' Microsecond to Second \n'15' Microsecond to Minute \n'16' Microsecond to Hour "
                            "\n '17' Microsecond to Day \n'18' Microsecond to Week \n'19' Microsecond to Month "
                            "\n '20' Microsecond to Year \n'21' Microsecond to Decade \n'22' Microsecond to Century "
                            "\n '23' Millisecond to Nanosecond \n'24' Millisecond to Microsecond "
                            "\n '25' Millisecond to Second \n'26' Millisecond to Minute \n'27' Millisecond to Hour "
                            "\n '28' Millisecond to Day \n'29' Millisecond to Week \n'30' Millisecond to Month "
                            "\n '31' Millisecond to Year \n'32' Millisecond to Decade \n'33' Millisecond to Century "
                            "\n '34' Second to Nanosecond \n'35' Second to Microsecond \n'36' Second to Millisecond"
                            "\n '37' Second to Minute \n'38' Second to Hour \n'39' Second to Day "
                            "\n '40' Second to Week \n'41' second to Month \n'42' Second to Year "
                            "\n '43' Second to Decade \n'44' Second to Century \n'45' Minute to Nanosecond "
                            "\n '46' Minute to Microsecond \n'47' Minute to Millisecond \n '48' Minute to Second "
                            "\n '49' Minute to Hour \n '50' Minute to Day \n '51' Minute to Week \n'52' Minute to Month "
                            "\n '53' Minute to Year \n '54' Minute to Decade \n'55' Minute to Century "
                            "\n '56' Hour to Nanosecond \n'57' Hour to Microsecond \n'58' Hour to Millisecond "
                            "\n '59' Hour to Second \n'60' Hour to Minute \n'61' Hour to Day "
                            "\n '62' Hour to Week \n'63' Hour to Month \n'64' Hour to Year "
                            "\n '65' Hour to Decade \n'66' Hour to Century \n'67' Day to Nanosecond "
                            "\n '68' Day to Microsecond \n'69' Day to Millisecond \n'70' Day to Second "
                            "\n '71' Day to Minute \n'72' Day to Hour \n'73' Day to Week \n'74' Day to Month "
                            "\n '75' Day to Year \n'76' Day to Decade \n'77' Day to Century "
                            "\n '78' Week to Nanosecond \n '79' Week to Microsecond \n'80' Week to Millisecond "
                            "\n '81' Week to Second \n '82' Week to Minute \n '83' Week to Hour "
                            "\n '84' Week to Day \n'85' Week  to Month \n '86' Week to Year "
                            "\n '87' Week to Decade \n'88' Week to Century \n'89' Month to Nanosecond "
                            "\n '90' Month to Microsecond \n'91' Month to Millisecond \n '92' Month to Second "
                            "\n '93' Month to Minute \n '94' Month to Hour \n '95' Month to Day \n'96' Month to Week "
                            "\n '97' Month to Year \n '98' Month to Decade \n'99' Month to Century "
                            "\n '100' Year to Nanosecond \n '101' Year to Microsecond \n'102' Year to Millisecond "
                            "\n '103' Year to Second \n '104' Year to Minute \n '105' Year to Hour "
                            "\n '106' Year to Day \n'107' Year to Week \n '108' Year to Month "
                            "\n '109' Year to Decade \n'110' Year to Century "
                            "\n '111' Decade to Nanosecond \n '112' Decade to Microsecond \n'113' Decade to Millisecond "
                            "\n '114' Decade to Second \n '115' Decade to Minute \n '116' Decade to Hour "
                            "\n '117' Decade to Day \n'118' Decade to Week \n '119' Decade to Month "
                            "\n '120' Decade to Year \n'121' Decade to Century \n '122' Century to Nanosecond "
                            "\n '123' Century to Microsecond \n'124' Century to Millisecond "
                            "\n '125' Century to Second \n '126' Century to Minute \n '127' Century to Hour "
                            "\n '128' Century to Day \n'129' Century to Week \n '130' Century to Month "
                            "\n '131' Century to Year \n'132' Century to Decade : "))

        num1 = int(input("Enter the number: "))
        if choice6 == 1:
            print(num1, " Nanosecond = ", (num1 * 0.001), " Microsecond")
        elif choice6 == 2:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 2), " Millisecond")
        elif choice6 == 3:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3), " Second")
        elif choice6 == 4:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 60)), " Minute")
        elif choice6 == 5:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 3600)), " Hour")
        elif choice6 == 6:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 3600 * 24)), " Day")
        elif choice6 == 7:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 3600 * 24 * 7)), " Week")
        elif choice6 == 8:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 3600 * 24 * 30)), " Month")
        elif choice6 == 9:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 3600 * 24 * 365)), " Year")
        elif choice6 == 10:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 3600 * 24 * 3650)), " Decade")
        elif choice6 == 11:
            print(num1, " Nanosecond = ", (num1 * 0.001 ** 3 * (1 / 3600 * 24 * 36500)), " Century")
        elif choice6 == 12:
            print(num1, " Microsecond = ", (num1 * 1000), " Nanosecond")
        elif choice6 == 13:
            print(num1, " Microsecond = ", (num1 * 0.001), " Millisecond")
        elif choice6 == 14:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2), " Second")
        elif choice6 == 15:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 60)), " Minute")
        elif choice6 == 16:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 3600)), " Hour")
        elif choice6 == 17:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 3600 * 24)), " Day")
        elif choice6 == 18:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 3600 * 24 * 7)), " Week")
        elif choice6 == 19:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 3600 * 24 * 30)), " Month")
        elif choice6 == 20:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 3600 * 24 * 365)), " Year")
        elif choice6 == 21:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 3600 * 24 * 3650)), " Decade")
        elif choice6 == 22:
            print(num1, " Microsecond = ", (num1 * 0.001 ** 2 * (1 / 3600 * 24 * 36500)), " Century")
        elif choice6 == 23:
            print(num1, " Millisecond = ", (num1 * 1000 * 1000), " Nanosecond")
        elif choice6 == 24:
            print(num1, " Millisecond = ", (num1 * 1000), " Microsecond")
        elif choice6 == 25:
            print(num1, " Millisecond = ", (num1 * 0.001), " Second")
        elif choice6 == 26:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 60)), " Minute")
        elif choice6 == 27:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 3600)), " Hour")
        elif choice6 == 28:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 3600 * 24)), " Day")
        elif choice6 == 29:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 3600 * 24 * 7)), " Week")
        elif choice6 == 30:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 3600 * 24 * 30)), " Month")
        elif choice6 == 31:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 3600 * 24 * 365)), " Year")
        elif choice6 == 32:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 3600 * 24 * 3650)), " Decade")
        elif choice6 == 33:
            print(num1, " Millisecond = ", (num1 * 0.001 * (1 / 3600 * 24 * 36500)), " Century")
        elif choice6 == 34:
            print(num1, " Second = ", (num1 * 1000 ** 3), " Nanosecond")
        elif choice6 == 35:
            print(num1, " Second = ", (num1 * 1000 ** 2), " Microsecond")
        elif choice6 == 36:
            print(num1, " Second = ", (num1 * 1000), " Millisecond")
        elif choice6 == 37:
            print(num1, " Second = ", (num1 / 60), " Minute")
        elif choice6 == 38:
            print(num1, " Second = ", (num1 / 3600), " Hour")
        elif choice6 == 39:
            print(num1, " Second = ", (num1 / (3600 * 24)), " Day")
        elif choice6 == 40:
            print(num1, " Second = ", (num1 / (3600 * 24 * 7)), " Week")
        elif choice6 == 41:
            print(num1, " Second = ", (num1 / (3600 * 24 * 30)), " Month")
        elif choice6 == 42:
            print(num1, " Second = ", (num1 / (3600 * 365)), " Year")
        elif choice6 == 43:
            print(num1, " Second = ", (num1 / (3600 * 3650)), " Decade")
        elif choice6 == 44:
            print(num1, " Second = ", (num1 / (3600 * 36500)), " Century")
        elif choice6 == 45:
            print(num1, " Minute = ", (num1 * 1000 ** 3 * 60), " Nanosecond")
        elif choice6 == 46:
            print(num1, " Minute = ", (num1 * 1000 ** 2 * 60), " Microsecond")
        elif choice6 == 47:
            print(num1, " Minute = ", (num1 * 1000 * 60), " Millisecond")
        elif choice6 == 48:
            print(num1, " Minute = ", (num1 * 60), " Second")
        elif choice6 == 49:
            print(num1, " Minute = ", num1 / 60, " Hour")
        elif choice6 == 50:
            print(num1, " Minute = ", num1 / (60 * 24), " Day")
        elif choice6 == 51:
            print(num1, " Minute = ", num1 / (60 * 24 * 7), " Week")
        elif choice6 == 52:
            print(num1, " Minute = ", num1 / (60 * 24 * 30), " Month")
        elif choice6 == 53:
            print(num1, " Minute = ", num1 / (60 * 24 * 365), " Year")
        elif choice6 == 54:
            print(num1, " Minute = ", num1 / (60 * 24 * 3650), " Decade")
        elif choice6 == 55:
            print(num1, " Minute = ", num1 / (60 * 24 * 36500), " Century")
        elif choice6 == 56:
            print(num1, " Hour = ", num1 * 1000 ** 3 * 3600, " Nanosecond")
        elif choice6 == 57:
            print(num1, " Hour = ", num1 * 1000 ** 2 * 3600, " Microsecond")
        elif choice6 == 58:
            print(num1, " Hour = ", num1 * 1000 * 3600, " Millisecond")
        elif choice6 == 59:
            print(num1, " Hour = ", num1 * 3600, " Second")
        elif choice6 == 60:
            print(num1, " Hour = ", num1 * 60, " Minute")
        elif choice6 == 61:
            print(num1, " Hour = ", num1 / 24, " Day")
        elif choice6 == 62:
            print(num1, " Hour = ", num1 / (24 * 7), " Week")
        elif choice6 == 63:
            print(num1, " Hour = ", num1 / (24 * 30), " Month")
        elif choice6 == 64:
            print(num1, " Hour = ", num1 / (24 * 365), " Year")
        elif choice6 == 65:
            print(num1, " Hour = ", num1 / (24 * 3650), " Decade")
        elif choice6 == 66:
            print(num1, " Hour = ", num1 / (24 * 36500), " Century")
        elif choice6 == 67:
            print(num1, " Day = ", num1 * 1000 ** 3 * 3600 * 24, " Nanosecond")
        elif choice6 == 68:
            print(num1, " Day = ", num1 * 1000 ** 2 * 3600 * 24, " Microsecond")
        elif choice6 == 69:
            print(num1, " Day = ", num1 * 1000 * 3600 * 24, " Millisecond")
        elif choice6 == 70:
            print(num1, " Day = ", num1 * 3600 * 24, " Second")
        elif choice6 == 71:
            print(num1, " Day = ", num1 * 60 * 24, " Minute")
        elif choice6 == 72:
            print(num1, " Day = ", num1 * 24, " Hour")
        elif choice6 == 73:
            print(num1, " Day = ", num1 / (24 * 7), " Week")
        elif choice6 == 74:
            print(num1, " Day = ", num1 / (24 * 7 * 30), " Month")
        elif choice6 == 75:
            print(num1, " Day = ", num1 / (24 * 7 * 365), " Year")
        elif choice6 == 76:
            print(num1, " Day = ", num1 / (24 * 7 * 3650), " Decade")
        elif choice6 == 77:
            print(num1, " Day = ", num1 / (24 * 7 * 36500), " Century")
        elif choice6 == 78:
            print(num1, " Week = ", num1 * 1000 ** 3 * 3600 * 24 * 7, " Nanosecond")
        elif choice6 == 79:
            print(num1, " Week = ", num1 * 1000 ** 2 * 3600 * 24 * 7, " Microsecond")
        elif choice6 == 80:
            print(num1, " Week = ", num1 * 1000 * 3600 * 24 * 7, " Millisecond")
        elif choice6 == 81:
            print(num1, " Week = ", num1 * 3600 * 24 * 7, " Second")
        elif choice6 == 82:
            print(num1, " Week = ", num1 * 60 * 24 * 7, " Minutes")
        elif choice6 == 83:
            print(num1, " Week = ", num1 * 24 * 7, " Hour")
        elif choice6 == 84:
            print(num1, " Week = ", num1 * 7, " Day")
        elif choice6 == 85:
            print(num1, " Week = ", (num1 * 30) / 7, " Month")
        elif choice6 == 86:
            print(num1, " Week = ", (num1 * 365) / 7, " Year")
        elif choice6 == 87:
            print(num1, " Week = ", (num1 * 3650) / 7, " Decade")
        elif choice6 == 88:
            print(num1, " Week = ", (num1 * 36500) / 7, " Century")
        elif choice6 == 89:
            print(num1, " Month = ", num1 * 1000 ** 3 * 3600 * 24 * 30, " Nanosecond")
        elif choice6 == 90:
            print(num1, " Month = ", num1 * 1000 ** 2 * 3600 * 24 * 30, " Microsecond")
        elif choice6 == 91:
            print(num1, " Month = ", num1 * 1000 * 3600 * 24 * 30, " Millisecond")
        elif choice6 == 92:
            print(num1, " Month = ", num1 * 3600 * 24 * 30, " Second")
        elif choice6 == 93:
            print(num1, " Month = ", num1 * 60 * 24 * 30, " Minute")
        elif choice6 == 94:
            print(num1, " Month = ", num1 * 24 * 30, " Hour")
        elif choice6 == 95:
            print(num1, " Month = ", num1 * 30, " Day")
        elif choice6 == 96:
            print(num1, " Month = ", num1 * 4.34, " Week")
        elif choice6 == 97:
            print(num1, " Month = ", (num1 * 365) / 30, " Year")
        elif choice6 == 98:
            print(num1, " Month = ", (num1 * 3650) / 30, " Decade")
        elif choice6 == 99:
            print(num1, " Month = ", (num1 * 36500) / 30, " Century")
        elif choice6 == 100:
            print(num1, " Year = ", num1 * 1000 ** 3 * 3600 * 24 * 365, " Nanosecond")
        elif choice6 == 101:
            print(num1, " Year = ", num1 * 1000 ** 2 * 3600 * 24 * 365, " Microsecond")
        elif choice6 == 102:
            print(num1, " Year = ", num1 * 1000 * 3600 * 24 * 365, " Millisecond")
        elif choice6 == 103:
            print(num1, " Year = ", num1 * 3600 * 24 * 365, " Second")
        elif choice6 == 104:
            print(num1, " Year = ", num1 * 60 * 24 * 365, " Minutes")
        elif choice6 == 105:
            print(num1, " Year = ", num1 * 24 * 365, " Hours")
        elif choice6 == 106:
            print(num1, " Year = ", num1 * 365, " Days")
        elif choice6 == 107:
            print(num1, " Year = ", num1 * 12 * 4.34, " Weeks")
        elif choice6 == 108:
            print(num1, " Year = ", num1 * 30, " Months")
        elif choice6 == 109:
            print(num1, " Year = ", num1 / 10, " Decade")
        elif choice6 == 110:
            print(num1, " Year = ", num1 / 100, " Century")
        elif choice6 == 111:
            print(num1, " Decade = ", num1 * 1000 ** 3 * 3600 * 24 * 3650, " Nanosecond")
        elif choice6 == 112:
            print(num1, " Decade = ", num1 * 1000 ** 2 * 3600 * 24 * 3650, " Microsecond")
        elif choice6 == 113:
            print(num1, " Decade = ", num1 * 1000 * 3600 * 24 * 3650, " Millisecond")
        elif choice6 == 114:
            print(num1, " Decade = ", num1 * 3600 * 24 * 3650, " Second")
        elif choice6 == 115:
            print(num1, " Decade = ", num1 * 60 * 24 * 3650, " Minutes")
        elif choice6 == 116:
            print(num1, " Decade = ", num1 * 24 * 3650, " Hours")
        elif choice6 == 117:
            print(num1, " Decade = ", num1 * 3650, " Days")
        elif choice6 == 118:
            print(num1, " Decade = ", num1 * 10 * 12 * 4.34, " Weeks")
        elif choice6 == 119:
            print(num1, " Decade = ", num1 * 10 * 12, " Months")
        elif choice6 == 120:
            print(num1, " Decade = ", num1 * 10 * 12, " Years")
        elif choice6 == 121:
            print(num1, " Decade = ", num1 / 10, " Century")
        elif choice6 == 122:
            print(num1, " Century = ", num1 * 1000 ** 3 * 3600 * 24 * 36500, " Nanosecond")
        elif choice6 == 123:
            print(num1, " Century = ", num1 * 1000 ** 2 * 3600 * 24 * 36500, " Microsecond")
        elif choice6 == 124:
            print(num1, " Century = ", num1 * 1000 * 3600 * 24 * 36500, " Millisecond")
        elif choice6 == 125:
            print(num1, " Century = ", num1 * 3600 * 24 * 36500, " Second")
        elif choice6 == 126:
            print(num1, " Century = ", num1 * 60 * 24 * 36500, " Minute")
        elif choice6 == 127:
            print(num1, " Century = ", num1 * 24 * 36500, " Hour")
        elif choice6 == 128:
            print(num1, " Century = ", num1 * 36500, " Days")
        elif choice6 == 129:
            print(num1, " Century = ", num1 * 100 * 12 * 4.34, " Weeks")
        elif choice6 == 130:
            print(num1, " Century = ", num1 * 100 * 12, " Months")
        elif choice6 == 131:
            print(num1, " Century = ", num1 * 100, " Years")
        elif choice6 == 132:
            print(num1, " Century = ", num1 * 10, " Decades")

        else:
            print("Invalid Input")
            break


    elif choice == 7:
        choice7 = int(input("Enter the your choice for Digital Storage \n '1' Bit to Byte "
                            "\n'2' Bit to Kilobyte \n '3' Bit to Megabyte \n '4' Bit to Gigabyte "
                            "\n '5' Bit to Terabyte \n '6' Bit to Petabyte \n '7' Byte to Bit "
                            "\n'8' Byte to Kilobyte \n '9' Byte to Megabyte \n '10' Byte to Gigabyte "
                            "\n '11' Byte to Terabyte \n '12' Byte to Petabyte \n '13' Kilobyte to Bit "
                            "\n'14' Kilobyte to Byte \n '15' Kilobyte to Megabyte \n '16' Kilobyte to Gigabyte "
                            "\n '17' Kilobyte to Terabyte \n '18' Kilobyte to Petabyte \n '19' Megabyte to Bit "
                            "\n'20' Megabyte to Byte \n '21' Megabyte to Kilobyte \n '22' Megabyte to Gigabyte "
                            "\n '23' Megabyte to Terabyte \n '24' Megabyte to Petabyte \n '25' Gigabyte to Bit "
                            "\n'26' Gigabyte to Byte \n '27' Gigabyte to Kilobyte \n '28' Gigabyte to Megabyte "
                            "\n '29' Gigabyte to Terabyte \n '30' Gigabyte to Petabyte \n '31' Terabyte to Bit "
                            "\n'32' Terabyte to Byte \n '33' Terabyte to Kilobyte \n '34' Terabyte to Megabyte "
                            "\n '35' Terabyte to Gigabyte \n '36' Terabyte to Petabyte \n '37' Petabyte to Bit "
                            "\n'38' Pitabyte to Byte \n '39' Pitabyte to Kilobyte \n '40' Pitabyte to Megabyte "
                            "\n '41' Pitabyte to Gigabyte \n '42' Pitabyte to Terabyte : "))
        num1 = int(input("Enter the number: "))
        if choice7 == 1:
            print(num1, " Bit = ", (num1 * 0.125), " Byte")
        elif choice7 == 2:
            print(num1, " Bit = ", (num1 * 0.0009765625 * 0.125), " Kilobyte")
        elif choice7 == 3:
            print(num1, " Bit = ", (num1 * 0.0009765625 * 0.0009765625 * 0.125), " Megabyte")
        elif choice7 == 4:
            print(num1, " Bit = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.125), " Gigabyte")
        elif choice7 == 5:
            print(num1, " Bit = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.125),
                  " Terabyte")
        elif choice7 == 6:
            print(num1, " Bit = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.0009765625
                                    * 0.125), " Pitabyte")
        elif choice7 == 7:
            print(num1, " Byte = ", (num1 * 8), " Bit")
        elif choice7 == 8:
            print(num1, " Byte = ", (num1 * 0.0009765625), " Kilobyte")
        elif choice7 == 9:
            print(num1, " Byte = ", (num1 * 0.0009765625 * 0.0009765625), " Megabyte")
        elif choice7 == 10:
            print(num1, " Byte = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625), " Gigabyte")
        elif choice7 == 11:
            print(num1, " Byte = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.0009765625), " Terabyte")
        elif choice7 == 12:
            print(num1, " Byte = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.0009765625),
                  " Pitabyte")
        elif choice7 == 13:
            print(num1, " Kilobyte = ", (num1 * 1024 * 8), " Bit")
        elif choice7 == 14:
            print(num1, " Kilobyte = ", (num1 * 1024), " Byte")
        elif choice7 == 15:
            print(num1, " Kilobyte = ", (num1 * 0.0009765625), " Megabyte")
        elif choice7 == 16:
            print(num1, " Kilobyte = ", (num1 * 0.0009765625 * 0.0009765625), " Gigabyte")
        elif choice7 == 17:
            print(num1, " Kilobyte = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625), " Terabyte")
        elif choice7 == 18:
            print(num1, " Kilobyte = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625 * 0.0009765625), " Pitabyte")
        elif choice7 == 19:
            print(num1, " Megabyte = ", (num1 * 1024 * 1024 * 8), " Bit")
        elif choice7 == 20:
            print(num1, " Megabyte = ", (num1 * 1024 * 1024), " Byte")
        elif choice7 == 21:
            print(num1, " Megabyte = ", (num1 * 1024), " Kilobyte")
        elif choice7 == 22:
            print(num1, " Megabyte = ", (num1 * 0.0009765625), " Gigabyte")
        elif choice7 == 23:
            print(num1, " Megabyte = ", (num1 * 0.0009765625 * 0.0009765625), " Terabyte")
        elif choice7 == 24:
            print(num1, " Megabyte = ", (num1 * 0.0009765625 * 0.0009765625 * 0.0009765625), " Pitabyte")
        elif choice7 == 25:
            print(num1, " Gigabyte = ", (num1 * 1024 * 1024 * 1024 * 8), " Bit")
        elif choice7 == 26:
            print(num1, " Gigabyte = ", (num1 * 1024 * 1024 * 1024), " Byte")
        elif choice7 == 27:
            print(num1, " Gigabyte = ", (num1 * 1024 * 1024), " Kilobyte")
        elif choice7 == 28:
            print(num1, " Gigabyte = ", (num1 * 1024), " Megabyte")
        elif choice7 == 29:
            print(num1, " Gigabyte = ", (num1 * 0.0009765625), " Terabyte")
        elif choice7 == 30:
            print(num1, " Gigabyte = ", (num1 * 0.0009765625 * 0.0009765625), " Pitabyte")
        elif choice7 == 31:
            print(num1, " Terabyte = ", (num1 * 1024 * 1024 * 1024 * 1024 * 8), " Bit")
        elif choice7 == 32:
            print(num1, " Terabyte = ", (num1 * 1024 * 1024 * 1024 * 1024), " Byte")
        elif choice7 == 33:
            print(num1, " Terabyte = ", (num1 * 1024 * 1024 * 1024), " Kilobyte")
        elif choice7 == 34:
            print(num1, " Terabyte = ", (num1 * 1024 * 1024), " Megabyte")
        elif choice7 == 35:
            print(num1, " Terabyte = ", (num1 * 1024), " Gigabyte")
        elif choice7 == 36:
            print(num1, " Terabyte = ", (num1 * 0.0009765625), " Pitabyte")
        elif choice7 == 37:
            print(num1, " Pitabyte = ", (num1 * 1024 * 1024 * 1024 * 1024 * 1024 * 8), " Bit")
        elif choice7 == 38:
            print(num1, " Pitabyte = ", (num1 * 1024 * 1024 * 1024 * 1024 * 1024), " Byte")
        elif choice7 == 39:
            print(num1, " Pitabyte = ", (num1 * 1024 * 1024 * 1024 * 1024), " Kilobyte")
        elif choice7 == 40:
            print(num1, " Pitabyte = ", (num1 * 1024 * 1024 * 1024), " Megabyte")
        elif choice7 == 41:
            print(num1, " Pitabyte = ", (num1 * 1024 * 1024), " Gigabyte")
        elif choice7 == 42:
            print(num1, " Pitabyte = ", (num1 * 1024), " Terabyte")
        else:
            print("Invalid Input")
            break


    elif choice == 8:
        choice8 = int(input("Enter the your choice for Speed:"
                            " \n'1' Miles/hour to Feet/sec \n'2' Miles/hour to Meter/sec "
                            "\n'3' Miles/hour to Kilometer/hour \n'4' Feet/sec to Miles/hour "
                            "\n'5' Feet/sec to Meter/sec \n'6' Feet/sec to Kilometer/hour "
                            "\n'7' Kilometer/hour to Miles/hour \n'8' Kilometer/hour to Meter/sec "
                            "\n'9' Kilometer/hour to Feet/sec :"))
        num1 = int(input("Enter the number: "))
        if choice8 == 1:
            print(num1, " Miles/hour = ", (num1 * 1.46667), " Feet/sec")
        elif choice8 == 2:
            print(num1, " Miles/hour = ", (num1 * 0.44704), " Meter/sec")
        elif choice8 == 3:
            print(num1, " Miles/hour = ", (num1 * 1.60934), " Kilometer/hour")
        elif choice8 == 4:
            print(num1, " Feet/sec = ", (num1 * 0.681818), " Miles/hour")
        elif choice8 == 5:
            print(num1, " Feet/sec = ", (num1 * 0.3048), " Meter/sec")
        elif choice8 == 6:
            print(num1, " Feet/sec = ", (num1 * 1.09728), " Kilometer/hour")
        elif choice8 == 7:
            print(num1, " Kilometer/hour = ", (num1 * 0.621371), " Miles/hour")
        elif choice8 == 8:
            print(num1, " Kilometer/hour = ", (num1 * 0.277778), " Meter/sec")
        elif choice8 == 9:
            print(num1, " Kilometer/hour = ", (num1 * 0.911344), " Feet/sec")
        else:
            print("Invalid Input")
            break

    condition1 = input("Do you want to check more, Press Y or y: ")
    if condition1 == "y" or condition1 == "Y":
        condition = "True"
    else:
        break
