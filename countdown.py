import datetime
import time
import os

while True:

    os.system("clear")
    print("\n")
    print("Time left for X-mas HoHoHo *<:D")

    this_year = int(time.strftime("%Y"))

    future_date = datetime.datetime(this_year, 12, 24)

    todays_date = datetime.datetime.today()

    difference = (future_date - todays_date)

    total_seconds = int(difference.total_seconds())

    days_left = int(total_seconds / 60 / 60 / 24)
    hours_left = int(total_seconds / 60 / 60 % 24)
    minutes_left = int(total_seconds / 60 % 60)
    seconds_left = int(total_seconds % 60)

    print(days_left, "Days", hours_left, "Hours", minutes_left, "Minutes", seconds_left, "Seconds")
    time.sleep(1)