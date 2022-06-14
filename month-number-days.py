# the function will take a year and a month as inputs.
# function(year=2022, month=2) and return the number of days in any given month.
# February has 28 days except for a leap year, it has 29 days.

# function for leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
 
# take input from user
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# return the number of days in a month
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) == True and month == 2:
        return 29
    elif month <= 12:
        return month_days[month-1]
    else:
        print("enter a valid month")

days = days_in_month(year, month)
print(days)
