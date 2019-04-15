import datetime


# Get the instantaneous date and time in the format "YYYY-MM-DD HH:MM:SS"
def get_date():
    now = datetime.datetime.today()

    second = now.second
    minute = now.minute
    hour = now.hour
    day = now.day
    month = now.month
    year = now.year

    date = str(year) + "-"
    if month < 10: date = date + "0" + str(month) + "-"
    else: date = date + str(month) + "-"
    if day < 10: date = date + "0" + str(day) + "-"
    else: date = date + str(day) + " "
    if hour < 10: date = date + "0" + str(hour) + ":"
    else: date = date + str(hour) + ":"
    if minute < 10: date = date + "0" + str(minute) + ":"
    else: date = date + str(minute) + ":"
    if second < 10: date = date + "0" + str(second)
    else: date = date + str(second)

    return date
