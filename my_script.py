from utils import is_leap_year


if __name__ == '__main__':
    date = input("Insert a date in format dd-mm-yyyy: ")
    day, month, year = [int(elem) for elem in date.split("-")]

    if month == 2:
        # take care of February
        if is_leap_year(year):
            days_num = 29
        else:
            days_num = 28
    else:
        if 1 <= month <= 7:
            days_num = 30 if month % 2 == 0 else 31
        else:
            days_num = 31 if month % 2 == 0 else 30

    print(f"Number of days in month {month}: {days_num}")