# Problem statement
# Write a function that calculates the corresponding day of the week for any particular date in the past or future.

# For example, for the date 28th August 2020 happens to be Friday. Hence the expected output will be Friday.

import datetime

def calculate_datetime(day,month,year):

    
    date=datetime.date(year,month,day)

    return date.strftime("%A")


day = 28
month = 8
year = 2020

print(calculate_datetime(day,month,year))