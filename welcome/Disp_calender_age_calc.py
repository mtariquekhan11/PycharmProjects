# Author: Mohd Tarique Khan
# Date: 26/10/2019
# Purpose: To display the requested calender, current month calender and age calculator


def current_month(date):
    # display the current calendar
    print("\nLocal date and time:", localtime)      # Printing Local date and Time
    print("\nCurrent date:", date)                  # Printing Current date only
    print(calendar.month(date.year, date.month))    # Printing Current month calendar


def other_month(y, m):
    # display the requested month calendar
    print("\nLocal date and time:", localtime)     # Printing Local date and Time
    print(calendar.month(y, m))                    # Printing requested month calendar
    print("\nCurrent date:", date)                 # Printing Current date only


def full_calendar(y):
    print(calendar.calendar(y))             # Display full year calendar for the requested year


def age_calc(yyob, mmob, ddayob):
    dob = datetime.date(yyob, mmob, ddayob)     # Date of Birth(dob) as input

    print("\nDate of Birth :", dob)

    print("\nCurrent Date :", datetime.date.today())    # Printing current date

    age = (datetime.date.today() - dob)         # Calculating ags in number of days

    print("\nDays =", age)

    yrsage = float(age.days/365)            # Converting age into years as float
    yearscount = str(yrsage)                # Typecasting calculated years in string

    print("\nYours age is approximately", round(yrsage), "Years")   # Printing the age years approx by rounding
    print(yearscount[0:2], "Years")

    monthsage = float(age.days % 365)       # calculating rest number of days after deducting years
    monthscount = int(round(monthsage, 0) / 30)   # Converting rest number of days in approx months
    print(monthscount, "Months")



if __name__ == '__main__':

    condition = "True"

    import time         # import time module
    import calendar     # import calender module
    import datetime     # import datetime module

    date = datetime.date.today()
    localtime = time.asctime(time.localtime(time.time()))

    while condition is "True":
        choice = int(input("Enter '1' for Current month\n '2' for Any other month"
                           "\n '3' for Full year calender\n '4' for Age Calculator"))
        if choice == 1:
            current_month(date)
        elif choice == 2:
            mm = int(input("Enter the number of month(MM format):"))
            yyyy = int(input("Enter the year(YYYY format):"))
            other_month(yyyy, mm)
        elif choice == 3:
            yyyy = int(input("Enter the year(YYYY format):"))
            full_calendar(yyyy)
        elif choice == 4:
            dayob = int(input("Enter your Day of Birth(DD):"))
            mob = int(input("Enter your Month of Birth(MM):"))
            yob = int(input("Enter your Year of Birth(YYYY):"))
            age_calc(yob, mob, dayob)

        else:
            print("Sorry wrong input")
            break


        condition1 = input("\nDo you want to check more, Press Y or y: ")
        if condition1 == "y" or condition1 == "Y":
            condition = "True"
        else:
            break
