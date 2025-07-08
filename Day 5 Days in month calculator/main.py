def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return ("leap year")

            else:
                return ("not a leap year")

        else:
            return ("leap year")

    else:
        return ("not a leap year")


def day_in_month(year, month, condition):
    if condition == "leap year":
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    elif condition == "not a leap year":
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month -= 1

    return month_days[month]


year = int(input("Write your year"))
month = int(input("Write your month"))
condition = is_leap(year)
days = day_in_month(year, month, condition)

print(f"Your month has {days}")