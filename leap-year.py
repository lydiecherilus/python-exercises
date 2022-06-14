# The program will output whether a given year is a leap year or not. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# A leap year is evenly divisible by 4 except if the year is evenly divisible by 100, 
# unless** the year is also evenly divisible by 400

# Solution
# ask for user to enter a year
year = int(input("Which year do you want to check? "))
# check if the year is a leap and print "Leap year." or "Not leap year."
if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
