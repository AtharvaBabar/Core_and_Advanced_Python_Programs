#Q1. Python program to check leap year  or not.

def is_leap_year(year):
    # A leap year is either:
    # - Divisible by 4 but not by 100, or
    # - Divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # If conditions are met, it's a leap year
    return False  # Otherwise, it's not a leap year

# Taking input from the user
year = int(input("Enter a year: "))

# Checking if the year is a leap year and printing the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


'''
OUTPUT:
Enter a year: 2024
2024 is a leap year.

Enter a year: 1900
1900 is not a leap year.
'''
