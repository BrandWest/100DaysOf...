import datetime as dt

current = dt.datetime.now()
year = current.year
month = current.month
day = current.day
hour = current.hour
minute = current.minute
weekday = current.weekday()

if year == 2023:
    print(current, year, month, day, hour, minute, weekday)

#Creating new dt obhect
date_of_birth = dt.datetime(year=2020 ,month=10 ,day=15)
print(date_of_birth)